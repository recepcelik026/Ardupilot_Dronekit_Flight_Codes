#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 02:20:39 2021
@author: tr
"""

import rospy
from ogretici_paket.msg import Bataryadurum
from ogretici_paket.msg import takimnumarasi
from ogretici_paket.msg import IHA_Boylam
from ogretici_paket.msg import IHA_irtifa
from ogretici_paket.msg import IHA_dikilme
from ogretici_paket.msg import IHA_yonelme
from ogretici_paket.msg import IHA_yatis
from ogretici_paket.msg import IHA_hiz
from ogretici_paket.msg import IHA_batarya
from ogretici_paket.msg import IHA_otonom
from ogretici_paket.msg import IHA_kilitlenme
from ogretici_paket.msg import Hedef_Merkez_X
from ogretici_paket.msg import Hedef_Merkez_Y
from ogretici_paket.msg import Hedef_Genislik
from ogretici_paket.msg import Hedef_Yukseklik

def mesajDinle():
    rospy.init_node("Abone_dugumu")
    rospy.Subscriber("takım_numarası",takimnumarasi,takim_fonksiyonu)
    rospy.Subscriber("IHA_Enlem",Bataryadurum,enlem_fonksiyonu)
    rospy.Subscriber("IHA_Boylam",IHA_Boylam,boylam_fonksiyonu)
    rospy.Subscriber("IHA_irtifa",IHA_irtifa,irtifa_fonksiyonu)
    rospy.Subscriber("IHA_dikilme",IHA_dikilme,dikilme_fonksiyonu) 
    rospy.Subscriber("IHA_yonelme",IHA_yonelme,yonelme_fonksiyonu) 
    rospy.Subscriber("IHA_yatis",IHA_yatis,yatis_fonksiyonu)
    rospy.Subscriber("IHA_hiz",IHA_hiz,hiz_fonksiyonu) 
    rospy.Subscriber("IHA_batarya",IHA_batarya,batarya_fonksiyonu) 
    rospy.Subscriber("IHA_otonom",IHA_otonom,otonom_fonksiyonu)
    rospy.Subscriber("IHA_kilitlenme",IHA_kilitlenme,kilitlenme_fonksiyonu) 
    rospy.Subscriber("Hedef_Merkez_X",Hedef_Merkez_X,X_fonksiyonu)
    rospy.Subscriber("Hedef_Merkez_Y",Hedef_Merkez_Y,Y_fonksiyonu)
    rospy.Subscriber("Hedef_Genislik",Hedef_Genislik,Genislik_fonksiyonu) 
    rospy.Subscriber("Hedef_Yukseklik",Hedef_Yukseklik,Yukseklik_fonksiyonu)
    
    rospy.spin() #sürekli dönmeyi saglar    

def takim_fonksiyonu(mesaj):
    rospy.loginfo("takım_numarası: %s" %mesaj.takim)
def enlem_fonksiyonu(mesaj):
    rospy.loginfo("IHA_enlem: %s" %mesaj.batarya)
def boylam_fonksiyonu(mesaj):
    rospy.loginfo("IHA_Boylam: %s" %mesaj.boylam)
def irtifa_fonksiyonu(mesaj):
    rospy.loginfo("IHA_irtifa: %s" %mesaj.irtifa)
def dikilme_fonksiyonu(mesaj):
    rospy.loginfo("IHA_dikilme: %s" %mesaj.dikilme)
def yonelme_fonksiyonu(mesaj):
    rospy.loginfo("IHA_yonelme: %s" %mesaj.yonelme)
def yatis_fonksiyonu(mesaj):
    rospy.loginfo("IHA_yatis: %s" %mesaj.yatis)
def hiz_fonksiyonu(mesaj):
    rospy.loginfo("IHA_hiz: %s" %mesaj.hiz)
def batarya_fonksiyonu(mesaj):
    rospy.loginfo("IHA_batarya: %s" %mesaj.batarya)
def otonom_fonksiyonu(mesaj):
    rospy.loginfo("IHA_otonom: %s" %mesaj.otonom)
def kilitlenme_fonksiyonu(mesaj):
    rospy.loginfo("IHA_kilitlenme: %s" %mesaj.kilitlenme)
def X_fonksiyonu(mesaj):
    rospy.loginfo("Hedef_Merkez_X: %s" %mesaj.X)
def Y_fonksiyonu(mesaj):
    rospy.loginfo("Hedef_Merkez_Y: %s" %mesaj.Y)
def Genislik_fonksiyonu(mesaj):
    rospy.loginfo("Hedef_Genislik: %s" %mesaj.genislik)
def Yukseklik_fonksiyonu(mesaj):
    rospy.loginfo("Hedef_Yukseklik: %s" %mesaj.yukseklik)



mesajDinle()