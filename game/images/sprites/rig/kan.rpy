default kan_pose = "a11"
default kan_face = "default1"

layeredimage kan:
    always "/sprites/kan/[kan_pose]/[kan_face]/0.png"

    group mouth:
        attribute kan_001:
            "kan_001"
        attribute kan_002:
            "kan_002"
        attribute kan_003:
            "kan_003"
        attribute kan_idle:
            "kan_idle"

image kan_idle:
    "/sprites/kan/[kan_pose]/[kan_face]/0.png" 