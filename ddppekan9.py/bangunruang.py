import math 

def kubus (sisi):
    luas = 6*sisi**2
    print("luas permukaan kubus dengan sisi",sisi,"adalah",luas)
def balok (panjang, lebar, tinggi):
    luas = 2*((panjang*lebar)+(panjang*tinggi)+(tinggi*lebar))
    print("luas permukaan balok dengan panjang",panjang,",lebar",lebar,"dan tinggi",tinggi,"adalah",luas)
def tabung (r, tinggi):
    luas = 2*math.pi*r*(r+tinggi)
    print("luas permukaan tabung dengan jari-jari",r,"dan tinggi",tinggi,"adalah",luas)
def kerucut (r, tinggi):
    luas = 1/3*math.pi*r**2*tinggi
    print("luas permukaan kerucut dengan jari-jari",r,"dantinggi",tinggi,"adalah",luas)
def bola (r):
    luas = 4*math.pi*r**2
    print("luas permukaan bola dengan jari-jari",r,"adalah",luas)