init python:
    renpy.register_shader("breakup", fragment_100="""
    uniform float u_time;
    uniform vec2 u_resolution;
    uniform sampler2D tex0;
    uniform sampler2D tex1;
    const int BREAKUP_DIRECTIONS = 8;
    const vec2 breakup_disp[] = {
        vec2(-7.0, 0.0), vec2(-7.0, 2.0), vec2(-5.0, 4.0), vec2(-4.0, 6.0),
        vec2(-2.0, 7.0), vec2(1.0, 7.0), vec2(3.0, 6.0), vec2(5.0, 5.0)
    };
    uniform int breakup_mode;

    void main() {
        vec2 uv = gl_FragCoord.xy / u_resolution.xy;
        vec4 color1 = texture2D(tex0, uv);
        vec4 color2 = texture2D(tex1, uv);
        
        float frame = u_time * 40.0;  // BREAKUP_MOVE_FRAMES
        float state = 40.0 - frame;   // BREAKUP_MOVE_FRAMES
        
        // Calculate the breakup displacement
        int dir = int(mod(state, float(BREAKUP_DIRECTIONS)));
        vec2 disp = breakup_disp[dir] * (40.0 - state);  // BREAKUP_MOVE_FRAMES

        // Apply breakup effect based on the mode
        if ((breakup_mode & 8) != 0) { // BREAKUP_MODE_JUMBLE
            disp = -disp;
        }
        if ((breakup_mode & 2) == 0) { // BREAKUP_MODE_LEFT
            disp.x = -disp.x;
        }
        if ((breakup_mode & 1) != 0) { // BREAKUP_MODE_LOWER
            disp.y = -disp.y;
        }

        vec2 breakup_uv = uv + disp / u_resolution.xy;
        
        // Todo BreakupMask

        if (mod(gl_FragCoord.x + gl_FragCoord.y, 2.0) > 1.0) {
            gl_FragColor = texture2D(tex1, breakup_uv);
        } else {
            gl_FragColor = texture2D(tex0, uv);
        }
    }
    """)


transform breakup():
        shader "breakup"










