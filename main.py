from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.utils import platform

# ✅ FIX PRINCIPAL: solo fija el tamaño en escritorio/preview,
# NO en Android (que causaba la pantalla negra)
if platform not in ('android', 'ios'):
    Window.size = (360, 640)

KV = '''
ScreenManager:
    id: sm
    CalcScreen:
    HistoryScreen:

<CalcScreen>:
    name: "calc"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.05, 0.05, 0.1, 1

        MDTopAppBar:
            title: "Labubu Neón"
            left_action_items: [["calculator", lambda x: None]]
            right_action_items: [["history", lambda x: app.switch_to_history()]]
            elevation: 2
            md_bg_color: 1, 0.1, 0.6, 1

        # ✅ FloatLayout permite animar pos_hint correctamente
        MDBoxLayout:
            size_hint_y: 0.30
            FloatLayout:
                Image:
                    id: labubu_img
                    source: "image_67379f.png"
                    size_hint: None, None
                    size: "130dp", "130dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    allow_stretch: True
                    keep_ratio: True

        MDBoxLayout:
            size_hint_y: 0.13
            padding: ["20dp", "5dp"]
            md_bg_color: 0.1, 0.1, 0.2, 1
            MDLabel:
                id: display
                text: "0"
                halign: "right"
                valign: "center"
                font_style: "H3"
                theme_text_color: "Custom"
                text_color: 0, 1, 1, 1
                bold: True

        MDGridLayout:
            cols: 4
            spacing: "8dp"
            padding: "15dp"
            size_hint_y: 0.57

            MDFillRoundFlatButton:
                text: "C"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 1, 0.2, 0.2, 1
                on_release: app.clear_display()
            MDFillRoundFlatButton:
                text: "("
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0.6, 0.2, 1, 1
                on_release: app.append_to_display("(")
            MDFillRoundFlatButton:
                text: ")"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0.6, 0.2, 1, 1
                on_release: app.append_to_display(")")
            MDFillRoundFlatButton:
                text: "/"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 1, 0.1, 0.6, 1
                on_release: app.append_to_display("/")

            MDFillRoundFlatButton:
                text: "7"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("7")
            MDFillRoundFlatButton:
                text: "8"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("8")
            MDFillRoundFlatButton:
                text: "9"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("9")
            MDFillRoundFlatButton:
                text: "*"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 1, 0.1, 0.6, 1
                on_release: app.append_to_display("*")

            MDFillRoundFlatButton:
                text: "4"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("4")
            MDFillRoundFlatButton:
                text: "5"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("5")
            MDFillRoundFlatButton:
                text: "6"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("6")
            MDFillRoundFlatButton:
                text: "-"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 1, 0.1, 0.6, 1
                on_release: app.append_to_display("-")

            MDFillRoundFlatButton:
                text: "1"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("1")
            MDFillRoundFlatButton:
                text: "2"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("2")
            MDFillRoundFlatButton:
                text: "3"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("3")
            MDFillRoundFlatButton:
                text: "+"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 1, 0.1, 0.6, 1
                on_release: app.append_to_display("+")

            MDFillRoundFlatButton:
                text: "Hist"
                size_hint: 1, 1
                font_size: "16sp"
                md_bg_color: 0.6, 0.2, 1, 1
                on_release: app.switch_to_history()
            MDFillRoundFlatButton:
                text: "0"
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display("0")
            MDFillRoundFlatButton:
                text: "."
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0, 0.7, 1, 1
                on_release: app.append_to_display(".")
            MDFillRoundFlatButton:
                text: "="
                size_hint: 1, 1
                font_size: "20sp"
                md_bg_color: 0.2, 0.9, 0.2, 1
                on_release: app.calculate_result()

<HistoryScreen>:
    name: "history"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.05, 0.05, 0.1, 1
        MDTopAppBar:
            title: "Historial Labubu"
            left_action_items: [["arrow-left", lambda x: app.switch_to_calc()]]
            right_action_items: [["trash-can", lambda x: app.clear_history()]]
            elevation: 2
            md_bg_color: 1, 0.1, 0.6, 1
        ScrollView:
            MDList:
                id: history_list
'''


class CalcScreen(MDScreen):
    pass


class HistoryScreen(MDScreen):
    pass


class LabubuCalcApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        self.animar_labubu()

    def animar_labubu(self):
        img = self.root.get_screen("calc").ids.labubu_img
        # ✅ Animación corregida: incluye center_x y center_y,
        # funciona bien con FloatLayout
        anim = (
            Animation(
                pos_hint={"center_x": 0.5, "center_y": 0.58},
                duration=1.2,
                t='in_out_sine'
            ) +
            Animation(
                pos_hint={"center_x": 0.5, "center_y": 0.42},
                duration=1.2,
                t='in_out_sine'
            )
        )
        anim.repeat = True
        anim.start(img)

    def append_to_display(self, text):
        display = self.root.get_screen("calc").ids.display
        if display.text in ("0", "Error"):
            display.text = text
        else:
            display.text += text

    def clear_display(self):
        self.root.get_screen("calc").ids.display.text = "0"

    def calculate_result(self):
        display = self.root.get_screen("calc").ids.display
        try:
            result = str(eval(display.text))
            self.add_to_history(f"{display.text} = {result}")
            display.text = result
        except Exception:
            display.text = "Error"

    def add_to_history(self, item_text):
        self.root.get_screen("history").ids.history_list.add_widget(
            OneLineListItem(text=item_text)
        )

    def clear_history(self):
        self.root.get_screen("history").ids.history_list.clear_widgets()

    def switch_to_history(self):
        self.root.current = "history"

    def switch_to_calc(self):
        self.root.current = "calc"


if __name__ == "__main__":
    LabubuCalcApp().run()
