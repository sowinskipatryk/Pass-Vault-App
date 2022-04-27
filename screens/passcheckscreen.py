from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivy.core.clipboard import Clipboard
import string
import sqlite3

characters = string.ascii_letters + string.digits


class PassCheckScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_service(self):
        if not self.ids.service_field.text:
            self.ids.info_service.text = "Empty input field!"
            self.ids.password_field.password = False
            self.ids.password_field.text = ""
        elif any(letter not in characters for letter in self.ids.service_field.text):
            self.ids.info_service.text = "Wrong service name!"
            self.ids.password_field.password = False
            self.ids.password_field.text = ""
        else:
            conn = sqlite3.connect('vault.db')
            c = conn.cursor()
            c.execute("SELECT * FROM services")
            found = False
            for key, value in c.fetchall():
                if key == self.ids.service_field.text:
                    self.ids.password_field.text = value
                    self.ids.password_field.password = True
                    self.ids.info_service.text = ""
                    found = True
            if not found:
                self.ids.info_service.text = "There is no such service!"
                self.ids.password_field.password = False
                self.ids.password_field.text = ""
            conn.commit()
            conn.close()

    def toggle_eye(self):
        if self.ids.eye_pass.icon == 'eye-off':
            self.ids.eye_pass.icon = 'eye'
            self.ids.password_field.password = False
        else:
            self.ids.eye_pass.icon = 'eye-off'
            self.ids.password_field.password = True

    def clipboard_copy(self):
        Clipboard.copy(self.ids.password_field.text)

    def build(self):
        screen = MDScreen()
        return screen
