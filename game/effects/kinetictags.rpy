default preferences.chaos_on = False

init python:
    import random
    import math

    
    class DispTextStyle():

        custom_tags = ["omega", "bt", "fi", "sc", "rotat", "chaos", "move"]
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



    class BounceText(renpy.Displayable):
        def __init__(self, child, char_offset, amp=20, period=4.0, speed = 1.0, **kwargs):

           
            super(BounceText, self).__init__(**kwargs) 


            self.child = child
            self.amp = amp 
            self.char_offset = char_offset 
            self.period = period 
            self.speed = speed 

        def render(self, width, height, st, at):

            curr_height = math.sin(self.period*((st * self.speed)+(float(self.char_offset) * -.1))) * float(self.amp)




            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            
            render.subpixel_blit(child_render, (0, curr_height))

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


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

   
    class ScareText(renpy.Displayable):
        def __init__(self, child, square=2, **kwargs):
            super(ScareText, self).__init__(**kwargs)

            self.child = child

            self.square = square

        def render(self, width, height, st, at):
            
            xoff = (random.random()-.5) * float(self.square)
            yoff = (random.random()-.5) * float(self.square)

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]


    class ChaosText(renpy.Displayable):
        
        font_list = ["FOT-PopJoyStd-B.otf", "GrenzeGotisch-VariableFont_wght.ttf", "Pacifico-Regular.ttf", "RobotoSlab-ExtraBold.ttf",\
                    "RobotoSlab-Medium.ttf", "SyneTactile-Regular.ttf", "TurretRoad-Bold.ttf", "TurretRoad-ExtraBold.ttf", "TurretRoad-ExtraLight.ttf", \
                    "TurretRoad-Light.ttf", "TurretRoad-Medium.ttf", "TurretRoad-Regular.ttf"]
        
        color_choice = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        def __init__(self, orig_text, **kwargs):

            super(ChaosText, self).__init__(**kwargs)

            
            self.child = renpy.text.text.Text(orig_text)
            self.orig_text = orig_text
            self.last_style = None 

        def render(self, width, height, st, at):
            if not preferences.chaos_on:                
                if self.last_style is not None:
                    
                    self.child.set_text(self.last_style.apply_style(self.orig_text))
                    child_render = renpy.render(self.child, width, height, st, at)
                    self.width, self.height = child_render.get_size()
                    render = renpy.Render(self.width, self.height)
                    render.subpixel_blit(child_render, (0, 0))
                    return render

            
            new_style = DispTextStyle()
            new_color = ""
            
            for i in range(0,6):
                new_color += renpy.random.choice(self.color_choice)
            new_color = "#" + new_color
            new_style.add_tags("color=" + str(new_color))
            
            rand_size = renpy.random.randint(0,50)
            new_style.add_tags("size="+str(rand_size))
            
            rand_font = renpy.random.choice(self.font_list)
            new_style.add_tags("font="+rand_font)
            
            self.child.set_text(new_style.apply_style(self.orig_text))
            
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self,0)

            self.last_style = new_style
            return render

        def visit(self):
            return [ self.child ]


    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=300, **kwargs):
            super(RotateText, self).__init__(**kwargs)

            self.child = child

            self.speed = speed 

        def render(self, width, height, st, at):

            theta = math.radians(st * float(self.speed))
            t = Transform(child=self.child,  rotate=st*float(self.speed))
            child_render = renpy.render(t, width, height/2, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height/2)

            render.blit(child_render, (0,0))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    class SwapText(renpy.Displayable):
        def __init__(self, start_tags, text1, text2, end_tags, swap_time, **kwargs):
            super(SwapText, self).__init__(**kwargs)
            
            self.start_tags = start_tags
            self.text1 = text1
            self.text2 = text2
            self.end_tags = end_tags
           
            self.s_time = swap_time
           
            self.timer = 0.0
           
            self.swap_to_1 = False
            self.child = Text(start_tags + text1 + end_tags)
            self.st = 0.0


        def render(self, width, height, st, at):
            delta = st - self.st 
            self.timer += delta
            if self.timer > self.s_time:
              
                if self.swap_to_1:
                    self.child.set_text(self.start_tags + self.text1 + self.end_tags)
                    self.swap_to_1 = False
                    self.timer = 0.0
                else:
                    self.child.set_text(self.start_tags + self.text2 + self.end_tags)
                    self.swap_to_1 = True
                    self.timer = 0.0

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0,0))
            renpy.redraw(self, 0)

            self.st = st 
            return render

        def visit(self):
            return [ self.child ]


    class MoveText(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(MoveText, self).__init__(**kwargs)
            self.affect_distance = 150
            self.child = child
            self.mouse_pos = (1000,1000)
            self.pos = (0,0)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            trans_x = self.mouse_pos[0] - self.pos[0] - (self.width / 2)
            trans_y = self.mouse_pos[1] - self.pos[1] - (self.height / 2)

            vl = math.hypot(trans_x,trans_y)
            xpos, ypos = self.pos
            
            if vl < self.affect_distance:
                distance = 3.0 * (self.affect_distance-vl) / self.affect_distance
                xpos -= distance * trans_x / vl
                ypos -= distance * trans_y / vl
                self.pos = (xpos, ypos)
           
            render.subpixel_blit(child_render, (xpos, ypos))
            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            self.mouse_pos = (x,y)
           
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


    def bounce_tag(tag, argument, contents):
        new_list = [ ] 
        amp, period, speed = 20, 4.0, 1.0
        if argument == "": 
            amp = 20
        else:
            argument = argument.split('-')
            if len(argument) == 1 and argument[0][0].isdigit(): 
                amp = int(argument[0])
            else:
                for arg in argument:
                    if arg[0] == 'a':
                        amp = int(arg[1:])
                    elif arg[0] == 'p':
                        period = float(arg[1:])
                    elif arg[0] == 's':
                        speed = float(arg[1:])

        char_offset = 0  

        my_style = DispTextStyle() 
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:              
                    char_text = Text(my_style.apply_style(char))  
                    char_disp = BounceText(char_text, char_offset, amp=amp, period=period, speed=speed)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp)) 
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = BounceText(my_img, char_offset, amp=amp, period=period, speed=speed)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    char_offset += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))

            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, amp=amp, period=period, speed=speed)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else:
                new_list.append((kind,text))

        return new_list

    def fade_in_tag(tag, argument, contents):
        new_list = [ ]
        my_index, fade_time, slide_distance = 0, 5.0, 100
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


    def scare_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ScareText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = ScareText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    def chaos_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_disp = ChaosText(my_style.apply_style(char))
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list


    def rotate_tag(tag, argument, contents):
        new_list = [ ]

        if argument == "":
            argument = 400
        else:
            argument = int(argument)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = RotateText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = RotateText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    def swap_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return contents
        text1, _, argument = argument.partition("@")
        text2, _, argument = argument.partition("@")
        if len(text1) != len(text2):
            new_list.append((renpy.TEXT_TEXT, "ERROR!"))
        swap_time = float(argument)

        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:

                char_disp = SwapText(my_style.start_tags(), text1, text2, my_style.end_tags(), swap_time)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list


    def move_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = MoveText(char_text)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = MoveText(my_img)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    def paragraph_tag(tag, argument):
        return [(renpy.TEXT_PARAGRAPH, "")]

    def omega_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return contents

        bt_tag = None
        sc_tag = None
        fi_tag = False
        rot_tag = None
        chao_tag = False
        fi_arg_1 = None
        fi_arg_2 = None

        args = [ ]
        arg_count = argument.count('@') 
        for x in range(arg_count): 
            new_arg, _, argument = argument.partition('@')
            args.append(new_arg)
        args.append(argument)

        for arg in args:
            tag, _, value = arg.partition('=')
            if tag == "BT":
                if value != "":
                    bt_tag = value
                else:
                    bt_tag = 10
            elif tag == "SC":
                if value != "":
                    bt_tag = value
                else:
                    bt_tag = 5

            elif tag == "FI":
                fi_tag = True
                str1, _, str2 = value.partition('-')
                fi_arg_1 = int(str1)
                fi_arg_2 = float(str2)
            elif tag == "ROT":
                rot_tag = value
            elif tag == "CH":
                chao_tag = True

        my_style = DispTextStyle()
        my_index = 0
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:

                    if chao_tag:
                        char_disp = ChaosText(my_style.apply_style(char))
                    else:
                        char_disp = Text(my_style.apply_style(char))

                    if bt_tag is not None:
                        char_disp = BounceText(char_disp, my_index, bt_tag)
                    if sc_tag is not None:
                        char_disp = ScareText(char_disp, sc_tag)
                    if fi_tag:
                        char_disp = FadeInText(char_disp, my_index + fi_arg_1, fi_arg_2)
                    if rot_tag is not None:
                        char_disp = RotateText(char_disp, rot_tag)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    config.custom_text_tags["bt"] = bounce_tag
    config.custom_text_tags["fi"] = fade_in_tag
    config.custom_text_tags["sc"] = scare_tag
    config.custom_text_tags["rotat"] = rotate_tag
    config.custom_text_tags["chaos"] = chaos_tag
    config.custom_text_tags["swap"] = swap_tag
    config.custom_text_tags["move"] = move_tag
    config.custom_text_tags["omega"] = omega_tag
    config.self_closing_custom_text_tags["para"] = paragraph_tag
