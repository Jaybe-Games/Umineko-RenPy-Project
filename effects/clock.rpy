##################################---Clock Time---#######################
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade in the clock.
transform rotateshort:
    xanchor 0.5
    yanchor 0.5
    xalign -0.0095
    yalign 0.1
    rotate (timuhour*6)

transform rotatelong:
    xanchor 0.5
    yanchor 0.5
    xalign -0.0365
    yalign 0.05
    rotate (timuminutes*0.5)

transform clock_rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 10 rotate 360
    repeat
transform clock_rotation_h:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 355
    linear 1 rotate 364
transform clock_rotation_m:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 338
    linear 1 rotate 459

transform clock_rotation_h1:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 300
    linear 2 rotate 330
transform clock_rotation_m1:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 2 rotate 360

transform clock_rotation_h2:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 77
    linear 2 rotate 188
transform clock_rotation_m2:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 185
    linear 2 rotate 1560

transform clock_rotation_h3:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 188
    linear 3 rotate 541
transform clock_rotation_m3:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 140
    linear 3 rotate 1480

transform clock_rotation_h4:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 205
    linear 1 rotate 215
transform clock_rotation_m4:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 334
    linear 1 rotate 428

transform clock_rotation_h5:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 230
    linear 1 rotate 245
transform clock_rotation_m5:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 311
    linear 1 rotate 700

transform clock_rotation_h6:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 268
    linear 1 rotate 275
transform clock_rotation_m6:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 99
    linear 1 rotate 160

transform clock_rotation_h7:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 275
    linear 1 rotate 287
transform clock_rotation_m7:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 160
    linear 1 rotate 260

transform clock_rotation_h8:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 313
    linear 1 rotate 318
transform clock_rotation_m8:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 195
    linear 1 rotate 310

transform clock_rotation_h9:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 100
    linear 1 rotate 200
transform clock_rotation_m9:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 1 rotate 900

init offset = -1

screen cinemalogo():
    zorder 999
    add "images/system/cinemalogo.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 780)]

screen clocktimu():
    add "gui/time/clock.png" at Position(xpos = -75, ypos = 14)
    add "gui/time/clock_m.png" at rotatelong
    add "gui/time/clock_h.png" at rotateshort
    add "gui/time/clock_c.png" at Position(xpos = 50, ypos = 145)

screen clocktimu_break():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break1():
    zorder 50
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m1, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h1, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break2():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m2, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h2, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break3():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m3, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h3, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break4():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m4, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h4, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break5():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m5, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h5, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break6():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m6, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h6, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break7():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m7, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h7, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)

screen clocktimu_break8():
    add "gui/time/clock.png" at [alpha_dissolve, Position(xpos = 1000, ypos = 300)]
    add "gui/time/clock_m.png" at [clock_rotation_m8, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_h.png" at [clock_rotation_h8, Position(xpos = 1430, ypos = 727)]
    add "gui/time/clock_c.png" at Position(xpos = 1380, ypos = 700)


screen clocktimu_break_big():
    add "gui/time/clock.png" at alpha_dissolve
    add "gui/time/clock_m.png" at [clock_rotation_m, Position(xpos = 380, ypos = 360)]
    add "gui/time/clock_h.png" at [clock_rotation_h, Position(xpos = 380, ypos = 360)]
    add "gui/time/clock_c.png" at Position(xpos = 335, ypos = 330)
