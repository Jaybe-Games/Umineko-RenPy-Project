# Position definitions
transform m:
    xanchor 0.5
    xpos 960

    yanchor 1.0
    ypos 1200

transform l:
    xanchor 0.5
    xpos 480

    yanchor 1.0
    ypos 1200

transform r:
    xanchor 0.5
    xpos 1440

    yanchor 1.0
    ypos 1200

transform r2:
    xanchor 0.5
    xpos 1040

    yanchor 1.0
    ypos 1200

transform r3:
    xanchor 0.5
    xpos 980

    yanchor 1.0
    ypos 1200

transform l2:
    xanchor 0.5
    xpos 880

    yanchor 1.0
    ypos 1200

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
