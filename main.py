from kivy.app import App
from kivy.uix.widget import Widget
from PIL import Image

class PongGame(Widget):
    c_image_path = '1.png'

    def update_contrast(self, cvalue):
        c_image = Image.open(self.c_image_path)
        self.change_contrast(c_image, self.ids.contrast.value)
        c_image.save('temp_' + self.c_image_path, 'PNG');

        self.ids.displayed_image.source = 'temp_' + self.c_image_path

    def change_contrast(self, img, level):
        factor = (259 * (level + 255)) / (255 * (259 - level))
        def contrast(c):
            return 128 + factor * (c - 128)
        return img.point(contrast)

class PongApp(App):
    def build(self):
        game = PongGame()
        return game


if __name__ == '__main__':
    PongApp().run()
