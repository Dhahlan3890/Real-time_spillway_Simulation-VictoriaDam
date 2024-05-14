#=================== CREATED BY ================ AHAMED DHAHLAN ==========================


import pygame
import sys
import random
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initialize Pygame
pygame.init()

image = pygame.image.load(resource_path('assets\dam ob.jpg'))
icon_image = pygame.image.load(resource_path('assets\logo2.png'))

#print(resource_path('assets\dam ob.jpg'))


# Set up font
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 26)
font2 = pygame.font.Font(None, 20)
button_font = pygame.font.Font(None, 22)
font4 = pygame.font.Font(None, 40)
font5 = pygame.font.Font(None, 12)


# Constants
WIDTH, HEIGHT = 1000, 500
BLUE = (0, 0, 255)
SILVER = (192, 192, 192)
GRAY = (247,235,178,180)
RED = (255,0,0)
GREEN = (100,255,0)

surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

def background_scene(image):
    size = pygame.transform.scale(image, (WIDTH,HEIGHT))
    screen.blit(size, (0,0))
    screen.blit(surface, (0,0))

button_color = (50,50,50)

# Set up button properties
button_width, button_height = 120, 25
screen_info = pygame.display.Info()

# Get screen width and height
scr_width = screen_info.current_w
scr_height = screen_info.current_h

button_x, button_y = 100/1000*WIDTH, 334/500*HEIGHT


def draw_button():
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    text = font1.render("Simulate", True, (255,255,255))
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)



box1_color = SILVER
box2_color = SILVER
box3_color = SILVER
box4_color = SILVER
box5_color = SILVER
box6_color = SILVER
box7_color = SILVER
box8_color = SILVER

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
pygame.display.set_caption("Real time dam simulation")



#screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)

# Create the blue box
box_width, box_height = 400, 437.95
water_width, water_height = 400, 0
box1_width, box1_height = 40, 95
box2_width, box2_height = 40, 95
box3_width, box3_height = 40, 95
box4_width, box4_height = 40, 95
box5_width, box5_height = 40, 95
box6_width, box6_height = 40, 95
box7_width, box7_height = 40, 95
box8_width, box8_height = 40, 95
ls_width, ls_height = 40, 40
box_x, box_y = (WIDTH - box_width) // 2, HEIGHT - box_height +30
water_x, water_y = (WIDTH - water_width) // 2, HEIGHT - water_height +30
box1_x, box1_y = (WIDTH - box1_width-350) // 2, HEIGHT - box1_height - 270
box2_x, box2_y = (WIDTH - box2_width-250) // 2, HEIGHT - box2_height - 270
box3_x, box3_y = (WIDTH - box3_width-150) // 2, HEIGHT - box3_height - 270
box4_x, box4_y = (WIDTH - box4_width-50) // 2, HEIGHT - box4_height - 270
box5_x, box5_y = (WIDTH - box5_width +50) // 2, HEIGHT - box5_height - 270
box6_x, box6_y = (WIDTH - box6_width +150) // 2, HEIGHT - box6_height - 270
box7_x, box7_y = (WIDTH - box7_width +250) // 2, HEIGHT - box7_height - 270
box8_x, box8_y = (WIDTH - box8_width +350) // 2, HEIGHT - box8_height - 270



#########################################################

water_fall_start1 = -500
water_fall_start2 = -500
water_fall_start3 = -500
water_fall_start4 = -500
water_fall_start5 = -500
water_fall_start6 = -500
water_fall_start7 = -500
water_fall_start8 = -500

flow_rate = 0

class Droplet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((2, 7))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = random.randint(1, 15)

    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > 1000/500*HEIGHT:
            self.rect.y = (box1_y +95)/500*HEIGHT
            x_values = [random.uniform(water_fall_start1/1000*WIDTH, (water_fall_start1+box1_width)/1000*WIDTH),
                        random.uniform(water_fall_start2/1000*WIDTH, (water_fall_start2+box1_width)/1000*WIDTH),
                         random.uniform(water_fall_start3/1000*WIDTH, (water_fall_start3+box1_width)/1000*WIDTH),
                          random.uniform(water_fall_start4/1000*WIDTH, (water_fall_start4+box1_width)/1000*WIDTH),
                           random.uniform(water_fall_start5/1000*WIDTH, (water_fall_start5+box1_width)/1000*WIDTH),
                            random.uniform(water_fall_start6/1000*WIDTH, (water_fall_start6+box1_width)/1000*WIDTH),
                             random.uniform(water_fall_start7/1000*WIDTH, (water_fall_start7+box1_width)/1000*WIDTH),
                              random.uniform(water_fall_start8/1000*WIDTH, (water_fall_start8+box1_width)/1000*WIDTH) ]
            self.rect.x = random.choice(x_values)



# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create droplets
for _ in range(20000):
    droplet = Droplet(random.randint(0, 0), random.randint(100, HEIGHT))
    all_sprites.add(droplet)

##############################################################

# Set up clock to control the frame rate
clock = pygame.time.Clock()

GS = [[(255,255,255,200)] * 7 for _ in range(8)]

L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,L31,L32 = [RED]*32
water_fall_start1 = -500
water_fall_start2 = -500
water_fall_start3 = -500
water_fall_start4 = -500
water_fall_start5 = -500
water_fall_start6 = -500
water_fall_start7 = -500
water_fall_start8 = -500


box1_level, box2_level, box3_level, box4_level, box5_level, box6_level, box7_level, box8_level = 0,0,0,0,0,0,0,0

button_clicked = False
up_key_pressed = False
down_key_pressed = False
# Main game loop
while True:
    
#################################################################################
    #WIDTH = screen.get_width()
    #HEIGHT = screen.get_height()
    
    font = pygame.font.Font(None, int(34/500*HEIGHT))
    font1 = pygame.font.Font(None, int(24/500*HEIGHT))
    font2 = pygame.font.Font(None, int(20/500*HEIGHT))
    button_font = pygame.font.Font(None, int(22/500*HEIGHT))
    font4 = pygame.font.Font(None, int(40/500*HEIGHT))

    button_width, button_height = 120/1000*WIDTH, 25/500*HEIGHT

    button_x, button_y = 88/1000*WIDTH, 380/500*HEIGHT

    ls_width, ls_height = 40/1000*WIDTH, 40/500*HEIGHT
    water_x, water_y = (WIDTH - water_width) // 2, (HEIGHT - water_height +30)/500*HEIGHT

    


   
            
        
        
        
        

        

    

