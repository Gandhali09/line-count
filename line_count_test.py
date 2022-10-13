"""
Unit Test Cases
"""
from utils import read_file_paths, count_file_lines, summary

def test_read_file_paths_invalid_path():
    """Function to test read_file_paths method when path is invalid"""
    file_paths = read_file_paths("abc")
    assert not file_paths

def test_read_file_paths_valid_path():
    """Function to test read_file_paths method when path is valid"""
    file_paths = read_file_paths("./mock_dir")
    assert file_paths == ['./mock_dir/test.txt']

def test_read_file_paths_with_extension():
    """Function to test read_file_paths method when path and extension are given"""
    file_paths = read_file_paths("./mock_dir", ".py")
    assert file_paths == ['./mock_dir/test.py']

def test_count_file_lines_empty_path_list():
    """Function to test count_file_lines method when path list is empty"""
    file_paths = []
    file_dict = count_file_lines(file_paths)
    assert not file_dict

def test_count_file_lines():
    """Function to test count_file_lines method when path list is not empty"""
    file_paths = ['./mock_dir/test.txt']
    file_dict = count_file_lines(file_paths)
    assert file_dict == {'./mock_dir/test.txt': 5}

def test_summary_empty_dict():
    """Function to test summary method when file dictionary is empty"""
    file_dict = {}
    sumamry_dict = summary(file_dict)
    assert not sumamry_dict

def test_summary():
    """Function to test summary method when file dictionary is not empty"""
    file_dict = {'./mock_dir/test.txt': 5}
    sumamry_dict = summary(file_dict)
    assert sumamry_dict == {
        'Average lines per file': 5.0,
        'Number of files found': 1,
        'Total number of lines': 5}

if __name__ == "__main__":
    test_read_file_paths_invalid_path()
    test_read_file_paths_valid_path()
    test_count_file_lines_empty_path_list()
    test_count_file_lines()
    test_summary_empty_dict()
    test_summary()
