text = open('/Users/aharris/Desktop/Python/euler11Supplement.txt')
stringGrid = text.read()
grid = []

for i in range(20):
    newString = stringGrid[0:60]
    stringGrid = stringGrid[60:]
    newList = list(map(int, newString.split()))
    grid.append(newList)

bigProduct = 1
horizontal = 1
vertical = 1
diagRight = 1
diagLeft = 1

for i in range(20):
    for j in range(20):
        print()
        print('horizontal', end='  --  ')
        try:
            horizontal = 1
            for k in range(4):
                horizontal *= grid[i][j+k]
                print(str(grid[i][j+k]) + ' ', end=' ')
        except IndexError:
            horizontal = 1
        if horizontal > bigProduct:
            bigProduct = horizontal

        print()
        print('vertical', end='  --  ')
        try:
            vertical = 1
            for k in range(4):
                vertical *= grid[i+k][j]
                print(str(grid[i+k][j]) + ' ', end=' ')
        except IndexError:
            vertical = 1
        if vertical > bigProduct:
            bigProduct = vertical

        print()
        print('diagRight', end='  --  ')
        try:
            diagRight = 1
            for k in range(4):
                diagRight *= grid[i+k][j+k]
                print(str(grid[i+k][j+k]) + ' ', end=' ')
        except IndexError:
            diagRight = 1
        if diagRight > bigProduct:
            bigProduct = diagRight

        print()
        print('diagLeft', end='  --  ')

        if j >= 3:
            try:
                diagLeft = 1
                for k in range(4):
                    diagLeft *= grid[i+k][j-k]
                    print(str(grid[i+k][j-k]) + ' ', end=' ')
            except IndexError:
                diagLeft = 1
            if diagLeft > bigProduct:
                bigProduct = diagLeft


print(bigProduct)
