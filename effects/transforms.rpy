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

init python:
    config.layers = ['black', 'master', 'curtain', 'transient', 'screens', 'overlay']

image black_background = Solid(Color('#000'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
image black_cover = Solid(Color('#000'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
image white_cover = Solid(Color('#fff'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
image red_cover = Solid(Color('#e11'), xalign=0.5, yalign=0.5, xzoom=2.0, yzoom=2.0)
