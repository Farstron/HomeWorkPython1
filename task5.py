X1,Y1 = map(int, input("Введите координаты первой точки:").split())
X2,Y2 = map(int, input("Введите координаты второй точки:").split())
print('Расстояние между точками:', round(((X1-X2)**2+(Y1-Y2)**2)**0.5,4))