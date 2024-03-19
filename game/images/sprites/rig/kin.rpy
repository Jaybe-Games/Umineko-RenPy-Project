default kin_pose = "a11"
default kin_face = "default1"

layeredimage kin:
    always "/sprites/kin/[kin_pose]/[kin_face]/0.png"

    group mouth:
        attribute kin_001:
            "kin_001"
        attribute kin_002:
            "kin_002"
        attribute kin_003:
            "kin_003"
        attribute kin_idle:
            "kin_idle"

image kin_idle:
    "/sprites/kin/[kin_pose]/[kin_face]/0.png" 