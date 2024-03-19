default bea_pose = "a11"
default bea_face = "default1"

layeredimage bea:
    always "/sprites/bea/[bea_pose]/[bea_face]/0.png"

    group mouth:
        attribute bea_001:
            "bea_001"
        attribute bea_002:
            "bea_002"
        attribute bea_003:
            "bea_003"
        attribute bea_idle:
            "bea_idle"

image bea_idle:
    "/sprites/bea/[bea_pose]/[bea_face]/0.png" 



