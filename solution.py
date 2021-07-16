def formingMagicSquare(s):
    mysum = 0
    bestscore = 45 #worst case scenario
    squares = [[[2,9,4],[7,5,3],[6,1,8]], [[4,9,2],[3,5,7],[8,1,6]]]
    for a in range(2):
        for b in range(4):
            squares[a] = rotate(squares[a])
            mysum = 0
            for x in range(3):
                for y in range(3):
                    mysum += abs(s[x][y]-squares[a][x][y])
            bestscore = mysum if mysum < bestscore else bestscore
    return(bestscore)           
        
def rotate(s):
    #this function rotates the matrix 90 degrees
    newarray = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(3):
        for y in range(3):
            newarray[x][y] = s[2-y][x]
    return(newarray)
