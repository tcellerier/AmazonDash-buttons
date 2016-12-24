#!/usr/bin/python
# -*- coding: utf-8 -*-

# Script d'identification des nouveaux boutons Amazon dash
# Autre possibilité : exécuter sudo tcpdump port 67 or port 68 -e -n

# script requires:
# library scapy: pip install --user scapy
# sudo apt-get install tcpdump

from scapy.all import *
import time


def button_detect(pkt):

    if not pkt.haslayer(Ether):
        return

    print ""
    print time.strftime('%X ') + pkt.summary() # affiche l'heure et un résumé du paquet
   
    print "New button: " + pkt[Ether].src


# filtre sur les 2 verisions :
#  Bouton v1 : 1 ARP request from 0.0.0.0
#  Bouton v2 : 2 DHCP requests from 0.0.0.0 first, followed by ARP requests for other network devices (e.g. the gateway) using the IP address they have been assigned
#                NB : Les DHCP requests ne sont pas réémises si le bouton est repressé trop rapidement 
def startSniff():
	print sniff(prn=button_detect, filter="(arp or (udp and src port 68 and dst port 67)) and src host 0.0.0.0", store=0)



if __name__ == '__main__':
	startSniff()