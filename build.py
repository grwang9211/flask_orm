from genericpath import isdir
import os
import shutil, errno

from flask_script import Manager

from model.model2python import GenCodeCommand

if __name__ == "__main__":
    if ( os.path.isdir("app")) : 
        shutil.rmtree( "app")
    shutil.copytree( "skeleton", "app")
    print (  os.path.dirname(os.path.realpath(__file__)))
    r = GenCodeCommand() 
    r.run()