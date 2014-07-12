littlebits-gesture-synth
========================

Create live music experiences using in-air gestures: use your hand to control the audio filter on the Korg Synth kit.


python setup
--------
* get python installed (I tested with 2.7.2)
* install the requests library, preferably with PIP: "pip install requests" (http://docs.python-requests.org/en/latest/user/install/)

clone this repo & configure
--------
* update your device ID and the bearer authorization in this file: "/python/myrequest.py"
  * Littlebits cloud documentation: http://developer.littlebitscloud.cc/api-http
    * click "Find out how to get your access token here" for instructions

leap motion
--------
* connect leap motion. use one of the standard leapmotion apps to verify it's working

go!
--------
* open terminal and run: "python Sample.py"
