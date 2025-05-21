import time
import threading

def countdown_timer(seconds):
    def run():
        nonlocal seconds  # must be declared before use
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            seconds -= 1
        print("\nTime's up! 🔔")

    thread = threading.Thread(target=run)
    thread.start()

if __name__ == "__main__":
    try:
        duration = int(input("Enter countdown time in seconds: "))
        countdown_timer(duration)
    except ValueError:
        print("Invalid input. Please enter an integer.")
