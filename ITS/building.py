from room import Room


class Building:

    def __init__(self,name:str,adress:str,floors:int):
        self.name=name
        self.adress=adress
        self.floors:int=floors
        self.rooms:list[Room]=[]

    def get_name(self):
        return self.name
    
    def get_adress(self):
        return self.adress
    
    def get_floors(self):
        return self.floors
    def get_rooms(self):
        return self.rooms
    
    
    
    
    
    def add_room(self,room:Room) -> bool:
        if room not in self.get_rooms() and room.floor<= self.get_floors():
            self.rooms.append(room)
            return True
        else:
            return False
        
        