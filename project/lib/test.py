# import pickle
# with open('./recommend/Recommend-System/labelindex.txt','rb') as f:
#     k = pickle.load(f)
#     # print(k)

# with open('./recommend/Recommend-System/textlabelMartix.txt','rb') as f:
#     k = pickle.load(f)
#     print(k)

import subprocess
import time
import signal
import getopt
import sys

# def signal_handler(signal,frame,a):
#     a.terminate()

# def a():
#     p = subprocess.Popen(['python3 /Users/xiaoxinchen/111/project/lib/t1.py'],shell = True)
#     time.sleep(5)
#     if (p.returncode == None):
#         print(p.pid)
#         signal.signal(signal.SIGINT,signal_handler)
#         print(p.returncode)
#         return 0
#     else:
#         return 1

# print("a =",a())
# print('end')

print(sys.argv[1])


