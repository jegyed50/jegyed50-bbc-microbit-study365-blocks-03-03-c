# JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-03-C
# Fish animation with create big image and scroll image

twohalffish = images.create_big_image("""
    . . # . . . . . . .
        . # # . . # . . . .
        # # # # # # . . . .
        . # # . . # . . . .
        . . # . . . . . . .
""")

def on_forever():
    twohalffish.scroll_image(1, 200)
basic.forever(on_forever)
