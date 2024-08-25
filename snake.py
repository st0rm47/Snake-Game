class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        
class Snake:
    def __init__ (self, x, y,block_size):
        # Create a new snake with a head at (x, y) and a tail at (x, y)
        self.head = Node(x, y)
        self.tail = self.head
        
        # The snake is initially of length 1 and moving to the right
        self.length = 1
        self.direction = 1
        self.block_size = block_size
    
    def move(self):
        #Move the snake in the current direction
        new_head = Node(self.head.x, self.head.y)
        if self.direction == 1:
            # Move right
            new_head.x += self.block_size
        elif self.direction == 2:
            # Move down
            new_head.y += self.block_size
        elif self.direction == 3:
            # Move left
            new_head.x -= self.block_size
        else:
            # Move up
            new_head.y -= self.block_size
        
        # Update the head of the snake
        new_head.next = self.head
        self.head = new_head
        
        # If the snake has moved, remove the tail
        self.remove_tail()
    
    def remove_tail(self):
        # Remove the tail of the snake
        current = self.head
        # Find the second-to-last node of the snake
        while current.next != self.tail:
            current = current.next
        # Remove the tail
        current.next = None
        self.tail = current
        
    def grow(self):
        # Grow the snake by adding a new head
        new_head = Node(self.head.x, self.head.y)
        new_head.next = self.head
        self.head = new_head
        self.length += 1
        
    def change_direction(self, direction):
        # Change the direction of the snake
        self.direction = direction
        
    def get_head(self):
        # Return the coordinates of the head of the snake
        return (self.head.x, self.head.y)
    
    def get_direction(self):
        # Return the current direction of the snake
        return self.direction

    

        
        