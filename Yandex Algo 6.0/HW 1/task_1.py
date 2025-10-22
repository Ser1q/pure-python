from math import sqrt

def closest_side(x1, y1, x2, y2, x, y):

    top = abs(y - y2)
    bottom = abs(y - y1)

    left = abs(x - x1)
    right = abs(x - x2)

    # minimal distnce to one of the sides 
    x_axis = min(top, bottom)
    y_axis = min(left, right)

    # for sides
    if x >= x1 and x <= x2:
        if top < bottom:
            return "N"
        else: 
            return "S"
    elif y >= y1 and y <= y2:
        if left < right:
            return "W"
        else: 
            return "E"
    else:
        # distance to the corners
        c_nw = sqrt(((x - x1)**2 + (y - y2)**2))
        c_ne = sqrt(((x - x2)**2 + (y - y2)**2))
        c_sw = sqrt(((x - x1)**2 + (y - y1)**2))
        c_se = sqrt(((x - x2)**2 + (y - y1)**2))

        corner_distances = {c_nw: "NW", c_ne: "NE", c_sw: "SW", c_se: "SE"}

        key_dist = min(c_nw, c_ne, c_sw, c_se) 

        return corner_distances[key_dist]
    
print(closest_side(-1, -1, 1, 1, -2, 2))
    
print(closest_side(-1, -1, 1, 1, 0, 0))

print(closest_side(-1, -2, 5, 3, -4, 6,))

    