init python:
    import random
    import math

    # This will maintain what styles we want to apply and help us apply them
    class DispTextStyle():
        # Notes:
        #   - "" denotes a style tag. Since it's usually {=user_style} and we partition
        #     it over the '=', it ends up being an empty string
        #   - If you want to add your own tags to the list, I recommend adding them
        #     before the ""
        #   - Self-closing tags should not be added here and should be handled
        #     in the text tag function.
        custom_tags = ["bt"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain", 'cps', 'bgm']
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Separate the tag and its info
            # Add tag to dictionary if we accept it
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            # Remove mark tag as cleared if should no longer apply it
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # Go through and apply all the tags
            new_string += self.start_tags()
            # Add the character in the middle
            new_string += char
            # Now close all the tags we opened
            new_string += self.end_tags()
            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""
            # Go through the custom tags
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            # Go through the standard tags
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            # The only tags we are required to end are any custom text tags.
            # And should also end them in the reverse order they were applied.
            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string


    ### TEXT WRAPPER CLASSES ###
    # Basic text displacement demonstration
    class BounceText(renpy.Displayable):
        def __init__(self, child, char_offset, amp=20, period=4.0, speed = 1.0, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(BounceText, self).__init__(**kwargs) # REMEMBER TO RENAME HERE TO YOUR CLASS

            # For all of my classes, I assume I am being passed a displayable
            # of class Text. If you might not, I recommend going with the default of
            # self.child = renpy.displayable(child)
            self.child = child
            self.amp = amp # The amplitude of the sine wave
            self.char_offset = char_offset # The offset into the sine wave
            self.period = period # Affects the distance between peaks in the wave.
            self.speed = speed   # Affects how fast our wave moves as a function of time.

        def render(self, width, height, st, at):
            # Where the current offset is calculated
            # (self.char_offset * -.1) makes it look like the left side is leading
            # We use st to allow this to change over time
            curr_height = math.sin(self.period*((st * self.speed)+(float(self.char_offset) * -.1))) * float(self.amp)

            ####  A Transform can be used for several effects   ####
            # t = Transform(child=self.child,  alpha = curr_height)

            # Create a render from the child.
            # Replace self.child with t to include an alpha or zoom transform
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (0, curr_height))

            renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    ### CUSTOM TAG FUNCTIONS ###
    # Letters move in a sine wave.
    # Arguments are separated by dashes.
    # Arguments:
    # 'a': (int) The amplitude (height) of the text's sine wave motion. How high and low it'll go from it's default position in pixels.
    # 'p': (float) The period of the wave. Distance between peaks in the wave.
    # 's': (float) The speed of the wave. How fast it moves with time.
    # Example: {bt=[height]}Text{/bt}
    # Example: {bt=h5-p2.0-s0.5}Text{/bt}
    # If a lone number is given, it is treated as the amplitude only to ensure backwards compatibility
    # Example: {bt=10}Text{/bt}
    def bounce_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        amp, period, speed = 20, 4.0, 1.0
        if argument == "": # If the argument received is blank, insert a default value
            amp = 20
        else:
            argument = argument.split('-')
            if len(argument) == 1 and argument[0][0].isdigit(): # Default behavior to ensure backward compatibility
                amp = int(argument[0])
            else:
                for arg in argument:
                    if arg[0] == 'a':
                        amp = int(arg[1:])
                    elif arg[0] == 'p':
                        period = float(arg[1:])
                    elif arg[0] == 's':
                        speed = float(arg[1:])

        char_offset = 0 # Since we want our text to move in a wave,
                        # we want to let each character know where it is in the wave.
                        # So they move in harmony. Otherwise they rise and fall all together.
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, amp=amp, period=period, speed=speed) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
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
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, amp=amp, period=period, speed=speed)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    # Some text effects won't allow for a paragraph break if applied to a whole line
    # Which can cause your text to just continue straight off the screen.
    # To amend this, you can insert the {para} tag.
    # This will let the Text displayable holding us know when to wrap.
    # Can also use \n in most cases. But leaving this for people who may already be using it
    # or for cases where \n doesn't work.
    def paragraph_tag(tag, argument):
        return [(renpy.TEXT_PARAGRAPH, "")]

    # This tag is made to automatically wrap several Classes inside one another
    # This is to reduce strain on the render pipeline and memory from nested classes
    # Notes:
    # GradientText and GlitchText are omitted because they were made after the 1.0 release.
    # SwapText and MoveText are omitted for possible issues.
    # SwapText because is not included in this due to it replacing whole sections rather than
    # individual letters. Would be better to embed an Omega inside a SwapText.
    # MoveText because of potential issues of having things like BounceText affect
    # affecting the position of the letter visually.
    # Would be better to have an event call attached to one of those so it can account
    # for the transformations of other tags
    # Argument Notes (all tag args accept same arguments as original tag):
    # BT: BounceText
    # SC: ScareText
    # FI: FadeInText
    # ROT: RotateText
    # CH: ChaosText
    # All tag arguments are seperated by @.
    # Example: {omega=BT=[bt_arg]@SC=[sc_arg]@FI=[fi_arg1]-[fi_arg2]@ROT=[rot_arg]@CH}Text{/omega}

    # Define our new text tags
    config.custom_text_tags["bt"] = bounce_tag
    config.self_closing_custom_text_tags["para"] = paragraph_tag


