from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.utils import platform

# Solo redimensionar en escritorio, no en Android
if platform != 'android':
    Window.size = (360, 640)

# Interfaz gráfica en lenguaje KV
KV = '''
ScreenManager:
    id: sm
    CalcScreen:
    HistoryScreen:

<CalcScreen>:
    name: "calc"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Kuromi Calculadora"
            left_action_items: [["calculator", lambda x: None]]
            right_action_items: [["history", lambda x: app.switch_to_history()]]
            elevation: 2
            md_bg_color: 1, 0, 0, 1

        MDFloatLayout:
            size_hint_y: 0.35

            # Cambiado a Image local usando kuromi.png
            Image:
                id: kuromi_img
                source: "kuromi.png"
                size_hint: None, None
                size: "180dp", "180dp"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                allow_stretch: True
                keep_ratio: True

        MDBoxLayout:
            size_hint_y: 0.15
            padding: ["20dp", "10dp"]
            md_bg_color: 1, 1, 1, 1
            MDLabel:
                id: display
                text: "0"
                halign: "right"
                valign: "center"
                font_style: "H3"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                bold: True

        MDGridLayout:
            cols: 4
            spacing: "8dp"
            padding: "16dp"
            size_hint_y: 0.50

            MDFillRoundFlatButton:
                text: "AC"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.clear_all()
            MDFillRoundFlatButton:
                text: "C"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.delete_last()
            MDFillRoundFlatButton:
                text: "("
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("(")
            MDFillRoundFlatButton:
                text: ")"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display(")")

            MDFillRoundFlatButton:
                text: "7"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("7")
            MDFillRoundFlatButton:
                text: "8"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("8")
            MDFillRoundFlatButton:
                text: "9"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("9")
            MDFillRoundFlatButton:
                text: "/"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("/")

            MDFillRoundFlatButton:
                text: "4"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("4")
            MDFillRoundFlatButton:
                text: "5"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("5")
            MDFillRoundFlatButton:
                text: "6"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("6")
            MDFillRoundFlatButton:
                text: "*"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("*")

            MDFillRoundFlatButton:
                text: "1"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("1")
            MDFillRoundFlatButton:
                text: "2"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("2")
            MDFillRoundFlatButton:
                text: "3"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("3")
            MDFillRoundFlatButton:
                text: "-"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("-")

            MDFillRoundFlatButton:
                text: "."
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display(".")
            MDFillRoundFlatButton:
                text: "0"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("0")
            MDFillRoundFlatButton:
                text: "="
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.calculate_result()
            MDFillRoundFlatButton:
                text: "+"
                size_hint: 1, 1
                font_size: "22sp"
                md_bg_color: 1, 0, 0, 1
                on_release: app.append_to_display("+")

<HistoryScreen>:
    name: "history"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Historial Kuromi"
            left_action_items: [["arrow-left", lambda x: app.switch_to_calc()]]
            right_action_items: [["trash-can", lambda x: app.clear_history()]]
            elevation: 2
            md_bg_color: 1, 0, 0, 1

        ScrollView:
            MDList:
                id: history_list
'''

class CalcScreen(MDScreen):
    pass

class HistoryScreen(MDScreen):
    pass

class KuromiCalcApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        self.animar_kuromi()

    def animar_kuromi(self):
        img = self.root.get_screen("calc").ids.kuromi_img
        animacion = (
            Animation(pos_hint={"center_x": 0.5, "center_y": 0.55}, duration=1.5, t='in_out_sine') +
            Animation(pos_hint={"center_x": 0.5, "center_y": 0.45}, duration=1.5, t='in_out_sine')
        )
        animacion.repeat = True
        animacion.start(img)

    def append_to_display(self, text):
        display = self.root.get_screen("calc").ids.display
        if display.text == "0" or display.text == "Error":
            display.text = text
        else:
            display.text += text

    def clear_all(self):
        self.root.get_screen("calc").ids.display.text = "0"

    def delete_last(self):
        display = self.root.get_screen("calc").ids.display
        if len(display.text) > 1 and display.text != "Error":
            display.text = display.text[:-1]
        else:
            display.text = "0"

    def calculate_result(self):
        display = self.root.get_screen("calc").ids.display
        expression = display.text
        try:
            if expression.strip() == "" or expression == "0":
                return
            result = str(eval(expression))
            display.text = result
            self.add_to_history(f"{expression} = {result}")
        except Exception:
            display.text = "Error"

    def add_to_history(self, item_text):
        history_list = self.root.get_screen("history").ids.history_list
        item = OneLineListItem(text=f"[color=#ff0000]{item_text}[/color]")
        history_list.add_widget(item)

    def clear_history(self):
        history_list = self.root.get_screen("history").ids.history_list
        history_list.clear_widgets()

    def switch_to_history(self):
        self.root.current = "history"
        self.root.transition.direction = "left"

    def switch_to_calc(self):
        self.root.current = "calc"
        self.root.transition.direction = "right"

if __name__ == "__main__":
    KuromiCalcApp().run()
