import os,sys
from interface import UserInterface
def pathing_creator(folder):
    if getattr(sys,'frozen',False):
        path=os.path.dirname(os.path.realpath(sys.executable))  
    elif __file__:
        path=os.path.dirname(__file__)
    return os.path.join(path,folder)

pathing=pathing_creator('storage')
interface=UserInterface(pathing)
interface.loadInterface()
