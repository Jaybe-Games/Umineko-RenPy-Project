init python:
    import random
    import math
    from enum import Enum, IntFlag

    BREAKUP_DISSOLVE_FRAMES = 1000
    BREAKUP_WIPE_FRAMES = 3000
    BREAKUP_MOVE_FRAMES = 850
    BREAKUP_CELLSEPARATION = 16
    
    class BreakupMode(IntFlag):
        LEFT = 1
        LOWER = 2
        JUMBLE = 4

    # This class essentially just holds some vertex buffers inside of python and provides methods to conveniently add textured
    # vertices in various shapes.
    class TriangleBlitter:
        def __init__(self):
            self.vertices = []
            self.attributes = []
            self.indices = []
            self.vertex_counter = 0
            self.max_vertices = 65000
            self.fewer_triangles = False
            self.meshes = []

        def set_textured_vertex(self, should_index, s, t, x, y):
            self.vertices.extend([x, y])
            self.attributes.extend([s, t])
            if should_index:
                self.indices.append(self.vertex_counter)
                
            self.vertex_counter += 1

        def set_indexed_vertex(self, index):
            self.indices.append(index)

        def add_ellipse(self, s, t, radius_s, radius_t, x, y, radius_x, radius_y):
            degrees = 0
            rot_x = math.cos(degrees * math.pi / 180)
            rot_y = math.sin(degrees * math.pi / 180)
            dt = 1.25 / math.sqrt(radius_x if radius_x > radius_y else radius_y)
            num_segments = int(2 * math.pi / dt + 1) if not self.fewer_triangles else 2

            if self.vertex_counter + (3 + num_segments - 2) > self.max_vertices:
                self.finish()

            start = self.vertex_counter

            if num_segments == 2:
                self.set_textured_vertex(True, s + radius_s, t + radius_t, x + radius_x, y + radius_y)
                self.set_textured_vertex(True, s - radius_s, t - radius_t, x - radius_x, y - radius_y)
                self.set_textured_vertex(True, s - radius_s, t + radius_t, x - radius_x, y + radius_y)
                self.set_indexed_vertex(start)
                self.set_indexed_vertex(start + 1)
                self.set_textured_vertex(True, s + radius_s, t - radius_t, x + radius_x, y - radius_y)
                return

            self.set_textured_vertex(False, s, t, x, y)
            cos_rads = math.cos(dt)
            sin_rads = math.sin(dt)
            dx, dy = 1.0, 0.0
            s_transpose = rot_x * radius_s * dx - rot_y * radius_t * dy
            t_transpose = rot_y * radius_s * dx + rot_x * radius_t * dy
            x_transpose = rot_x * radius_x * dx - rot_y * radius_y * dy
            y_transpose = rot_y * radius_x * dx + rot_x * radius_y * dy
            self.set_textured_vertex(False, s + s_transpose, t + t_transpose, x + x_transpose, y + y_transpose)

            for i in range(1, num_segments):
                temp_dx = cos_rads * dx - sin_rads * dy
                dy = sin_rads * dx + cos_rads * dy
                dx = temp_dx
                s_transpose = rot_x * radius_s * dx - rot_y * radius_t * dy
                t_transpose = rot_y * radius_s * dx + rot_x * radius_t * dy
                x_transpose = rot_x * radius_x * dx - rot_y * radius_y * dy
                y_transpose = rot_y * radius_x * dx + rot_x * radius_y * dy
                self.set_indexed_vertex(start)
                self.set_indexed_vertex(start + i)
                self.set_textured_vertex(True, s + s_transpose, t + t_transpose, x + x_transpose, y + y_transpose)

            self.set_indexed_vertex(start)
            self.set_indexed_vertex(start + num_segments)
            self.set_indexed_vertex(start + 1)

        def add_triangle(self, s1, t1, s2, t2, s3, t3, x1, y1, x2, y2, x3, y3):
            if self.vertex_counter + 3 > self.max_vertices:
                self.finish()

            self.set_textured_vertex(True, s1, t1, x1, y1)
            self.set_textured_vertex(True, s2, t2, x2, y2)
            self.set_textured_vertex(True, s3, t3, x3, y3)

        def copy_triangle(self, x_src1, y_src1, x_src2, y_src2, x_src3, y_src3, x_dst, y_dst):
            self.add_triangle(
                x_src1 / self.image_w, y_src1 / self.image_h,
                x_src2 / self.image_w, y_src2 / self.image_h,
                x_src3 / self.image_w, y_src3 / self.image_h,
                x_src1 + x_dst, y_src1 + y_dst,
                x_src2 + x_dst, y_src2 + y_dst,
                x_src3 + x_dst, y_src3 + y_dst
            )

        def copy_circle(self, x_src, y_src, radius, x_dst, y_dst, resize_factor=1.0):
            self.add_ellipse(
                x_src / self.image_w, y_src / self.image_h,
                radius / self.image_w, radius / self.image_h,
                x_dst, y_dst, radius * resize_factor, radius * resize_factor
            )

        def update_sizes(self, src_size, dst_size):
            self.image_w, self.image_h = src_size
            self.target_w, self.target_h = dst_size

        def use_fewer_triangles(self, arg=True):
            self.fewer_triangles = arg

        # Create a mesh from the vertices we have already stored, and clear out the internal buffers.
        # While a renpy mesh can store 2**31-1 vertices, the index array can only refer to at most 65536 of them.
        # So we need to regularly do this.
        def finish(self):
            self.meshes.append(self.mesh())
            self.vertices.clear()
            self.attributes.clear()
            self.indices.clear()
            self.vertex_counter = 0
        
        # Convert the vertices in our buffer into a mesh for renpy usage
        def mesh(self):
            mesh = renpy.gl2.gl2mesh2.Mesh2(renpy.gl2.gl2mesh.TEXTURE_LAYOUT, len(self.vertices), len(self.indices) // 3)
            mesh.set_geometry_data(self.vertices)
            mesh.set_attribute_data(self.attributes)
            mesh.set_triangle_data(self.indices)
            return mesh

    class BreakupCell:
        def __init__(self):
            self.cell_x = 0
            self.cell_y = 0
            self.x_movement = 0
            self.y_movement = 0
            self.state = 0
            self.disp_x = 0
            self.disp_y = 0
            self.resize_factor = 1.0
            self.diagonal = 0

    class BreakupData:
        def __init__(self):
            self.breakup_cells = []
            self.diagonal_indices = []
            self.cell_factor = 0
            self.num_cells_x = 0
            self.num_cells_y = 0
            self.blitter = None
            self.breakup_mode = None
            self.tot_frames = 0
            self.max_diagonal_to_contain_broken_cells = 0

    class Breakup(renpy.Displayable):
        def __init__(self, widget, factor, breakup_direction_flagset, **properties):
            super(Breakup, self).__init__(**properties)
            self.factor = factor
            self.widget = renpy.displayable(widget)
            self.width = 0
            self.height = 0

            self.breakup_direction_flagset = breakup_direction_flagset
            self.breakup_data = None

        def init_breakup(self):
            cell_factor = BREAKUP_CELLSEPARATION
            w, h = self.width, self.height

            # Calculate how many cells to make: one for every `cell_factor` pixels horizontally or vertically
            num_cells_x = int((w + cell_factor - 1) // cell_factor) + 1
            num_cells_y = int((h + cell_factor - 1) // cell_factor) + 1

            # Initialise the remaining data structure
            data = BreakupData()
            data.breakup_cells = [BreakupCell() for _ in range(num_cells_x * num_cells_y)]
            data.diagonal_indices = [None] * (num_cells_x + num_cells_y - 1)
            data.cell_factor = cell_factor
            data.num_cells_x = num_cells_x
            data.num_cells_y = num_cells_y
            self.breakup_data = data

            # Create the blitter that will store the vertices we generate
            self.breakup_data.blitter = TriangleBlitter()

        def once_per_breakup_effect_breakup_setup(self, num_cells_x, num_cells_y):
            data = self.breakup_data

            # Check if the setup has already been run
            if data.breakup_mode and data.breakup_mode == self.breakup_direction_flagset:
                return

            # Seed the RNG. on-ru does this based on sprite ID I think, but it really doesn't matter that much,
            # we can just keep it constant
            random.seed(0)

            data.breakup_mode = self.breakup_direction_flagset
            data.tot_frames = BREAKUP_DISSOLVE_FRAMES + BREAKUP_WIPE_FRAMES

            total_diag_count = num_cells_x + num_cells_y - 1
            n = 0
            cells = data.breakup_cells
            diagonal_indices = data.diagonal_indices

            # Iterate through the diagonals from one corner to the other
            for this_diag_no in range(total_diag_count):
                # Store the index of the first cell in this diagonal
                diagonal_indices[this_diag_no] = n

                # Iterate through all the cells in the diagonal
                for x in range(this_diag_no, -1, -1):
                    y = this_diag_no - x
                    if y >= num_cells_y:
                        continue
                    if x >= num_cells_x:
                        continue

                    # Determine the cell's state, that is, the frame in which it should totally disappear.
                    # The frame where it will start and finish dissolving/flying away will be calculated based on that
                    state = BREAKUP_DISSOLVE_FRAMES
                    if total_diag_count > 1:
                        fake_diag_no = this_diag_no - (random.randint(0, 19))
                        if fake_diag_no < 0:
                            fake_diag_no = 0
                        state += (fake_diag_no * BREAKUP_WIPE_FRAMES // (total_diag_count - 1))

                    # Calculate the cell's starting position
                    cell = cells[n]
                    cell.cell_x = x if self.breakup_direction_flagset & BreakupMode.LEFT else num_cells_x - x - 1
                    cell.cell_y = num_cells_y - y - 1 if self.breakup_direction_flagset & BreakupMode.LOWER else y
                    cell.diagonal = this_diag_no
                    cell.state = state

                    # Determine the direction in which to move the cell, depending on the specified flags
                    x_dir, y_dir = 1, 1
                    if self.breakup_direction_flagset & BreakupMode.JUMBLE:
                        x_dir, y_dir = -x_dir, -y_dir
                    if self.breakup_direction_flagset & BreakupMode.LEFT:
                        x_dir = -x_dir
                    if self.breakup_direction_flagset & BreakupMode.LOWER:
                        y_dir = -y_dir

                    # Calculate the angle in which to move the cell...
                    ax = this_diag_no - (num_cells_y - 1)
                    ax = x if ax <= 0 else x - ax
                    ay = this_diag_no - (num_cells_x - 1)
                    ay = y if ay <= 0 else y - ay
                    angle = math.atan2(-ay, ax) if ax != 0 else math.pi / 2.0
                    plusminus50 = random.randint(-50, 50)
                    plusminus45degrees = (math.pi / 4.0) * plusminus50 / 50.0
                    angle += plusminus45degrees

                    # ...and the vector X and Y components based on that
                    cell.x_movement = x_dir * math.cos(angle)
                    cell.y_movement = y_dir * math.sin(angle)

                    # Increment the overall cell counter
                    n += 1

        # Resize and displace each cell according to how early or late it should be in the breakup process.
        def effect_breakup_new(self, breakup_factor):
            data = self.breakup_data
            cells = data.breakup_cells
            duration = 1000
            frame = data.tot_frames * breakup_factor // duration

            maximum_diagonal = 0
            state = 0
            touched = False

            for cell in cells:
                state = cell.state - frame
                cell.disp_x = 0
                cell.disp_y = 0
                touched = False
                cell.resize_factor = 1.0

                # Resize the cell...
                if state < BREAKUP_DISSOLVE_FRAMES:
                    cell.resize_factor = 0.0 if state <= 0 else 1.0 * state / BREAKUP_DISSOLVE_FRAMES
                    touched = True

                # ...and displace it
                if 0 < state < BREAKUP_MOVE_FRAMES:
                    cell.disp_x = cell.x_movement * (BREAKUP_MOVE_FRAMES - state)
                    cell.disp_y = cell.y_movement * (BREAKUP_MOVE_FRAMES - state)
                    touched = True

                # Find the maximum diagonal on which there are cells which needed to be moved/scaled.
                # The solid region will be drawn below this diagonal.
                if touched and cell.diagonal > maximum_diagonal:
                    maximum_diagonal = cell.diagonal

            data.max_diagonal_to_contain_broken_cells = maximum_diagonal

        # Draw the solid region that has not yet been dissolved.
        # This region can have 3, 4, or 5 vertices and must thus be composed of 1, 2, or 3 triangles.
        # See https://www.desmos.com/geometry/wwgdxtmcaz for a visualisation. Observe how the number of vertices
        # making up the combined shaded region, as well as the number of triangles making up the shaded region,
        # changes as you change the value of `a`, representing the frame of the breakup increasing with time.
        def draw_unbroken_breakup_regions(self, dst_x, dst_y):
            data = self.breakup_data
            cells = data.breakup_cells

            num_cells_x = data.num_cells_x
            num_cells_y = data.num_cells_y
            max_x = num_cells_x - 1
            max_diagonal_index = num_cells_x + num_cells_y - 2

            f = data.cell_factor

            diagonal_indices = data.diagonal_indices

            # Find the last cell to disappear, equivalent to the orange vertex `p_1` in the visualisation.
            # This vertex is shared between all triangles to be drawn.
            last_cell = cells[num_cells_x * num_cells_y - 1]

            if data.max_diagonal_to_contain_broken_cells + 1 >= max_diagonal_index:
                # Nothing is locked in place yet, or, only one cell is (can't make a triangle from that -- zero area)
                return

            # Find the first and last cell of the last diagonal that contains broken cells,
            # that is, on the border between the “cloud of dissolved cells” and the solid region
            # (the latter of which we are supposed to draw in this method).
            first_on_diagonal_index = diagonal_indices[data.max_diagonal_to_contain_broken_cells]
            last_on_diagonal_index = diagonal_indices[data.max_diagonal_to_contain_broken_cells + 1] - 1
            diagonal_cell_indices = [first_on_diagonal_index, last_on_diagonal_index]

            # First, draw the outer two triangles `T_2` and `T_3`, the red and blue triangles in the visualisation.
            for cell_index in diagonal_cell_indices:
                cell = cells[cell_index]

                # Check if the cell is located on an edge of the rectangle that is not adjacent to the last cell,
                # and would thus form a corner of either `T_2` or `T_3`.
                if cell.cell_x != last_cell.cell_x and cell.cell_y != last_cell.cell_y:
                    # Find the third corner of the triangle. It will necessarily coincide with one of the vertices of the rectangle,
                    # hence `shared_corner`
                    shared_corner_x, shared_corner_y = 0, 0
                    if cell.cell_x == 0 or cell.cell_x == max_x:
                        shared_corner_x = cell.cell_x
                        shared_corner_y = last_cell.cell_y
                    else:
                        shared_corner_x = last_cell.cell_x
                        shared_corner_y = cell.cell_y

                    # Draw the triangle we constructed.
                    data.blitter.copy_triangle(
                        cell.cell_x * f, cell.cell_y * f,
                        last_cell.cell_x * f, last_cell.cell_y * f,
                        shared_corner_x * f, shared_corner_y * f,
                        dst_x, dst_y
                    )

            # Finally, draw the central triangle `T_1`, purple in the visualisation.
            data.blitter.copy_triangle(
                cells[last_on_diagonal_index].cell_x * f, cells[last_on_diagonal_index].cell_y * f,
                cells[first_on_diagonal_index].cell_x * f, cells[first_on_diagonal_index].cell_y * f,
                last_cell.cell_x * f, last_cell.cell_y * f,
                dst_x, dst_y
            )

        def break_up_image(self, target_w, target_h, dst_x, dst_y):
            data = self.breakup_data
            cells = data.breakup_cells

            blitter = data.blitter
            blitter.update_sizes((self.width, self.height), (target_w, target_h))

            # Calculate general properties 
            self.once_per_breakup_effect_breakup_setup(data.num_cells_x, data.num_cells_y)
            self.effect_breakup_new(self.factor)
                    
            # Draw the region of the image that has not yet been broken up
            self.draw_unbroken_breakup_regions(dst_x, dst_y)

            # Draw the breakup cells as individual circles
            for cell in cells:
                x = cell.cell_x * data.cell_factor
                y = cell.cell_y * data.cell_factor
                if cell.diagonal > data.max_diagonal_to_contain_broken_cells:
                    break
                if cell.resize_factor > 0:
                    blitter.use_fewer_triangles(cell.resize_factor < 0.15)
                    blitter.copy_circle(x, y, 12, x + cell.disp_x + dst_x, y + cell.disp_y + dst_y, cell.resize_factor)

            # Convert the vertices we added to the buffer into meshes for use in renpy
            blitter.finish()
            return blitter.meshes

        def event(self, ev, x, y, st):
            return self.widget.event(ev, x, y, st)

        def visit(self):
            return [self.widget]
        
        def get_placement(self):
            return self.widget.get_placement()

        def render(self, width, height, st, at):
            child = renpy.render(self.widget, width, height, st, at)
            self.width, self.height = child.get_size()

            if self.breakup_data is None:
                self.init_breakup()
            
            meshes = self.break_up_image(width, height, 0, 0)
            total = renpy.Render(width, height)

            # We cannot add multiple meshes to one Render, so we need to create an individual Render for each mesh,
            # and blit it onto `total`
            for mesh in meshes:
                sub = renpy.Render(width, height)
                sub.mesh = mesh
                sub.add_shader("renpy.texture")
                sub.blit(child, (0, 0))
                total.blit(sub, (0, 0))

            # Clear the meshes so the vertex data does not accumulate over time
            meshes.clear()

            return total
