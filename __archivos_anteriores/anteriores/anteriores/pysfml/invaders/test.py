from PySFML import sf
import random

window = sf.RenderWindow(sf.VideoMode(640, 480), "My game", sf.Style.Fullscreen)

def area_to_tuple(area):
    left = area.Left
    top = area.Top
    width = area.GetWidth()
    height = area.GetHeight()
    return (left, top, width, height)

class Sprite(sf.Sprite):

    def __init__(self, image, center=(0, 0)):
        sf.Sprite.__init__(self, image)
        self._create_collision_area()
        self.collision_ratio = 30
        self.center = center
        self.SetCenter(*self.center)

    def _create_collision_area(self):
        self.collision_area = sf.IntRect(0, 0, 0, 0)

    def create_collision_preview(self, color):
        "Genera una figura que representa el area colisionable."

        left = self.collision_area.Left
        right = self.collision_area.Right
        top = self.collision_area.Top
        bottom = self.collision_area.Bottom

        return sf.Shape.Rectangle(left, top, right, bottom, color)

    def post_update(self):
        x, y = self.GetPosition()
        center_x, center_y = self.center
        y-= center_y

        self.collision_area.Left = x - self.collision_ratio
        self.collision_area.Right = x + self.collision_ratio
        
        self.collision_area.Top = y - self.collision_ratio
        self.collision_area.Bottom = y + self.collision_ratio

    def collide_with(self, other_sprite):
        area_to_tuple(self.collision_area)
        area_to_tuple(other_sprite.collision_area)

        return self.collision_area.Intersects(other_sprite.collision_area)


class SpriteGroup:

    def __init__(self):
        self.sprites = []
        self.to_remove = []
        self.to_insert = []

    def add(self, sprite):
        self.to_insert.append(sprite)

    def draw(self, window, debug_color=None):
        red = sf.Color(255, 200, 200, 60)

        for sprite in self.sprites:
            x, y = sprite.GetPosition()

            window.Draw(sprite)

            if debug_color:
                collision_preview = sprite.create_collision_preview(debug_color)
                window.Draw(collision_preview)

    def _update_sprite_changes(self):

        if self.to_remove:
            for x in self.to_remove:
                self.sprites.remove(x)

            self.to_remove = []

        if self.to_insert:
            for x in self.to_insert:
                self.sprites.insert(0, x)
            self.to_insert = []

    def update(self, input, dt):
        self._update_sprite_changes()
        self._propagate('update', input, dt)
        self._propagate('post_update')

    def _propagate(self, id, *k):
        for sprite in self.sprites:
            callback = getattr(sprite, id)
            callback(*k)

    def remove(self, sprite):
        self.to_remove.append(sprite)

    def get_collisions_with(self, other_group):
        collisions = []

        for sprite in self.sprites:
            for other in other_group.sprites:

                if sprite.collide_with(other):
                    collisions.append((sprite, other))

        return collisions




class Enemy(Sprite):

    def __init__(self, image):
        Sprite.__init__(self, image, (32, 0))
        self.SetPosition(random.randint(40, 600), -64)

    def update(self, input, dt):
        speed = 100
        self.Move(0, dt * speed)


class Shot(Sprite):

    def __init__(self, sprites, image, x, y):
        Sprite.__init__(self, image, (16, 16))
        self.SetPosition(x, y - 30)
        self.counter = 0
        self.sprites = sprites

    def update(self, input, dt):
        x, y = self.GetPosition()

        if y < 0:
            self.die()
        else:
            self.Move(0, - 500 * dt)
            self.counter += dt * 700
            self.SetRotation(self.counter)

    def die(self):
        self.sprites.remove(self)


