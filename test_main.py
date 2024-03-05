import pytest
import os
import tempfile
from main import combine_files, add_btw

def test_combine_files():
    for file in [['text_1.txt', 'text_2.txt'], ['text_2.txt', 'text_3.txt']]:
        fd, temp_path = tempfile.mkstemp()
        try:
            combine_files(file[0], file[1], temp_path)
            with open(temp_path, 'r') as temp_out:
                lines = temp_out.readlines()
                with open(file[0], 'r') as file1:
                    with open(file[1], 'r') as file2:
                        l1 = file1.readlines()
                        l2 = file2.readlines()
                        if len(l1) > len(l2):
                            for i in range(len(l2)):
                                assert lines[i] == l1[i].strip() + ' ' + l2[i].strip() + '\n'
                            for i in range(len(l2), len(l1)):
                                assert lines[i] == l1[i].strip() + '\n'
                        else:
                            for i in range(len(l1)):
                                assert lines[i] == l1[i].strip() + ' ' + l2[i].strip() + '\n'
                            for i in range(len(l1), len(l2)):
                                assert lines[i] == l2[i].strip() + '\n'
        finally:
            os.close(fd)
            os.remove(temp_path)

def test_add_btw():
    for file in ['text_1.txt', 'text_2.txt', 'text_3.txt']:
        fd, temp_path = tempfile.mkstemp()
        try:
            add_btw(file, temp_path)
            with open(temp_path, 'r') as temp_out:
                lines = temp_out.readlines()
                with open(file, 'r') as file:
                    l = file.readlines()
                    for i in range(len(l)):
                        assert lines[i] == l[i].strip().replace('.', '') + ' btw.\n'
        finally:
            os.close(fd)
            os.remove(temp_path)