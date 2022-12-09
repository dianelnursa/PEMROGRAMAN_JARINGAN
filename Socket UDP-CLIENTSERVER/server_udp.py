import socket  # import socket module
import sys  # import  module sys
import mysql.connector  # import modul akses ke mysql database

# mengkoneksikan python dengan database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="testpython"
)
# untuk menyimpan kode yang hanya boleh dijalankan ketika file Anda dieksekusi sebagai skrip
if __name__ == '__main__':
    # penetapan ip localhost
    host = "127.0.0.1"
    # penetapan port
    port = 4111
    # menetapkan variabel (sock_dgram menadakan pakai socket udp)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # method untuk mengikat alamat(nama host, pasangan nomor port) ke soket.
    s.bind((host, port))

    # menerima pesan data masuk dari client
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        # apabila data bernilai atau pesan itu adalah exit maka koneksi diakhiri
        if data == "exit":
            print("client disconnected.")
            break
        print(f"client : {data}")  # menampilkan data pesan

        # mengeksekusi query atau perintah SQL yang berada di dalam objek db
        cursor = db.cursor()

        # perintah menambahkan field baru ke dalam tabel chatting yang berisi id dan isi_chat, sedangkan "%s" sebagai
        # placeholder untuk value atau data yang akan kita tambahkan agar tidak terkena SQL Injection
        sql = "INSERT INTO chatting (id, isi_pesan) VALUES (%s, %s)"
        # perintah menambahkan data value
        value = ("((INSERT ISNULL(MAX(id)+1, 0) FROM chatting WITH (SERIALIZABLE,UPDLOCK))", data)

        cursor.execute(sql, value)
        # perintah menyimpan query
        db.commit()
        # menkonversi pesan menjadi uppercase (huruf kapital) pengembalian nilai di client
        data = data.upper()
        data = data.encode("utf-8")
        # mentransmisikan pesan data kembali ke koneksi client
        s.sendto(data, addr)
    # Menutup koneksi
    s.close()
