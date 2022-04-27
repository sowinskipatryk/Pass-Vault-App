from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
import sqlite3

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def validate_pass(self):
        if not self.ids.loginpass_field.text:
            self.ids.info_label.text = "Empty input field!"
        else:
            conn = sqlite3.connect('vault.db')
            c = conn.cursor()
            c.execute("SELECT * FROM admin")
            if self.ids.loginpass_field.text != c.fetchall()[0][0]:
                self.ids.info_label.text = "Wrong login password!"
            else:
                self.manager.current = "passcheck"
            conn.commit()
            conn.close()

    def toggle_eye(self):
        if self.ids.eye_icon.icon == 'eye-off':
            self.ids.eye_icon.icon = 'eye'
            self.ids.loginpass_field.password = False
        else:
            self.ids.eye_icon.icon = 'eye-off'
            self.ids.loginpass_field.password = True

    def build(self):
        screen = MDScreen()
        return screen
