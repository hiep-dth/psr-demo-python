import os
from pynput import keyboard
import sys
import threading

class Menu:
    def __init__(self):
        self.options = [
            "Send file",
            "Send file by chunk",
            "Send sample data"
        ]
        self.selected = 0
        self.running = True
        
    def display_menu(self):
        os.system('clear')  # Clear console for macOS/Linux
        print("Use arrow keys to navigate, Enter to select:\n")
        for i, option in enumerate(self.options):
            if i == self.selected:
                print(f"> {option}")
            else:
                print(f"  {option}")
    
    def execute_option(self):
        os.system('clear')
        if self.selected == 0:
            print("Executing: Send file")
            # Add your file sending logic here
        elif self.selected == 1:
            print("Executing: Send file by chunk")
            # Add your chunk sending logic here
        elif self.selected == 2:
            print("Executing: Send sample data")
            # Add your sample data sending logic here
        
        input("\nPress Enter to exit...")
    
    def on_press(self, key):  # Fixed method name
        try:
            if key == keyboard.Key.up:
                self.selected = max(0, self.selected - 1)
                self.display_menu()
            elif key == keyboard.Key.down:
                self.selected = min(len(self.options) - 1, self.selected + 1)
                self.display_menu()
            elif key == keyboard.Key.enter:
                self.running = False
                self.execute_option()
                return False  # Stop listener
        except AttributeError:
            pass
    
    def run(self):
        self.display_menu()
        with keyboard.Listener(on_press=self.on_press) as listener:  # Fixed reference
            while self.running:
                pass

def main():
    menu = Menu()
    menu.run()

if __name__ == "__main__":
    main()