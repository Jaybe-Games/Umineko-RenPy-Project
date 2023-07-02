# Position definitions

transform m:
    xalign 0.5
    zoom 0.990
    yanchor 1.0
    ypos 1210

transform l:
    xanchor 0.5
    xpos 525
    zoom 0.995
    yanchor 1.0
    ypos 1210

transform r:
    xanchor 0.5
    xpos 1350
    zoom 0.990
    yanchor 1.0
    ypos 1210

transform r2:
    xanchor 0.5
    xpos 1040
    zoom 0.990
    yanchor 1.0
    ypos 1210

transform r3:
    xanchor 0.5
    xpos 980
    zoom 0.990
    yanchor 1.0
    ypos 1210

transform l2:
    xanchor 0.5
    xpos 880
    zoom 0.990
    yanchor 1.0
    ypos 1210

transform leftedge:
    xanchor 0.5
    xpos 400
    zoom 0.990
    yanchor 1.0
    ypos 1210

transform rightedge:
    xanchor 0.5
    xpos 1500
    zoom 0.990
    yanchor 1.0
    ypos 1210
# Color transforms

transform grayscale:
    matrixcolor SaturationMatrix(0.0)

transform sepia_shader:
    matrixcolor SepiaMatrix()

transform inverse_shader:
    matrixcolor InvertMatrix(1.0)

transform reset_shader:
    matrixcolor IdentityMatrix()


image butterfly1 = Movie(channel="movie", play="videos/butterfly1.mov", Delay=False, loop=False, side_mask=True, image="images/efe/no83_0051.png")
image butterfly1_0 = Movie(channel="movie", play="videos/Butterfly1_0.mov", side_mask=True, Delay=False, loop=False, start_image="images/efe/no83_0051.png")

transform bgani:
    subpixel True
    xoffset 250
    xalign 0.5
    yalign 0.5
    ease 120 xoffset -250
    ease 120 xoffset 250
    repeat

transform rotatebg:
    subpixel True
    zoom 1.65
    xalign 0.5
    yalign 0.5
    rotate 0
    linear 300 rotate 360
    repeat

transform shakezoom:
    subpixel True
    zoom 1.05
    xalign 0.5
    yalign 0.5

transform boatswing:
    subpixel True
    xalign 0.5
    yalign 0.5
    ease 5 xoffset -50
    ease 5 xoffset 50
    repeat

transform normalboat:
    subpixel True
    zoom 1.05
    xalign 0.5
    yalign 0.5
    ease 1.1333333333333334 offset (0, 180)
    ease 1.1333333333333334 offset (0,-25)
    repeat

transform extremboat:
    subpixel True
    zoom 1.05
    xalign 0.5
    yalign 0.5
    ease 0.4333333333333334 offset (0, 180)
    ease 0.4333333333333334 offset (0,-25)
    repeat

transform slowerboat:
    subpixel True
    zoom 1.05
    xalign 0.5
    yalign 0.5
    ease 4.9333333333333334 offset (0, 180)
    ease 4.9333333333333334 offset (0,-25)
    repeat

transform buttondissolvetitle:
    alpha 0.0
    pause 0.5
    ease 0.5 alpha 1.0

transform buttondissolve1:
    subpixel True
    alpha 0.0
    pause 1.0
    ease 0.5 alpha 1.0

transform buttondissolve2:
    subpixel True
    alpha 0.0
    pause 1.5
    ease 0.5 alpha 1.0

transform buttondissolve3:
    subpixel True
    alpha 0.0
    pause 2.0
    ease 0.5 alpha 1.0
transform buttondissolve4:
    subpixel True
    alpha 0.0
    pause 2.5
    ease 0.5 alpha 1.0

transform buttondissolve5:
    subpixel True
    alpha 0.0
    pause 3.0
    ease 0.5 alpha 1.0

transform bganistart:
    subpixel True
    xoffset 250
    xalign 0.5
    yalign 0.5

transform gamemenubuttontransform:
    subpixel True
    xoffset 500
    zoom 0.85
    xalign 0.5
    yalign 0.5
    linear 0.4 xoffset 0

transform hanatoptransform:
    subpixel True
    yoffset -500
    xalign 0.5
    yalign 0.0
    linear 0.4 yoffset 0

transform hanabottomtransform:
    subpixel True
    yoffset 500
    xalign 0.5
    yalign 1.0
    linear 0.4 yoffset 0

transform chapterdissolve:
    alpha 1.0
    pause 3
    ease 0.5 alpha 0.0

