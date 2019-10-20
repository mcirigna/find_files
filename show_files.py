from __future__ import print_function
import sys, os, time, datetime, argparse, stat

def getPermissions(fileStat):
    """
    fileStat : used to retrieve file permissions
    return : permissions as string (ex: '-rrw-r--r--')
    source : https://stackoverflow.com/questions/17809386/how-to-convert-a-stat-output-to-a-unix-permissions-string
    """
    is_dir = 'd' if stat.S_ISDIR(fileStat.st_mode) else '-'
    dic = {'7':'rwx', '6' :'rw-', '5' : 'r-x', '4':'r--', '0': '---'}
    perm = str(oct(fileStat.st_mode)[-3:])
    return is_dir + ''.join(dic.get(x,x) for x in perm)


def showFiles(startTime, endTime, verbose):
    """ 
    for all files created between startTime and endTime
        print (file, path, birthtime, permissions, size, hardlinks)
    """
    for root, _, files in os.walk("/"):
        for file in files:
            try:            
                path = os.path.join(root, file)
                fileStat = os.stat(path)
                birthtime = datetime.datetime.fromtimestamp(fileStat.st_ctime)
                permissions = getPermissions(fileStat)
                size = fileStat.st_size
                hardlinks = fileStat.st_nlink
            except:
                if verbose: print("Inaccessible: {0}".format(path))
            else:
                if (startTime is not None and birthtime < startTime) or (endTime is not None and birthtime > endTime):
                    break
                else:
                    print('\n{0}'.format(file))
                    print(path)
                    print(birthtime.strftime('%Y-%m-%d %H:%M:%S'), permissions, size, hardlinks)

if __name__ == '__main__':
    """
    for all files created between startTime and endTime
        print   file 
                path 
                birthtime permissions size hardlinks
    """
    parser = argparse.ArgumentParser(description='Show files within a specified time frame using format year-month-day',
                                    epilog='example: python3 show_files.py --after 2013-09-14 --before 2016-10-22')
    parser.add_argument('-a', '--after', metavar='date', type=str, help='show files after date')
    parser.add_argument('-b', '--before', metavar='date', type=str, help='show files before date')
    parser.add_argument('-v', '--verbose', action='store_true', help='show inaccessible files')
    args = parser.parse_args()

    if args.after:
        try:
            startTime = datetime.datetime.strptime(args.after, '%Y-%m-%d')
        except:
            sys.exit('invalid date {0}'.format(args.after))
    else:
        startTime = None

    if args.before:
        try:
            endTime = datetime.datetime.strptime(args.before, '%Y-%m-%d')
        except:
            sys.exit('invalid date {0}'.format(args.before))
    else:
        endTime = None

    verbose = True if args.verbose else False

    showFiles(startTime, endTime, verbose)