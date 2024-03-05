# Assignment: File Manipulation in Python

In this assignment, you will be working with file manipulation in Python. You will be implementing two functions: `combine_files` and `add_btw`.

## Function Descriptions

### `combine_files(path1, path2, output_path)`

This function takes in the paths of two text files and an output file. It reads the contents of the two input files, combines them line by line, and writes the result to the output file. If one file has more lines than the other, the remaining lines from the longer file are appended to the end of the output file.

Here's an example of how the function works:

- `file1` contents:
    ```
    line1
    line2
    line3
    ```

- `file2` contents:
    ```
    lineA
    lineB
    ```

- `output_file` contents after calling `combine_files('file1', 'file2', 'output_file')`:
    ```
    line1 lineA
    line2 lineB
    line3
    ```

### `add_btw(path, output_path)`

This function takes in the path of a text file and an output file. It reads the contents of the input file, modifies each line by removing the period (if any) and appending the string ' btw.' at the end, and writes the result to the output file.

Here's an example of how the function works:

- `file` contents:
    ```
    This is a line.
    This is another line.
    ```

- `output_file` contents after calling `add_btw('file', 'output_file')`:
    ```
    This is a line btw.
    This is another line btw.
    ```

### Please do not modify the tests; they are designed to check if your functions are working correctly, also don't touch the text files themselves.
#### to run the tests you should first install pytest module, using *```pip install pytest```* and the just run *```pytest```* from he terminal.

Good luck!