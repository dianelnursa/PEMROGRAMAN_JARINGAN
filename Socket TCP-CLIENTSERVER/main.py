import socket #import socket module
import sys #import socket module

class Utama():
    #percababangan untuk pilihan
    def __init__(self):
        print("masukan pilihan :")
        print("1) server") #pilihan untuk sebagai server
        print("2) Client") #pilihan untuk sebagai client
        print("3) keluar") #pilihan untuk keluar dari semua pilihan

        pilihan = input("pilihan anda adalah :") #inputan pilihan


        # kondisi apabila server
        if pilihan=="1":
            lokasi = socket.gethostbyname("127.0.0.1")
            # menetapkan variabel (sock_stream menadakan pakai socket tcp)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # untuk menghubungkan alamat ip dengan nomor port ke socket sekaligus pendeklarasian penetapan ip localhost dan portnya
            s.bind((lokasi, 2121))
            # jumlah maksimum yaitu 5 koneksi yang dapat ditangani server dari koneksi tcp
            s.listen(5)
            # menampilkan pesan koneksivitas server
            print("server aktif")

            # menerima koneksi yang dikirim dari client.
            client, alamat = s.accept()
            # menampilkan detail koneksi
            print("menerima koneksi dari : ", alamat)
            # kondisi perulangan untuk komunikasi pesan client-server
            while True:
                # decoding pesan server dari socket dengan maksimum bufsize tersebut dalam satu waktu
                data = client.recv(1024).decode()
                if not data: break
                # menampilkan data yg diterima dari client
                print("pesan masuk :", str(data))
                # inputan untuk balas pesan oleh server
                data = input(">")
                # encoding (pengiriman) data server ke socket
                client.send(data.encode())


        #kondisi apabila client
        elif pilihan=="2":
            alamatServer = input("Masukan Alamat Server :")
            # menetapkan variabel (sock_stream menadakan pakai socket tcp)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # konek ke socket/jaringannya
            s.connect((alamatServer, 2121))
            # inputan untuk balas pesan oleh client
            pesan = input(">")
            #kondisi apabila input dari client bernilai bye maka komunikasi client-ser berakhir
            while pesan!="bye":
                # encoding (pengiriman) data client ke socket
                s.send(pesan.encode())
                # Menerima data TCP, data dikembalikan sebagai string
                data = s.recv(1024).decode()
                # menampilkan data yg diterima dari server
                print("server :", data)
                # inputan untuk balas pesan oleh server
                pesan = input(">")
        else:
            quit()

#untuk menyimpan kode yang hanya boleh dijalankan ketika file Anda dieksekusi sebagai skrip,
# Ketika kode dalam file diimpor sebagai modul, kode di dalam pernyataan if tidak dieksekusi.
if __name__ == '__main__':
    Utama()
    sys.exit()


