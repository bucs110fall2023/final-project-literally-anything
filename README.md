[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12872519&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Mars Patrol
## CS110 Final Project  Fall, 2023

## Team Members

Steven Lin

Andrew Zou

***

## Project Description

A version  of Moon Patrol. 

***    

## GUI Design

### Initial Design

![<Screenshot 2023-11-13 at 5.57.43 PM.png>](assets/gui.jpg)

### Final Design

![assets/finalgui.jpg](<assets/Screenshot 2023-12-08 at 2.33.39 PM.png>)

## Program Design

### Features

1. start menu
2. moveable character
3. obstacle collisions
4. scrolling background
5. game over screen

### Classes

1. Main class managing properties of the main game  
2. Controller class to handle game states and interactions
3. Player class containing properties of the player and player movement 
4. Obstacles class containing properties of obstacles 
5. Score class to manage score 


## ATP

Test Case 1: Player Movement

Test Description: Verify that the player jumps/ducks as expected
Test Steps:
Start the game.
Press the spacebar or up arrow.
Verify the player jumps upwards and then lands back down.
Press the down arrow.
Verify the player ducks
Expected Outcome: The player should jump up and down or ducks in response to the spacebar or arrow keys.

Test Case 2: Collision Detection and Game Over condition

Test Description: Ensure that collisions between the player and obstacles are detected correctly.
Test Steps:
Start the game.
Play until player touches obstacle. 
Verify the collison is detected and game ends with game over screen.
Expected Outcome: When player touches obstacles, the game should end with game over screen.

Test Case 3: Error Handling

Test Description: Verify that the program handles unexpected inputs gracefully.
Test Steps:
Start the game.
Enter invalid characters or inputs during gameplay.
Verify that the program does not crash and displays appropriate error messages.

Test Case 4: Score

Test Description: The score should be tracked as the game progresses 
Test Steps:
Start the game.
Play game.
Observe the score counter go up.
Lose the game.
Verify score counter ends.

Expected Outcome: Score counter should go up when game is being played and stop when the game is over.

Test Case 5: Play again

Test Description:  Verify the game will restart after game over screen
Test Steps: 
Start the game.
Play until game over screen.
Press play again.
Verify the game starts again with new score.
Expected Outcome: Score resets and game begins again

