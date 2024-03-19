default but_pose = "a11"
default but_face = "default1"

layeredimage but:
    always "/sprites/but/[but_pose]/[but_face]/0.png"

    group mouth:
        attribute but_001:
            "but_001"
        attribute but_002:
            "but_002"
        attribute but_003:
            "but_003"
        attribute but_idle:
            "but_idle"

image but_idle:
    "/sprites/but/[but_pose]/[but_face]/0.png" 