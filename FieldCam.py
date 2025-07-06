from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FieldCamLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text='📷 FieldCam - Rock Scan Mode', size_hint=(1, 0.2)))

        self.rock_button = Button(text='Rock Mode (ISO 50, 1/250)', size_hint=(1, 0.2))
        self.rock_button.bind(on_press=self.set_rock_mode)
        self.add_widget(self.rock_button)

        self.photo_button = Button(text='Take Photo', size_hint=(1, 0.2))
        self.photo_button.bind(on_press=self.take_photo)
        self.add_widget(self.photo_button)

        self.status = Label(text='Status: Ready', size_hint=(1, 0.2))
        self.add_widget(self.status)

    def set_rock_mode(self, instance):
        self.status.text = 'Rock Mode Activated (simulated)'
        # Here you'd set camera ISO, shutter, WB using real camera API

    def take_photo(self, instance):
        self.status.text = 'Pretend we took a photo! 📸'
        # This is where you'd trigger the actual camera shutter

class FieldCamApp(App):
    def build(self):
        return FieldCamLayout()

if __name__ == '__main__':
    FieldCamApp().run()
