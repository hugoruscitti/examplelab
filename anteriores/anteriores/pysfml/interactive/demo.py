import interactive
from PySFML import sf

if __name__ == '__main__':
    window = interactive.InteractiveRenderWindow()
    window.start()

    image = sf.Image()
    image.LoadFromFile('image.png')

    sprite = sf.Sprite(image)
    window.add(sprite)
