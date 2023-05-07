init python:
    
    import random
    
    random.seed()
    
    def Rain(image, min_particles=1000, max_particles=1500, speed=5000, wind=0, xborder=(0,100), yborder=(2000,3000), **kwargs):

        return Particles(SnowFactory(image, min_particles, max_particles, speed, wind, xborder, yborder, **kwargs))

    def Rain2(image, min_particles=1000, max_particles=1500, speed=4000, wind=0, xborder=(0,100), yborder=(2000,3000), **kwargs):

        return Particles(SnowFactory(image, min_particles, max_particles, speed, wind, xborder, yborder, **kwargs))

    def Rain3(image, min_particles=1000, max_particles=1500, speed=3000, wind=0, xborder=(0,100), yborder=(2000,3000), **kwargs):

        return Particles(SnowFactory(image, min_particles, max_particles, speed, wind, xborder, yborder, **kwargs))

    def Rain4(image, min_particles=1000, max_particles=1500, speed=2500, wind=0, xborder=(0,100), yborder=(200,3000), **kwargs):

        return Particles(SnowFactory(image, min_particles, max_particles, speed, wind, xborder, yborder, **kwargs))
    

    class SnowFactory(object):

        def __init__(self, image, min_particles, max_particles, speed, wind, xborder, yborder, **kwargs):
         

            self.max_particles = max_particles
            self.speed = speed
            self.wind = wind
            
            self.xborder = xborder
            self.yborder = yborder
            
            self.depth = kwargs.get("depth", 10)
            
            self.image = self.image_init(image)

            self.min_particles = min_particles
            

        def create(self, particles, st):

            if particles is None or len(particles) < self.max_particles:
            
                if len(particles) < self.min_particles:
                    return [ SnowParticle(self.image[0],
                            random.uniform(-self.wind, self.wind),
                            self.speed,
                            random.randint(self.xborder[0], self.xborder[1]),
                            random.randint(self.yborder[0], self.yborder[1]),
                            ) ]
                
                depth = random.randint(1, self.depth)
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],
                                    random.uniform(-self.wind, self.wind)*depth_speed,
                                    self.speed*depth_speed, 
                                    random.randint(self.xborder[0], self.xborder[1]),
                                    random.randint(self.yborder[0], self.yborder[1]),
                                    ) ]
        
        
        def image_init(self, image):

            rv = [ ]
            
            for depth in range(self.depth):
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):

            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):

        def __init__(self, image, wind, speed, xborder, yborder):

            self.image = image
            
            if speed <= 0:
                speed = 1
                
            self.wind = wind
            
            self.speed = speed

            self.oldst = None
                      
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            if self.ypos > renpy.config.screen_height or\
            (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None

            return int(self.xpos), int(self.ypos), st, self.image

init:
    image rain = Rain("/images/system/drop.png")
    image rain2 = Rain2("/images/system/drop2.png")
    image rain3 = Rain3("/images/system/drop3.png")
    image rain4 = Rain4("/images/system/drop4.png")
