while True:
    print("light level:"+ input.light_level())
    if input.light_level() < 7: 
        light.set_all(light.rgb(255, 255, 255))
    else:
        light.clear()
