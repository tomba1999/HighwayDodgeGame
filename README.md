## Table of Contents
- [Overview](#overview)
- [Use Cases](#use-cases)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Challenges and Solutions](#challenges-and-solutions)
- [Further Improvements](#further-improvements)
- [Distribution of Work](#distribution-of-work)

## Overview

### Purpose
The "Highway Dodge Game" is an engaging arcade-style driving game designed to showcase the application of Python programming skills and the `pygame` library. The project emphasizes key development practices such as real-time input handling, collision detection, and dynamic content rendering. Its development served as a practical learning exercise in understanding complex game development concepts, including game loops, object-oriented programming, and interactive multimedia content management.

### Gameplay Mechanics
"Highway Dodge Game" offers a fast-paced driving experience where players navigate a car through a bustling highway filled with various obstacles. Players control the car using simple keyboard commands to dodge other vehicles and avoid collisions. Key features include:

- **Dynamic Obstacles**: Cars and trucks that vary in speed and frequency, challenging players to remain vigilant.
- **Power-Ups**: Collectible shields grant temporary invincibility, allowing players to survive otherwise lethal situations.
- **Scoring System**: Distance traveled is converted into points, rewarding players for their endurance and maneuvering skills.
- **Car Selection**: Before gameplay, players choose their vehicle, adding a personalized touch to the gaming experience.
- **Progression**: The game's difficulty incrementally increases as the player progresses, with obstacles becoming more frequent.
- **End-Game Condition**: The game ends when the player collides with an obstacle without a shield active. The final score is based on the distance traveled before the crash.

## Use Cases

### Must-Have Use Cases:

#### Use Case 1: Initializing the Game Environment
- **Title**: Initialize Game
- **Primary Actor**: Game System
- **Preconditions**: Game software is installed and launched.
- **Postconditions**: Game is initialized and ready for user interaction.
- **Main Success Scenario**:
  1. Game launches and begins initialization.
  2. System loads configurations and sets default values.
  3. Resources such as images, sounds, and fonts are loaded.
  4. Main game window is set up and displayed.
- **Extensions**: None
- **Special Requirements**: Fast load time to enhance user experience.
- **Assumptions**: All resources are available and correctly formatted.
- **Frequency of Use**: Once per game launch.
- **Miscellaneous**: Could include version check for resources.

#### Use Case 2: Handling User Input
- **Title**: Handle User Input
- **Primary Actor**: Player
- **Preconditions**: Game is actively running.
- **Postconditions**: Player's input is processed.
- **Main Success Scenario**:
  1. Player presses a key or combination of keys.
  2. System detects and interprets the key press.
  3. Appropriate action is executed based on the input (move car, activate shield).
- **Extensions**:
  3a. Invalid key press:
     - System ignores the input.
- **Special Requirements**: Input must be responsive and non-blocking.
- **Assumptions**: User is using a standard keyboard.
- **Frequency of Use**: Constantly during gameplay.
- **Miscellaneous**: Input handling should support multiple key presses simultaneously.

#### Use Case 3: Updating Game State
- **Title**: Update Game State
- **Primary Actor**: Game System
- **Preconditions**: Game is initialized and running.
- **Postconditions**: Game elements are updated based on game logic.
- **Main Success Scenario**:
  1. System calculates new positions for all dynamic elements.
  2. Collision detection is performed.
  3. Game scores and other statistics are updated.
  4. Game state is refreshed to reflect changes.
- **Extensions**:
  2a. Collision detected:
     - Adjust game state according to the type of collision (e.g., game over, reduce life).
- **Special Requirements**: Update must be smooth to ensure fluid gameplay.
- **Assumptions**: Game logic is consistent and error-free.
- **Frequency of Use**: Every game loop iteration.
- **Miscellaneous**: Performance optimizations may be required for complex scenarios.

#### Use Case 4: Rendering the Game Screen
- **Title**: Render Game Screen
- **Primary Actor**: Game System
- **Preconditions**: Game state has been updated.
- **Postconditions**: Current game state is visually represented on the screen.
- **Main Success Scenario**:
  1. System gathers all visual elements based on the current game state.
  2. Elements are drawn to the screen in the correct order.
  3. Screen refreshes to display the updated visuals.
- **Extensions**: None
- **Special Requirements**: Rendering must be synchronized with the screen refresh rate.
- **Assumptions**: The system supports the required graphics operations.
- **Frequency of Use**: Every frame (typically 30-60 times per second).
- **Miscellaneous**: May include handling of different resolutions and aspect ratios.

### Implemented Nice-to-Have Use Cases:

#### Use Case 5: Viewing the High Score
- **Title**: View High Score
- **Primary Actor**: Player
- **Preconditions**: Player selects to view high scores from the menu.
- **Postconditions**: High scores are displayed to the player.
- **Main Success Scenario**:
  1. Player selects the high score option from the main menu.
  2. System retrieves high score data from storage.
  3. High scores are displayed on the screen.
- **Extensions**:
  2a. No high scores available:
     - Display a message indicating no high scores exist.
- **Special Requirements**: Ensure data integrity and security.
- **Assumptions**: High score data is stored and accessible.
- **Frequency of Use**: As desired by the player.
- **Miscellaneous**: Could include online leaderboard integration.

#### Use Case 6: Choosing a Car
- **Title**: Choose Car
- **Primary Actor**: Player
- **Preconditions**: Player is at the car selection screen.
- **Postconditions**: Player has selected a car.
- **Main Success Scenario**:
  1. Player views available cars.
  2. Player selects a car by clicking or pressing a key.
  3. Selection is confirmed, and the chosen car is used in gameplay.
- **Extensions**: None
- **Special Requirements**: Visual feedback on selection.
- **Assumptions**: All car models are correctly implemented.
- **Frequency of Use**: Once per game session or as desired.
- **Miscellaneous**: Could include customization options.

### Other Suggested Nice-to-Have Use Cases:

#### Use Case 7: Pause and Resume Game
- **Title**: Pause and Resume Game
- **Primary Actor**: Player
- **Preconditions**: Game is actively running.
- **Postconditions**: Game is paused/resumed.
- **Main Success Scenario**:
  1. Player presses the pause button.
  2. Game state is frozen, and a pause menu is displayed.
  3. Player chooses to resume the game.
  4. Game state is unfrozen, and play continues.
- **Extensions**:
  3a. Player chooses to exit to the main menu:
     - Terminate the current game session and return to the main menu.
- **Special Requirements**: Pause without loss of game state.
- **Assumptions**: User interface includes a clear indicator of the game being paused.
- **Frequency of Use**: As needed by the player.
- **Miscellaneous**: Could include quick save/load features.

#### Use Case 8: Multiple Levels or Stages
- **Title**: Progress Through Levels
- **Primary Actor**: Player
- **Preconditions**: Player starts or continues a game.
- **Postconditions**: Player progresses through various levels.
- **Main Success Scenario**:
  1. Player completes the requirements of the current level.
  2. System loads the next level with increased difficulty or different themes.
  3. Player starts playing the new level.
- **Extensions**:
  1a. Player fails to meet the level requirements:
     - Provide the option to retry the level or return to the main menu.
- **Special Requirements**: Seamless transition between levels.
- **Assumptions**: Each level is designed and tested for progressive difficulty.
- **Frequency of Use**: Each game session may progress through multiple levels.
- **Miscellaneous**: Could include different environmental graphics and challenges.

## Installation and Setup

### Dependencies

To ensure that "Highway Dodge Game" runs smoothly, the following dependencies must be installed on your system:

- **Python**: The game is developed using Python. Ensure you have Python 3.6 or newer installed. You can download it from [python.org](https://www.python.org).
- **pygame**: This game uses the `pygame` library for rendering graphics, handling sounds, and managing game dynamics. After installing Python, install pygame by running the following command in your terminal or command prompt:
  ```bash
  pip install pygame
  
### Running the Game

The game is packaged in a zip file for easy distribution. Follow these instructions to start playing:

1. **Download the Game**:
   - Download the zip file containing the game from the provided link or location.

2. **Extract the Zip File**:
   - Right-click on the downloaded file and select "Extract All…" or use your preferred archive manager. Ensure you note the folder where the files are being extracted.

3. **Run the Game**:
   - Navigate to the extracted folder and look for an executable file named `highway_dodge_game.exe`.
   - Double-click on the `highway_dodge_game.exe` file to launch the game. No additional setup or installation is required.

4. **Enjoy Playing**:
   - Once the game launches, you can start playing immediately by following the on-screen instructions to navigate through the game menus.

By following these steps, you should be able to start playing "Highway Dodge Game" quickly and without complications.

## Usage

### Controls

"Highway Dodge Game" is designed to be intuitive and straightforward. Below are the keyboard controls that allow players to navigate the game environment and manage their vehicle effectively:

- **Left Arrow Key (`←`)**: Press this key to steer your car to the left. This is essential for dodging obstacles and positioning your car safely on the highway.
- **Right Arrow Key (`→`)**: Press this key to steer your car to the right. Use this control to avoid oncoming obstacles and navigate through tight spaces.
- **Up Arrow Key (`↑`)**: Use this key to increase your car’s speed. Accelerating is useful for quickly moving past hazards and maintaining a competitive edge.
- **Down Arrow Key (`↓`)**: Press this key to decrease your car’s speed. Decelerating is crucial for managing complex scenarios and ensuring precise movements.
- **Space Bar**: This key activates the shield power-up, which provides temporary invincibility. Activate the shield when collisions seem imminent to protect your car. Remember, shield usage is limited and should be employed strategically.

## Code Structure

### Key Components

#### Initialization Module
- **Purpose**: Sets up the necessary environment to run the game, including initializing the `pygame` library, setting up the display window, and loading system configurations.
- **Key Functions**:
  - `pygame.init()`: Initializes all imported `pygame` modules.
  - `pygame.display.set_mode()`: Configures the main display window where the game will render.
  - `pygame.mixer.init()`: Initializes the mixer module for sound management.

#### Resource Management
- **Purpose**: Handles the loading and management of game resources such as images, sounds, and fonts, ensuring they are available when needed during gameplay.
- **Key Functions**:
  - `load_frames()`: Extracts frames from a GIF file for use as animated backgrounds.
  - `pygame.image.load()`: Loads static images from disk, used for car and obstacle graphics.

#### Game Mechanics
- **Purpose**: Contains the logic for player actions, obstacle movement, and interactions between game elements like collision detection.
- **Key Functions**:
  - `game_loop()`: The main game loop which continuously updates and renders the game state.
  - `create_obstacle()`: Generates obstacles at random positions and intervals on the game map.
  - `adjust_speeds()`: Adjusts the speeds of obstacles to ensure varied gameplay dynamics.

#### Event Handling
- **Purpose**: Manages input from the user (e.g., keyboard inputs) and system events (e.g., quitting the game).
- **Key Functions**:
  - Within `game_loop()`, checks for events using `pygame.event.get()` and responds accordingly, such as moving the car or activating shields.

#### Rendering
- **Purpose**: Manages all drawing-related tasks, updating the game window with current game visuals at each frame.
- **Key Functions**:
  - `draw_car()`: Draws the car at its current position.
  - `draw_obstacles()`: Renders obstacles on the screen.
  - `pygame.display.update()`: Refreshes the display to reflect any changes made to the visuals.

#### UI Components
- **Purpose**: Manages user interface elements like menus, buttons, and score displays.
- **Key Functions**:
  - `home_screen()`: Displays the initial game menu that allows users to start the game, change settings, or exit.
  - `draw_button()`, `draw_text()`: Helper functions used to draw UI elements like buttons and text on the screen.

#### Sound Management
- **Purpose**: Handles the loading and playing of background music and sound effects to enhance the gaming experience.
- **Key Functions**:
  - `pygame.mixer.music.load()`: Loads a music file to be played as the background track.
  - `pygame.mixer.Sound()`: Manages short sound effects, like collision sounds or power-up activations.

## Challenges and Solutions

### Challenge 1: Balancing Game Theory and Fun
- **Description**: Ensuring that the game was not only functional but also engaging and enjoyable presented a significant challenge. The need to balance complex game mechanics with entertaining gameplay required careful consideration of game theory and player experience.
- **Solution**: The development team focused on iterative gameplay testing and feedback sessions to refine mechanics and ensure the game felt rewarding. Adjustments were made to difficulty progression, obstacle behavior, and reward systems to enhance the fun factor.

### Challenge 2: Managing Continuous Development Improvements
- **Description**: During the development process, the team frequently encountered opportunities for enhancements and feature additions. Deciding when to stop adding new features and focus on polishing existing ones was challenging.
- **Solution**: To manage this, the team implemented a feature freeze deadline. This allowed the developers to shift focus from adding new features to refining the gameplay and ensuring a bug-free, smooth player experience.

### Challenge 3: Avoiding Impossible Gameplay Situations
- **Description**: A significant gameplay challenge was the creation of scenarios where players had no possible escape from obstacles, leading to unavoidable frustration.
- **Solution**: The team adjusted the game's algorithm to monitor the spacing and timing of obstacles. This ensured that at least one path remained open for the player to navigate through, reducing unavoidable collisions.

### Challenge 4: Preventing Collisions Between Cars of Different Speeds
- **Description**: Ensuring that faster cars do not run into slower ones was technically complex and impacted the game's realism and playability.
- **Solution**: The implementation involved creating a dynamic barrier system where cars within the same lane would adjust their speeds if they were too close to each other, thereby preventing high-speed rear-end collisions.

## Further Improvements

### 1. Multiplayer Mode
- **Description**: Introduce a multiplayer feature where players can compete against each other in real-time or through a turn-based system.

### 2. More Diverse Environments
- **Description**: Expand the game's settings to include different thematic backgrounds and road conditions, such as night-time driving, rainy weather, or snowy roads.

### 3. Advanced Obstacle and Power-Up Types
- **Description**: Introduce new obstacles and power-ups with unique behaviors, such as moving obstacles that change lanes or speed-boosting power-ups.

### 4. Customizable Vehicles
- **Description**: Allow players to customize their vehicles in terms of appearance (color, decals) and performance attributes (speed, handling).

### 5. Achievement System
- **Description**: Implement an achievement system with rewards for reaching specific milestones or completing challenges.

## Distribution of Work

The development of "Highway Dodge Game" was a collaborative effort, with team members sharing responsibilities primarily in programming and various specialized areas to ensure a well-rounded and efficiently executed project. Below is the breakdown of the distribution of work among the team members:

- **General Programming**: All team members actively participated in the coding process. This collaborative approach ensured that everyone contributed to and had a thorough understanding of the game's technical foundation.

- **Project Leadership and Gameplay Management**:
  - **Tomislav**: As the project leader, Tomislav was chiefly responsible for overseeing the development process and specifically led the gameplay aspects of the project. His role was crucial in guiding the team through game mechanics decisions and ensuring that the gameplay was engaging and functional.

- **Design Leadership**:
  - **Chingis**: Chingis took the lead on the design aspects of the game, including the visual elements and user interface. His leadership in this area was instrumental in creating a visually appealing and user-friendly gaming environment.

- **Documentation Oversight**:
  - **William**: Responsible for leading the documentation efforts, William ensured that all aspects of the game and its development were well-documented. This included detailing the game's design, usage instructions, code structure, and the challenges and solutions encountered during development.

This structure of team roles allowed for efficient project management and the effective integration of different areas of expertise, resulting in a cohesive and well-developed game.
