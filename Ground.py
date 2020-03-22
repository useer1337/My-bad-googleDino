class Ground:
    def __init__(self, x: int, y: int, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self):
        self.x = self.x - 5
        if self.x < -550:
            self.x = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.image
