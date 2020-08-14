from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
# map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#initialize rooms

rooms = {}
rooms[0] = player.current_room.get_exits()


traveled = []
invert = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

#while 
print(len(room_graph))
while len(rooms) < len(room_graph) - 1:
    print("currentroomid",player.current_room.id)
    
    if player.current_room.id not in rooms:
        rooms[player.current_room.id] = player.current_room.get_exits()
        print("rooms",rooms)
        lastRoom = traveled[-1]
        print("lastroom",lastRoom)
        rooms[player.current_room.id].remove(lastRoom)
        print("roomsremovedlast",rooms)
    
    while len(rooms[player.current_room.id]) == 0:
        reverse = traveled.pop()
        print("reverse",reverse)
        traversal_path.append(reverse)
        player.travel(reverse)

    direction = rooms[player.current_room.id].pop(0)
    print("direction",direction)
    traversal_path.append(direction)
    traveled.append(invert[direction])
    player.travel(direction)
    print("traversal_path",traversal_path)
    print("traveled",traveled)



# while s.size() > 0:
#     v = s.pop()
#     while player.current_room.id not in visited:
#         visited[player.current_room.id] = v
#         traversal_path.append("n")
#         player.travel("n")
#         rooms[player.current_room.id] = player.current_room.get_exits()
#         print("cooms",rooms)
        



#   get possible room directions to travel
#   pick a random direction and travel and store directions traveled for backtracking
#   travel in that direction until not avail
#   choose another direction and repeat
#   else backtrack to a previous room with unvisited rooms and then choose a random direction
#   repeat until no unexplored choices left








# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
