# To ust this example, connect your sensor to I2C2.
# If using a grove module and beaglebone grove cape,
# use the J5 grove socket on the cape. If using the
# beaglebone green, you can use the grove I2C socket
# on the beaglebone.

import time
import python_i2c_heart_rate_sensor as heartsense

sensor = heartsense.heartsense()
while True:
    value = sensor.read()
    print "Heart rate (bpm):",value
    time.sleep(0.2)
