import json

class LevelManager:
    def __init__(self):
        with open("assets/levels/levels.json",'r') as level:
            self.__file_data = json.load(level)

    def addLevel(self,newlevel):
        self.__file_data.append(newlevel)
        self.updateLevels

    def deleteLevel(self,index):
        self.__file_data.pop(index)
        self.updateLevels()

    def updateLevels(self):
        with open("assets/levels/levels.json",'w') as level:
            json.dump(self.__file_data, level)

    def LoadLevels(self):
        return self.__file_data