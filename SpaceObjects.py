class SpaceObjects:
    def __init__(self, x=0, y=0, width=0, height=0, img=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img


class PlayerShip(SpaceObjects):
    # player = {'player_img': player_img, 'px': 10, 'py': 10}
    pass


class AlienShip(SpaceObjects):
    # alien = {'alien_img': alien_img, 'ax': 250, 'ay': 50}
    pass


class Asteroid(SpaceObjects):
    pass
