
# HOMEWORK 4 --- ES2
# Stopwatch

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Hector Rivera
# NUMBER OF HOURS TO COMPLETE: 3.5
# YOUR COLLABORATION STATEMENT(s): While I didn't work with anyone, i did look for multiple sources of inspiration
#online and tried to follow many tutorials.
#
#
#*****************************************

# Create a micro:bit stopwatch which displays the number
# of seconds that you hold down one of the micro:bit buttons.

# You may wish to accomplish this using a while loop that
# checks whether the button is being pressed. When it is,
# you can update the time elapsed and when it is not, you
# can display that time.

# You will want to make use of the microbit function called
# microbit.running_time() which has a return value of the
# number of milliseconds since the microbit started running.

# You will need to add some while loops and other code in
# order to turn this into a stopwatch that times how long
# the button is held down for.

import microbit
while True:
    microbit.display.scroll("GO")
    time0 = microbit.running_time()
    time1 = microbit.running_time()
    if microbit.button_a.is_pressed() == True:
        while microbit.button_a.is_pressed() == True:
            microbit.display.show(microbit.Image.STICKFIGURE)
            time1 = microbit.running_time()
            elapsed_time = time1 - time0
        timeinseconds = elapsed_time/1000
        microbit.display.scroll(round(timeinseconds, 3))
        microbit.sleep(1000)
        elapsed_time = 0