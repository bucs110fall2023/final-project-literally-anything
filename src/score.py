import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.clock = pygame.time.Clock()

    def __str__(self):
        return str(self.score)

    def update(self, highscore):
        delta_time = self.clock.tick()
        self.score += int(delta_time/10)
        if self.score > highscore:
            self.high_score = self.score
        return int(self.score)
    
    def save_high(score):
        tracker = open("highscore.txt", "w")
        tracker.write(str(score))
        tracker.close()
        
    def open_high(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
    
class Highscore:
    def __init__(self):
        pass
    
    def save_high(score):
        tracker = open("highscore.txt", "w")
        tracker.write(str(score))
        tracker.close()
        
    def open_high(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
        
        