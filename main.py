from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class PillApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Welcome to Pillsperfections!', font_size=24)
        layout.add_widget(label)
        return layout


if __name__ == '__main__':
    PillApp().run()
