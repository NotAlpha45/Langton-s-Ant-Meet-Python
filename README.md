# Langton-s-Ant-Meet-Python
Implementing Langton's ant with pygame from scratch
## About
The Langton's ant is a 2D universal turing machines with very simple instructions, yet very complex emergent behaviour. To know more: [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant).
## Implementation
The visualization was done with [pygame](https://www.pygame.org/docs/). The scale is in pixels. Each pixel represents one step.
## Main Version
The first iteration of the algorithm implements two basic instructions - 
1) If current square (pixel) is black, turn it white and rotate -90°.
2) If current square (pixel) is white, turn it black and rotate +90°.
## Implementation Of Instructions
The `walk` function implements the instructions that are executed with each loop of the game loop. For 90° rotations, there are 4 possible angular position within a full rotation of 360°, those are - 0, 90, 180, -90.  
***Note that, the coordinate system is used here is according to the pygame system. 0° is facing up, +90° is facing right, -90° is facing left and 180° is facing down.*** </br>
The `walk` function checks for these 4 positions and then in each position, it again checks whether the pixel is black or white. Then, changes the x position `pos_x` or y position `pos_y` to move to another square. Note, `(pos_x, pos_y)` is the initial position.  
The `color_detect` function checks for the color of a pixel. It takes the x and y coordinate as a parameter. Then picks up the color using the `get_at` method and then compares the first 3 values (ignoring the alpha value) by converting them into a tuple.  
