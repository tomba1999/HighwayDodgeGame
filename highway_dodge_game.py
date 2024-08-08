import pygame
import sys
import random
from PIL import Image

# Initialize pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module

# Constants
UNIT = 50
NUM_UNITS_WIDTH = 13  # Width in units, including borders
NUM_UNITS_HEIGHT = 16
win_width = UNIT * NUM_UNITS_WIDTH  # 650 pixels
win_height = UNIT * NUM_UNITS_HEIGHT  # 800 pixels
border_width = UNIT  # 1 unit = 50 pixels on both sides
lane_width = UNIT * 2  # 2 units = 100 pixels
num_lanes = 6  # 6 lanes

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# Fonts
title_font = pygame.font.SysFont(None, 80)
button_font = pygame.font.SysFont(None, 40)

# Set up display
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Highway Dodge Game")


# Load background frames
def extract_frames(gif_path):
    gif = Image.open(gif_path)
    frames = []
    try:
        while True:
            frame = gif.convert("RGBA")
            frames.append(frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    return frames


gif_path = r'resources/Backround2.gif'
frames = extract_frames(gif_path)


def load_frames(frames):
    pygame_frames = []
    for frame in frames:
        mode = frame.mode
        size = frame.size
        data = frame.tobytes()
        image = pygame.image.fromstring(data, size, mode)
        pygame_frames.append(image)
    return pygame_frames


pygame_frames = load_frames(frames)
pygame_frames = [pygame.transform.scale(frame, (win_width, win_height)) for frame in pygame_frames]

# Load car image
car_image_path = r'resources/OrangeCar.png'
car_image = pygame.image.load(car_image_path)
car_image = pygame.transform.scale(car_image,
                                   (int(UNIT * 1.5), int(UNIT * 1.5 * 1.8)))  # Scale the image to the car's dimensions

# Load truck images
truck_image_path_1 = r'resources/BlueTruck.png'  # Replace with the actual path to your first truck image
truck_image_path_2 = r'resources/YellowTruck.png'  # Replace with the actual path to your second truck image

truck_image_1 = pygame.image.load(truck_image_path_1)
truck_image_2 = pygame.image.load(truck_image_path_2)

# Scale truck images to the obstacle dimensions
truck_image_1 = pygame.transform.scale(truck_image_1, (int(UNIT * 1.5), int(UNIT * 1.5 * 1.8)))
truck_image_2 = pygame.transform.scale(truck_image_2, (int(UNIT * 1.5), int(UNIT * 1.5 * 1.8)))

# Load soundtrack
soundtrack_path = r'resources/soundtrack.mp3'  # Replace with the actual path to your soundtrack file
secondary_soundtrack_path = r'resources/secondary_soundtrack.mp3'  # Replace with the actual path to your secondary soundtrack file

# Load and set up soundtracks
pygame.mixer.music.load(soundtrack_path)
secondary_track = pygame.mixer.Sound(secondary_soundtrack_path)

# Game variables
car_width = int(UNIT * 1.5)  # 1.5 units = 75 pixels
car_height = int(car_width * 1.8)
car_x = (win_width - car_width) // 2
car_y = win_height - car_height - 10
car_speed_x = 0
car_speed_y = 0
max_speed_forward_backward = 12
max_speed_sideways = 8.5  # Slower max speed for sideways movement
acceleration = 1  # General acceleration for forward/backward movement
acceleration_sideways = 2.5  # Acceleration specifically for sideways movement
deceleration_sideways = 2  # Faster deceleration for sideways movement
deceleration_forward_backward = 1  # Slower deceleration for forward/backward movement

obs_width = car_width
obs_height = car_height
lane_offsets = [border_width + i * lane_width for i in range(num_lanes)]
obs = []

shield_width = UNIT  # Same width as a unit
shield_height = UNIT  # Same height as a unit
shield_item = None
shield_duration = 2 * 30  # Shield lasts for 2 seconds (120 frames if 30 FPS)
shield_active = False
shield_timer = 0
shields_collected = 1  # Player starts with one shield

# Load shield image
shield_image_path = r'resources/Shield.png'  # Replace with the actual path to your shield image
shield_image = pygame.image.load(shield_image_path)
shield_image = pygame.transform.scale(shield_image, (shield_width, shield_height))  # Scale the image to the shield's dimensions


# Hurtbox variables
hurtbox_offset_x = car_width * 0.1  # 10% offset from the left
hurtbox_offset_y = car_height * 0.1  # 10% offset from the top
hurtbox_width = car_width * 0.8  # 80% of the car's width
hurtbox_height = car_height * 0.8  # 80% of the car's height

# Load car images
car_images = {
    "orange": pygame.transform.scale(pygame.image.load(r'resources/OrangeCar.png'), (int(UNIT * 1.5), int(UNIT * 1.5 * 1.8))),
    "purple": pygame.transform.scale(pygame.image.load(r'resources/PurpleCar.png'), (int(UNIT * 1.5), int(UNIT * 1.5 * 1.8))),
    "green": pygame.transform.scale(pygame.image.load(r'resources/GreenCar.png'), (int(UNIT * 1.5), int(UNIT * 1.5 * 1.8)))
}

# Default selected car
selected_car = "orange"
car_image = car_images[selected_car]

last_distance = 0
highscore = 0

# Global variables
obs = []
min_distance = 1000  # Start with 1000
elapsed_time = 0  # To track the time elapsed

# Create a clock object
clock = pygame.time.Clock()

# Global variables
min_distance = 1000  # Start with 1000
elapsed_time = 0  # To track the time elapsed

# Global variables
obs = []
min_distance = 1000  # Start with 1000
elapsed_time = 0  # To track the time elapsed
game_over = False  # Track if the game ended in a collision

def controls_screen():
    run = True
    while run:
        win.fill(white)
        draw_text('Controls', title_font, black, win, win_width // 2 - 100, 50)

        # Display the controls information
        controls_text = [
            "Press LEFT to move the car to the left",
            "Press RIGHT to move the car to the right",
            "Press UP to speed the car up",
            "Press DOWN to slow the car down",
            "Press SPACE to activate your shield",
            "You have one shield item at default.",
            "When you have used your shield, you",
            "can collect a new one.",
            "The shield is active for 2 seconds only."
        ]

        for i, line in enumerate(controls_text):
            draw_text(line, button_font, black, win, 50, 150 + i * 40)

        back_button = pygame.Rect(20, 20, 100, 40)
        draw_button('Back', button_font, gray, back_button, win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return  # Go back to the home screen

        pygame.display.update()

def view_highscore_screen():
    global highscore

    run = True
    while run:
        win.fill(white)
        draw_text('Highscore', title_font, black, win, win_width // 2 - 100, 50)

        # Display the highscore
        draw_text(f"Highscore: {highscore:.1f} km", button_font, black, win, win_width // 2 - 100, 200)

        back_button = pygame.Rect(20, 20, 100, 40)
        draw_button('Back', button_font, gray, back_button, win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return  # Go back to the home screen

        pygame.display.update()


def car_selection_screen():
    global selected_car, car_image

    run = True
    while run:
        win.fill(white)
        draw_text('Choose Your Car', title_font, black, win, win_width // 2 - 200, 50)

        # Define positions for car images
        orange_car_pos = (win_width // 2 - 300, 200)
        purple_car_pos = (win_width // 2 - 100, 200)
        green_car_pos = (win_width // 2 + 100, 200)
        back_button_pos = (20, 20)

        # Draw car images
        win.blit(car_images["orange"], orange_car_pos)
        win.blit(car_images["purple"], purple_car_pos)
        win.blit(car_images["green"], green_car_pos)

        # Draw borders around selected car
        if selected_car == "orange":
            pygame.draw.rect(win, blue, (*orange_car_pos, car_images["orange"].get_width(), car_images["orange"].get_height()), 5)
        elif selected_car == "purple":
            pygame.draw.rect(win, blue, (*purple_car_pos, car_images["purple"].get_width(), car_images["purple"].get_height()), 5)
        elif selected_car == "green":
            pygame.draw.rect(win, blue, (*green_car_pos, car_images["green"].get_width(), car_images["green"].get_height()), 5)

        # Draw back button
        back_button = pygame.Rect(*back_button_pos, 100, 40)
        draw_button('Back', button_font, gray, back_button, win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    car_image = car_images[selected_car]
                    return  # Go back to the home screen
                elif pygame.Rect(*orange_car_pos, car_images["orange"].get_width(), car_images["orange"].get_height()).collidepoint(event.pos):
                    selected_car = "orange"
                elif pygame.Rect(*purple_car_pos, car_images["purple"].get_width(), car_images["purple"].get_height()).collidepoint(event.pos):
                    selected_car = "purple"
                elif pygame.Rect(*green_car_pos, car_images["green"].get_width(), car_images["green"].get_height()).collidepoint(event.pos):
                    selected_car = "green"

        pygame.display.update()


# Functions for game mechanics
def create_obstacle(min_distance):
    global obs

    possible_lanes = list(range(num_lanes))

    # Remove lanes that have an obstacle too close to the top
    for ob in obs:
        if ob[1] < min_distance:
            lane = lane_offsets.index(ob[0])
            if lane in possible_lanes:
                possible_lanes.remove(lane)

    # Ensure at least one lane is always free
    if len(possible_lanes) > 1:
        lane = random.choice(possible_lanes)
        x_pos = lane_offsets[lane]

        # Keep track of speed counts
        speed_counts = {}
        for ob in obs:
            speed = ob[2]
            if speed not in speed_counts:
                speed_counts[speed] = 0
            speed_counts[speed] += 1

        # Generate a speed ensuring no more than 3 lanes have the same speed
        while True:
            speed = random.uniform(6, 11)
            if speed_counts.get(speed, 0) < 3:
                break

        # Randomly choose a truck image
        truck_image = random.choice([truck_image_1, truck_image_2])

        obs.append([x_pos, -obs_height, speed, truck_image])


def draw_car(x, y):
    win.blit(car_image, (x, y))


# Function to draw obstacles
def draw_obstacles(obstacles):
    for ob in obstacles:
        truck_image = ob[3]
        win.blit(truck_image, (ob[0], ob[1]))


def adjust_speeds(obstacles):
    barrier_distance = 50  # Distance behind each slower car to place the barrier
    for i in range(len(obstacles)):
        for j in range(len(obstacles)):
            if i != j and obstacles[i][0] == obstacles[j][0]:  # Same lane
                if obstacles[i][1] < obstacles[j][1]:  # obstacles[i] is above obstacles[j]
                    if obstacles[j][1] - (obstacles[i][1] + obs_height) < barrier_distance:
                        obstacles[j][2] = obstacles[i][2]  # Match speed


def create_shield():
    global shield_item, shields_collected
    if shield_item is None and shields_collected == 0 and random.randint(1, 90) == 1:  # Rare spawn only if no shields
        lane = random.randint(0, num_lanes - 1)
        x_pos = lane_offsets[lane] + (lane_width - shield_width) // 2
        y_pos = -shield_height
        shield_item = [x_pos, y_pos]


def draw_shield_item(x, y):
    win.blit(shield_image, (x, y))



def draw_shield(x, y):
    pygame.draw.rect(win, (0, 255, 255), [x - 5, y - 5, car_width + 10, car_height + 10], 3)


def quit_game():
    pygame.mixer.music.stop()  # Stop the music
    secondary_track.stop()  # Stop the secondary track
    pygame.quit()
    sys.exit()


# UI Functions
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_button(text, font, color, rect, surface):
    pygame.draw.rect(surface, color, rect)
    draw_text(text, font, black, surface, rect.x + 10, rect.y + 10)


# Home Screen
def home_screen():
    global last_distance, game_over

    run = True
    while run:
        win.fill(white)

        # Display "Game Over" if the game ended in a collision
        if game_over:
            draw_text('Game Over', title_font, red, win, win_width // 2 - 200, 100)
        else:
            draw_text('Highway Dodge', title_font, black, win, win_width // 2 - 200, 100)

        # Adjust button positions
        start_button = pygame.Rect(win_width // 2 - 200, 300, 200, 50)
        controls_button = pygame.Rect(win_width // 2, 300, 200, 50)
        choose_car_button = pygame.Rect(win_width // 2 - 200, 400, 200, 50)
        view_highscore_button = pygame.Rect(win_width // 2, 400, 200, 50)
        exit_button = pygame.Rect(win_width - 100, 20, 80, 40)

        draw_button('New Game', button_font, gray, start_button, win)
        draw_button('Controls', button_font, gray, controls_button, win)
        draw_button('Choose Car', button_font, gray, choose_car_button, win)
        draw_button('Highscore', button_font, gray, view_highscore_button, win)
        draw_button('Exit', button_font, gray, exit_button, win)

        # Display last distance
        if last_distance > 0:
            draw_text(f"Last Distance: {last_distance:.1f} km", button_font, red, win, win_width // 2 - 200, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_over = False  # Reset game_over status
                    return True  # Start the game
                elif controls_button.collidepoint(event.pos):
                    controls_screen()  # Go to controls screen
                elif choose_car_button.collidepoint(event.pos):
                    car_selection_screen()  # Go to car selection screen
                elif view_highscore_button.collidepoint(event.pos):
                    view_highscore_screen()  # Go to highscore screen
                elif exit_button.collidepoint(event.pos):
                    quit_game()

        pygame.display.update()
    return False

def game_loop():
    global car_x, car_y, car_speed_x, car_speed_y, shield_active, shield_timer, shields_collected, obs, shield_item, car_image, last_distance, highscore, min_distance, elapsed_time, game_over

    # Reset min_distance and elapsed_time
    min_distance = 1000
    elapsed_time = 0

    # Start the primary soundtrack
    pygame.mixer.music.set_volume(0.5)  # Set volume for the primary track (optional)
    pygame.mixer.music.play(-1)  # Play the music indefinitely

    # Start the secondary soundtrack
    secondary_track.set_volume(0.8)  # Set volume for the secondary track (optional)
    secondary_track.play(-1)  # Play the sound indefinitely

    car_x = (win_width - car_width) // 2
    car_y = win_height - car_height - 10
    car_speed_x = 0
    car_speed_y = 0
    shield_active = False
    shield_timer = 0
    shields_collected = 1
    obs = []
    shield_item = None

    distance = 0.0  # Initialize distance
    distance_increment = 0.1  # Increment by 0.1 km every second
    distance_timer = 0  # Timer for distance increment

    run = True
    clock = pygame.time.Clock()
    frame_index = 0
    frame_rate = 24  # Number of frames per second for the GIF
    frame_delay = int(30 / frame_rate)

    while run:
        dt = clock.tick(30) / 1000.0  # Delta time in seconds

        # Update elapsed time
        elapsed_time += dt

        # Decrease min_distance by 5 every second until it reaches 150
        if min_distance > 200:
            min_distance = max(150, 1000 - int(elapsed_time) * 4)

        if frame_index >= len(pygame_frames):
            frame_index = 0

        win.blit(pygame_frames[frame_index], (0, 0))

        if clock.get_time() % frame_delay == 0:
            frame_index += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit_game()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and car_x > border_width:
            car_speed_x = max(car_speed_x - acceleration_sideways, -max_speed_sideways)
        elif keys[pygame.K_RIGHT] and car_x < win_width - border_width - car_width:
            car_speed_x = min(car_speed_x + acceleration_sideways, max_speed_sideways)
        else:
            if car_speed_x > 0:
                car_speed_x = max(car_speed_x - deceleration_sideways, 0)
            elif car_speed_x < 0:
                car_speed_x = min(car_speed_x + deceleration_sideways, 0)

        if keys[pygame.K_UP] and car_y > 0:
            car_speed_y = max(car_speed_y - acceleration, -max_speed_forward_backward)
        elif keys[pygame.K_DOWN] and car_y < win_height - car_height:
            car_speed_y = min(car_speed_y + acceleration, max_speed_forward_backward)
        else:
            if car_speed_y > 0:
                car_speed_y = max(car_speed_y - deceleration_forward_backward, 0)
            elif car_speed_y < 0:
                car_speed_y = min(car_speed_y + deceleration_forward_backward, 0)

        car_x += car_speed_x
        car_y += car_speed_y

        if random.randint(1, 15) == 1:
            create_obstacle(min_distance)

        create_shield()

        adjust_speeds(obs)

        for ob in obs:
            ob[1] += ob[2]
            if ob[1] > win_height:
                obs.remove(ob)

        car_hurtbox = pygame.Rect(car_x + hurtbox_offset_x, car_y + hurtbox_offset_y, hurtbox_width, hurtbox_height)

        for ob in obs:
            if shield_active:
                continue
            ob_rect = pygame.Rect(ob[0], ob[1], obs_width, obs_height)
            if car_hurtbox.colliderect(ob_rect):
                run = False
                game_over = True  # Set game_over to True
                last_distance = distance
                if last_distance > highscore:
                    highscore = last_distance

        if shield_item:
            if car_x < shield_item[0] + shield_width and car_x + car_width > shield_item[0] and car_y < shield_item[
                1] + shield_height and car_y + car_height > shield_item[1]:
                shield_item = None
                shields_collected += 1

        if keys[pygame.K_SPACE] and shields_collected > 0 and not shield_active:
            shield_active = True
            shield_timer = shield_duration
            shields_collected -= 1

        if shield_active:
            shield_timer -= 1
            if shield_timer <= 0:
                shield_active = False

        # Update distance
        distance_timer += dt
        if distance_timer >= 1:
            distance += distance_increment
            distance_timer = 0

        draw_car(car_x, car_y)
        draw_obstacles(obs)

        if shield_item:
            shield_item[1] += 6
            draw_shield_item(shield_item[0], shield_item[1])
            if shield_item[1] > win_height:
                shield_item = None

        if shield_active:
            draw_shield(car_x, car_y)

        # Draw distance counter
        draw_text(f"{distance:.1f} km", button_font, red, win, win_width - 120, 10)

        # Draw shield icon in bottom left corner
        if shields_collected > 0:
            win.blit(shield_image, (10, win_height - shield_height - 10))
        else:
            dark_shield = pygame.Surface(shield_image.get_size())
            dark_shield.fill((50, 50, 50))
            win.blit(dark_shield, (10, win_height - shield_height - 10))

        pygame.display.update()

    # Stop the soundtracks when the game ends
    pygame.mixer.music.stop()
    secondary_track.stop()

    # Return to home screen
    return True


# Start the game
while True:
    if home_screen():
        game_loop()
    else:
        break
