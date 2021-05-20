#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 07:35:19 2021
@author: tr
"""

import rospy
from ogretici_paket.srv import GecenZaman

def GecenZamanFonksiyonu(istek):
    robot_hiz = 0.5
    sure = istek.hedef_konum / robot_hiz
    return sure

def cevapGonder():
    rospy.init_node("server_dugumu")
    rospy.Service("Zaman",GecenZaman,GecenZamanFonksiyonu)
    rospy.spin()
    
cevapGonder()