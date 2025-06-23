from kivy.app import App
from kivy.uix.label import Label

class PillsperfectionsApp(App):
    def build(self):
        return Label(text="Hello from Pillsperfections!")

if __name__ == '__main__':
    PillsperfectionsApp().run()
