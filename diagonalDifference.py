###########Problem
# Given a square matrix, calculate the absolute difference between the sums of
# its diagonal
# For example, the square matrix is [1,2,3; 4,5,6; 9,8,9]
# The left to right diagonal = 1 + 5 + 9 = 15. The right to left diagonal
#  = 3 + 5+ 9 = 17. Their absolute difference is |15 - 17| = 2

def diagonalDifference(arr):
    leftdiag = rightdiag = 0
    for i in range(n):
        leftdiag += arr[i][i]
        rightdiag += arr[i][n-1-i]

    return abs(leftdiag - rightdiag)



if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)