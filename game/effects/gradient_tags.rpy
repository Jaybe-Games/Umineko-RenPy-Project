init python:

    def color_gradient(color_1, color_2, range, index):
        if index == 0:
            return color_1
        if range == index:
            return color_2
        start_col = Color(color_1)
        end_col = Color(color_2)
        return start_col.interpolate(end_col, index * 1.0/range).hexcode

 
    def gradient_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return
        else: 
            col_1, _, col_2 = argument.partition('-')
        
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


    class GradientText(renpy.Displayable):
        def __init__(self, char, col_list, id, list_end, **kwargs):

            super(GradientText, self).__init__(**kwargs)

            self.char = char
            self.child = Text(char)
            self.col_list = col_list 
            self.id = id
            self.list_end = list_end
            
            for i, element in enumerate(col_list):
                if self.id < element[2]:
                    self.curr_grad = i
                    break
            
            if self.curr_grad == 0:
                self.curr_range = self.col_list[0][2]
            else:
                self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

        def render(self, width, height, st, at):
            my_style = DispTextStyle()
            
            if self.curr_grad == 0:
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id))
            else: 
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id - self.col_list[self.curr_grad - 1][2]))

            
            self.child.set_text(my_style.apply_style(self.char))
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self, 0)

            
            self.id += 1
            
            if self.id > self.col_list[self.curr_grad][2]:
                self.curr_grad += 1
                
                if self.curr_grad == self.list_end:
                    self.curr_grad = 0
                    self.id = 0
                    self.curr_range = self.col_list[0][2]
                
                else:
                    self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

            return render

        def visit(self):
            return [ self.child ]

    def gradient2_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return
        else: 
            arg_num, _, argument = argument.partition('-') 
        arg_num = int(arg_num)
        
        col_list = []
        end_num = 0
        for i in range(arg_num):
            col_1, _, argument = argument.partition('-')   
            col_2, _, argument = argument.partition('-')   
            end_num_arg, _, argument = argument.partition('-') 
            end_num += int(end_num_arg) 
            col_list.append((col_1, col_2, end_num))

        my_index = 0
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    char_disp = GradientText(my_style.apply_style(char), col_list, my_index, arg_num)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
                    
                    if my_index >= col_list[arg_num-1][2]:
                        my_index = 0
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    config.custom_text_tags["gradient"] = gradient_tag
    config.custom_text_tags["gradient2"] = gradient2_tag
