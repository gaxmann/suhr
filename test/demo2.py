from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

# Lade den KV-Code
Builder.load_file('deine_datei.kv')  # Ersetze 'deine_datei.kv' mit dem Namen deiner KV-Datei

class ClockScreen(Screen):
    sky_image = StringProperty('sky.png')  # Pfad zu deinem Bild
    time = StringProperty('12:00')         # Beispielzeit, ersetze dies durch deine Logik

class MyApp(App):
    z_font2 = StringProperty('DejaVuSans.ttf')  # Beispiel-Schriftart
    night_mode = False  # Beispiel für night_mode

    def build(self):
        return ClockScreen()

    def run_totalupdate(self):
        print("Total update ausgeführt")

    def switch_to_settings(self):
        print("Zu den Einstellungen wechseln")

if __name__ == '__main__':
    MyApp().run()
    