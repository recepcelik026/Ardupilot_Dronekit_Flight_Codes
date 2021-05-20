#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 07:42:24 2021
@author: tr
"""

import rospy
from ogretici_paket.srv import GecenZaman


def istekteBulun():
    rospy.wait_for_service("zaman")
    try:
        servis = rospy.ServiceProxy("zaman",GecenZaman)
        cevap = servis(x)
        return cevap.gecen_sure
    except rospy.ServiceException:
        print("Servisle alakalı hata!")
        
hedef = float(input("Hedef Konumu Giriniz: "))
t = istekteBulun(hedef)
print("Hedefe varana kadar gecen sure: ",t )   




 