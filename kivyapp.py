import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from loadTest import load_data
from numpy.random import choice
from functools import partial

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
        self.current_word = self.random_word()
        self.article = self.current_word['article']
        self.word = self.current_word['word']
        self.rows = 5
        self.word_label = Label(text=self.word)
        self.add_widget(self.word_label)

        self.der = Button(text='Der')
        self.der.bind(on_press=partial(self.check_article, article='Der'))
        self.add_widget(self.der)

        self.die = Button(text='Die')
        self.die.bind(on_press=partial(self.check_article, article='Die'))
        self.add_widget(self.die)

        self.das = Button(text='Das')
        self.das.bind(on_press=partial(self.check_article, article='Das'))
        self.add_widget(self.das)

        self.next = Button(text='Nächste')
        self.next.bind(on_press=self.next_word)
        self.add_widget(self.next)

        return

    def random_word(self):
        die_length = len(words['Die'])
        das_length = len(words['Das'])
        der_length = len(words['Der'])
        total_words = float(die_length + das_length + der_length)

        random_article = choice(
            ['Der', 'Die', 'Das'],
            p=[der_length/total_words, die_length/total_words, das_length/total_words]
        )

        word = choice(words[random_article])
        print(word)

        return {'article': random_article, 'word': word}

    def next_word(self, instance):
        self.current_word = self.random_word()
        self.article = self.current_word['article']
        self.word = self.current_word['word']
        self.word_label.text = self.word
        self.der.background_color = [1, 1, 1, 1]
        self.die.background_color = [1, 1, 1, 1]
        self.das.background_color = [1, 1, 1, 1]


    def check_article(self, instance, article):
        if self.article == 'Der':
            self.der.background_color = [0.25, 0.9, 0.2, 0.75]
        if self.article == 'Das':
            self.das.background_color = [0.25, 0.9, 0.2, 0.75]
        if self.article == 'Die':
            self.die.background_color = [0.25, 0.9, 0.2, 0.75]




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
    words = load_data('resources/words.txt')
    german_app = MyApp()
    german_app.run()
