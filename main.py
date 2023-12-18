
# On start do a reset
maxSecondCount = 60
reset = 1
secondCounter = maxSecondCount

def on_gesture_shake():
    global reset, secondCounter
    reset = 1
    secondCounter = maxSecondCount
    images.icon_image(IconNames.YES).show_image(0)
    basic.pause(200)
    images.create_image("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """).show_image(0)
    basic.pause(200)
    images.icon_image(IconNames.YES).show_image(0)
    basic.pause(200)
    images.create_image("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """).show_image(0)
    basic.pause(200)
    reset = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global secondCounter
    if not (secondCounter == 0) and reset == 0:
        basic.show_string("" + str((secondCounter)))
        basic.pause(1000)
        secondCounter += -1
    else:
        while secondCounter == 0:
            images.create_image("""
                . # # . .
                # . . # .
                # . . # .
                # . . # .
                . # # . .
                """).show_image(0)
            basic.pause(200)
            images.create_image("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """).show_image(0)
            basic.pause(200)
basic.forever(on_forever)