#########################################################################################

    GS = [[(255,255,255,200)] * 7 for _ in range(8)]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the button area
            x, y = pygame.mouse.get_pos()
            if button_x <= x <= button_x + button_width and \
                    button_y <= y <= button_y + button_height:
                button_clicked = not button_clicked
        
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)



    keys = pygame.key.get_pressed()


    # Increase the height of the box when the up arrow key is pressed
    if keys[pygame.K_UP] or up_key_pressed:
        box_y -= 0.001
        box_height += 0.001
        water_height += 0.1/500*HEIGHT

        if box_height >= 438.04:
            box4_level, box5_level = 7, 7
            water_fall_start4 = box4_x
            water_fall_start5 = box5_x
            flow_rate = 78 * 2

        if box_height >= 438.08:
            box3_level, box6_level = 7, 7
            water_fall_start3 = box3_x
            water_fall_start6 = box6_x
            flow_rate = 78 * 4

        if box_height >= 438.12:
            box2_level, box7_level = 7, 7
            water_fall_start2 = box2_x
            water_fall_start7 = box7_x
            flow_rate = 78 * 6

        if box_height >= 438.16:
            box1_level, box8_level = 7, 7
            water_fall_start1 = box1_x
            water_fall_start8 = box8_x
            flow_rate = 78 * 8

        if box_height >= 438.20:
            box4_level, box5_level = 25, 25
            flow_rate = 250*2 + 78 * 6

        if box_height >= 438.24:
            box3_level, box6_level = 25, 25
            flow_rate = 250*4 + 78 * 4

        if box_height >= 438.28:
            box2_level, box7_level = 25, 25
            flow_rate = 250*6 + 78 * 2

        if box_height >= 438.32:
            box1_level, box8_level = 25, 25
            flow_rate = 250*8

        if box_height >= 438.36:
            box4_level, box5_level = 47, 47
            flow_rate = 438 * 2 + 250*6

        if box_height >= 438.40:
            box3_level, box6_level = 47, 47
            flow_rate = 438 * 4 + 250*4

        if box_height >= 438.44:
            box2_level, box7_level = 47, 47
            flow_rate = 438 * 6 + 250*2

        if box_height >= 438.48:
            box1_level, box8_level = 47, 47
            flow_rate = 438 * 8

        if box_height >= 438.52:
            box4_level, box5_level = 95, 95
            flow_rate = 625 * 2 + 438 * 6

        if box_height >= 438.56:
            box3_level, box6_level = 95, 95
            flow_rate = 625 * 4 + 438 * 4

        if box_height >= 438.60:
            box2_level, box7_level = 95, 95
            flow_rate = 625 * 6 + 438 * 2

        if box_height >= 438.64:
            box1_level, box8_level = 95, 95
            flow_rate = 625 * 8



        if box_height >= 438.66:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [BLUE] * 32
            #print("gate L32 opened")
        elif box_height >= 438.65:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30 = [BLUE] * 31
            #print("gate L30 opened")
        elif box_height >= 438.61:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31 = [BLUE] * 30
            #print("gate L31 opened")
        elif box_height >= 438.58:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28 = [BLUE] * 29
            #print("gate L28 opened")
        elif box_height >= 438.57:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29 = [BLUE] * 28
            #print("gate L29 opened")
        elif box_height >= 438.54:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26 = [BLUE] * 27
            #print("gate L26 opened")
        elif box_height >= 438.53:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27 = [BLUE] * 26
            #print("gate L27 opened")
        elif box_height >= 438.50:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24 = [BLUE] * 25
            #print("gate L24 opened")
        elif box_height >= 438.49:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25 = [BLUE] * 24
            #print("gate L25 opened")
        elif box_height >= 438.46:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22 = [BLUE] * 23
            #print("gate L22 opened")
        elif box_height >= 438.45:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23 = [BLUE] * 22
            #print("gate L23 opened")
        elif box_height >= 438.42:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20 = [BLUE] * 21
            #print("gate L20 opened")
        elif box_height >= 438.41:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21 = [BLUE] * 20
            #print("gate L21 opened")
        elif box_height >= 438.38:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18 = [BLUE] * 19
            #print("gate L18 opened")
        elif box_height >= 438.37:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19 = [BLUE] * 18
            #print("gate L19 opened")
        elif box_height >= 438.34:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16 = [BLUE] * 17
            #print("gate L16 opened")
        elif box_height >= 438.33:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17 = [BLUE] * 16
            #print("gate L17 opened")
        elif box_height >= 438.30:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14 = [BLUE] * 15
            #print("gate L14 opened")
        elif box_height >= 438.29:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15 = [BLUE] * 14
            #print("gate L15 opened")
        elif box_height >= 438.26:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12 = [BLUE] * 13
            #print("gate L12 opened")
        elif box_height >= 438.25:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13 = [BLUE] * 12
            #print("gate L13 opened")
        elif box_height >= 438.22:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10 = [BLUE] * 11
            #print("gate L10 opened")
        elif box_height >= 438.21:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11 = [BLUE] * 10
            #print("gate L11 opened")
        elif box_height >= 438.18:
            L1, L3,L2,L5, L4,L7, L6, L9, L8 = [BLUE] * 9
            #print("gate L8 opened")
        elif box_height >= 438.17:
            L1, L3,L2,L5, L4,L7, L6, L9 = [BLUE] * 8
            #print("gate L9 opened")
        elif box_height >= 438.14:
            L1, L3,L2,L5, L4,L7, L6 = [BLUE] * 7
            #print("gate L6 opened")
        elif box_height >= 438.13:
            L1, L3,L2,L5, L4,L7 = [BLUE] * 6
            #print("gate L7 opened")
        elif box_height >= 438.10:
            L1, L3,L2,L5, L4 = [BLUE] * 5
            #print("gate L4 opened")
        elif box_height >= 438.09:
            L1, L3,L2,L5 = [BLUE] * 4
            #print("gate L5 opened")
        elif box_height >= 438.06:
            L1, L3,L2 = [BLUE] * 3
            #print("gate L2 opened")
        elif box_height >= 438.05:
            L1, L3 = [BLUE] * 2
            #print("gate L3 opened")
        elif box_height >= 438.01:
            L1 = BLUE
            #print("gate L1 opened")



    if keys[pygame.K_DOWN]:
        box_y += 0.001
        box_height -= 0.001
        water_height -= 0.1/500*HEIGHT
        

        if box_height < 438.04 - 0.06:
            box4_level, box5_level = 0, 0
            water_fall_start4 = -500
            water_fall_start5 = -500
            flow_rate = 0

        elif box_height < 438.08 - 0.06:
            box3_level, box6_level = 0, 0
            water_fall_start3 = -500
            water_fall_start6 = -500
            flow_rate = 78 * 2

        elif box_height < 438.12 - 0.06:
            box2_level, box7_level = 0, 0
            water_fall_start2 = -500
            water_fall_start7 = -500
            flow_rate = 78 * 4

        elif box_height < 438.16 - 0.06:
            box1_level, box8_level = 0, 0
            water_fall_start1 = -500
            water_fall_start8 = -500
            flow_rate = 78 * 6

        elif box_height < 438.20 - 0.06:
            box4_level, box5_level = 7, 7
            flow_rate = 78 * 8

        elif box_height < 438.24 - 0.06:
            box3_level, box6_level = 7, 7
            flow_rate = 250 * 2 + 78 * 6

        elif box_height < 438.28 - 0.06:
            box2_level, box7_level = 7, 7
            flow_rate = 250 * 4 + 78 * 4

        elif box_height < 438.32 - 0.06:
            box1_level, box8_level = 7, 7
            flow_rate = 250 * 6 + 78 * 2

        elif box_height < 438.36 - 0.06:
            box4_level, box5_level = 25, 25
            flow_rate = 250 * 8

        elif box_height < 438.40 - 0.06:
            box3_level, box6_level = 25, 25
            flow_rate = 438 * 2 + 250 * 6

        elif box_height < 438.44 - 0.06:
            box2_level, box7_level = 25, 25
            flow_rate = 438 * 4 + 250 * 4

        elif box_height < 438.48 - 0.06:
            box1_level, box8_level = 25, 25
            flow_rate = 438 * 6 + 250 * 2

        elif box_height < 438.52 - 0.06:
            box4_level, box5_level = 47, 47
            flow_rate = 438 * 8

        elif box_height < 438.56 - 0.06:
            box3_level, box6_level = 47, 47
            flow_rate = 625 * 2 + 438 * 6

        elif box_height < 438.60 - 0.06:
            box2_level, box7_level = 47, 47
            flow_rate = 625 * 4 + 438 * 4

        elif box_height < 438.64 - 0.06:
            box1_level, box8_level = 47, 47
            flow_rate = 625 * 6 + 438 * 2

        


        if box_height < 437.98:
            L1, L3, L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 =[RED] * 32
            #print("gate L1 closed")
        elif box_height < 438.02:
            L3, L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 31
            #print("gate L3 closed")
        elif box_height < 438.03:
            L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 30
            #print("gate L2 closed")
        elif box_height < 438.06:
            L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 29
            #print("gate L5 closed")
        elif box_height < 438.07:
            L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 28
            #print("gate L4 closed")
        elif box_height < 438.10:
            L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 27
            #print("gate L7 closed")
        elif box_height < 438.11:
            L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 26
            #print("gate L6 closed")
        elif box_height < 438.14:
            L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 25
            #print("gate L9 closed")
        elif box_height < 438.15:
            L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 24
            #print("gate L8 closed")
        elif box_height < 438.18:
            L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 23
            #print("gate L11 closed")
        elif box_height < 438.19:
            L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 22
            #print("gate L10 closed")
        elif box_height < 438.22:
            L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 21
            #print("gate L13 closed")
        elif box_height < 438.23:
            L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 20
            #print("gate L12 closed")
        elif box_height < 438.26:
            L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 19
            #print("gate L15 closed")
        elif box_height < 438.27:
            L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 18
            #print("gate L14 closed")
        elif box_height < 438.30:
            L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 17
            #print("gate L17 closed")
        elif box_height < 438.31:
            L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 16
            #print("gate L16 closed")
        elif box_height < 438.34:
            L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 15
            #print("gate L19 closed")
        elif box_height < 438.35:
            L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 14
            #print("gate L18 closed")
        elif box_height < 438.38:
            L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 13
            #print("gate L21 closed")
        elif box_height < 438.39:
            L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 12
            #print("gate L20 closed")
        elif box_height < 438.42:
            L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 11
            #print("gate L23 closed")
        elif box_height < 438.43:
            L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 10
            #print("gate L22 closed")
        elif box_height < 438.46:
            L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 9
            #print("gate L25 closed")
        elif box_height < 438.47:
            L24, L27, L26, L29, L28, L31, L30, L32 = [RED] *8
            #print("gate L24 closed")
        elif box_height < 438.50:
            L27, L26, L29, L28, L31, L30, L32 = [RED] *7
            #print("gate L27 closed")
        elif box_height < 438.51:
            L26, L29, L28, L31, L30, L32 = [RED] *6
            #print("gate L26 closed")
        elif box_height < 438.54:
            L29, L28, L31, L30, L32 = [RED] *5
            #print("gate L29 closed")
        elif box_height < 438.55:
            L28, L31, L30, L32 = [RED] *4
            #print("gate L28 closed")
        elif box_height < 438.58:
            L31, L30, L32 = [RED] *3
            #print("gate L31 closed")
        elif box_height < 438.59:
            L30, L32 = [RED] *2
            #print("gate L30 closed")
        elif box_height < 438.63:
            L32 = RED
            #print("gate L32 closed")

        

    # Clear the screen
    screen.fill((255, 255, 255))
    background_scene(image)

    pygame.draw.rect(surface, GRAY, (box_x/1000*WIDTH, (box_y-500)/500*HEIGHT, box_width/1000*WIDTH, (500+box_height)/500*HEIGHT))

    for i in range(8):
        pygame.draw.rect(screen, box1_color, (globals()[f"box{i+1}_x"]/1000*WIDTH, globals()[f"box{i+1}_y"]/500*HEIGHT, globals()[f"box{i+1}_width"]/1000*WIDTH, globals()[f"box{i+1}_height"]/500*HEIGHT))
        height_text1 = font1.render(str(globals()[f"box{i+1}_level"]/10), True, (0, 0, 0))
        screen.blit(height_text1, (globals()[f"box{i+1}_x"]/1000*WIDTH, (globals()[f"box{i+1}_y"]-20)/500*HEIGHT))
        pygame.draw.rect(screen, BLUE, (globals()[f"box{i+1}_x"]/1000*WIDTH, globals()[f"box{i+1}_y"]/500*HEIGHT + (95-globals()[f"box{i+1}_level"])/500*HEIGHT, globals()[f"box{i+1}_width"]/1000*WIDTH, globals()[f"box{i+1}_level"]/500*HEIGHT))
    # Draw the blue box
    
    for i in range(0,32):
        pygame.draw.rect(screen, globals()[f"L{i+1}"], ((750+50*(i%5))/1000*WIDTH, (50+50*(i//5))/500*HEIGHT, ls_width, ls_height))

    
    for j in range(8):
        box_level = globals()[f"box{j+1}_level"]
        if box_level > 9.35 * 10:
            GS[j][5] = BLUE
            GS[j][6] = BLUE
        elif 9.3 * 10 < box_level <= 9.35 * 10:
            GS[j][5] = BLUE
        elif 4.68 * 10 < box_level <= 9.3 * 10:
            GS[j][4] = BLUE
            GS[j][5] = BLUE
        elif 4.65 * 10 < box_level <= 4.68 * 10:
            GS[j][4] = BLUE
        elif 2.48 * 10 < box_level <= 4.65 * 10:
            GS[j][3] = BLUE
            GS[j][4] = BLUE
        elif 2.45 * 10 < box_level <= 2.48 * 10:
            GS[j][3] = BLUE
        elif 0.68 * 10 < box_level <= 2.45 * 10:
            GS[j][2] = BLUE
            GS[j][3] = BLUE
        elif 0.65 * 10 < box_level <= 0.68 * 10:
            GS[j][2] = BLUE
        elif 0.15 * 10 < box_level <= 0.65 * 10:
            GS[j][1] = BLUE
            GS[j][2] = BLUE
        elif 0.025 * 10 < box_level <= 0.15 * 10:
            GS[j][1] = BLUE
        elif box_level > 0:
            GS[j][0] = BLUE
            GS[j][1] = BLUE
        
        


    for j in range(8):
        for i in range(7):
            pygame.draw.rect(screen, GS[j][i], ((310 + 50*j)/1000*WIDTH, (80-12*i)/500*HEIGHT, 10/1000*WIDTH, 10/500*HEIGHT))
            height_text1 = font2.render(f"Vx{i+1}", True, GS[j][i])
            screen.blit(height_text1, ((320 + 50*j)/1000*WIDTH, (80 - 12*i)/500*HEIGHT))

  
    

    for i in range(0,32):
        ls_text = font2.render(f'LS{i+1}', True, (255, 255, 255))
        screen.blit(ls_text, ((755+50*(i%5))/1000*WIDTH, (65+50*(i//5))/500*HEIGHT))

    for i in range(int(400/1000*WIDTH)):
        vibration = random.uniform(0,5)
        pygame.draw.rect(surface, (0,0,255,200), (i+300/1000*WIDTH, HEIGHT-vibration-water_height+15, 5/1000*WIDTH, water_height+vibration-15))

    
    
    # Render and display the blue box height
    pygame.draw.rect(surface, GRAY, (5/1000*WIDTH, 5/500*HEIGHT, 280/1000*WIDTH, 60/500*HEIGHT))
    height_text = font.render(f"Water Level: {box_height:.3f} m", True, (0,0,0))
    #shadow_text = font.render(f"Water Level: {box_height:.3f} m", True, (50, 50, 100))
    #screen.blit(shadow_text, (10/1000*WIDTH + 1.5, 10/500*HEIGHT + 1.5))
    screen.blit(height_text, (10/1000*WIDTH, 10/500*HEIGHT))
    height_text = font1.render(f"Flow Rate: {flow_rate:.3f} m3/s", True, (0,0,0))
    #shadow_text = font1.render(f"Flow Rate: {flow_rate:.3f} m3/s", True, (50, 50, 100))
    #screen.blit(shadow_text, (10/1000*WIDTH + 1, 40/500*HEIGHT + 1))
    screen.blit(height_text, (10/1000*WIDTH, 40/500*HEIGHT))

    all_sprites.update()

    all_sprites.draw(screen)

    resized_icon = pygame.transform.scale(icon_image, (WIDTH//4,HEIGHT//4))

    screen.blit(resized_icon, (19/1000*WIDTH, HEIGHT//4.5))

    height_text = font1.render("MAHAWELI AUTHORITY", True, (255, 255, 255))
    shadow_text = font1.render("MAHAWELI AUTHORITY", True, (25, 25, 50))
    
    screen.blit(shadow_text, (50/1000*WIDTH+2, 250/500*HEIGHT+2))
    screen.blit(height_text, (50/1000*WIDTH, 250/500*HEIGHT))
    height_text = font1.render("OF", True, (255, 255, 255))
    shadow_text = font1.render("OF", True, (25, 25, 50))
    
    screen.blit(shadow_text, (132/1000*WIDTH+2, 270/500*HEIGHT+2))
    screen.blit(height_text, (132/1000*WIDTH, 270/500*HEIGHT))
    height_text = font1.render("SRI LANKA", True, (255, 255, 255))
    shadow_text = font1.render("SRI LANKA", True, (25, 25, 50))
    
    screen.blit(shadow_text, (100/1000*WIDTH+2, 290/500*HEIGHT+2))
    screen.blit(height_text, (100/1000*WIDTH, 290/500*HEIGHT))
    height_text = font2.render("EIC OFFICE - VICTORIA", True, (255, 255, 255))
    shadow_text = font2.render("EIC OFFICE - VICTORIA", True, (25, 25, 50))
    
    screen.blit(shadow_text, (72/1000*WIDTH+2, 310/500*HEIGHT+2))
    screen.blit(height_text, (72/1000*WIDTH, 310/500*HEIGHT))

    height_text = font5.render("Dhahaln A.S.A. - Thaseenthan S. - Senevirathne H.A.M.I.C.", True, (0,0,0))
    pygame.draw.rect(surface, (255, 255, 255, 180), (980/1000*WIDTH - height_text.get_width(), 480/500*HEIGHT - height_text.get_height(), 280/1000*WIDTH, 60/500*HEIGHT))
    
    screen.blit(height_text, (990/1000*WIDTH - height_text.get_width(), 485/500*HEIGHT - height_text.get_height()))
    height_text1 = font5.render("Faculty of Engineering - University of Ruhuna", True, (0,0,0))
    screen.blit(height_text1, (990/1000*WIDTH - height_text.get_width(), 495/500*HEIGHT - height_text.get_height()))



    if button_clicked:
        pygame.draw.rect(screen, (0, 255, 0), (button_x, button_y, button_width, button_height))
        text = font1.render("Stop", True, (255,255,255))
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text, text_rect)
        if box_height < 438.7:
            up_key_pressed = True
    else:
        pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
        text = font1.render("Auto Simulate", True, (255,255,255))
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text, text_rect)
        up_key_pressed = False


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)



    #updated_box_height = box_height
