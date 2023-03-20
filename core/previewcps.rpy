init -10 python:
    
    class PreviewSlowText(renpy.Displayable):
        """
        A class to display a preview of the current CPS settings.

        Attributes:
        -----------
        text : string
            The text to display for this displayable preview.
        properties : dict
            Optional keyword arguments that will be applied to the text
            to style it.
        """
        def __init__(self, text, **properties):

            super(PreviewSlowText, self).__init__()

            # Store original arguments for recreating the Text child later
            self.original_text = text
            self.original_properties = properties

            # Text displayable that represents PreviewSlowText.
            self.current_child = self.new_text()

            # The "start time" of the animation
            self.start_st = None
            # The current st of the animation
            self.current_st = 0

        def new_text(self):
            """Create a new Text object with the current CPS."""
            return Text(self.original_text, slow_cps = preferences.text_cps,
                        **self.original_properties)

        def update_cps(self):
            """Update the displayable to show the text at the new CPS."""
            self.current_child = self.new_text()
            self.start_st = self.current_st

        def render(self, width, height, st, at):
            """Render the text to the screen."""

            # Record when this animation is starting
            if self.start_st is None:
                self.start_st = st
            # Keep track of the current st
            self.current_st = st

            # Trigger this function again when possible,
            # to test and/or update all of this stuff again.
            renpy.redraw(self, 0)

            # Create a render (canvas).
            render = renpy.Render(width, height)

            # Calculate the "virtual" start time
            new_st = st - self.start_st

            # Place the Text child onto it, with the adjusted st
            render.place(self.current_child, st = new_st, at = at)

            # Return the render.
            return render