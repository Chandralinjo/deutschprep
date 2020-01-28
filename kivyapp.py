import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.11.1')


class HomePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2
        self.add_widget(Label(text='Welcome'))

        self.start = Button(text='Start')
        self.start.bind(on_press=self.start_button)
        self.add_widget(self.start)

        return

    def start_button(self, instance):
        german_app.screen_manager.current = 'main'


class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 4
        self.add_widget(Label(text='Proba'))

        self.der = Button(text='Der')
        self.add_widget(self.der)

        self.die = Button(text='Die')
        self.add_widget(self.die)

        self.das = Button(text='Das')
        self.add_widget(self.das)

        return


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.home_page = HomePage()
        screen = Screen(name='home')
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        self.main_page = MainPage()
        screen = Screen(name='main')
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    german_app = MyApp()
    german_app.run()
