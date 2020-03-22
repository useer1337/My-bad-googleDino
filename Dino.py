class Dino:
    def __init__(self, x: int, y: int, first_image, second_image, rect):
        self.rect = rect
        self.rect.x = x
        self.rect.y = y
        self.first_image = first_image
        self.second_image = second_image
        self.flag = 0
        self.dino_flag = 0

    def jump(self):
        if self.flag == 0:
            self.rect.y -= 10
            if self.rect.y == 85:
                self.flag = 1

        if self.flag == 1:
            self.rect.y += 10
            if self.rect.y == 155:
                self.flag = 0

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        if self.dino_flag == 0:
            self.dino_flag += 1
            return self.first_image
        else:
            self.dino_flag -= 1
            return self.second_image

    def get_rect(self):
        return self.rect
