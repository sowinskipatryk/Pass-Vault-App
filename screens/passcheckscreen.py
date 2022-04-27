from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivy.core.clipboard import Clipboard
import string
# from __package import decrypt

passes = {
    'google': 'SuperStrongPass',
    'facebook': 'qwerty',
}

characters = string.ascii_letters + string.digits


class PassCheckScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_service(self):
        try:
            if not self.ids.service_field.text:
                self.ids.info_service.text = "Empty input field!"
                self.ids.password_field.password = False
                self.ids.password_field.text = ""
            elif any(letter not in characters for letter in self.ids.service_field.text):
                self.ids.info_service.text = "Wrong service name!"
                self.ids.password_field.password = False
                self.ids.password_field.text = ""
            else:
                self.ids.password_field.text = passes[str(self.ids.service_field.text).lower()]
                self.ids.password_field.password = True
                self.ids.info_service.text = ""
        except KeyError:
            self.ids.info_service.text = "There is no such service!"
            self.ids.password_field.password = False
            self.ids.password_field.text = ""
        except ValueError:
            self.ids.info_service.text = "Wrong service name!"
            self.ids.password_field.password = False
            self.ids.password_field.text = ""

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