from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.passcheckscreen import PassCheckScreen
from screens.loginscreen import LoginScreen
from kivy.core.window import Window
import sqlite3


class PassVaultApp(MDApp):

    win_size = Window.size = (450, 650)
    Window.minimum_width = win_size[0]
    Window.minimum_height = win_size[1]

    def build(self):

        conn = sqlite3.connect('vault.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists admin(
        master_key text)
        """)
        c.execute("""CREATE TABLE if not exists services(
        service_name text,
        password text)
        """)
        # c.execute("INSERT INTO admin VALUES ('1234')")
        # c.execute("INSERT INTO services VALUES ('google', 'SuperSecretPassword')")
        # c.execute("INSERT INTO services VALUES ('facebook', 'qwerty')")
        conn.commit()
        conn.close()

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(PassCheckScreen(name='passcheck'))

        return sm


if __name__ == '__main__':
    PassVaultApp().run()
