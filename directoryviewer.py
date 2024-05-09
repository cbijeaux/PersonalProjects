import os

class directory:
    @staticmethod
    def pullAllDirectoryFiles(directorypathing):
        return os.listdir(directorypathing)
    @staticmethod
    def deleteFilefromDirectory(directorypathing,titleoffile):
        os.remove(os.join(directorypathing,titleoffile))