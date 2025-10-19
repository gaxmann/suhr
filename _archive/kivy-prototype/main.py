##
## --- Version 2.0.0.alpha.0.1
## --- Das ist der Anfang des Projekts Sonnenuhr, 18.05.2025
##


import os
import time
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.config import Config
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform
from kivy.uix.button import Button
from kivy.uix.behaviors import FocusBehavior
import datetime
import pytz
from skyfield import api
from PIL import Image, ImageDraw
from plyer import gps
import copy


# Benutzerdefinierte Button-Klasse mit Fokus-Unterstützung
class FocusButton(FocusBehavior, Button):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == 'spacebar' and self.focus:
            self.dispatch('on_press')
            return True
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

img_path_old=''
colset=[[(0,0,0), (255,255,255), (64,64,64), (96,96,96)], [(255,255,255), (0,0,0), (96,96,96), (64,64,64)]]
CONF_SCREEN=[Window.width, Window.height]     
imglastrun=0

class ClockScreen(Screen):
    time = StringProperty('')
    sky_image = ObjectProperty(None)
    planets = None  # Wird in __init__ gesetzt
    tmsc = None     # Wird in __init__ gesetzt

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = App.get_running_app()
        
        # Binde das night_mode-Property an die Methode on_night_mode_change
        app.bind(night_mode=self.on_night_mode_change)
        # Weitere Initialisierungen (falls vorhanden)...

        # Schritt 1: Pfad dynamisch setzen
        if platform == 'android':
            # Auf Android: Verwende user_data_dir
            self.currpath = app.user_data_dir
            de421_path = os.path.join(self.currpath, 'de421.bsp')
            # Kopiere de421.bsp in user_data_dir, falls nicht vorhanden
            if not os.path.exists(de421_path):
                local_de421 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'de421.bsp')
                shutil.copy(local_de421, de421_path)
                            
        else:
            # Auf Linux: Verwende lokalen Pfad
            self.currpath = os.path.dirname(os.path.abspath(__file__))
            de421_path = os.path.join(self.currpath, 'de421.bsp')

        self.tmppath = os.path.join(self.currpath, 'tmp/')

        for datei in os.listdir(self.tmppath):
            dateipfad = os.path.join(self.tmppath, datei)
            if os.path.isfile(dateipfad):
                os.remove(dateipfad)
                
        if not os.path.exists(de421_path):
            raise FileNotFoundError(f"Ephemeridendatei nicht gefunden: {de421_path}")
            
        # Schritt 2: Skyfield-Setup
        self.tmsc = api.load.timescale()
        self.planets = api.load_file(de421_path)

        # Initialisiere die Uhr
        tz = pytz.timezone(app.timezone)
        now = datetime.datetime.now(tz)
        self.update_time(now)
        Window.bind(on_resize=self.on_window_resize)
        Clock.schedule_interval(self.update_time, 15) # 60

    def on_window_resize(self, window, width, height):
        global CONF_SCREEN, imglastrun
        CONF_SCREEN=[Window.width, Window.height]     
        if platform != 'android': print("Fenstergröße:", Window.size)
        app = App.get_running_app()
        tz = pytz.timezone(app.timezone)
        now = datetime.datetime.now(tz)
        self.update_sky_image(now)

    def on_night_mode_change(self, instance, value):
        """Wird aufgerufen, wenn sich night_mode ändert."""
        # print("Dunkelmodus geändert zu:", value)
        app = App.get_running_app()
        # Hole die aktuelle Zeit mit der Zeitzone der App
        tz = pytz.timezone(app.timezone)
        now = datetime.datetime.now(tz)
        # Aktualisiere das Bild sofort
        self.update_sky_image(now)

    def update_time(self, dt):
        app = App.get_running_app()
        tz = pytz.timezone(app.timezone)
        now = datetime.datetime.now(tz)
        if app.use_24_hour:
            self.time = now.strftime('%H:%M')
        else:
            self.time = now.strftime('%I:%M %p')
        self.update_sky_image(now)

    def update_sky_image(self, local_time):
        global img_path_old, colset
        global CONF_SCREEN, imglastrun
        if imglastrun==int(time.time()): return
        imglastrun=int(time.time())

        app = App.get_running_app()
        if app.night_mode: cc=0 
        else: cc=1
        # print(colset[cc])
        if app.use_gps_hourly:
            lat, lon = 42.90654025282736, -9.266993290995226
        else:
            try:
                lat, lon = map(float, app.gps_coords.split(','))
            except:
                lat, lon = 42.90654025282736, -9.266993290995226
        toposloc = api.Topos(latitude_degrees=lat, longitude_degrees=lon)
        toposabs = self.planets['earth'] + toposloc

        utc_time = local_time.astimezone(pytz.utc)
        t = self.tmsc.utc(utc_time.year, utc_time.month, utc_time.day, utc_time.hour, utc_time.minute, utc_time.second)
        astro_sun = toposabs.at(t).observe(self.planets['sun'])
        app_sun = astro_sun.apparent()
        alt_sun, azi_sun, _ = app_sun.altaz()

        sirius = api.Star(ra_hours=(6, 45, 08.9172928), dec_degrees=(-16, 42, 58.016949))
        astro_sirius = toposabs.at(t).observe(sirius)
        app_sirius = astro_sirius.apparent()
        alt_sirius, azi_sirius, _ = app_sirius.altaz()

        img = Image.new('RGB', CONF_SCREEN, color=colset[cc][0])
        draw = ImageDraw.Draw(img)
        x_sun, y_sun = self.calc_obj(alt_sun.degrees, azi_sun.degrees)
        draw.ellipse((x_sun - 10, y_sun - 10, x_sun + 10, y_sun + 10), fill=colset[cc][2])
        x_sirius, y_sirius = self.calc_obj(alt_sirius.degrees, azi_sirius.degrees)
        draw.ellipse((x_sirius - 5, y_sirius - 5, x_sirius + 5, y_sirius + 5), fill=colset[cc][1])

        # draw.ellipse((5, 5, 15, 15), fill='yellow')

        # Erstelle einen eindeutigen Dateinamen mit einem Zeitstempel
        timestamp = int(time.time())
        img_path = os.path.join(self.tmppath, f'sky_{timestamp}.png')
        # img_path = os.path.join(self.tmppath, 'sky.png')
        img.save(img_path)

        if img_path_old!='':
            if os.path.exists(img_path_old):
                os.remove(img_path_old)
                # print("Datei gelöscht.")
            else:
                print("Datei "+img_path_old+"existiert nicht.")
        img_path_old=copy.copy(img_path)

        if self.ids.sky_image:
            self.ids.sky_image.source = img_path
            self.ids.sky_image.reload()

    def calc_obj(self, alt, azi):
        x = 300 + 200 * (azi / 180.0)
        y = 480 - 200 * (alt / 90.0)
        return x, y

    def switch_to_settings(self):
        self.manager.transition = NoTransition()
        self.manager.current = 'settings'