class Ship(Sprite):

    def __init__(self, sprites):
        self.sprites = sprites
        image = sf.Image()
        image.LoadFromFile('images/ship.png')

        self.shot_image = sf.Image()
        self.shot_image.LoadFromFile('images/shot.png')

        Sprite.__init__(self, image, (32, 64))
        self._load_sounds()
        self._set_initial_position()

    def _set_initial_position(self):
        self.SetX(320)
        self.SetY(480)
        self.delay_to_shot = 0

    def _load_sounds(self):
        buffer = sf.SoundBuffer()
        buffer.LoadFromFile('sounds/shot.wav')
        self.shot_sound = sf.Sound()
        self.shot_sound.SetBuffer(buffer)

    def update(self, input, dt):
        speed = 300
        x, y = self.GetPosition()

        if input.IsKeyDown(sf.Key.Left) and x > 10:
            self.Move(dt * -speed, 0)
        elif input.IsKeyDown(sf.Key.Right) and x < 630:
            self.Move(dt * speed, 0)

        if input.IsKeyDown(sf.Key.Down) and y < 480:
            self.Move(0, dt * speed)
        elif input.IsKeyDown(sf.Key.Up) and y > 64:
            self.Move(0, dt * -speed)

        if input.IsKeyDown(sf.Key.Space) and self.delay_to_shot < 0:
            self.delay_to_shot = 0.25   # permite 4 disparos por segundo.
            self.shot()

        self.delay_to_shot -= dt

    def shot(self):
        x, y = self.GetPosition()
        self.sprites.add(Shot(self.sprites, self.shot_image, x, y))
        self.shot_sound.Play()




def test_collisions():
    event = sf.Event()
    input = window.GetInput()
    running = True


    ships = SpriteGroup()
    shots = SpriteGroup()
    enemies = SpriteGroup()

    # Genera la nave
    ship = Ship(shots)
    ships.add(ship)

    window.UseVerticalSync(True)

    enemy_image = sf.Image()
    enemy_image.LoadFromFile('images/enemy.png')

    enemy = Enemy(enemy_image)
    enemies.add(enemy)

    red_color = sf.Color(255, 0, 0, 100)
    green_color = sf.Color(0, 255, 0, 100)
    dt_counter = 0


    enemy.SetPosition(250, 250)
    ship.SetPosition(300, 300)

    ships.update(input, 0.1)
    enemies.update(input, 0.1)


    print enemies.get_collisions_with(ships)

    while running:

        while window.GetEvent(event):

            if event.Type == sf.Event.Closed:
                running = False

            if event.Type == sf.Event.KeyPressed:
                if event.Key.Code == sf.Key.Escape:
                    running = False



        dt = window.GetFrameTime()
        dt_counter += dt


        #ships.update(input, dt)
        #enemies.update(input, dt)

        window.Clear(sf.Color(30, 30, 30))

        ships.draw(window, debug_color=green_color)
        shots.draw(window, debug_color=green_color)
        enemies.draw(window, debug_color=red_color)

        window.Display()
    pass






def main():
    event = sf.Event()
    input = window.GetInput()
    running = True


    shots = SpriteGroup()
    ships = SpriteGroup()
    enemies = SpriteGroup()

    # Genera la nave
    ship = Ship(shots)
    ships.add(ship)

    window.UseVerticalSync(True)

    enemy_image = sf.Image()
    enemy_image.LoadFromFile('images/enemy.png')

    enemy = Enemy(enemy_image)
    enemies.add(enemy)

    red_color = sf.Color(255, 0, 0, 100)
    green_color = sf.Color(0, 255, 0, 100)
    dt_counter = 0


    while running:

        while window.GetEvent(event):

            if event.Type == sf.Event.Closed:
                running = False

            if event.Type == sf.Event.KeyPressed:
                if event.Key.Code == sf.Key.Escape:
                    running = False



        dt = window.GetFrameTime()
        dt_counter += dt


        if dt_counter > 1:
            enemy = Enemy(enemy_image)
            enemies.add(enemy)
            dt_counter -= 1


        for (enemy, shot) in enemies.get_collisions_with(shots):
            enemies.remove(enemy)
            shots.remove(shot)

        ships.update(input, dt)
        shots.update(input, dt)
        enemies.update(input, dt)

        window.Clear(sf.Color(30, 30, 30))

        ships.draw(window, debug_color=green_color)
        shots.draw(window, debug_color=green_color)
        enemies.draw(window, debug_color=red_color)

        window.Display()



if __name__ == '__main__':
    main()
