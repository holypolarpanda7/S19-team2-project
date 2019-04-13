# S19-team2-project

## Getting started:

To use this wifi localization Neural Network, you will have to fingerprint any number of locations you desire within the indoor space you wish to map.  To do so you will have to set up a machine that has a wifi card or a wireless dongle at each location to be fingerprinted, so a laptop or other mobile device is recommended.

### Obtain raw data:

There are some very important key words to use here: number of scans, number of training vectors, number of locations, & number of APs...

You choose each of these values based on your needs for this neural network model.  The training data for the NN will need to be set up in a dataset that consists of the label/features vectors.  Here the labels are [loc 0 - your choice], the features are RSSI values from wireless access points(APs).  The trick is that you will have to plan the number of locations according to your environmet and figure out the count of APs that works best for you.

Example vector:
AP1   AP2   AP3   AP4   Loc
[-50,  -74, -66,  -55,   0]

To do so use the WifiInfoView.exe program, if you are on a linux machine you will need 'wine' to run a windows executable.  Keep in mind that if you are using a Jupyter notebook and are on a remote system, you will not be collecting wifi info for your machine.  The db_wifiinfo.bat and db_wifi_bash.ipynb are for windows/linus respectivley and will run the .exe a number of times to produce scans of any location you are at.  Keep in mind that a robust data set is one that is takeover different periods of time because of the nature of signal interference in APs.

You should now be able to take all the raw data neccessary.