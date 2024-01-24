from itertools import combinations

def collides(obj1, obj2):
    if(obj2["x1"] > obj1["x2"] or obj1["x1"] > obj2["x2"]):
        return False
    if(obj2["y1"] > obj1["y2"] or obj1["y1"] > obj2["y2"]):
        return False
    return True

def number_of_collisions(objects):
    return [collides(pair[0],pair[1]) for pair in combinations(objects, 2)].count(True)


# print(number_of_collisions([{'x1': 1, 'y1': 1, 'x2': 3, 'y2': 3}, {'x1': 0, 'y1': 2, 'x2': 4, 'y2': 2}]))
# print(number_of_collisions([{'x1': 0, 'y1': 0, 'x2': 2, 'y2': 2}, {'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5}]))
# print(number_of_collisions([{'x1': 0, 'y1': 0, 'x2': 2, 'y2': 2}, {'x1': 2, 'y1': 2, 'x2': 5, 'y2': 5}]))
# print(number_of_collisions([{'x1': 209, 'y1': 87, 'x2': 242, 'y2': 164}, {'x1': 82, 'y1': 199, 'x2': 100, 'y2': 241}, {'x1': 220, 'y1': 35, 'x2': 272, 'y2': 61}, {'x1': 559, 'y1': 103, 'x2': 657, 'y2': 186}, {'x1': 390, 'y1': 411, 'x2': 429, 'y2': 436}, {'x1': 591, 'y1': 216, 'x2': 662, 'y2': 251}, {'x1': 88, 'y1': 436, 'x2': 103, 'y2': 488}, {'x1': 93, 'y1': 544, 'x2': 128, 'y2': 618}, {'x1': 6, 'y1': 510, 'x2': 58, 'y2': 534}, {'x1': 585, 'y1': 65, 'x2': 678, 'y2': 137}, {'x1': 78, 'y1': 183, 'x2': 171, 'y2': 248}, {'x1': 168, 'y1': 123, 'x2': 217, 'y2': 137}]))

