# Space_Shooter

This is a 2D side scrolling space shooter developed with the Pygame library. 

There are two levels, the first features two waves of enemy ships and asteroids. 
After clearing both waves a wormhole appears that the player needs to fly through to reach the second level.
The second level is an asteroid field. 

## Installation
Clone the repository and install using the following command

```python3 setup.py install```

To run the program: navigate to the space_shooter package directory and run the program with

```python3 space_shooter.py```

This was developed using the latest version of python. You may need install a the latest version of the python interpreter if Pygame errors on build.

## NPC Types:

* Alien
    * Movement: Flies in a straight line to the left
* Big Alien
    * Movement: Zigzags up and down while flying to the left
* Asteroid
    * Movement: Randomized horizontal and vertical movement
    
## Collisions:
* The player can collide with all NPC types

## Controls:
* Move: WASD
* Shoot: Left click

## Assets Used: 
* Big Alien Ship: https://free-game-assets.itch.io/free-enemy-spaceship-2d-sprites-pixel-art
* Background and all other sprites: https://ansimuz.itch.io/
