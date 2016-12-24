#!/usr/bin/python
# -*- coding: utf-8 -*-

# script requires:
# library scapy: pip install --user scapy
# sudo apt-get install tcpdump

from scapy.all import * 
import time
import os



############# PARAMETRES #############

buttons = { 'but1': 'ab:64:bd:25:57:51', 'But2': '45:63:01:b2:59:Bf'}

#######################################



def button_detect(pkt):
   
    if not pkt.haslayer(Ether):
        return

    min_delay = 2.5    # delai minimum en secondes pour la prise en compte d'un nouveau paquet
    mac = pkt[Ether].src
    if not (mac in lasttime):   # 1ere fois que le boutton est pressé
        delay_lastpush = 999
    else:
        delay_lastpush = time.time() - lasttime[mac]


    if delay_lastpush >= min_delay:
        lasttime[mac] = time.time()
        
        # actions des boutons
        if mac == buttons['but1']:
            print "\n" + time.strftime('%X ') + "Bouton 1déclenché"
           
        elif mac == buttons['but2']:
            print "\n" + time.strftime('%X ') + "Bouton 2 déclenché"

    else:
        print "delay too short between 2 packets: " + str(delay_lastpush) + " sec. (min " + str(min_delay) + "s)" 



def startSniff():

    global lasttime
    lasttime = {}

    sniff_filters = " or ".join(["ether host " + buttons[button] for button in buttons]) # filtre uniquement sur les adresses mac des boutons
    print(sniff(prn=button_detect, filter=sniff_filters, store=0))



if __name__ == '__main__':
    startSniff()


