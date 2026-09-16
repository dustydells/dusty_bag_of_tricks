from PIL import Image
import os
import glob

def png_jpg_converter(img_path, desired_file_type):
    '''
    Convert images between png and jpg. This function goes well with a 
    glob for loop. Use the glob library. The code is commented out at the
    bottom of the function.

    Parameters:
        img_path:
            The path to the image you want to convert. Must be a jpg or png.
        desired_file_type:
            The file type you want to convert the image to. Either "jpg" or "png"
    Returns:
        Nothing, but the file should have changed
    '''
    # Standardize capitalization of input
    desired_file_type = desired_file_type.lower()

    # Read in the image.
    img = Image.open(img_path)

    # Check if the user specified jpg
    if desired_file_type == 'jpg':
        # Remove the extension 
        filename = os.path.splitext(img_path)[0]

        # Save a new version of the image as a png.
        img.save(f'{filename}.jpg')

        # Delete the old file.
        os.remove(f'{filename}.png')
    
    elif desired_file_type == 'png':
        # Remove the extension 
        filename = os.path.splitext(img_path)[0]

        # Save a new version of the image as a jpg.
        img.save(f'{filename}.png')

        # Delete the old file.
        os.remove(f'{filename}.jpg')
    
    else:
        print('Desired file type not recognized. Please use "jpg" or "png."')

    # # Here's how to loop through a folder of images because you probably forgot.
    # folder_path = 'ART\\deerface\\bad_pages_quarantine\\*' # asterisk means any file name in that folder

    # # Loop through every file in the specified folder
    # for file in glob.glob(folder_path):
    #     print(file)

        
# # Usage example of png_jpg_converter
# img_path = 'ART\\deerface\\bad_pages_quarantine\\pg52.jpg'
# desired_file_type = 'png'

# png_jpg_converter(img_path, desired_file_type)

