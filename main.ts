// JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-03-C
// Fish animation with create big image and scroll image
let twohalffish = images.createBigImage(`
    . . # . . . . . . .
    . # # . . # . . . .
    # # # # # # . . . .
    . # # . . # . . . .
    . . # . . . . . . .
    `)
basic.forever(function () {
    twohalffish.scrollImage(1, 200)
})
