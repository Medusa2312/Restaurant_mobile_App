from kivy.app import App
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy_garden.mapview import MapMarkerPopup
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

Window.size = (400, 700)



class TakeAway(MDScreen):
    def build(self):
        screen_manager.add_widget(Builder.load_file('TakeAway.kv'))
        self.theme_cls.primary_palette = "Teal"


class Restaurant(MDApp):
    marker = MapMarkerPopup(lat=42.48343, lon=3.128874)
    ids = DictProperty({})

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        # mainscreen = Builder.load_file('MainScreen.kv')
        self.title = 'La Vieille Cave'
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = 'Light'
        screen_manager.add_widget(Builder.load_file('SplashScreen.kv'))
        screen_manager.add_widget(Builder.load_file('MainScreen.kv'))
        screen_manager.add_widget(Builder.load_file("TakeAway.kv"))
        screen_manager.add_widget(Builder.load_file("TakeAway_pasta.kv"))
        screen_manager.add_widget(Builder.load_file('Buy_Now.kv'))
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)

    def change_screen(self, dt):
        screen_manager.current = 'MainScreen'

    def switch_screen(self):
        screen_manager.nav_drawer = 'TakeAway'

    def callback(self, btn=Button, icon=''):

        if btn.icon == 'anchor':
            Snackbar(text="La Vieille Cave 12, rue Marius Douzans Banyuls/Mer.").open()
            btn.bind(on_press=lambda x: self.callback)

        elif btn.icon == 'phone-outgoing':
            btn = Button(text=str("06.51.13.47.27"))
            btn.bind(on_press=self.callback)

    def go_to_nav_drawer(self, *args):
        screen_manager.current = "MainScreen"
        # elif button.icon == 'cart':
        # screen_manager.root = 'Payment'

    def add_item(self, pressed=True, btn=Button):
        screen_manager.current = "Buy_Now"
        btn = Button(icon='plus-box-outline', text=1)
        i = 1
        if btn.icon is pressed:
            self.ids.counter.text = 1 + i
            btn.bind(on_press=self.add_item)





Restaurant().run()
