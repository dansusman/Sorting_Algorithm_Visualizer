import time
import sys
import pygame
import bubble_sort

dimensions = (1024, 512)

statuses = ["Currently Sorting", "Sorting Complete!"]

# Pygame Initialisation
pygame.init()

# make window of desired dimensions 
display = pygame.display.set_mode((dimensions[0], dimensions[1]))

# make background white
display.fill(pygame.Color("white"))

# if the algorithm is done, exit program
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Update the screen based on the current state of the sorting (each tick)
def update(algorithm, display=display):
    display.fill(pygame.Color("white"))
    
    # make top bar display which algorithm is being used currently, the amount of time that has passe
    # since the beginning of the sort, and the current status (sorting or done)
    pygame.display.set_caption("Algorithm: {}     Time: {:.3f}      Status: {}".format(
        algorithm.name, time.time() - algorithm.start_time, statuses[0]))
    
    k = int(dimensions[0]/len(algorithm.arr))
    
    # make a rectangle whose height corresponds to the int at a specific location in the array to be sorted
    for i in range(len(algorithm.arr)):
        color = (247, 202, 201)
        pygame.draw.rect(display, color, (i*k, dimensions[1], k, -algorithm.arr[i]))
    #play_sound(swap2) # - Uncomment if you want sound to play with each swap
    check_events()
    pygame.display.update()

# update the scene each tick until the algorithm has completed, at which point reflect that status
# in the top bar
def keep_open(algorithm, display, time):
    pygame.display.set_caption("Algorithm: {}     Time: {:.3f}        {}".format(algorithm.name, time, statuses[1]))
    while True:
        check_events()
        pygame.display.update()


def main():
    algorithm = bubble_sort.BubbleSort()
    time_elapsed = algorithm.run()[1]
    keep_open(algorithm, display, time_elapsed)
        
        
if __name__ == "__main__":
    main()
