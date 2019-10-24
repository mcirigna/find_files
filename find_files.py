import os, datetime, stat, csv

def get_permissions(fileStat):
    """
    fileStat : used to retrieve file permissions
    return : permissions as string (ex: '-rrw-r--r--')
    source : https://stackoverflow.com/questions/17809386/how-to-convert-a-stat-output-to-a-unix-permissions-string
    """
    is_dir = 'd' if stat.S_ISDIR(fileStat.st_mode) else '-'
    dic = {'7':'rwx', '6' :'rw-', '5' : 'r-x', '4':'r--', '0': '---'}
    perm = str(oct(fileStat.st_mode)[-3:])
    return is_dir + ''.join(dic.get(x,x) for x in perm)


def get_files(folder, recursive, startDate, endDate):
    """ 
    for all files in folder created between startDate and endDate
        get (file, path, birthtime, permissions, size, hardlinks)
    """
    rows = [ ['file','path','creationtime','permissions','size','hardlinks'] ]
    for root, _, files in os.walk(folder):
        for file in files:
            try:            
                path = os.path.join(root, file)
                fileStat = os.stat(path)
                birthtime = datetime.datetime.fromtimestamp(fileStat.st_ctime).date()
                permissions = get_permissions(fileStat)
                size = fileStat.st_size
                hardlinks = fileStat.st_nlink
            except:
                pass
            else:
                if (startDate is not None and birthtime < startDate) or (endDate is not None and birthtime > endDate):
                    break
                else:
                    rows.append([file,path,birthtime.strftime('%Y-%m-%d'), permissions, size, hardlinks])
        if not recursive: break
    return rows

if __name__ == '__main__':
    # Prompt User -> Get Files -> Create CSV file
    # compatibility for python 2
    try:
        input = raw_input
    except NameError:
        pass

    folder = input('What folder would you like to search?\n> ')
    while not os.path.isdir(folder):
        folder = input('Not a valid directory. Try again.\n> ')

    recursive = str(input('Would you like to search sub directories? Y/n\n> ')).lower().strip()[0]
    while True:
        if recursive == 'y':
            recursive = True
            break
        elif recursive == 'n':
            recursive = False
            break
        else:
            recursive = str(input('Please enter yes or no.\n> ')).lower().strip()[0]
    
    startInput = input('What start date should be used to filter the files?\n> ')
    while True:
        try:
            startDate = datetime.datetime.strptime(startInput, '%Y-%m-%d').date()
        except:
            startInput = input('The date should be formatted like 2015-11-23, try again.\n> ')
        else:
            break

    endInput = input('What end date should be used to filter the files?\n> ')
    while True:
        try:
            endDate = datetime.datetime.strptime(endInput, '%Y-%m-%d').date()
        except:
            endInput = input('The date should be formatted like 2015-11-23, try again.\n> ')
        else:
            break

    name = input('The output will be in a csv file. What should the file name be?\n> ')
    while True:
        if name[-4:] != '.csv':
            name += '.csv'
        if os.path.exists(name):
            name = input('That file already exists, try another name.\n> ')
        else:
            break
    
    rows = get_files(folder, recursive, startDate, endDate)

    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    csvfile.close()