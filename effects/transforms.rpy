# Position definitions
transform zero_center:
    xanchor 0.5
    xpos 960

    yanchor 1.0
    ypos 1200

transform zero_left:
    xanchor 0.5
    xpos 480

    yanchor 1.0
    ypos 1200

transform zero_right:
    xanchor 0.5
    xpos 1440

    yanchor 1.0
    ypos 1200

transform zero_right2:
    xanchor 0.5
    xpos 1040

    yanchor 1.0
    ypos 1200

transform zero_left2:
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

transform inactive:
    matrixcolor Matrix([
        0.5, 0, 0, 0,
        0, 0.5, 0, 0,
        0, 0, 0.5, 0,
        0, 0, 0, 1
    ])

transform active:
    matrixcolor IdentityMatrix(0.0)


image rain_layer1 = Movie(channel="rain", play="videos/rain1_mask.webm", mask="videos/rain1.webmhd.webm", framedrop=False, loop=-1)
