import os

files_to_process = ['/home/wisie/sandbox/udemy-course-labs/L15-lab/scr1.py', '/home/wisie/sandbox/udemy-course-labs/L15-lab/scr2.py']
    

print('opening', os.path.basename(files_to_process[0]))
script1 = open(files_to_process[0], 'r')
source1 = script1.read()
print('executing the code...')
exec(source1)
script1.close()

print('opening', os.path.basename(files_to_process[1]))
script2 = open(files_to_process[1], 'r')
source2 = script2.read()
print('executing the code...')
exec(source2)
script2.close()
