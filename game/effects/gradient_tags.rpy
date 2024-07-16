init python:
    ##### Made these ones just for fun. Leaving them in here just in case anyone wants
    ##### to use them. Probably will not add them to the Omega tag or to DispTextStyle

    # Takes in two colors, a range and an index and interpolates a new color
    # between the start and end points based on the range and index.
    # color_1: (String of hex color in #rrggbb format) Start of the gradient
    # color_2: (Same as above) End of the gradient
    # range: (int) The number of elements in the gradient
    # id:    (int) The offset into the gradient's range
    # Return: String of interpolated hex color in rrggbb format
    def color_gradient(color_1, color_2, range, index):
        if index == 0:
            return color_1
        if range == index:
            return color_2
        start_col = Color(color_1)
        end_col = Color(color_2)
        return start_col.interpolate(end_col, index * 1.0/range).hexcode

    # Applies a static gradient over text
    # Note: Hex Color = A string giving a hexadecimal color, in the form "#rrggbb".
    # color_1: (Hex Color) The starting color
    # color_2: (Hex Color) The ending color
    # Args are separated by an '-'
    # Example: {gradient=[color_1]-[color_2]}{/gradient}
    def gradient_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return
        else: # Note: all arguments must be supplied
            col_1, _, col_2 = argument.partition('-')
        # Get a count of all the letters we will be applying colors to
        count = 0
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        continue
                    count += 1
        count -= 1
        my_index = 0
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    new_list.append((renpy.TEXT_TAG, "color=" + color_gradient(col_1, col_2, count, my_index)))
                    new_list.append((renpy.TEXT_TEXT, char))
                    new_list.append((renpy.TEXT_TAG, "/color"))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # A custom displayable that applies a gradient over a letter of text.
    # Honestly didn't test this works with other text tags since was just for fun
    class GradientText(renpy.Displayable):
        def __init__(self, char, col_list, id, list_end, **kwargs):
            """
            col_list format
                (color_1, color_2, end_id)
            list_end should be the number of gradients in the list
            """
            super(GradientText, self).__init__(**kwargs)

            self.char = char
            self.child = Text(char)
            self.col_list = col_list # Calling it grad_list for gradient might be more appropriate.
            self.id = id
            self.list_end = list_end
            # Figure out which gradient we are in
            for i, element in enumerate(col_list):
                if self.id < element[2]:
                    self.curr_grad = i
                    break
            # Determine the current range (for color_gradient func later)
            if self.curr_grad == 0:
                self.curr_range = self.col_list[0][2]
            else:
                self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

        def render(self, width, height, st, at):
            my_style = DispTextStyle()
            # Get the color to apply to the text
            if self.curr_grad == 0:
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id))
            else: # color_gradient() expects id to be within the range given. So must reduce to that if exceeding it.
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id - self.col_list[self.curr_grad - 1][2]))

            # Usual retrieval and drawing of child render
            self.child.set_text(my_style.apply_style(self.char))
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self, 0)

            # Iterate id for next render
            self.id += 1
            # If we are at the end of the range update gradient
            if self.id > self.col_list[self.curr_grad][2]:
                self.curr_grad += 1
                # If at the end of our color list, reset back to 0
                if self.curr_grad == self.list_end:
                    self.curr_grad = 0
                    self.id = 0
                    self.curr_range = self.col_list[0][2]
                # Otherwise just update the range
                else:
                    self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

            return render

        def visit(self):
            return [ self.child ]

    config.custom_text_tags["gradient"] = gradient_tag


init:
    ## Do I need to explain that?
    ## Go to your say screen and look for "text what" and write "at dialogue_gradient"
    transform dialogue_gradient(color1=Color("#ffffff"), color2=Color("#8a8a8a")):
        mesh(2,2)
        shader "gradient.vertical_down"
        u_color1 color1.rgba
        u_color2 color2.rgba

    transform bgm_gradient(color1=Color("#c1fbf2"), color2=Color("#dbfcf7")):
            mesh(2,2)
            shader "gradient.vertical_down"
            u_color1 color1.rgba
            u_color2 color2.rgba

init python:
    ## float gradient_size = 59.1 is default for Arno Pro Fontsize 50, adjust it to your font
    renpy.register_shader("gradient.vertical_down", variables="""
        uniform vec4 u_color1;
        uniform vec4 u_color2;
        uniform vec2 u_model_size;
        varying float v_position;
        attribute vec4 a_position;
    """, vertex_300="""
        v_position = a_position.y;
    """, fragment_300="""
        float gradient_size = 59.1;
        float gradient_position = mod(v_position, gradient_size) / gradient_size;
        gl_FragColor *= mix(u_color1, u_color2, gradient_position);
    """)

init python:
    def red_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "gradient=#ff0000-#f51d1d")] + contents + [(renpy.TEXT_TAG, "/gradient")]
    def blue_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "gradient=#0aecf0-#45f2f5")] + contents + [(renpy.TEXT_TAG, "/gradient")]
    def gold_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "gradient=#ffff00-#ffcc00")] + contents + [(renpy.TEXT_TAG, "/gradient")]
    def bgm(tag, argument, contents):
        return [(renpy.TEXT_TAG, "gradient=#27BFD1-#96DBE9")] + contents + [(renpy.TEXT_TAG, "/gradient")]

    config.custom_text_tags["red"] = red_tag
    config.custom_text_tags["blue"] = blue_tag
    config.custom_text_tags["gold"] = gold_tag
    config.custom_text_tags["bgm"] = bgm
