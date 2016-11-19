# Jackson Brown
# INFO 370
# A2 - Network Centrality

import numpy # I tried to do it without numpy, always use numpy

# prep the matrix
# returns the sums of each column,
# zeros the diagonal
# and the dvector for the matrix
def prepMatrix(matrix):
    sums = []
    dvector = []
    size = len(matrix)
    cindex = 0

    # for each column
    while cindex < size:
        rindex = 0
        tempSum = 0

        # for each row
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

# normalize the matrix by the sums of each column
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

# the matrix
rawMatrix = [
    [1, 0, 2, 0, 4, 3],
    [3, 0, 1, 1, 0, 0],
    [2, 0, 4, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [8, 0, 3, 0, 5, 2],
    [0, 0, 0, 0, 0, 0]
]

# constants
alphaConst = 0.85
epsilonConst = 0.00001

# prep the matrix and split the values
sAndD = prepMatrix(rawMatrix)
columnSums = sAndD[0]
dvector = sAndD[1]

# normalize the matrix
normalize(rawMatrix, columnSums)

# artical vector
avector = [3/14, 2/14, 5/14, 1/14, 2/14, 1/14]

# initial pi vector
pivector = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

# reshape them to be 6x1 vectors
pivector = numpy.reshape(pivector, (6, 1))
avector = numpy.reshape(avector, (6, 1))

# initial residuals to check against
deltas = [1, 1, 1, 1, 1, 1]

iteration = 0

while True:
    # compute the tempVector (first part of pi^(k+1) formula)
    tempVector = numpy.multiply(alphaConst, rawMatrix)
    tempVector = numpy.dot(tempVector, pivector)

    # compute the dotArticle (second part of the pi^(k+1) formula)
    alphaD = numpy.multiply(alphaConst, dvector)
    dotPi = numpy.dot(alphaD, pivector)
    dotPi = dotPi + (1 - alphaConst)
    dotArticle = numpy.multiply(dotPi, avector)

    # get the new pi-vector
    piNew = tempVector + dotArticle

    # compute the change
    deltas = piNew - pivector

    # check if the change in any tau is less than the epsilon constant
    converged = True
    for tau in deltas:
        converged = converged and (tau < epsilonConst)

    # leave the loop if true
    if converged:
        break

    # if change is greater than epsilon constant,
    # set pi-vector to the new pi-vector and increase interation
    pivector = piNew
    iteration = iteration + 1

# loop is finished
# compute the eiganfactor
eiganfactor = (100 * (numpy.dot(rawMatrix, pivector)/numpy.sum(numpy.dot(rawMatrix, pivector))))

# woohoo!
print('Iterations until converged: ' + str(iteration))
print('--------------------------------------')

print('Returned pi-vector:')
print(pivector)
print('--------------------------------------')

print('Eiganfactors: ')
print(eiganfactor)
print('--------------------------------------')
