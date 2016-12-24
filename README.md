# Amazon-dash-buttons

## Requirements
* sudo apt-get install tcpdump
* pip install --user scapy

## How to
### Identify new buttons
* python new_dash_identify.py
  * Press the button and its mac address will show up


### Trigger actions 
* modify the file actions_dash.py with the button mac adresses and the actions to trigger
* python actions_dash.py


### Automaticaly launch actions_dash.py at startup
* Modify the file actions_dash
* sudo cp actions_dash /etc/init.d/
* sudo chmod 755 /etc/init.d/actions_dash
* sudo update-rc.d actions_dash defaults (sudo update-rc.d actions_dash remove => remove auto start)

* sudo service actions_dash start => start service
 
