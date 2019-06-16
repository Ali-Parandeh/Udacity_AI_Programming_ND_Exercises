#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Alireza Parandeh
# DATE CREATED: 12.05.2019                   
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
# Check https://www.tutorialspoint.com/python3/os_listdir.htm for instructions on how to use the standard Python 3 library module
from os import listdir

# Helper function to convert a file name into pet label
def pet_labeler(filename):
    # Converts the filename string into lowecase characters then splits the filename string by _ to break into words and saves it as a list inside word_list_pet_image variable
    word_list_pet_image = filename.lower().split("_")
    
    # Create pet_name starting as empty string
    pet_name = ""

    # Loops to check if word in pet name is only
    # alphabetic characters - if true append word
    # to pet_name separated by trailing space 
    for word in word_list_pet_image:
        if word.isalpha():
            pet_name += word + " "

    # Strip off starting/trailing whitespace characters 
    pet_label = pet_name.strip()
    
    # Initialising a list and appending the pet label string to the list to create a list for passing as value to the results dictionary
    pet_label_list = []
    pet_label_list.append(pet_label)
    return pet_label_list

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Loops over the image directory given to the programme by user in command line and creates a list of file names and saves it inside filename_list
    filename_list = listdir(image_dir)
    
    # Initialising an empty dictionary to store the pet labels in
    results_dic = {}
    
    # Loops over the filename list and converts each file name into a pet label using the pet_labeler helper function
    for idx in range(0, len(filename_list), 1):
        pet_label_list = pet_labeler(filename_list[idx])
        # Check if a file name is already inside the results_dic dictionary. 
        # Only add a new pet label if file name is not inside. 
        # This check is to prevent different files with the same names overwrite existing values in the results dictionary
        if filename_list[idx] not in results_dic:
            results_dic[filename_list[idx]] = pet_label_list
        else:
            print("Warning: Key=", filename_list[idx], "already exists in results_dic with value =", results_dic[filename_list[idx]])
    # Returns the constructed dictionary of pet names formatted as key= filename - ex: German_shepherd_dog_04890.jpg and value = pet label as a list - ex: ["german shepherd dog"]
    return results_dic

