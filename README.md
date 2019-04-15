# S19-team2-project

## Getting started:

To use this wifi localization Neural Network, you will have to fingerprint any number of locations you desire within the indoor space you wish to map.  To do so you will have to set up a machine that has a wifi card or a wireless dongle at each location to be fingerprinted, so a laptop or other mobile device is recommended.

## Obtain data:

There are some very important key words to use here: number of scans, number of training vectors, number of locations, & number of APs...

You choose each of these values based on your needs for this neural network model.  The training data for the NN will need to be set up in a dataset that consists of the label/features vectors.  Here the labels are [loc 0 - your choice], the features are RSSI values from wireless access points(APs).  The trick is that you will have to plan the number of locations according to your environmet and figure out the count of APs that works best for you.

Example vector:
AP1   AP2   AP3   AP4   Loc
(-50,  -74, -66,  -55,   0)

### Raw data:

To do so use the WifiInfoView.exe program, if you are on a linux machine you will need 'wine' to run a windows executable.  Keep in mind that if you are using a Jupyter notebook and are on a remote system, you will not be collecting wifi info for your machine.  The db_wifiinfo.bat and db_wifi_bash.ipynb are for windows/linus respectivley and will run the .exe a number of times to produce scans of any location you are at.  Keep in mind that a robust data set is one that is takeover different periods of time because of the nature of signal interference in APs.

Because of the tendency for the scans to produce NULL data where a signal has been momentarily lost, it is a good idea to get at least 10 scans per desired vector for the net.  In the provided examples the data is taken continouosly ie (1-max_loc_scans). But one could take 10 scans at each location moving from location to location in order to space them out over time and allow small variance in time for the raw data.

You should now be able to take all the raw data neccessary.

### Process data:

Ensure that the raw data is set up in location folders(named loc_1-MAXLOC), with vector sub folders(named vec_1-MAXVEC), and a number of scans (likey 5-10 named dbXX.csv where XX is 1-MAXSCANS) inside of the vector folders.

If you have continous data as in teh example then you should be able to reuse the data_to_vector.ipynb to sort the vector files.

NOTE: clean_loc_data is a bash file for removing vec_X folders from each loc_X folder quickly.

Once the files are setup correctly, modify the important key word numbers inside of builddata.ipynb and run the script to produce a training set for your Neural Net.

### Conduct a PCA: