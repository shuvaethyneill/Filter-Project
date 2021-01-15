# ECOR 1051 Milestone 3 P8: Batch User Interface
# Team 109
# Date of Submission: April 2, 2020

# Team Members:
# Shuvaethy Neill 101143478 (Team Leader)
# Francesca Siconolfi 101148917
# Mahmoud Aldirawi 101150112

from Cimpl import *
from T109_image_filters import *

def choose_file(name: str) -> object:
    name = input("What text file would you like to use? ") #asks the user to enter the name of the text file
    """Author: Francesca Siconolfi (101148917)
    
    Type Annotation: (str) -> object
    
    The user enters the name of the text file, the function accepts it and returns the file. 
    
    >>> choose_file()
    What text file would you like to use? sample_batch_file.txt
    *returns file*
    
    """    

    batch_file = open(name)
    
    return batch_file

def apply_filter(batch_file) -> None:
    
    """Author: Francesca Siconolfi (101148917)
    
    Type Annotation: (object) -> None
    
    The functioin takes the file chosen by the user, and reads and splits the 3 items contained in the file. It takes the image, the chosen filters found in the file, and applies them to the image cumatively. It saves the new image in the same folder in which the text file and this program file is contained in. 
    
    >>> apply_filter(batch_file)
    *applies filters on given image and saves it*
    """      
    
    #CONSTANTS
    COLOUR1 = "cyan"
    COLOUR2 = "yellow"
    COLOUR3 = "magenta"
    THRESHOLD = 10
    
    for line in batch_file:
    
        items = line.split(" ")
        file = items[0]
        new_image = load_image(file) #loads the image given in the file
        for i in range(2, len(items)):
        
            if items[i] == "2":
                new_image = two_tone(new_image, COLOUR1, COLOUR2)
            
            elif items[i] == "3":
                new_image = three_tone(new_image, COLOUR1, COLOUR3, COLOUR2)
            
            elif items[i] == "X":
                new_image = extreme_contrast(new_image)
            
            elif items[i] == "T":
                new_image = sepia(new_image)
            
            elif items[i] == "P":   
                new_image = posterize(new_image)
            
            elif items[i] == "E":
                new_image = detect_edges(new_image, THRESHOLD)
            
            elif items[i] == "I":
                new_image = detect_edges_better(new_image, THRESHOLD)
            
            elif items[i] == "V":
                new_image = flip_vertical(new_image)
            
            elif items[i] == "H":
                new_image = flip_horizontal(new_image)
            
            save_as(new_image, "testing.png") #saves the image with a new name
            file = "testing.png"
        
        save_as(new_image, str(items[1]))
        
batch_file = choose_file()
apply_filter(batch_file)