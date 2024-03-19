default sha_pose = "a11"
default sha_face = "default1"

layeredimage sha:
    always "/sprites/sha/[sha_pose]/[sha_face]/0.png"

    group mouth:
        attribute sha_001:
            "sha_001"
        attribute sha_002:
            "sha_002"
        attribute sha_003:
            "sha_003"
        attribute sha_idle:
            "sha_idle"

image sha_idle:
    "/sprites/sha/[sha_pose]/[sha_face]/0.png" 