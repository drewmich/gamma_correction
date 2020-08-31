# Python script to adjust gamma on all images in a directory

This is a python script I wrote to adjust the gamma on images either adaptively or with a provided value from (0-1).

After downloading the script, users can save it anywhere, but in order to run the script they must be in the same working directory. How to run:
The script takes 4 arguments including the script name.

    1st argument: main.py
    2nd argument: full path to folder where adjusted images will be saved
    3rd argument: full path to folder where raw images reside (input and output folders can bs the same)
    4th argument: must be either "clahe" or a numerical value between (0-1) exclusive
    
For example:

    ./main.py "/Users/drewmichelini/Images/output" "/Users/drewmichelini/Images/input/" clahe
    
or:

    ./main.py "/Users/drewmichelini/Images/output" "/Users/drewmichelini/Images/input/" .95
    
  
After running, each image from the input directory will have a corresponding image in the output directory. "adjusted_" will be prepended to each filename in the output directory.

The script uses OpenCV to accomplish most of the work.
  
