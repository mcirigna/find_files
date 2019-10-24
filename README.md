# find_files

Description

    find files created within Start Date and End Date
    enter dates using format month/day/year like 10/30/2019
    works with python2 and python3
    added support for windows
    outputs to a csv file
    this program does not consider hours minutes or seconds, only date

CSV output structure

    file, path, birthdate, permissions, size, hardlinks

Example

    python find_files.py
    
    What folder would you like to search?
    > /Users/jeff/Desktop
    Would you like to search sub directories? Y/n
    > Y
    What start date should be used to filter the files?
    > 10/01/2019
    What end date should be used to filter the files?
    > 10/24/2019
    The output will be in a csv file. What should the file name be?
    > output
    Your output file is located at: /Users/jeff/Desktop/output.csv

