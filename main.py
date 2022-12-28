number = 0

def on_gesture_shake():
    global number
    basic.clear_screen()
    number = randint(1, 6)
    if number == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
