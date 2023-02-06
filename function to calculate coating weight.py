def coating_weight(depth, density):
    volume = depth * 10**-6
    area = 1
    weight = volume * density * 1000
    return weight / area
