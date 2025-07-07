from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.clock import Clock
from kivy.graphics.transformation import Matrix
import time

class ZoomImage(Scatter):
    source = StringProperty('')
    reset_on_double_tap = BooleanProperty(True)
    auto_reset_delay = NumericProperty(10.0)  # Sekunden, 0 = aus

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_rotation = False
        self.do_translation = True
        self.do_scale = True
        self.scale_min = 1.0
        self.scale_max = 10.0
        self.auto_bring_to_front = False

        self.img = Image(source=self.source, allow_stretch=True, keep_ratio=True)
        self.add_widget(self.img)

        self._touch_time = 0
        self._reset_event = None

    def on_source(self, instance, value):
        self.img.source = value

    def on_touch_down(self, touch):
        # Prüfe, ob das Touch innerhalb ist (und nicht z. B. auf einem Button)
        if not self.collide_point(*touch.pos):
            return super().on_touch_down(touch)

        # Doppel-Tap erkennen
        now = time.time()
        if self.reset_on_double_tap and (now - self._touch_time) < 0.3:
            self.reset_view()
        self._touch_time = now

        # Auto-Reset Timer neu starten
        if self.auto_reset_delay > 0:
            if self._reset_event:
                self._reset_event.cancel()
            self._reset_event = Clock.schedule_once(self._auto_reset, self.auto_reset_delay)

        return super().on_touch_down(touch)

    def reset_view(self):
        self.transform = Matrix().identity()
        self.center = self.parent.center if self.parent else (0, 0)

    def _auto_reset(self, dt):
        self.reset_view()

