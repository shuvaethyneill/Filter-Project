# ECOR 1051 Milestone 3 P8: Final Filter Function Code 
# Team 109
# Date of Submission: April 2, 2020

# Team Members:
# Shuvaethy Neill 101143478 (Team Leader)
# Francesca Siconolfi 101148917
# Mahmoud Aldirawi 101150112

from Cimpl import *
from  simple_Cimpl_filters import grayscale

#Red Filter Function
def red_channel(image: Image) -> Image:
    
    """ Author: Mahmoud Aldirawi (101150112)
    
    (Cimpl.Image) -> Cimpl.Image
    
    Function changes each pixel of the final image to only contain red (g and b 
    have the value of 0), in other words this function copies the initial image 
    and produces and returns the same image except with a red filter. 
    
    >>> red_channel(original_image)
    Image is displayed.
    """    
    new_image = copy(image)
    
    for pixel in image:
        x, y, (r, g, b) = pixel
        new_colour = create_color(r, 0, 0) #This sets b and g to be zero, leaving only red
        set_color(new_image, x, y, new_colour)
    return new_image 

#Green Filter Function
def green_channel(initial_image: Image) -> Image:
 
    """ Author: Shuvaethy Neill (101143478)
    
    (Cimpl.Image) -> Cimpl.Image
    
    Function changes each pixel of the final image to only contain green (r and 
    b have the value of 0), in other words this function copies the initial 
    image and produces and returns the same image except with a green filter. 

    >>> green_channel(original_image)
    Image is displayed.
    """
    final_image = copy(initial_image)
 
    for pixel in initial_image:
        x, y, (r, g, b) = pixel
        final_colour = create_color(0, g, 0) #This sets b and r to be zero, leaving only green
        set_color(final_image, x, y, final_colour)   
    return final_image 

#Blue Filter Function
def blue_channel(original: Image) -> Image:
    
    """ Author: Francesca Siconolf (101148917)
    
    (Cimpl.Image) -> Cimpl.Image
     
    Function changes each pixel of the final image to only contain blue (r and 
    g have the value of 0), in other words this function copies the initial 
    image and produces and returns the same image except with a blue filter.
   
    >>>blue_channel(original_image)
    Image is displayed.
    """
    new = copy(original)
    
    for pixel in new:
        x, y, (r, g, b) = pixel
        new_colour = create_color(0, 0, b) #This sets r and g to be zero, leaving only blue
        set_color(new, x, y, new_colour) 
    return new
   
#Combine Filter Function
def combine (image1: Image, image2: Image, image3: Image) -> Image:
   
    """Author: Shuvaethy Neill (101143478)
    
    (Cimpl.Image, Cimpl.Image, Cimpl.Image) -> Cimpl.Image
    
    Function changes each pixel of the final image to contain the combined rgb 
    colour by adding each r, g, and b value of each pixel in the three 
    filter images and produces and returns  the same image except with the 
    combined filter. 

    >>> combine (red_image, green_image, blue_image)
    Image is displayed. 
    """
   
    final_image = copy(image1)
    for pixel in final_image:
        (x, y, (r, g, b)) = pixel
        (r1, g1, b1) = get_color(image1, x, y)
        (r2, g2, b2) = get_color(image2, x, y)
        (r3, g3, b3) = get_color(image3, x, y) 
        total_red = (r1 + r2 + r3)
        total_green = (g1 + g2 + g3)
        total_blue = (b1 + b2 + b3)
        final_colour = create_color(total_red, total_green, total_blue)
        set_color(final_image, x, y, final_colour)       
    return final_image

#Two Tone Filter Function
def two_tone(image: Image, colour1: str, colour2: str) -> Image:
    
    """" Author: Shuvaethy Neill (101143478)
    
    (Cimpl.Image, str, str) -> Cimpl.Image
    
    This function accepts 3 parameters (an image and two strings which are the 
    names of colours chosen by the user) and returns a copy of the image with 
    only those chosen two colours (tones). The brightness of each pixel in the 
    image is what determines what colour it will be changed it. The range of 
    brightness is as follows:
    0 - 127 -> first colour
    128 - 255 -> second colour
    
    >>>two_tone(original_image, "black", "white")
    Displays image with those two tones. 
    
    """
    new_image = copy(image)
    colours = [colour1, colour2]  #List for inputed strings
    rgb_list = [] #New list for rgb values
    
    for i in range(len(colours)):
        if colours[i] == "black":
            rgb_list += (0, 0, 0)
            
        elif colours[i] == "white":
            rgb_list += (255, 255, 255)
            
        elif colours[i] == "red":
            rgb_list += (255, 0, 0)
            
        elif colours[i] == "lime":
            rgb_list += (0, 255, 0)
            
        elif colours[i] == "blue" :
            rgb_list += (0, 0, 255)
            
        elif colours[i] == "yellow":
            rgb_list += (255, 255, 0)
            
        elif colours[i] == "cyan":
            rgb_list += (0, 255, 255)
            
        elif colours[i] == "magenta":
            rgb_list += (255, 0, 255)
            
        elif colours[i] == "gray":
            rgb_list += (128, 128, 128)
            
    colour1 = create_color(rgb_list[0], rgb_list[1], rgb_list[2])
    colour2 = create_color(rgb_list[3], rgb_list[4], rgb_list[5]) 
        
    for pixel in image:
        x, y, (r, g, b) = pixel
        avg = (r + g +b) / 3 
        if avg < 128:
            set_color(new_image, x, y, colour1)
        else: 
            set_color(new_image, x, y, colour2)
         
    return new_image

#Three Tone Filter Function
def three_tone(image: Image, colour1: str, colour2: str, colour3: str) -> Image:
    
    """ Author: Shuvaethy Neill (101143478)
    
    (Cimpl.Image, str, str, str) -> Cimpl.Image
    
    This function accepts 4 parameters (an image and three strings which are the 
    names of colours chosen by the user) and returns a copy of the image with 
    only those chosen three colours (tones). The brightness of each pixel in the 
    image is what determines what colour it will be changed it. The range of 
    brightness is as follows:
    0 - 84 -> first colour
    85 - 170 -> second colour
    171 - 255 -> third colour
    
    >>>three_tone(original_image, "black", "white", "yellow")
    Displays image with those three tones. 
    
    """
    new_image = copy(image)
    colours= [colour1, colour2, colour3] #List for inputted strings
    rgb_list = [] #New list for rgb values
    
    for i in range(len(colours)):
        if colours[i] == "black":
            rgb_list += (0, 0, 0)
            
        elif colours[i] == "white":
            rgb_list += (255, 255, 255)
            
        elif colours[i] == "red":
            rgb_list += (255, 0, 0)
            
        elif colours[i] == "lime":
            rgb_list += (0, 255, 0)
            
        elif colours[i] == "blue" :
            rgb_list += (0, 0, 255)
            
        elif colours[i] == "yellow":
            rgb_list += (255, 255, 0)
            
        elif colours[i] == "cyan":
            rgb_list += (0, 255, 255)
            
        elif colours[i] == "magenta":
            rgb_list += (255, 0, 255)
            
        elif colours[i] == "gray":
            rgb_list += (128, 128, 128)
            
    colour1 = create_color(rgb_list[0], rgb_list[1], rgb_list[2])
    colour2 = create_color(rgb_list[3], rgb_list[4], rgb_list[5]) 
    colour3 = create_color(rgb_list[6], rgb_list[7], rgb_list[8])
    
    for pixel in image:
        x, y, (r, g, b) = pixel
        avg = (r + g +b) / 3 
        if avg < 84:
            set_color(new_image, x, y, colour1)
        elif 84 < avg < 170: 
            set_color(new_image, x, y, colour2)
        else:
            set_color(new_image, x, y, colour3)
               
    return new_image   

#Extreme Contrast Filter Function
def extreme_contrast(image: Image) -> Image:
    
    """ Author: Mahmoud Aldirawi (101150112)
    
    (Cimpl.Image) -> Cimpl.Image
    
    This function accepts 1 parameter (an image chosen by the user) and returns 
    a copy of the image returns a copy of an image in which the contrast between 
    the pixels has been maximized (extreme contrast filter applied to it). 
    
    To create this filter the rgb values are manipulated as follows:
    value between 0 - 127 -> value is changed to 0
    value between 128 - 1255 -> value is changed to 255
    
    >>>extreme_contrast(original_image)
    *Displays image with extreme contrast filter*
    """    
    
    contrast_image = copy(image)
    
    for pixel in image:
        x, y, (r, g, b) = pixel
        image_color= get_color(contrast_image, x, y)
        
        if image_color[0] <= 127:
            r = 0
        elif image_color[0] > 127:
            r = 255
        if image_color[1] <= 127:
            g = 0
        elif image_color[1] > 127:
            g = 255
        if image_color[2] <= 127:
            b = 0
        elif image_color[2] > 127:
            b = 255
        contrast = create_color(r, g, b)
        set_color(contrast_image, x, y, contrast)
        
    return contrast_image


