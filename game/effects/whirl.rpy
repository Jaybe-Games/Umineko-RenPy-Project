init python:

    import math

    renpy.register_shader("whirl_shader", variables="""
        uniform float u_whirl_angle;
    """, fragment_250="""

        // Convert the texture coordinate range from
        // (0 to 1) to (-1 to 1), which makes the math
        // easier.
        vec2 tex_coord = v_tex_coord * 2.0 - 1.0;

        // Figure out how far the coordinate is from the center.
        float l = length(tex_coord);

        // Compute the sin (ws) and cosine (wc) of the angle
        // we whirl this pixel by.
        float ws = sin(l * u_whirl_angle);
        float wc = cos(l * u_whirl_angle);

        // Rotate the coordinates.
        tex_coord.xy = vec2(
            tex_coord.x * wc + tex_coord.y * ws,
            tex_coord.x * -ws + tex_coord.y * wc);

        // Convert back to (0 to 1).
        tex_coord = (tex_coord / 2.0) + 0.5;

        // Look up the coordinate, to find the actual color.
        gl_FragColor = texture2D(tex0, tex_coord);
    """)

transform whirl(old_widget, new_widget):
    # This takes 4 seconds in total.
    delay 5

    # Start with the old child.
    old_widget

    # Describe the mesh and tell Ren'Py to use the shader
    # register above.
    mesh True
    shader "whirl_shader"

    # Start with a 0 angle.
    u_whirl_angle 0.0

    # Over 2 seconds, rotate by 720 degrees.
    # The shader takes radians, where 2 * pi radians are equal
    # to 360 degrees.
    ease 2.0 u_whirl_angle (4 * math.pi)

    # Quickly dissolve to the new child.
    new_widget with Dissolve(.1)

    # As we're doing that, and continuing on, spend 2 seconds
    # going back to no whirl.
    ease 2.0 u_whirl_angle 0.0