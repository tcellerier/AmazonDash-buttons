# Amazon-dash-buttons

## Requirements
* sudo apt-get install tcpdump
* pip install --user scapy
* Set up the buttons with Amazon app but stop at the product configuration page
* interface mon0 in monitor mode. See https://github.com/seemoo-lab/nexmon

## How to
### Identify new buttons
* sudo python amazondash_identify_new.py
  * Press the button and its mac address will show up


### Trigger actions 
* modify the file amazondash.py with the button mac adresses and the actions you want to trigger
* sudo python amazondash.py


### Automaticaly launch amazondash.py at startup
* Modify the file amazondash
* sudo cp amazondash /etc/init.d/
* sudo chmod 755 /etc/init.d/amazondash
* sudo update-rc.d amazondash defaults (sudo update-rc.d amazondash remove => remove auto start)

* To start the service immediately : sudo service amazondash start 
 
 
 ### Update v2 ###
 Mode completely offline: the button never connects to the internet. It requires a wifi interface in Monitor mode (mon0).
 Steps: Setup the button to your wifi to find the Mac address and then set it up to a fake wifi (like your phone AP).
 =>  Now the hack is completely invisible to Amazon
