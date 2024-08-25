import pygame
import random
import sys
from snake import Snake

# Initialize the game parameters
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
block_size = width // 32


# Create the snake
snake = Snake (width // 2, height // 2, 8)

# Create Score
score = 0
font = pygame.font.Font(None, 36)

# Game State
paused = False
game_over= False

# Wall 
wall_color = (32,32,32)
wall_thickness = 25

# Wall rectangles
top_wall = pygame.Rect(0, 0, width, wall_thickness)
left_wall = pygame.Rect(0, 0, wall_thickness, height)
bottom_wall = pygame.Rect(0, height - wall_thickness, width, wall_thickness)
right_wall = pygame.Rect(width - wall_thickness, 0, wall_thickness, height)

# Check collision with the wall
def check_collision(snake):
    head_rect = pygame.Rect(snake.head.x, snake.head.y, width // 32, height // 32)
    if head_rect.colliderect(top_wall) or head_rect.colliderect(left_wall) or \
       head_rect.colliderect(bottom_wall) or head_rect.colliderect(right_wall):
        return True
    return False


#Check collision with the food
def check_food_collision(snake, food):
    head_rect = pygame.Rect(snake.head.x, snake.head.y, block_size, block_size)
    food_rect = pygame.Rect(food[0], food[1], block_size, block_size)
    return head_rect.colliderect(food_rect)

#Create the food location
def create_food():
    block_size = width // 32  # Same as the snake's size
    
    # Calculate the number of blocks that fit within the wall margins
    num_blocks_x = (width - 2 * wall_thickness) // block_size
    num_blocks_y = (height - 2 * wall_thickness) // block_size

    # Ensure food is placed inside the wall boundaries
    if num_blocks_x > 0 and num_blocks_y > 0:
        # Randomly place the food within the valid area
        food_x = random.randint(0, num_blocks_x - 1) * block_size + wall_thickness
        food_y = random.randint(0, num_blocks_y - 1) * block_size + wall_thickness
        return (food_x, food_y)
    
    # Return a default position if no valid placement is found (unlikely case)
    return (width // 2, height // 2)


# Create the first food
food = create_food()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            # Change the direction of the snake based on the key pressed
            if event.key == pygame.K_RIGHT:
                # Move right
                snake.change_direction(1)
            elif event.key == pygame.K_DOWN:
                # Move down
                snake.change_direction(2)
            elif event.key == pygame.K_LEFT:
                # Move left
                snake.change_direction(3)
            elif event.key == pygame.K_UP:
                # Move up
                snake.change_direction(4)
            elif event.key == pygame.K_ESCAPE:
                paused = not paused # Pause the game
    
    if not paused and not game_over:
        # Move the snake
        snake.move()
        
        # Check if the snake has eaten the food
        if check_food_collision(snake, food):
            # The snake has eaten the food and increase the score
            score += 1
            # Grow the snake
            snake.grow()
            # Create a new food location
            food = create_food()

        # Check if the snake has collided with the wall or itself
        if check_collision(snake):
            game_over = True
    
    # Draw the screen
    screen.fill((25, 50, 0))
    
    # Draw the walls
    pygame.draw.rect(screen, wall_color, top_wall)  
    pygame.draw.rect(screen, wall_color, left_wall)  
    pygame.draw.rect(screen, wall_color, bottom_wall)  
    pygame.draw.rect(screen, wall_color, right_wall)
    
    # Draw the snake
    current = snake.head
    while current is not None:
        pygame.draw.rect(screen, (50, 150, 250), (current.x, current.y, block_size, block_size),border_radius = 15)
        current = current.next
    
    # Draw the food
    pygame.draw.rect(screen, (55, 0, 0), (food[0], food[1], block_size - 10, block_size- 10), border_radius = 10)
    
    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (width - 120, 0))
    
    def display_message(message, y_offset):
        box_width = 400
        box_height = 100
        box_x = width // 2 - box_width // 2
        box_y = height // 2 - box_height // 2 
        pygame.draw.rect(screen, (192, 194, 201), (box_x, box_y, box_width, box_height))
        
        # Render the message text
        message_text = font.render(message, True, (0,0,0))
        screen.blit(message_text, (box_x + (box_width - message_text.get_width()) // 2, 
                                box_y + (box_height - message_text.get_height()) // 2))
        
    if paused:
        display_message("Paused", 0)
        
    if game_over:
        display_message("Game Over! Score: " + str(score), 50)
        pygame.display.flip()
        pygame.time.wait(5000)  # Wait for 5 seconds before quitting
        pygame.quit()
        sys.exit()
        
        
    # Update the display
    pygame.display.flip()
    
    # Control the speed of the game
    pygame.time.delay(30)
    
    

    

    
    

    
    