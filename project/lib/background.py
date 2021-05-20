import sys
sys.path.append("..")
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from model.hobby import Hobby
from model.userwithlabel import UserWithLabel
from lib.hobby import calTFIDF
import sys
import numpy as np
import time


username = sys.argv[1]
try:
    TFIDFMartix = np.array(calTFIDF(username))
    Hobby.update(username,TFIDFMartix)
    with open('./lib/log.txt','a+') as f:
        f.write(str(time.asctime(time.localtime(time.time()))+"\n"))
    # with open('./lib/tt.txt',"w+") as f:
    #     f.write(str(UserWithLabel.read(username)))
    # with open('./lib/t.txt',"w+") as f:
    #     f.write(str(list(Hobby.getMartix(username))))
except Exception as e:
    with open('./lib/log.txt','a+') as f:
        f.write(str(e.args))