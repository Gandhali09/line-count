"""
utils
"""
import os
import numpy as np

def read_file_paths(path, extension='.txt'):
    """Function to read file path for given directory and sub-directory """
    file_paths = []
    for root, _, files in os.walk(path):
        files = filter(lambda file: file.endswith(extension), files)
        for name in files:
            file_paths.append(os.path.join(root, name))
    return file_paths

def count_file_lines(file_paths):
    """Function to count number of lines for each of the files"""
    file_dict = {}
    for file_path in file_paths:
        with open(file_path, 'r', encoding="utf-8") as file:
            file_dict[file_path] = len(file.readlines())
    return file_dict

def summary(file_dict):
    """Function to create summary statistics for files count"""
    sumamry_dict = {}
    total_files = len(file_dict)
    if total_files:
        line_count = 0
        for val in file_dict.items():
            line_count = line_count+val[1]
            avg = line_count / total_files
        sumamry_dict['Number of files found'] = total_files
        sumamry_dict['Total number of lines'] = line_count
        sumamry_dict['Average lines per file'] = np.round(avg, 3)
    return sumamry_dict

def display_result(file_dict, sumamry_dict):
    """Function to display result"""
    if file_dict:
        for file in file_dict.items():
            print(file[0].ljust(90), str(file[1]))
        print('=====================================================================')
        for item in sumamry_dict.items():
            print(item[0].ljust(90), str(item[1]))
    else:
        print('Number of files found'.ljust(50), str(0))
