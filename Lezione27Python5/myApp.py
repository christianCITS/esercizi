import time 
import sys
sys.stdout=open("./file_per_le_print.txt","w+")
ii=1
while (ii<10):
    sys.stdout.flush()
    time.sleep(2)
    print("prova print")
    ii=1
sys.stdout.close()



