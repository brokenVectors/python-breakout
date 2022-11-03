from constants import width, height
from block_manager import *
class Ball:
    def __init__(self,x,y):
        self.position = [x,y]
        self.velocity = [0,0] # Breakout doesn't have ball acceleration, velocity stays constant until a collision occurs
        self.size = [10,10] # The ball is rendered as a circle, but acts as a rectangle
    def update(self, dt, colliders):
        # Solve collisions
        for collider in colliders:
            # x1 < x2 + w2 && x1 + w1 > x2 && y1 < y2 + h2 && h1 + y1 > y2
            vx = self.velocity[0]
            vy = self.velocity[1]
            x1 = self.position[0]
            x2 = collider.position[0]
            y1 = self.position[1]
            y2 = collider.position[1]
            w1 = self.size[0]
            w2 = collider.size[0]
            h1 = self.size[1]
            h2 = collider.size[1]
            
            isCollision = x1 + vx < x2 + w2 and x1 + vx + w1 > x2 and y1 + vy < y2 + h2 and h1 + y1 + vy > y2
            if isCollision:
                if (x1 >= x2) and (x1 <= x2 + w2) and (y1 <= y2):
                    self.velocity[0] *= 1
                    self.velocity[1] *= -1
                elif (x1 <= x2) and (y1 >= y2) and (y1 <= y2 + w2):
                    self.velocity[0] *= -1
                    self.velocity[1] *= 1
                elif (y1 >= y2 + h2) and (x1 >= x2) and (x1 <= x2 + w2):
                    self.velocity[0] *= 1
                    self.velocity[1] *= -1
                elif (x1 >= x2 + w2) and (y1 >= y2) and (y1 <= y2 + h2):
                    self.velocity[0] *= -1
                    self.velocity[1] *= 1
                else:
                    # Something went wrong and the collision couldn't be solved, likely due to a framedrop.
                    # Bring the ball back to try to solve it again.
                    self.position[0] -= self.velocity[0]
                    self.position[1] -= self.velocity[1]
                if isinstance(collider, Block):
                    remove_block(collider)
        # Solve collisions for window borders
        if self.position[1] < 0:
            self.position[1] = 0 # in case of velocity being higher than 1, reset position
            self.velocity[0] *= 1
            self.velocity[1] *= -1
        elif self.position[1] > height - self.size[1]:
            self.position[1] = height - self.size[1] # in case of velocity being higher than 1, reset position
            self.velocity[0] *= 1
            self.velocity[1] *= -1
        if self.position[0] < 0:
            self.position[0] = 0 # in case of velocity being higher than 1, reset position
            self.velocity[0] *= -1
            self.velocity[1] *= 1
        elif self.position[0] > width - self.size[0]:
            self.position[0] = width - self.size[0] # in case of velocity being higher than 1, reset position
            self.velocity[0] *= -1
            self.velocity[1] *= 1
        # Move ball
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]