#Sepia Tinting Filter Function
def sepia(image: Image) -> Image:
    """ Author: Francesca Siconolf (101148917)
    
    (Cimpl.Image) -> Cimpl.Image
    
    Passes the input file (picture) through a sepia filter, first by setting 
    all pixels to an equal grey tone, then multiplying the red and blue values,
    depending on the value of them.
    
    >>>sepia(original_image)
    *Displays image with sepia filter*
    """
    
    copy1 = copy(image)    
    new = grayscale(copy1)
    
    for pixel in new:
        x, y, (r, g, b) = pixel
        b_new = b
        r_new = r
        
        if r < 63:
            b_new = b * 0.9
            r_new *= 1.1
            new_colour = create_color(r_new, g, b_new)
            
        elif 63 <= r <= 191:
            b_new *= 0.85
            r_new *= 1.15
            new_colour = create_color(r_new, g, b_new)
        
        else:
            b_new *= 0.93
            r_new *= 1.08
            new_colour = create_color(r_new, g, b_new)
           
        set_color(new, x, y, new_colour)  
        
    return new          

#Posterizing Filter Help Function
def _adjust_component(value: int) -> int:
    """ Author: Shuvaethy Neill (101143478)
    
    This function takes the r, g, and b values of a pixel and determines the 
    quadrant in which each component lies in and returns the midpoint value of 
    that quadrant. This function is used to create a posterize filter. The 
    function's argument must be in the range of 0<= value <= 255. Possible 
    ranges for quadrants and their midpoints are as follows:
    0 - 63 -> 31
    64 - 127 -> 95
    128 - 191 -> 159
    192 - 255 -> 223
    """    
    if value <= 63:
        return 31
    elif value <= 127:
        return 95
    elif value <= 191:
        return 159
    else:
        return 223

#Posterizing Filter Function
def posterize(image: Image) -> Image:
    """ Author: Shuvaethy Neill (101143478)
    
    (Cimpl.Image) -> Cimpl.Image
    
    This function takes one parameter (an image), makes a copy of it, and 
    applies a posterize filter on it (takes the rgb value and replaces it with 
    the midpoint of its range). To calculate said new values, 
    the _adjust_component function is called.
  
    >>> posterize(original_image)
    *Image is displayed with posterize filter*
    """
    new_image = copy(image)
    
    for pixel in image:
        x, y,(r, g, b) = pixel
        posterize_colour = create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b)) 
        set_color(new_image, x, y, posterize_colour)
        
    return new_image

