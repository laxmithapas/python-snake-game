import pygame
import random
import math
from enum import Enum

# Initialize Pygame
pygame.init()

# Game Constants
WINDOW_SIZE = 800
GRID_SIZE = 20
GRID_COUNT = WINDOW_SIZE // GRID_SIZE
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

class GameMode(Enum):
    CLASSIC = 1
    SURVIVAL = 2
    HUNTER = 3

class PowerUpType(Enum):
    SPEED = 1
    INVINCIBILITY = 2
    GROWTH = 3

class GameObject:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, 
                        (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Snake:
    def __init__(self, x, y, color, is_player=True):
        self.body = [(x, y)]
        self.color = color
        self.direction = [1, 0]
        self.is_player = is_player
        self.speed = 1
        self.invincible = False
        self.power_up_timer = 0

    def move(self, game_objects):
        new_head = (self.body[0][0] + self.direction[0], 
                   self.body[0][1] + self.direction[1])
        
        # Wrap around screen
        new_head = (new_head[0] % GRID_COUNT, new_head[1] % GRID_COUNT)
        
        self.body.insert(0, new_head)
        self.body.pop()

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color,
                           (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                            GRID_SIZE, GRID_SIZE))

    def grow(self):
        self.body.append(self.body[-1])

class EnemySnake(Snake):
    def __init__(self, x, y):
        super().__init__(x, y, RED, False)
        self.target = None
        self.speed = 0.5

    def chase_target(self, target):
        self.target = target
        head = self.body[0]
        target_pos = target.body[0]

        # Calculate direction to target
        dx = target_pos[0] - head[0]
        dy = target_pos[1] - head[1]

        # Normalize direction
        length = math.sqrt(dx**2 + dy**2)
        if length > 0:
            dx = dx / length
            dy = dy / length

        # Update direction
        self.direction = [int(round(dx)), int(round(dy))]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Advanced Snake Game")
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.player = Snake(GRID_COUNT // 4, GRID_COUNT // 2, GREEN)
        self.enemies = [EnemySnake(GRID_COUNT - 5, GRID_COUNT - 5)]
        self.food = []
        self.power_ups = []
        self.score = 0
        self.game_mode = GameMode.CLASSIC
        self.spawn_food()
        self.spawn_power_up()

    def spawn_food(self):
        while len(self.food) < 3:
            x = random.randint(0, GRID_COUNT - 1)
            y = random.randint(0, GRID_COUNT - 1)
            self.food.append(GameObject(x, y, YELLOW))

    def spawn_power_up(self):
        if random.random() < 0.05 and len(self.power_ups) < 1:
            x = random.randint(0, GRID_COUNT - 1)
            y = random.randint(0, GRID_COUNT - 1)
            power_up_type = random.choice(list(PowerUpType))
            color = PURPLE if power_up_type == PowerUpType.INVINCIBILITY else BLUE
            self.power_ups.append((GameObject(x, y, color), power_up_type))

    def handle_collisions(self):
        head = self.player.body[0]

        # Food collision
        for food in self.food[:]:
            if (head[0], head[1]) == (food.x, food.y):
                self.food.remove(food)
                self.player.grow()
                self.score += 10
                self.spawn_food()

        # Power-up collision
        for power_up in self.power_ups[:]:
            if (head[0], head[1]) == (power_up[0].x, power_up[0].y):
                self.apply_power_up(power_up[1])
                self.power_ups.remove(power_up)

        # Enemy collision
        for enemy in self.enemies[:]:
            if (head[0], head[1]) in enemy.body:
                if self.player.invincible:
                    self.enemies.remove(enemy)
                    self.score += 50
                else:
                    return True

            # Enemy eats food
            for food in self.food[:]:
                if (enemy.body[0][0], enemy.body[0][1]) == (food.x, food.y):
                    self.food.remove(food)
                    enemy.grow()
                    self.spawn_food()

        return False

    def apply_power_up(self, power_up_type):
        if power_up_type == PowerUpType.SPEED:
            self.player.speed = 2
            self.player.power_up_timer = 300
        elif power_up_type == PowerUpType.INVINCIBILITY:
            self.player.invincible = True
            self.player.power_up_timer = 300
        elif power_up_type == PowerUpType.GROWTH:
            for _ in range(3):
                self.player.grow()

    def update_power_ups(self):
        if self.player.power_up_timer > 0:
            self.player.power_up_timer -= 1
            if self.player.power_up_timer == 0:
                self.player.speed = 1
                self.player.invincible = False

    def run(self):
        running = True
        move_counter = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.player.direction != [0, 1]:
                        self.player.direction = [0, -1]
                    elif event.key == pygame.K_DOWN and self.player.direction != [0, -1]:
                        self.player.direction = [0, 1]
                    elif event.key == pygame.K_LEFT and self.player.direction != [1, 0]:
                        self.player.direction = [-1, 0]
                    elif event.key == pygame.K_RIGHT and self.player.direction != [-1, 0]:
                        self.player.direction = [1, 0]
                    elif event.key == pygame.K_SPACE:
                        self.game_mode = GameMode((self.game_mode.value % 3) + 1)

            # Update game state
            move_counter += 1
            if move_counter >= FPS // (4 * self.player.speed):
                move_counter = 0
                self.player.move(None)
                
                # Update enemies based on game mode
                if self.game_mode in [GameMode.SURVIVAL, GameMode.HUNTER]:
                    for enemy in self.enemies:
                        enemy.chase_target(self.player)
                        enemy.move(None)

                # Check collisions
                if self.handle_collisions():
                    running = False

            # Spawn new enemies in survival mode
            if self.game_mode == GameMode.SURVIVAL and random.random() < 0.001:
                x = random.randint(0, GRID_COUNT - 1)
                y = random.randint(0, GRID_COUNT - 1)
                self.enemies.append(EnemySnake(x, y))

            self.update_power_ups()
            self.spawn_power_up()

            # Draw
            self.screen.fill(BLACK)
            
            # Draw game objects
            for food in self.food:
                food.draw(self.screen)
            for power_up in self.power_ups:
                power_up[0].draw(self.screen)
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)

            # Draw score and game mode
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {self.score}', True, WHITE)
            mode_text = font.render(f'Mode: {self.game_mode.name}', True, WHITE)
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(mode_text, (10, 50))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