class SettingsScreen(Screen):
    def switch_to_clock(self):
        self.manager.transition = NoTransition()
        self.manager.current = 'clock'

class ClockApp(App):
    use_24_hour = BooleanProperty(True)
    timezone = StringProperty('UTC')
    gps_coords = StringProperty('42.90654025282736, -9.266993290995226')
    use_gps_hourly = BooleanProperty(False)
    night_mode = BooleanProperty(False)
    is_android = BooleanProperty(platform == 'android')
    gps_interval = None

    def build(self):
        global CONF_SCREEN
        self.store = JsonStore('settings.json')
        if 'settings' in self.store:
            settings = self.store.get('settings')
            self.use_24_hour = settings.get('use_24_hour', True)
            self.timezone = settings.get('timezone', self.get_android_timezone())
            self.gps_coords = settings.get('gps_coords', '42.90654025282736, -9.266993290995226')
            self.use_gps_hourly = settings.get('use_gps_hourly', False) if platform == 'android' else False
            self.night_mode = settings.get('night_mode', False)
        else:
            self.use_24_hour = True
            self.timezone = self.get_android_timezone()
            self.gps_coords = '42.90654025282736, -9.266993290995226'
            self.use_gps_hourly = False
            self.night_mode = False
        sm = ScreenManager()
        sm.add_widget(ClockScreen(name='clock'))
        sm.add_widget(SettingsScreen(name='settings'))
        Window.clearcolor = (0, 0, 0, 1) if self.night_mode else (1, 1, 1, 1)
        Window.maximize()  # Maximiert das Fenster
        CONF_SCREEN=[Window.width, Window.height]     
        # print("Fenstergröße:", Window.size)
        return sm

    def get_android_timezone(self):
        try:
            from plyer import tz
            zz = tz.get_timezone()
            # from jnius import autoclass
            # TimeZone = autoclass('java.util.TimeZone')
            # tz = TimeZone.getDefault().getID()
            print("Zeitzone:", zz)
            return zz
        except:
            return 'UTC'

    def on_use_24_hour(self, instance, value):
        self.store.put('settings', use_24_hour=value, timezone=self.timezone, gps_coords=self.gps_coords, use_gps_hourly=self.use_gps_hourly, night_mode=self.night_mode)

    def on_timezone(self, instance, value):
        self.store.put('settings', use_24_hour=self.use_24_hour, timezone=value, gps_coords=self.gps_coords, use_gps_hourly=self.use_gps_hourly, night_mode=self.night_mode)

    def on_gps_coords(self, instance, value):
        try:
            lat, lon = map(float, value.split(','))
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                self.store.put('settings', use_24_hour=self.use_24_hour, timezone=self.timezone, gps_coords=value, use_gps_hourly=self.use_gps_hourly, night_mode=self.night_mode)
            else:
                self.gps_coords = '42.90654025282736, -9.266993290995226'
        except:
            self.gps_coords = '42.90654025282736, -9.266993290995226'

    def on_use_gps_hourly(self, instance, value):
        if platform == 'android':
            if value:
                self.fetch_gps()
                self.gps_interval = Clock.schedule_interval(self.fetch_gps_hourly, 3600)
            else:
                if self.gps_interval:
                    self.gps_interval.cancel()
                    self.gps_interval = None
                gps.stop()
        else:
            if value:
                print("GPS is only available on Android. Setting use_gps_hourly to False.")
                self.use_gps_hourly = False

    def fetch_gps(self):
        if platform != 'android':
            print("GPS is not supported on this platform")
            return
        gps.configure(on_location=self.on_location)
        gps.start()

    def fetch_gps_hourly(self, dt):
        self.fetch_gps()

    def on_location(self, **kwargs):
        if 'lat' in kwargs and 'lon' in kwargs:
            self.gps_coords = f"{kwargs['lat']}, {kwargs['lon']}"
        gps.stop()

    def on_night_mode(self, instance, value):
        self.store.put('settings', use_24_hour=self.use_24_hour, timezone=self.timezone, gps_coords=self.gps_coords, use_gps_hourly=self.use_gps_hourly, night_mode=value)
        Window.clearcolor = (0, 0, 0, 1) if value else (1, 1, 1, 1)

if __name__ == '__main__':
    ClockApp().run()