#Edge Detection Filter Function
def detect_edges(image: Image, threshold: float) -> Image:
    
    """Author: Shuvaethy Neill (101143478)
    
    (Cimpl.Image, float) -> Cimpl.Image
    
    This function accepts 2 parameters (an image and a positive float number 
    assigned to the variable threshold), and returns a copy of that image with 
    a filter that resembles a pencil sketch.This function scans through every 
    pixel in the given image and compares the contrast between two pixels. 
    If the pixel above the chosen pixel has a higher contrast then it will 
    change the chosen pixels color code to black, but if it has a lower contrast 
    then it will change the chosen pixels color code to white. This resembles a 
    pencil sketch as only the edges are visible in the image.
    
    >>> detect_edges(image, 7.5)
    *Shows a copy of the original image with the edge detection filter applied to it*
    """
    
    new_image = copy(image) 
    
    HEIGHT = get_height(new_image) 
    WIDTH = get_width(new_image) 
       
    for x in range(WIDTH): 
        for y in range(HEIGHT - 1):    
            
            black = create_color(0, 0, 0) 
            white = create_color(255, 255, 255) 
               
            r1,g1,b1 = get_color(new_image, x, y) #Gets rgb values for each pixel
            r2,g2,b2 = get_color(new_image, x, y + 1)  
               
            brightness_top = ((r1 + g1 + b1) // 3) #Averages the rgb values of each pixel
            brightness_bottom = ((r2 + g2 + b2) // 3)
                       
            contrast1 = abs(brightness_top - brightness_bottom) 
                   
            if contrast1 > threshold: #Changes the colour of the pixels depending if their contrast is higher or lower than the gven threshold
                set_color(new_image, x, y, black)
                   
            else: set_color(new_image, x, y, white)
    
    for x in range(WIDTH): #Sets the last row to white
        set_color(new_image, x, HEIGHT-1, white)
                                   
    return new_image 

#Improved Edge Detection Filter Function
def detect_edges_better(image: Image, threshold: float) -> Image:
    
    """Author: Shuvaethy Neill (101143478)
    
    (Cimpl.Image, float) -> Cimpl.Image
    
    This function accepts 2 parameters (an image and a positive float number 
    assigned to the variable threshold), and returns a copy of that image with 
    a filter that resembles a pencil sketch.This function scans through every 
    pixel in the given image and compares the contrast between two pixels. If 
    the pixel above the chosen pixel or the pixel to the right of the chosen 
    pixel has a higher contrast then it will change the chosen pixels color 
    code to black, but if it has a lower contrast then it will change the 
    chosen pixels color code to white. This resembles a pencil sketch as only 
    the edges are visible in the image.
    
    >>> detect_edges_better(image, 10)
    *Shows a copy of the original image with the improved edge detection filter applied to it*
    """
    
    new_image = copy(image) 
    
    HEIGHT = get_height(new_image) 
    WIDTH= get_width(new_image) 
       
    for x in range(WIDTH - 1): 
        for y in range(HEIGHT - 1):       
     
            black = create_color(0, 0, 0) 
            white = create_color(255, 255, 255) 
               
            r_top, g_top, b_top = get_color(new_image, x, y) #Gets the rgb value for each pixel
            r_bottom, g_bottom, b_bottom = get_color(new_image, x, y + 1) 
            r_side, g_side, b_side = get_color(new_image, x + 1, y)
            
            brightness_top = ((r_top + g_top + b_top) // 3)  #Averages the rgb value for each pixel
            brightness_bottom = ((r_bottom + g_bottom + b_bottom) // 3)
            brightness_beside = ((r_side + g_side + b_side) // 3)
                       
            contrast1 = abs(brightness_top - brightness_bottom)
            contrast2 = abs(brightness_top - brightness_beside)
                   
            if contrast1 > threshold or contrast2 > threshold: #Changes the colour of the pixels depending if their contrast is higher or lower than the gven threshold
                set_color(new_image, x, y, black)
                   
            else: set_color(new_image, x, y, white)
            
    for x in range(WIDTH): #Sets the last row to white
        set_color(new_image, x, HEIGHT - 1, white)    
        
    for y in range(HEIGHT): #Sets the last column to white
        set_color(new_image, WIDTH - 1, y, white)
                                   
    return new_image 

#Vertical Flipping Filter Function
def flip_vertical(image: Image) -> Image:
    """ Author: Francesca Siconolf (101148917)
    
    (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of the image where all the pixels are mirrored with
    respect to the y axis (vertical line).
    
    >>>flip_vertical(original_image)
    *Displays a copy of the original image flipped vertically*
    """
    first_copy = copy(image)
    second_copy = copy(image)
    
    WIDTH = get_width(first_copy)
    
    for x, y, (r, g, b) in first_copy:
        
        new_x = get_color(first_copy, x, y)
        set_color(second_copy, WIDTH - x - 1, y, new_x)
        
    return second_copy

#Horizontal Flipping Filter Function
def flip_horizontal(image: Image) -> Image:
    
    """ Author: Mahmoud Aldirawi (101150112)
    
    (Cimpl.Image) -> Cimpl.Image
    
    Return a copy of the image where all the pixels are mirrored with
    respect to the x axis (horizontal line).
    
    >>>flip_vertical(original_image)
    *Displays a copy of the original image flipped vertically*
    """
    new_image = copy(image)
    
    HEIGHT = get_height(image)
    WIDTH = get_width(image)
    new_image = copy(image)
        
    new_y = HEIGHT - 1
        
    for y in range(0, HEIGHT // 2):
        new_x = 0
        for x in range(0, WIDTH):
            pixel = get_color(image, x, y)
            r, g, b = pixel
            pixel_colour = create_color(r, g, b)
            set_color(new_image, new_x, new_y, pixel_colour)
                
            pixel2 = get_color(image, new_x, new_y)
            r, g, b = pixel2
            pixel2_colour = create_color(r, g, b)
            set_color(new_image, x, y, pixel2_colour)
                
            new_x += 1
        new_y -= 1
            
    return new_image