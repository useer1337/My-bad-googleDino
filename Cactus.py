class Cactus:
    def __init__(self, x: int, y: int, image, rect):
        self.rect = rect
        self.rect.x = x
        self.rect.y = y
        self.image = image

    def move(self):
        self.rect.x = self.rect.x - 5
        if self.rect.x < 0:
            self.rect.x = 400

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect
