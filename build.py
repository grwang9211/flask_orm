import os
from flask_script import Manager

from model.model2python import GenCodeCommand

if __name__ == "__main__":
    print (  os.path.dirname(os.path.realpath(__file__)))
    r = GenCodeCommand() 
    r.run()