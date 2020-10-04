"""

Created by Daniel Susman (dansusman)
Start Date: 09/2020

This is the visualizer for the various sorting algorithms implemented using the Algo
class. It demonstrates the operations and time taken for each algorithm, but cannot be
used to analyze and contrast time complexities. Pygame requires time to draw each rectangle,
so the visualization is for curiosity purposes only.

This is easily modifiable in that all that is required to add a new algorithm is inserting its
name into the sorting_algorithms dictionary.

For ease of use, I require the name of the desired sorting algorithm to be inputted in
as a command line argument. At the moment, snake_case is required. (e.g. bubble_sort)

"""
import time
import sys
import pygame
import bubble_sort
import selection_sort
import insertion_sort
import quicksort

dimensions = (1400, 700)

statuses = ["Currently Sorting", "Sorting Complete!"]

sorting_algorithms = {
    "bubble_sort": bubble_sort.BubbleSort(),
    "selection_sort": selection_sort.SelectionSort(),
    "insertion_sort": insertion_sort.InsertionSort(),
    "quick_sort": quicksort.QuickSort()
}

pygame.init()

# make window of desired dimensions
display = pygame.display.set_mode((dimensions[0], dimensions[1]))

# make background white
display.fill(pygame.Color("white"))

def check_events():
    """As needed in Pygame apps, checks if the algorithm is done. If it is, exit program"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Update the screen based on the current state of the sorting (each tick)
def update(algorithm, left_swap=None, right_swap=None, display=display):
    display.fill(pygame.Color("white"))
    
    # make top bar display which algorithm is being used currently, the amount of time that has passe
    # since the beginning of the sort, and the current status (sorting or done)
    pygame.display.set_caption("Algorithm: {}     Time: {:.3f}      Status: {}".format(
        algorithm.name, time.time() - algorithm.start_time, statuses[0]))
    
    k = int(dimensions[0]/len(algorithm.arr))
    
    # make a rectangle whose height corresponds to the int at a specific location in the array to be sorted
    for i in range(len(algorithm.arr)):
        color = (247, 202, 201)
        if left_swap == algorithm.arr[i]:
            color = (0, 255, 0)
        elif right_swap == algorithm.arr[i]:
            color = (255, 0, 0)
        pygame.draw.rect(display, color, (i*k, dimensions[1], k, -algorithm.arr[i]))
    #play_sound(swap2) # - Uncomment if you want sound to play with each swap
    check_events()
    pygame.time.wait(20)
    pygame.display.update()


def keep_open(algorithm, display, time):
    """Updates the scene each tick until the algorithm has completed, at which point 
    reflect that status in the top bar."""
    pygame.display.set_caption("Algorithm: {}     Time: {:.3f}        {}".format(
        algorithm.name, time, statuses[1]))
    while True:
        check_events()
        pygame.display.update()


def main():
    """Runs the visualization program if given valid input algorithm name."""
    # if the user fails to input a sorting algorithm, throw error
    if len(sys.argv) < 2:
        print("You must enter your desired sorting algorithm to run the program!")
    else:
        # try to parse the input for a valid sorting algorithm
        try:
            algorithm = sorting_algorithms[sys.argv[1]]
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
            except ValueError:
                pass
        except IOError:
            print("{} is not a valid sorting algorithm. Inputs MUST be in snake_case!".format(
                sys.argv[1]))    
if __name__ == "__main__":
    main()
