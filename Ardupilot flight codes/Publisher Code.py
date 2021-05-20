#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor
Publisher-Subscriber
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

def mesajYayinla():
    rospy.init_node("yayinci_dugumu")
    pub = rospy.Publisher("takım_numarası",takimnumarasi,queue_size=10)
    pub = rospy.Publisher("IHA_Enlem",Bataryadurum,queue_size=10) 
    pub = rospy.Publisher("IHA_Boylam",IHA_Boylam,queue_size=10) 
    pub = rospy.Publisher("IHA_irtifa",IHA_irtifa,queue_size=10)
    pub = rospy.Publisher("IHA_dikilme",IHA_dikilme,queue_size=10) 
    pub = rospy.Publisher("IHA_yonelme",IHA_yonelme,queue_size=10) 
    pub = rospy.Publisher("IHA_yatis",IHA_yatis,queue_size=10)
    pub = rospy.Publisher("IHA_hiz",IHA_hiz,queue_size=10) 
    pub = rospy.Publisher("IHA_batarya",IHA_batarya,queue_size=10) 
    pub = rospy.Publisher("IHA_otonom",IHA_otonom,queue_size=10)
    pub = rospy.Publisher("IHA_kilitlenme",IHA_kilitlenme,queue_size=10) 
    pub = rospy.Publisher("Hedef_Merkez_X",Hedef_Merkez_X,queue_size=10)
    pub = rospy.Publisher("Hedef_Merkez_Y",Hedef_Merkez_Y,queue_size=10)
    pub = rospy.Publisher("Hedef_Genislik",Hedef_Genislik,queue_size=10) 
    pub = rospy.Publisher("Hedef_Yukseklik",Hedef_Yukseklik,queue_size=10)
    
    
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        takim = "1"
        durum = "433.5"
        boylam = "222.3"
        irtifa = "222.3"
        dikilme = "5"
        yonelme = "256"
        yatis = "0"
        hiz = "223"
        batarya = "20"
        otonom = "0"
        kilitlenme = "1"
        X = "315"
        Y = "220"
        genislik = "12"
        yukseklik = "46"
        rospy.loginfo(takim)
        pub.publish(takim)
        rospy.loginfo(durum)
        pub.publish(durum)
        rospy.loginfo(boylam)
        pub.publish(boylam)
        
        rospy.loginfo(irtifa)
        pub.publish(irtifa)
        rospy.loginfo(dikilme)
        pub.publish(dikilme)
        rospy.loginfo(yonelme)
        pub.publish(yonelme)
        rospy.loginfo(yatis)
        pub.publish(yatis)
        rospy.loginfo(hiz)
        pub.publish(hiz)
        rospy.loginfo(batarya)
        pub.publish(batarya)
        rospy.loginfo(otonom)
        pub.publish(otonom)
        rospy.loginfo(kilitlenme)
        pub.publish(kilitlenme)
        rospy.loginfo(X)
        pub.publish(X)
        rospy.loginfo(Y)
        pub.publish(Y)
        rospy.loginfo(genislik)
        pub.publish(genislik)
        rospy.loginfo(yukseklik)
        pub.publish(yukseklik)
        rate.sleep()
        
mesajYayinla()