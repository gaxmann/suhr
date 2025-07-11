
# Reihenfolge der Screens definieren
screen_order = ['clock', 'settings', 'data', 'manual', 'about'] 
tmresetscatter=120

class SwipeScreen(Screen):
    def __init__(self, **kwargs):
        super(SwipeScreen, self).__init__(**kwargs)
        self._autocenter_event = None  # Speichert geplanten ClockEvent
        self.touch_start_time = None  # Startzeit der Berührung
        self.touch_start_x = None
        self.touch_start_y = None
        self.touch_end_x = None
        self.touch_end_y = None
        self.swipe_threshold = 100  # Mindestdistanz für einen Swipe in Pixel
        self.swipe_ratio_threshold = 4/3  # 5/3 Verhältnis horizontal zu vertikal
        self.last_swipe_time = 0  # Zeit des letzten Swipes
        self.swipe_cooldown = 0.1  # 0.1 Sekunden Pause zwischen Swipes
        self.max_swipe_duration = 0.3  # Maximale Berührungsdauer für einen Swipe in Sekunden

    def on_touch_down(self, touch):
        global lastenter
        lastenter = time.time()
        for child in self.children:
            if child.collide_point(*touch.pos) and isinstance(child, Button):
                return super(SwipeScreen, self).on_touch_down(touch)
        # Startzeit und Position der Berührung speichern
        self.touch_start_time = time.time()
        self.touch_start_x = touch.x
        self.touch_start_y = touch.y
        self.touch_end_x = touch.x  # Initialisiere Endposition
        self.touch_end_y = touch.y
        return super(SwipeScreen, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        global lastenter
        lastenter = time.time()
        # Endposition aktualisieren
        self.touch_end_x = touch.x
        self.touch_end_y = touch.y
        # Keine Swipe-Aktion hier ausführen
        return super(SwipeScreen, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        global lastenter
        lastenter = time.time()
        current_time = time.time()

        if self.touch_start_time is None or self.touch_start_x is None or self.touch_start_y is None:
            return super(SwipeScreen, self).on_touch_up(touch)

        # Berührungsdauer berechnen
        duration = current_time - self.touch_start_time

        # Distanz und Verhältnis berechnen
        delta_x = self.touch_end_x - self.touch_start_x
        delta_y = self.touch_end_y - self.touch_start_y
        if abs(delta_y) > 0:
            ratio = abs(delta_x) / abs(delta_y)
        else:
            ratio = float('inf')

        # Swipe nur erkennen, wenn die Dauer kurz ist UND der Finger innerhalb max_swipe_duration gehoben wird
        if (duration < self.max_swipe_duration and 
            ratio > self.swipe_ratio_threshold and 
            abs(delta_x) > self.swipe_threshold and
            current_time - self.last_swipe_time > self.swipe_cooldown):
            if delta_x > 0:
                self.swipe_right()
            else:
                self.swipe_left()
            self.last_swipe_time = current_time  # Zeit aktualisieren
        # Wenn die Dauer länger ist, wird es als Pan behandelt (keine Aktion hier, da Pan separat gehandhabt wird)

        # Variablen zurücksetzen
        self.touch_start_time = None
        self.touch_start_x = None
        self.touch_start_y = None
        self.touch_end_x = None
        self.touch_end_y = None

        if hasattr(self, 'doautocenter_scatter'):
            if self._autocenter_event:
                self._autocenter_event.cancel()
            self._autocenter_event = Clock.schedule_once(self.doautocenter_scatter, tmresetscatter)
        return super(SwipeScreen, self).on_touch_up(touch)

    def swipe_left(self):
        current_index = screen_order.index(self.manager.current)
        if current_index < len(screen_order) - 1:
            next_screen = screen_order[current_index + 1]
            self.manager.current = next_screen

    def swipe_right(self):
        current_index = screen_order.index(self.manager.current)
        if current_index > 0:
            prev_screen = screen_order[current_index - 1]
            self.manager.current = prev_screen
