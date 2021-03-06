# Loading EGG model
# =================
# This example - Copyright (c) 2012 - Tim Skillman
# EGG loader code by Paddy Gaunt, Copyright (c) 2012
# Version 0.02 - 20Jul12

import pi3d

# Setup display and initialise pi3d
display = pi3d.display(100,100,1200,900)
display.setBackColour(0.2,0.4,0.6,1)    # r,g,b,alpha

# load model_loadmodel
texs = pi3d.textures()
mymodel = pi3d.loadModel("models/Triceratops/Triceratops.egg",texs,"Triceratops", 0,-1,-40, -90,0,0, .005,.005,.005)
    
# Fetch key presses
mykeys = pi3d.key()

#create a light
mylight = pi3d.createLight(0,1,1,1,"",10,10,0)
mylight.on()
    
while 1:
    display.clear()

    mymodel.draw()
    mymodel.rotateIncY(3)
    
    k = mykeys.read()
    if k >-1:
        if k==112: display.screenshot("Triceratops.jpg")
        elif k==27:
            mykeys.close()
            texs.deleteAll()
            display.destroy()
            break
        else:
            print k
 
    display.swapBuffers()
