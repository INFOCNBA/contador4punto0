def on_received_number(receivedNumber):
    global cntr
    cntr = receivedNumber
    basic.show_number(cntr)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global cntr
    if cntr < 10:
        cntr += 1
    else:
        cntr += 3
    radio.send_number(cntr)
    basic.show_number(cntr)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global cntr
    while cntr > 0:
        if cntr < 10:
            cntr -= 1
        else:
            cntr -= 3
        radio.send_number(cntr)
        basic.show_number(cntr)

input.on_button_pressed(Button.B, on_button_pressed_b)



cntr = 0
radio.set_group(23)
cntr = 0
basic.show_number(cntr)

def on_forever():
    pass
basic.forever(on_forever)
