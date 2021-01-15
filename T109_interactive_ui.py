# ECOR 1051 Milestone 3 P8: Text-Based Interative User Interface
# Team 109
# Date of Submission: April 2, 2020

# Team Members:
# Shuvaethy Neill 101143478 (Team Leader)
# Francesca Siconolfi 101148917
# Mahmoud Aldirawi 101150112

from Cimpl import *
from T109_image_filters import *

#Print function
def print_prompt() -> str:
    """ Author: Shuvaethy Neill (101143478)
    
    Type Annotation: (None) -> str
    
    This function prompts the user to enter their command (accepts both 
    lowercase and uppercase) by printing the user interface. It also makes 
    sure that the command that they choose is among the list of accepted inputs.
    
    >>> print_prompt()
    L)oad image  S)ave-as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit 
    
    : i
    "I"
    
    >>> print_prompt()
    L)oad image  S)ave-as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit 
    
    : u
    "No such command"
    """
    print("L)oad image  S)ave-as")
    print("2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize")
    print("E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip")
    print("Q)uit \n")
    filter_input = str.upper(input(": "))
    
    return filter_input #returns what the user inputted

valid_commands = ["L", "S", "2", "3", "X", "T", "P", "E", "I", "V", "H", "Q"] #A list for all the valid commands

#Input function
def check_input(filter_input: str) -> Image:
    """Author: Shuvaethy Neill (101143478)
    
    Type Annotation: str -> Cimpl.Image
    
    This function takes a loaded image, the command and applies the specific 
    filter on the image. It returns the cumulatively filtered image based on 
    input of which filters were selected by the user.
    
    >>> check_input("L")
    *Loads the image*
    L)oad image  S)ave-as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit 
    : x
    *Displays image with extreme contrast filter applied to it*
    
    """
    image_selected = False #because no image is loaded
    
    if filter_input == "Q":
        image = 0
        print("No image loaded")
        filter_input = print_prompt() 
        
    while filter_input != "Q":
        
        if filter_input in valid_commands: #goes through this if statement if the user entered a valid command
            
            if filter_input == "L":
                image = load_image(choose_file())
                image_selected = True #now there is an image loaded
                show(image)
                
            elif filter_input == "S" and image_selected:
                save_as(image, 'final_image.jpg')
                
            elif filter_input == "2" and image_selected:
                image = two_tone(image, "yellow", "cyan")
                show(image)
                
            elif filter_input == "3" and image_selected:
                image = three_tone(image, "yellow", "magenta", "cyan")
                show(image)
                
            elif filter_input == "X" and image_selected:
                image = extreme_contrast(image)
                show(image)
                
            elif filter_input == "T" and image_selected:
                image = sepia(image)
                show(image)
                
            elif filter_input == "P" and image_selected:
                image = posterize(image)
                show(image)
                
            elif filter_input == "E" and image_selected:
                threshold = input('Threshold?: ') #gets threshold value from the user
                image = detect_edges(image, int(threshold))
                show(image)
                
            elif filter_input == "I" and image_selected:
                threshold = input('Threshold?: ') #gets threshold value from the user
                image = detect_edges_better(image, int(threshold)) 
                show(image)
                
            elif filter_input == "V" and image_selected:
                image = flip_vertical(image)
                show(image)
                
            elif filter_input == "H" and image_selected:
                image = flip_horizontal(image)
                show(image)
                
            elif image_selected != True:
                print("No image loaded")
                
            filter_input = print_prompt()
        else: #goes through this else statement if the user did not enter a valid command
            print("No such command")
            filter_input = print_prompt() #displays print prompt with valid commands again for user
            
    return image
        
filter_input = print_prompt()
check_input(filter_input)