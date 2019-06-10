# S19-team2-project

## Motivation:

In todays world we are more and more reliant on GPS and navigation to keep pace with demands at work and home.  Our current GPS technology relies on microwaves, which are very broad signals.  This means that the accuracy of GPS is only precise to about 10 meters most of the time.  The signals are attenuated further by dense structures, like mountains and buildings.  We propose a way to use platforms that are readily available to provide indoor wireless localization.  We propose, the use of a wirless card/dongle, a feed forward neural network, and an evironment with at least a few wireless access points to achieve this goal in earnest.  This method has the potential to increase the effectivness of indoor navigation greatly.

## Installing:

#### Python 3 
Python 3 can be found at https://python.org/downloads/

#### Jupyter Notebook
Jupyter Notebook can be found at https://jupyter.org/install

#### Wine
Wine (windows executables on non-windows OS)found at
https://wiki.winehq.org/Wine_Installation_and_Configuration

## Getting started:

To use this wifi localization Neural Network, you will have to fingerprint any number of locations you desire within the indoor space you wish to map.  To do so you will have to set up a machine that has a wifi card or a wireless dongle at each location to be fingerprinted, so a laptop or other mobile device is recommended.

## Obtain data:

There are some very important key words to use here: number of scans, number of training vectors, number of locations, & number of APs...

You choose each of these values based on your needs for this neural network model.  The training data for the NN will need to be set up in a dataset that consists of the label/features vectors.  Here the labels are [loc 0 - your choice], the features are RSSI values from wireless access points(APs).  The trick is that you will have to plan the number of locations according to your environmet and figure out the count of APs that works best for you.

Example vector-

AP1  | AP2 | AP3  | AP4 | AP5 |  location  
----:|----:| ----:|----:|----:|----------:
-50  | -74 | -66  | -55 | -60 |0          |

### Raw data:

To do so use the WifiInfoView.exe program, if you are on a linux machine you will need 'wine' to run a windows executable.  Keep in mind that if you are using a Jupyter notebook and are on a remote system, you will not be collecting wifi info for your machine.  The db_wifiinfo.bat and db_wifi_bash.ipynb are for windows/linus respectivley and will run the .exe a number of times to produce scans of any location you are at.  Keep in mind that a robust data set is one that is takeover different periods of time because of the nature of signal interference in APs.

Because of the tendency for the scans to produce NULL data where a signal has been momentarily lost, it is a good idea to get at least 10 scans per desired vector for the net.  The data collection process for this experiment produced about 1500 viable training vectors out of 3000, so it is safe to assume about a 50% effieciency in data collection.  In the provided examples the data is taken continuosly ie (1-max_loc_scans). But one could take 200 scans at each location moving from location to location in order to space them out over time and allow small variance in time for the raw data.  For best results the data should be taken over the period of a few days with dynamic AP interations (bistandards with cell phones).

You should now be able to take all the raw data neccessary.

### Process data:

Ensure that the raw data is set up in location folders(named loc_1-MAXLOC),and a number of scans (likey 1000-2000 named dbXX.csv where XX is 1-MAXSCANS) inside of the location folders.  In these examples there are vector sub folders that can be ignored.

NOTE: clean_loc_data is a bash file for removing vec_X folders from each loc_X folder quickly.  And many processing tools here are from experimentation.

Once the files are setup correctly, modify the important key word numbers inside of Data_preproccesssing_correst.ipynb and run the script to produce a training set for your Neural Net.

### Conduct a PCA:

open up demo_net.ipynb in the demo folder to continue with tutorial...
https://github.com/CSCI4850/S19-team2-project/blob/master/Demo/demo_net.ipynb

If this page does not load correctly it is because git can have trouble loading .ipynb files.
You can open and view these files by following these steps...

Open "https://nbviewer.jupyter.org/"
Paste the link to your notebook, (e.g. "https://github.com/CSCI4850/S19-team2-project/blob/master/Demo/demo_net.ipynb") there and then you get "https://nbviewer.jupyter.org/github/CSCI4850/S19-team2-project/blob/master/Demo/demo_net.ipynb"