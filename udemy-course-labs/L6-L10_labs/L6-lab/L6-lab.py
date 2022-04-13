import os


def wordcount(path):
    print('checking whether the file exists...')
    if os.path.isfile(path):
        print('the file exists')
        file = open(path, 'r')
        text = file.read()
        print(text)
        list = text.split(' ')
        length = len(list)
        print('The file has', length, 'words written')
        return len(list)
    else:
        return 'the file does not exist'



wordcount('/home/wisie/sandbox/udemy-course-labs/L6-lab/file.txt')
