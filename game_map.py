
from map_objects.tile import Tile
from map_objects.rectangle import Rect

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        
    def initialize_tiles(self):
        
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles
    
    def make_map(self):
        #Make two rooms for demonstation purposes
        room1 = Rect(20,15,10,15)
        room2 = Rect(35,15,10,15)
        
        self.create_room(room1)
        self.create_room(room2)
    
    def create_room(self, room):
    #Go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False
                
    def create_h_tunnel(self,x1, x2, y):
        for x in range(min(x1,x2), max(x1,x2)+1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
            
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1,y2), max(y1,y2)+1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
    
    def is_blocked(self, x, y ):
        if self.tiles[x][y].blocked:
            return True
        return False