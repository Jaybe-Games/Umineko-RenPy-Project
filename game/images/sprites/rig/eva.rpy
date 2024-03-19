default eva_pose = "a11"
default eva_face = "default1"

layeredimage eva:
    always "/sprites/eva/[eva_pose]/[eva_face]/0.png"

    group mouth:
        attribute eva_001:
            "eva_001"
        attribute eva_002:
            "eva_002"
        attribute eva_003:
            "eva_003"
        attribute eva_idle:
            "eva_idle"

image eva_idle:
    "/sprites/eva/[eva_pose]/[eva_face]/0.png" 