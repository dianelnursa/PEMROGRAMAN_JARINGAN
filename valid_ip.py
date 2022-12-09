import socket as skt
from binascii import hexlify
import ipaddress

print("\n============ TUGAS 02 DESEMBER 2022 ================")
print("NAMA: DIAN BUDI ELNURSA \nNIM: 200631100060\n==================================\n")
print("SOAL:\n 1. Tambahkan ip 0.0.0.0 jika dapat ip trsebut maka ip buktikan valid atau tidak valid, jika tidak valid tida perlu melakukan konversi.\n     Namun, Jika Valid lakukan juga beserta konversi\n 2. jika ada ip 192.168.0.256 maka ip tidak valid")
print("\nJAWAB:")

def TgsProgjar(ip_addr):
    ip = ip_addr.split(".")
    if len(ip) == 4:
        for i in ip:
            try:
                i = int(i)
                if 0 <= i <= 255:
                    pass
                else:
                    return False
            except:
                return False
    else:
        return False
    return True

list_ip = ['0.0.0.0', '192.168.0.256', '192.168.0.1',  '127.0.0.1.1']
for i in list_ip:
    if TgsProgjar(i):
        package_addr = skt.inet_aton(i)
        print("\nIP Address: {} \n => Status : valid Ip address \n =>".format(i), hexlify(package_addr))
    else:
        print("\nIP Address: {} \n => Status : Invalid Ip address".format(i))
