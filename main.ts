//  On start do a reset
let maxSecondCount = 60
let reset = 1
let secondCounter = maxSecondCount
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    reset = 1
    secondCounter = maxSecondCount
    images.iconImage(IconNames.Yes).showImage(0)
    basic.pause(200)
    images.createImage(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `).showImage(0)
    basic.pause(200)
    images.iconImage(IconNames.Yes).showImage(0)
    basic.pause(200)
    images.createImage(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `).showImage(0)
    basic.pause(200)
    reset = 0
})
basic.forever(function on_forever() {
    
    if (!(secondCounter == 0) && reset == 0) {
        basic.showString("" + ("" + secondCounter))
        basic.pause(1000)
        secondCounter += -1
    } else {
        while (secondCounter == 0) {
            images.createImage(`
                . # # . .
                # . . # .
                # . . # .
                # . . # .
                . # # . .
                `).showImage(0)
            basic.pause(200)
            images.createImage(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `).showImage(0)
            basic.pause(200)
        }
    }
    
})
