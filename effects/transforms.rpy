# Position definitions
transform m:
    xalign 0.5
    zoom 0.995
    yanchor 1.0
    ypos 1202

transform l:
    xanchor 0.5
    xpos 525
    zoom 0.995
    yanchor 1.0
    ypos 1202

transform r:
    xanchor 0.5
    xpos 1350
    zoom 0.995
    yanchor 1.0
    ypos 1202

transform r2:
    xanchor 0.5
    xpos 1040
    zoom 0.995
    yanchor 1.0
    ypos 1202

transform r3:
    xanchor 0.5
    xpos 980
    zoom 0.995
    yanchor 1.0
    ypos 1202

transform l2:
    xanchor 0.5
    xpos 880
    zoom 0.995
    yanchor 1.0
    ypos 1202

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
