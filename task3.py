def quarter_plane(X,Y):
    q = 0
    if X > 0 and Y > 0:
        q = 1
    if X < 0 and Y > 0:
        q = 2
    if X < 0 and Y < 0:
        q = 3
    if X > 0 and Y < 0:
        q = 4
    return q
X = int(input('Write X:'))
Y = int(input('Write Y:'))
print('Quarter:', quarter_plane(X,Y))