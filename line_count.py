"""
Line Count Program
"""
import argparse
from utils import read_file_paths, count_file_lines, summary, display_result

parser = argparse.ArgumentParser(prog = "LineCount")
parser.add_argument('--path', type=str,required=True)
parser.add_argument('--extension', type=str, default='.txt', required=False)

args = parser.parse_args()

if __name__ == '__main__':
    path_ = vars(args)['path']
    extension_ = vars(args)['extension']

    # read file path for directory and sub dierctories
    filePath = read_file_paths(path_, extension_)

    # count lines per file
    fileDict = count_file_lines(filePath)

    # create summary statistics
    sumamryDict = summary(fileDict)

    # Display the result
    display_result(fileDict, sumamryDict)
