import socket #import socket modul
import sys  #import sys

#untuk menyimpan kode yang hanya boleh dijalankan ketika file Anda dieksekusi sebagai skrip
if __name__ == '__main__':
    # mendefinisikan ip yang sama dengan yang ada di server
    host = "127.0.0.1"
    # mendefinisikan port yang harus sama dengan server
    port = 4111

    addr = (host, port)
    
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # untuk mentransmisikan pesan
    while True:
        data = input("Tulis Pesan : ")
        data = data.encode("utf-8")
        c.sendto(data, addr)
    # Untuk menerima pesan
        data, addr = c.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"terkirim ke server : {data}")