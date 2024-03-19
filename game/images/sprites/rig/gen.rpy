default gen_pose = "a11"
default gen_face = "default1"

layeredimage gen:
    always "/sprites/gen/[gen_pose]/[gen_face]/0.png"

    group mouth:
        attribute gen_001:
            "gen_001"
        attribute gen_002:
            "gen_002"
        attribute gen_003:
            "gen_003"
        attribute gen_idle:
            "gen_idle"

image gen_idle:
    "/sprites/gen/[gen_pose]/[gen_face]/0.png" 