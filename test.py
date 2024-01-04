import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Dam parameters
dam_width = 50
dam_height = 300
gate_width = 20
gate_height = 100
num_gates = 8
gate_gap = 10  # Adjust this value for the desired gap between gates

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dam Gates Opening Simulation")
clock = pygame.time.Clock()

# Dam class
class Dam(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((dam_width, dam_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - dam_height // 2))

# Gate class
class Gate(pygame.sprite.Sprite):
    def __init__(self, x_offset):
        super().__init__()
        self.image = pygame.Surface((gate_width, gate_height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2 + x_offset, HEIGHT - dam_height // 2 - gate_height // 2))

# Create sprites
dam = Dam()
gates = pygame.sprite.Group()

# Create eight gates with a gap between them
gate_offsets = [(i - num_gates // 2) * (gate_width + gate_gap) for i in range(num_gates)]
for offset in gate_offsets:
    gate = Gate(offset)
    gates.add(gate)

# Sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(dam, gates)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Refresh screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
