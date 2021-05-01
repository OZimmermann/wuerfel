Zahl = 0
while True:
    if input.button_is_pressed(Button.A):
        Zahl = randint(1, 6)
        if Zahl == 1:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        elif Zahl == 2:
            basic.show_leds("""
                . . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                """)
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        elif Zahl == 3:
            basic.show_leds("""
                . . . . #
                . . . . .
                . . # . .
                . . . . .
                # . . . .
                """)
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        elif Zahl == 4:
            basic.show_leds("""
                # . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . #
                """)
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        elif Zahl == 5:
            basic.show_leds("""
                # . . . #
                . . . . .
                . . # . .
                . . . . .
                # . . . #
                """)
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        else:
            basic.show_leds("""
                # . . . #
                . . . . .
                # . . . #
                . . . . .
                # . . . #
                """)
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)