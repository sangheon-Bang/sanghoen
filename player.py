import pygame
import slid


class Player:
    def __init__(self, x_postition, y_position):
        
        self.position = [x_postition, y_position]
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (slid.size, slid.size))
        self.rect = pygame.Rect(self.position[0] * slid.size, self.position[1] * slid.size, slid.size, slid.size)

    def update(self):
        print("update")

    def update_position(self, x_change, y_change):
        self.position[0] +=x_change
        self.position[1] +=y_change
        self.rect = pygame.Rect(self.position[0] * slid.size, self.position[1] * slid.size, slid.size, slid.size)

    def make(self, screen):
        screen.blit(self.image, self.rect)
