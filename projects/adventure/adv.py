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
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


#   get possible room directions to travel
#   pick a random direction and travel / store directions traveled for backtracking
#   travel in that direction to the next room
#   remove previous room from direction choices then choose another random direction and repeat
#   else backtrack to a previous room with unvisited rooms and then choose a random direction
#   repeat until no unexplored choices left


#######
# TRAVERSAL Method
#######

#initialize rooms
rooms = {}
rooms[0] = player.current_room.get_exits()

# array to store traveled roooms for backtracking
traveled = []
invert = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# while number of rooms explored is less than total number of rooms
def get_traversal():
    while len(rooms) < len(room_graph) - 1:


        #if current room is not in rooms
        if player.current_room.id not in rooms:

            #add current room to rooms
            rooms[player.current_room.id] = player.current_room.get_exits()
            # print("rooms",rooms)

            #get previous room traveleds
            prevRoom = traveled[-1]
            # print("lastroom",prevRoom)

            #remove previous room from one of the possible directions to travel
            # print('prevroom',prevRoom)
            rooms[player.current_room.id].remove(prevRoom)
            # print("roomsremovedlast",rooms)

        # print("currentroom",rooms)
        #Backtrack
        #while there are no directions left to travel
        while len(rooms[player.current_room.id]) == 0:

            #get last direction traveled
            reverse = traveled.pop()
            # print("reverse",reverse)

            #travel to previous room
            traversal_path.append(reverse)
            player.travel(reverse)

        #Travel
        # get a direction from the current room dict

        #first direction from array vers
        # direction = rooms[player.current_room.id].pop(0)

        #random dir from array
        random.shuffle(rooms[player.current_room.id])
        direction = rooms[player.current_room.id].pop(0)
        # print("direction",direction)

        #travel in the direction and append to traversal array
        player.travel(direction)
        traversal_path.append(direction)

        #record opposite direction for backtracking
        traveled.append(invert[direction])

        # print("traversal_path",traversal_path)
        # print("traveled",traveled)

            # removes previous room traveled if room is already discovered
        if len(traveled) > 0 and player.current_room.id in rooms:
            prevRoom = traveled[-1]
            # print("lastroom",prevRoom)

            #remove previous room from one of the possible directions to travel
            # print('prevroom',prevRoom)
            rooms[player.current_room.id].remove(prevRoom)
            # print("roomsremovedlast",rooms)
            
while True:
    traversal_path = []
    get_traversal()
    print(len(traversal_path))



#######
# TRAVERSAL TEST
#######

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
