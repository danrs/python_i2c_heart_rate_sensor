python I2C Heart Rate Sensor
============================

Python library for using the Grove I2C finger-clip heart rate sensor available from Seeed studio. This is a very simple sensor which communicates with the BeagleBone over I2C.

The sensor is a bit temperamental. I've had best results when using it on my fingernail, wrist and earlobe, but your mileage may vary. It often takes about 10 seconds or more for the sensor to start registering a pulse once you place it against your skin.

To install, download this library (git clone or click the download zip button) and place the unzipped contents somewhere handy on your BeagleBone Black or BeagleBone Green. Then cd to the directory of the library and execute the following command:

sudo python setup.py install

Ensure you have internet access so that you can install any required dependancies.

See usage examples in the examples folder.

Heart rate sensors may be purchased as Grove modules from Seeed studio:
With shell and strap:   http://www.seeedstudio.com/depot/Grove-Fingerclip-Heart-Rate-Sensor-with-shell-p-2420.html
PCB only:               http://www.seeedstudio.com/depot/Grove-Fingerclip-Heart-Rate-Sensor-p-2425.html

Note that the sensor is NOT a medical device, and should not be used as such. This software provides no guarantees or safeguards or anything like that, as stipulated in the LICENSE file.

Written by Daniel Smith for UNSW Australia and LaTrobe University.
MIT license and all text above must be included in any redistribution
