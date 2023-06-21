default menuquit = False
image confirmblack = Solid("#0000005a")

label quit_scene:
    $ menuquit = True
    hide window
    stop music fadeout 1.0
    play sound "audio/sfx/umise_018.ogg"
    scene black zorder 99
    with kanon_rev
    $ renpy.pause(4, hard=True)
    $ Quit(confirm=False)()
    return
init -3 python:
    class QuitWithScene(Action):
        def __call__(self):
            renpy.call_in_new_context("quit_scene")
            renpy.quit()
            return

label title_return:
    hide window
    stop music fadeout 2.0
    play sound "audio/sfx/umise_018.ogg"
    scene black zorder 99
    with kanon_rev
    $ renpy.pause(4, hard=True)
    return
init -3 python:
    class titurnd(Action):
        def __call__(self):
            renpy.call_in_new_context("title_return")
            return

image ctc_blink:
    "GUI/arrow.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

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

    #$ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    #if not list(set(process_list).intersection(stream_list)):
        #if currentuser != "":
            #"Ich weiß wer du bist, dein Name ist [currentuser]"
    #if list(set(process_list).intersection(stream_list)):
        #call stream from _call_stream

    #python:
        #process_list = []
        #currentuser = ""
        #if renpy.windows:
            #try:
                #process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            #except:
                #pass
            #try:
                #for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    #user = os.environ.get(name)
                    #if user:
                        #currentuser = user
            #except:
                #pass

transform bgani:
    subpixel True
    xoffset 250
    xalign 0.5
    yalign 0.5
    linear 120 xoffset -250
    linear 120 xoffset 250
    repeat