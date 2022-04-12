import os 

def log_it(*comms):
    f = open('/home/wisie/sandbox/udemy-course-labs/L17-lab/log_it.txt', 'a')
    for i in comms:
        f.write(i+'\n')
    f.close()

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')