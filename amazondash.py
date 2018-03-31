#!/usr/bin/python
# -*- coding: utf-8 -*-

# script requires:
# library scapy: pip install --user scapy
# sudo apt-get install tcpdump

from scapy.all import * 
from datetime import datetime
import os



############# PARAMETRES #############

buttons = { 'but1': 'ab:64:bd:25:53:40', 'but2': '45:63:01:b2:56:AA'}

#######################################



def button_detect(pkt):
 
    global lasttime

    # Show all the packet
    # print(pkt.show()) 

    # Lecture de l'adresse mac dans le paquet
    mac = ""
    if pkt.haslayer(Ether):
        mac = pkt[Ether].src
    elif  pkt.haslayer(Dot11): # Layer 802.11
        mac = pkt[Dot11].addr2

    if mac == "":
        return

    min_delay = 8    # delai minimum en secondes pour la prise en compte d'un nouveau paquet. min 3, 10 si en le bouton est connectée sur le réseau. 8 sinon
    now = datetime.now()
    
    if not (mac in lasttime):   # 1ere fois que le boutton est pressé
        delay_lastpush = 999
    else:
        delay_lastpush = (now - lasttime[mac]).total_seconds() # nombre de secondes.microsecondes

    print str(now)
    if delay_lastpush >= min_delay:
        lasttime[mac] = now
        
        # actions des boutons
        if mac == buttons['but1']:
            print "\n" + now.strftime('%X ') + "Bouton 1 déclenché"
           
        elif mac == buttons['but2']:
            print "\n" + now.strftime('%X ') + "Bouton 2 déclenché"

    else:
        print "delay too short between 2 packets: " + str(delay_lastpush) + " sec. (min " + str(min_delay) + "s)" 




def initSniff():
    global lasttime, sniff_filters
    lasttime = {} # On initialise la variable lasttime 
    sniff_filters = " or ".join(["ether src host " + buttons[button] for button in buttons])  # filtre uniquement sur les adresses mac des boutons


def startSniff(iface = "eth0"):
    print("Sniffing started on %s ..." % iface)
    print(sniff(iface=iface, prn=button_detect, filter=sniff_filters, store=0))



if __name__ == '__main__':
    initSniff()
    startSniff('mon0')
