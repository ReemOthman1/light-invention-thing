#while True:
    #print("light level:"+ input.light_level())
    #if input.light_level() < 7: 
        #light.set_all(light.rgb(255, 255, 255))
    #else:
        #light.clear()

while True:
    print("light level: " + input.light_level())
    if input.light_level() >5:
        light.set_all(light.rgb(0,0,0))
    else:
        light.set_all(light.rgb(255,255,255))
        light.set_brightness(100)
        pause(3000)