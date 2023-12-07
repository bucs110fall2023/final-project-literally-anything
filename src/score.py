import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.clock = pygame.time.Clock()

    def __str__(self):
        return str(self.score)

    def update(self):
        delta_time = self.clock.tick()
        self.score += int(delta_time/10)
        if self.score > self.high_score:
            self.high_score = self.score
        return int(self.score)