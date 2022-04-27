from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from screens.passcheckscreen import PassCheckScreen
from screens.loginscreen import LoginScreen
from kivy.core.window import Window


class PassVaultApp(MDApp):

    win_size = Window.size = (450, 650)
    Window.minimum_width = win_size[0]
    Window.minimum_height = win_size[1]

    def build(self):
        Builder.load_file('passvault.kv')

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(PassCheckScreen(name='passcheck'))

        return sm


if __name__ == '__main__':
    PassVaultApp().run()
