radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    cntr = receivedNumber
    basic.showNumber(cntr)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (cntr < 10) {
        cntr += 1
    } else {
        cntr += 3
    }
    
    radio.sendNumber(cntr)
    basic.showNumber(cntr)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    while (cntr > 0) {
        if (cntr < 10) {
            cntr -= 1
        } else {
            cntr -= 3
        }
        
        radio.sendNumber(cntr)
        basic.showNumber(cntr)
    }
})
let cntr = 0
radio.setGroup(23)
cntr = 0
basic.showNumber(cntr)
basic.forever(function on_forever() {
    
})
