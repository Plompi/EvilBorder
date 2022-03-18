import json

class LevelManager:
    def __init__(self):
        with open("assets/levels/levels.json",'r') as level:
            self.__file_data = json.load(level)

    def add_level(self,newlevel):
        self.__file_data.append(newlevel)
        self.update_levels()

    def delete_level(self,index):
        self.__file_data.pop(index)
        self.update_levels()

    def update_levels(self):
        with open("assets/levels/levels.json",'w') as level:
            json.dump(self.__file_data, level)

    def load_levels(self):
        return self.__file_data