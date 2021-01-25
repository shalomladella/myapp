from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem
from kivy.core.window import Window


class MainApp(MDApp):
    def build(self):
        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)
        contacts = ["Shalom", "Srujan", "Sherin", "Swetha"]
        for c in contacts:
            ml.add_widget(
                OneLineListItem(
                    text=c
                )
            )
        return sv


if __name__ == '__main__':
    Window.size = (360, 100)
    MainApp().run()
