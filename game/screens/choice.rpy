screen choice(items):
    style_prefix "choice"

    vbox:
        ## Check saveload.rpy if you wanna know why it's called "fucking_idiot" it's hilarious.
        for fucking_idiot in items:
            textbutton fucking_idiot.caption action fucking_idiot.action