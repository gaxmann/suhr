

# Reihenfolge der Screens definieren
screen_order = ['clock', 'settings', 'manual', 'about'] 
tmresetscatter=3

class SwipeScreen(Screen):
    def __init__(self, **kwargs):
        super(SwipeScreen, self).__init__(**kwargs)
        self._autocenter_event = None  # Speichert geplanten ClockEvent
        self.touch_start_x = None
        self.touch_start_y = None
        self.swipe_threshold = 100  # Mindestdistanz für einen Swipe in Pixel
        self.swipe_ratio_threshold = 5/3  # Verhältnis horizontal zu vertikal
        self.last_swipe_time = 0  # Zeit des letzten Swipes
        self.swipe_cooldown = 0.25  # 0.5 Sekunden Pause zwischen Swipes

    def on_touch_up(self, touch):
        if hasattr(self, 'doautocenter_scatter'): 
            if self._autocenter_event: self._autocenter_event.cancel()
            self._autocenter_event = Clock.schedule_once(self.doautocenter_scatter, tmresetscatter)
            # print("-CLOCKED")
        return super(SwipeScreen, self).on_touch_up(touch)
        
    def on_touch_down(self, touch):
        global lastenter
        lastenter = time.time()
        for child in self.children:
            if child.collide_point(*touch.pos) and isinstance(child, Button):
                return super(SwipeScreen, self).on_touch_down(touch)
        self.touch_start_x = touch.x
        self.touch_start_y = touch.y
        return super(SwipeScreen, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        global lastenter
        lastenter = time.time()
        current_time = time.time()
        # Nur Swipes erkennen, wenn Startwerte vorhanden und Cooldown vorbei
        if (self.touch_start_x is not None and self.touch_start_y is not None and 
            current_time - self.last_swipe_time > self.swipe_cooldown):
            delta_x = touch.x - self.touch_start_x
            delta_y = touch.y - self.touch_start_y
            if abs(delta_y) > 0:
                ratio = abs(delta_x) / abs(delta_y)
            else:
                ratio = float('inf')
            # Swipe-Bedingungen prüfen
            if ratio > self.swipe_ratio_threshold and abs(delta_x) > self.swipe_threshold:
                if delta_x > 0:
                    self.swipe_right()
                else:
                    self.swipe_left()
                # Geste freigeben
                self.touch_start_x = None
                self.touch_start_y = None
                self.last_swipe_time = current_time  # Zeit aktualisieren
        return super(SwipeScreen, self).on_touch_move(touch)

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




# ------



class ClockScreen(SwipeScreen):
    time = StringProperty('')  
    sky_image = StringProperty('processing.gif')

    def on_enter(self):
        app = App.get_running_app()
        # app.sky_image = os.path.join(fns.currpath, 'processing.gif') 
        Clock.schedule_once(self.update_scrollview, 0)
        Clock.schedule_once(self.center_scatter)

    def check_double_tap(self, scatter, touch):
        if scatter.collide_point(*touch.pos) and touch.is_double_tap:
            scatter.scale = 1.0
            scatter.center = self.ids.float_layout.center
            return True

    def doautocenter_scatter(self, dt):# Clock.schedule_once(self.doautocenter_scatter)
        # reset after tmresetscatter sec
        global lastenter
        current_time = time.time()
        # Nur Swipes erkennen, wenn Startwerte vorhanden und Cooldown vorbei
        try:
            lastenter
            if (current_time - lastenter > tmresetscatter-0.2): Clock.schedule_once(self.center_scatter)
        except:
            pass

    def center_scatter(self, dt):
        scatter = self.ids.scatter
        float_layout = self.ids.float_layout
        # Zentriere das Scatter-Widget im Layout
        scatter.center = float_layout.center
        scatter.scale = 1.0


