default persistent.wiki_unlocked = { "wiki_index" }

init python:

    def locked_handler(target):
        renpy.run(ShowMenu(target))

    def locked_sensitive(target):
        return target in persistent.wiki_unlocked

    config.hyperlink_handlers["locked"] = locked_handler
    config.hyperlink_sensitive["locked"] = locked_sensitive

define config.hyperlink_protocol = "locked"
define gui.hyperlink_text_insensitive_color = gui.insensitive_color