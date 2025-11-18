from threading import Thread, Lock
import sys
import time

# lock for synchronizing console output
console_lock = Lock()

def animate_text(text, delay=0.05): 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    with console_lock:
        animate_text(lyric, speed)

def sing_song():
    lyric = [
        ("Tante...", 0.08),
        ("Sudah terbiasa terjadi tante...", 0.09),
        ("Teman datang ketika lagi butuh saja...", 0.10),
        ("Coba kalau lagi susah...", 0.15),
        ("Mereka semua menghilaaaang...", 0.15)
    ]
    delay = [0.3, 2.5, 5.8, 9.5, 13.5]
        
    threads = [] 

    for i in range(len(lyric)): 
        line, speed = lyric[i]
        t = Thread(target=sing_lyric, args=(line, delay[i], speed))
        threads.append(t) 
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()