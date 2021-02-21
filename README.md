# Filter-Project
It should be noted that the following was written for a school project. The software is not intended to be released.

CONTACT INFORMATION: 
Shuvaethy Neill, shuvaethyneill@cmail.carleton.ca


DATE: 
Tuesday, April 7 2020


SOFTWARE NAME AND PRICING: 
SFM Photo Editing Version 1.0.0 - $6.99


DESCRIPTION:
This photo editor will take any image of your choosing and allow you to apply a 
variety of filters onto it. Image editing can be done using pre-defined 
filters using the file-based interface, or it can be done live using the 
text-based interface which gives the user the ability to view their image after 
each filter has been applied. The user can pass an image through thirteen filter 
functions offered. Upon satisfaction, the new filtered image is saved.

This editing software is made up of the following files:

T109_batch_ui.py
T109_user_interface.py
T109_image_filters.py 


INSTALLATION:
The user must have the following installed on their device to run the photo edting code:

- Python (version 3.7.3 or later - https://www.python.org/downloads/)
	- Download the latest version of Python onto your device 
	- Make sure to select the "Add Python x.x to PATH"
	
- Any programming environment (Wing101 (version 7.1.3 or later, PyCharm, etc.)
	- Download the latest version of Wing101 (http://wingware.com/)
	
- Pillow (version 7.0.0 or later -  https://pypi.org/project/Pillow/)
	- Open the command terminal on your device
	- Type: pip install Pillow
	

The following files must be downloaded and organized in the same folder:

- Cimpl.py (version 4.1 - Found on the ECOR 1051 cuLearn class website under the Milestone 1 
section in the "A folder containing Cimpl.py and Approved Sample Images")

- simple_Cimpl_filters.py (Found on the ECOR 1051 cuLearn class website under 
the Milestone 1 section in the "A folder containing Cimpl.py and Approved Sample Images")

- T109_image_filters.py

- T109_interactive_ui.py

- T109_batch_ui.py

- any image (png, jpg, etc.) that you would like to be filtered

Once all the files have been downloaded in the same folder and setup, the user 
is ready to run either the file-based or text-based interface to start their 
photo editing. 


USAGE:
Using this program is very simple. Follow these steps:

1. Launch your programming environment (preferably Wing101):

2. Open the “T109_interactive_ui.py” for the Text-Based system or 
“T109_batch_ui.py” for the File-Based System.

3. Once the file you chose is open, locate the green arrow in the top toolbar and 
click it to run the program.

4. If you are running the "T109_interactive_ui.py" file you will see a menu 
appear in the bottom right of your screen, this is the shell.

	- Load an image by typing in "L" and hitting return
	
	- Once an image is loaded you may apply any filter of your choosng using 
	their designated keys as shown in the menu (ie: 2, E, H)
	
	- If you are satisfied with your image you may save the image by typing 
	"S" into the shell, which will save your final image in the folder you 
	created during installation.
	
	- If you are not satisfied you may quit the program by typing "Q" into 
	the shell, and may rerun the program by repeating step 3.

5. If you are running the "T109_batch_ui.py" file you will first need to create 
your own text file.

	- Open Notepad or any equivalent text file creator.
	
	- Type in the name of the image you have chosen to edit (make sure the 
	image is placed in the folder you created during installation), followed 
	by a space, then the name the new image (what it will be called after it 
	has been filtered).
	
	- Now to apply the filters, type each filter key out followed by a space, 
	these are your options:
	
		"2" Two-Tone
		"3" Three-Tone
		"X" Extreme Contrast
		"T" Sepia Tinting
		"P" Posterized
		"E" Edge Detect
		"I" Improved Edge Detect
		"V" Vertical Flip
		"H" Horizontal Flip

	- Once you have saved the batch file (.txt), you may run the program.
	
	- You will be asked to enter the name of your newly created file.
	
	- Once done, you will have your newly filtered image.

6. Finally, to view the filtered images you've saved just locate your original 
folder that contain these files and they will be saved there.


CREDITS:
Shuvaethy Neill, 101143478, Team Leader
    Work Submitted:
        - Green Channel Filter
        - Combined Filter
        - Channel Filters Combination 
        - Extreme Contrast Test Function
        - Posterized Filter
        - Two Tone Filter
        - Three Tone Filter
        - Sepia Tinting Test Function
        - Edge Detection Filter
        - Improved Edge Detection Filter
        - Horizontal Flipping Test Function
        - Image Filters Combination
        - Test Image Filters Combination
        - Text-Based Interactive User Interface
        
Francesca Siconolfi, 101148917
    Work Submitted:
        - Blue Channel Filter
        - Sepia Tinting Filter
	- Posterized Test Function
        - Vertical Flipping Filter
        - Edge Detection Test Function
        - Improved Edge Detection Test Function
        - File-Based Batch User Interface

Mahmoud Aldirawi, 101150112
    Work Submitted:
        - Red Channel Filter
        - Extreme Contrast Filter
        - Horizontal Flipping Filter
        - Two Tone Test Function
        - Three Tone Test Function
        - Vertical Flipping Test Function
        

LICENSE:
Copyright (c) 2020 SFM Photo Editing

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
