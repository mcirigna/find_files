# show_files

Description
    show files created within specified time frame
    enter dates using format year-month-day
    works with python2 and python3

Output Structure
    file
    path
    birthtime permissions user group size number_of_hardlinks

Examples
    python show_files.py --after 2016-10-12
        - prints all files created after 2016-10-12

    python show_files.py --before 2006-04-14
        - prints all files created before 2006-04-14

    python3 show_files.py -a 2014-07-12 -b 2014-07-14
        - prints all files between 2014-07-12 and 2014-07-14

    python3 show_files.py --verbose -a 2014-07-12
        - verbose will indicate files that are inaccessible

