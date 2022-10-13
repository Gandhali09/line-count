## Line Count Program

Line count program takes a directory as a required argument and a filename extension as optional argument that defaults to “.txt”. The program locatea all files with the given extension in the given directory and all its subdirectories to produce a list of all matching files with the numbers of lines within the file. The program outputs the total number of lines and the average number of lines per file. 

For example:
``` console
./fileRead.ipynb                                                                           415
./lineCount.ipynb                                                                          287
./.ipynb_checkpoints/lineCount-checkpoint.ipynb                                            287
./.ipynb_checkpoints/fileRead-checkpoint.ipynb                                             415
=====================================================================
Number of files found                                                                      4
Total number of lines                                                                      1404
Average lines per file                                                                     351.0
```

### Code Analysis
- 'pylint line_count.py'

### Test
- 'pytest -q line_count_test.py'

### Run
- with extension: 'python3 line_count.py --path="." --extension=".py"'
- without extension: 'python3 line_count.py --path="."'
