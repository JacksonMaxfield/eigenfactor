def prepMatrix(matrix):
    sums = []
    dvector = []
    size = len(matrix)
    cindex = 0

    while cindex < size:
        rindex = 0
        tempSum = 0

        while rindex < size:
            if rindex == cindex:
                matrix[rindex][cindex] = 0

            tempSum = tempSum + matrix[rindex][cindex]
            rindex = rindex + 1

        sums.append(tempSum)

        if tempSum == 0:
            dvector.append(1)
        else:
            dvector.append(0)

        cindex = cindex + 1

    sAndD = [sums, dvector]
    return sAndD

def normalize(matrix, sums):
    size = len(matrix)
    cindex = 0

    while cindex < size:
        rindex = 0

        while rindex < size and sums[cindex] != 0:
            preVal = matrix[rindex][cindex]
            postVal = preVal / sums[cindex]
            matrix[rindex][cindex] = postVal
            rindex = rindex + 1

        cindex = cindex + 1

rawMatrix = [
    [1, 0, 2, 0, 4, 3],
    [3, 0, 1, 1, 0, 0],
    [2, 0, 4, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [8, 0, 3, 0, 5, 2],
    [0, 0, 0, 0, 0, 0]
]

alphaConst = 0.85
epsilonConst = 0.00001

sAndD = prepMatrix(rawMatrix)
columnSums = sAndD[0]
dvector = sAndD[1]

normalize(rawMatrix, columnSums)
avector = [3/14, 2/14, 5/14, 1/14, 2/14, 1/14]
pivector = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

r = 0

while ()

print('-----------------')
print('current matrix:')
print('-----------------')
for row in rawMatrix:
    print(row)
