define doorfade = Fade(1.0, 1.0, 2.8, color="#fff")
define doorfadeclosed = Fade(3.5, 1.0, 1.0, color="#000000")
define longfade = Fade(1.0, 1.0, 1.5, color="#fff")
define shortfade = Fade(0.5, 0.5, 0.5, color="#fff")
define longdissolve = Dissolve(1.5)
define quickgradientwipeupright = ImageDissolve("/images/masks/upright.png", 1.5, ramplen = 300)
define quickergradientwipeupright = ImageDissolve("/images/masks/upright.png", 0.5, ramplen = 300)
define gradientwipeupright = ImageDissolve("/images/masks/upright.png", 2.0, ramplen = 300)
define gradientwipedownleft = ImageDissolve("/images/masks/downleft.png", 2.0, ramplen = 300)
define doorclose = ImageDissolve("/images/masks/centerblind.png", 3.5, ramplen = 300, reverse = True)
define quickgradientwiperight = ImageDissolve("/images/masks/right.png", 1.0, ramplen = 300)
define quickergradientwiperight = ImageDissolve("/images/masks/right.png", 0.5, ramplen = 300)
define gradientwiperight = ImageDissolve("/images/masks/right.png", 3.5, ramplen = 300)
define quickgradientwipeleft = ImageDissolve("/images/masks/left.png", 1.0, ramplen = 300)
define quickergradientwipeleft = ImageDissolve("/images/masks/left.png", 0.5, ramplen = 300)
define gradientwipeleft = ImageDissolve("/images/masks/left.png", 3.5, ramplen = 300)
define quickgradientwipedown = ImageDissolve("/images/masks/down.png", 0.5, ramplen = 300)
define quickgradientwipeup = ImageDissolve("/images/masks/up.png", 0.5, ramplen = 300)
define gradientwipedown = ImageDissolve("/images/masks/down.png", 1.5, ramplen = 300)
define gradientwipeup = ImageDissolve("/images/masks/up.png", 1.5, ramplen = 300)
define longerdissolve = Dissolve(2.5)
define instant = Dissolve(0)
define gradientcirclefade = ImageDissolve("/images/masks/circle.png", 3.5, ramplen = 300, reverse=True)
define quickgradientcirclefade = ImageDissolve("/images/masks/circle.png", 0.5, ramplen = 300, reverse=True)
define flash = Fade(.25, .25, .50, color="#fff")
define quickflash = Fade(.0, 0.5, 0.25, color="#fff")
define openfade = Fade(1.5, 2.0, 2.0, color="#fff")
define fastdissolve = Dissolve(0.2)
define breakup_mask = Image("images/masks/breakup.png")
define witchfadein = ImageDissolve(breakup_mask,1.5,reverse=False, ramplen = 30)
define witchfadeinslow = ImageDissolve(breakup_mask,3,reverse=False, ramplen = 40)
define witchfadeinq = ImageDissolve(breakup_mask,0.99,alpha=False, ramplen = 40)
define witchfadeout = ImageDissolve(breakup_mask,2,alpha=True,reverse=True, ramplen = 40)
define witchfadeoutq = ImageDissolve(breakup_mask,0.99,alpha=False,reverse=True, ramplen = 40)
define trans1 = ImageDissolve("images/masks/1.png",2,reverse=False, ramplen = 512)
define trans1q = ImageDissolve("images/masks/1.png",.2,reverse=True, ramplen = 512)
define trans1q2 = ImageDissolve("images/masks/1.png",.2,reverse=False, ramplen = 512)
define trans2 = ImageDissolve("images/masks/2.png",2,reverse=False, ramplen = 512)
define kanon_r = ImageDissolve("images/masks/kanon_r.png",3,reverse=False, ramplen = 512)
define kanon_rev = ImageDissolve("images/masks/kanon_r.png",4,reverse=True, ramplen = 256)
define m1trans = ImageDissolve("images/masks/m1.png",1.5,reverse=True, ramplen = 512)
define m1trans1 = ImageDissolve("images/masks/m1.png",2,reverse=True, ramplen = 512)
define m1transb = ImageDissolve("images/masks/m1.png",.1,reverse=True, ramplen = 512)