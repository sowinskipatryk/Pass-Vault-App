from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_pass(self):
        if not self.ids.loginpass_field.text:
            self.ids.info_label.text = "Empty input field!"
        elif self.ids.loginpass_field.text != '1234':
            self.ids.info_label.text = "Wrong login password!"
            self.ids.loginpass_field.text = ""
        else:
            self.manager.current = "passcheck"

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
