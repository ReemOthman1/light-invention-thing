// while True:
// print("light level:"+ input.light_level())
// if input.light_level() < 7: 
// light.set_all(light.rgb(255, 255, 255))
// else:
// light.clear()
while (true) {
    console.log("light level: " + input.lightLevel())
    if (input.lightLevel() > 5) {
        light.setAll(light.rgb(0, 0, 0))
    } else {
        light.setAll(light.rgb(255, 255, 255))
        light.setBrightness(100)
        pause(3000)
    }
    
}
