# Advanced Snake Game

A modern twist on the classic Snake game, featuring multiple game modes, enemy AI, power-ups, and enhanced gameplay mechanics.

## Features

### Game Modes
- **Classic Mode**: Traditional snake gameplay
- **Survival Mode**: Battle against AI enemy snakes while collecting food
- **Hunter Mode**: Power up and hunt enemy snakes for points

### Power-Ups
- **Speed Boost** (Blue): Temporarily increases snake movement speed
- **Invincibility** (Purple): Makes you invulnerable and able to eat enemy snakes
- **Growth Boost**: Instantly adds 3 segments to your snake

### Gameplay Elements
- Multiple food items on screen
- AI-powered enemy snakes
- Screen wrapping mechanics
- Dynamic enemy spawning
- Score tracking system
- Power-up duration system

## Installation

### Prerequisites
- Python 3.x
- Pygame library

### Step-by-Step Installation
1. Install Python:
   - Visit https://www.python.org/downloads/
   - Download the latest Python version
   - Run installer
   - IMPORTANT: Check "Add Python to PATH" during installation

2. Install Pygame:
   ```bash
   pip install pygame
   ```

3. Download the Game:
   - Create a new file named `snake_game.py`
   - Copy the game code into this file
   - Save the file

## How to Play

### Starting the Game
1. Open Command Prompt/Terminal
2. Navigate to the game directory:
   ```bash
   cd path/to/game/directory
   ```
3. Run the game:
   ```bash
   python snake_game.py
   ```

### Controls
- **Arrow Keys**: Control snake movement
- **Spacebar**: Switch between game modes
- **Close Window/Alt+F4**: Exit game

### Gameplay Tips
1. **Classic Mode**:
   - Focus on collecting yellow food
   - Watch your growing length
   - Use screen wrapping to your advantage

2. **Survival Mode**:
   - Stay away from red enemy snakes
   - Collect power-ups when possible
   - Use strategic movement to avoid enemies

3. **Hunter Mode**:
   - Collect purple power-ups to become invincible
   - Chase and eat enemy snakes for bonus points
   - Time your power-ups strategically

### Scoring System
- Regular Food: 10 points
- Eating Enemy Snake: 50 points
- Try to achieve the highest score possible!

## Game Over Conditions
- Collision with enemy snake (without invincibility)
- Manual exit (Alt+F4 or window close button)

## Troubleshooting

### Common Issues and Solutions

1. **"Python not recognized" error**:
   - Reinstall Python
   - Ensure "Add Python to PATH" is checked during installation
   - Restart computer after installation

2. **"Pygame not found" error**:
   - Run `pip install pygame` again
   - Try `python -m pip install pygame`

3. **Game window closes immediately**:
   - Run game from Command Prompt to see error messages
   - Ensure all game code is copied correctly
   - Check Python and Pygame installations

### Still Having Issues?
- Verify Python installation with `python --version`
- Check Pygame installation with `pip show pygame`
- Ensure the game file is saved with `.py` extension
- Try running as administrator

## License
This game is free to use, modify, and distribute.

## Acknowledgments
- Inspired by the classic Snake game
- Enhanced with modern gaming features
- Built using Python and Pygame
