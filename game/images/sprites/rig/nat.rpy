default nat_pose = "a11"
default nat_face = "default1"

layeredimage nat:
    always "/sprites/nat/[nat_pose]/[nat_face]/0.png"

    group mouth:
        attribute nat_001:
            "nat_001"
        attribute nat_002:
            "nat_002"
        attribute nat_003:
            "nat_003"
        attribute nat_idle:
            "nat_idle"

image nat_idle:
    "/sprites/nat/[nat_pose]/[nat_face]/0.png" 