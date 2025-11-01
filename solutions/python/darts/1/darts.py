def score(x, y):
    #(x - center_x)² + (y - center_y)² < radius²
    if pow(x, 2) + pow(y, 2) <= 1:
        return 10
    if pow(x, 2) + pow(y, 2) <= 25:    
        return 5
    if pow(x, 2) + pow(y, 2) <= 100:
        return 1
    return 0
