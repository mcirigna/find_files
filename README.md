# find_files

Description

    find files created within specified time frame
    enter dates using format year-month-day
    works with python2 and python3
    added support for windows
    outputs to a csv file

CSV output structure

    file, path, birthtime, permissions, size, hardlinks

Example

    python find_files.py
    
    What folder would you like to search?
    > /Users/jeff/Desktop
    Would you like to search sub directories? Y/n
    > Y
    What start date should be used to filter the files?
    > 2015-10-23
    What end date should be used to filter the files?
    > 2019-01-14
    The output will be in a csv file. What should the file name be?
    > output.csv

