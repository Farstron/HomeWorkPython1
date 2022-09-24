def coordinates_plane(quarter):
    coor = []
    if quarter == 1:
        coor.append('>0')
        coor.append('>0')
    if quarter == 2:
        coor.append('<0')
        coor.append('>0')
    if quarter == 3:
        coor.append('<0')
        coor.append('<0')
    if quarter == 4:
        coor.append('>0')
        coor.append('<0')
    return coor
q = int(input("введите четверть:"))
c =[]
c = coordinates_plane(q)
print("x",c[0],"y",c[1])