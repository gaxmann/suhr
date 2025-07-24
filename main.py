from kivy.app import App
from kivy.lang import Builder

__version__ = "0.1"

kv = """
FloatLayout:
    Scatter:
        size_hint: None, None
        size: image.size  # Size Scatter to match size of image
        scale_min: 1.0
        scale_max: 8.0
        do_translation : True
        do_rotation: False
        do_scale: True
        center: self.parent.center
        Image:
            id: image
            source: 'sky.png'  # Your image here
            size_hint: None, None
            size: self.texture_size
"""


class ScatterImageApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    ScatterImageApp().run()