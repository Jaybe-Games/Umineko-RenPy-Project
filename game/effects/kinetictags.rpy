default cps = preferences.text_cps / 3

init python:
    import random
    import math

    
    class DispTextStyle():

        custom_tags = ["fi"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain", 'cps']
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        
        def add_tags(self, char):
            tag, _, value = char.partition("=") 
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False 

       
        def apply_style(self, char):
            new_string = ""
           
            new_string += self.start_tags()
            
            new_string += char
           
            new_string += self.end_tags()
            return new_string

       
        def start_tags(self):
            new_string = ""
            
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

       
        def end_tags(self):
            new_string = ""

            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string


    class FadeInText(renpy.Displayable):
        def __init__(self, child, char_num, fade_time, slide_distance=100, **kwargs):
            super(FadeInText, self).__init__(**kwargs)

            
            self.child = child
            self.fade_time = fade_time
            self.display_time = .01
            self.slide_distance = slide_distance
            
            cps = 0.0
            if preferences.text_cps != 0: 
                cps = (1.0 / preferences.text_cps)
            self.time_offset = char_num * cps  

        def render(self, width, height, st, at):
            curr_alpha = 0.0
            xoff = 5.0
            if st > self.time_offset:
                adjust_st = st - self.time_offset 
                curr_alpha = adjust_st/self.fade_time
                xoff = max(self.slide_distance - ((adjust_st/self.fade_time) * self.slide_distance), 0)
            
            t = Transform(child=self.child,  alpha = curr_alpha)
            child_render = renpy.render(t, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (xoff, 0))
            
            if st <= self.fade_time + self.time_offset:
                renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]
     
    def fade_in_tag(tag, argument, contents):
        new_list = [ ]
        my_index, fade_time, slide_distance = 0, .50, 0
        if argument != "":
            argument = argument.split('-')
            if len(argument) > 0:
                my_index = int(argument[0])
            if len(argument) > 1:
                fade_time = float(argument[1])
            if len(argument) > 2:
                slide_distance = int(argument[2])
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    char_text = Text(my_style.apply_style(char))
                    char_disp = FadeInText(char_text, my_index, fade_time, slide_distance)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = FadeInText(my_img, my_index, fade_time, slide_distance)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    my_index += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list


    config.custom_text_tags["fi"] = fade_in_tag


