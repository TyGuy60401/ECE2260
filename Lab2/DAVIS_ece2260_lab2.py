import numpy as np

def det_2x2(A):
    detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    return detA

def det_3x3(A):
    detA = 0
    for i in range(3):
        myList = [0, 1, 2]
        myList.pop(i)
        n = myList[0]
        m = myList[1]
        subA = np.array([[A[1][n], A[1][m]],
                         [A[2][n], A[2][m]]])
        detA += A[0][i]*det_2x2(subA) * ( (i%2==0) *2-1)
    return detA

def cramer_2x2(A, b):
    # To do
    subX = np.array([[b[0], A[0][1]],
                     [b[1], A[1][1]]])
    subY = np.array([[A[0][0], b[0]],
                     [A[1][0], b[1]]])
    
    x = np.array([det_2x2(subX)/det_2x2(A), 
                  det_2x2(subY)/det_2x2(A)])
    return x

def cramer_3x3(A, b):
    return

def main():
    # Set up a 2x2 array
    A = np.array([[1., 2.],
                  [3., 4.]])
    b = np.array([5., 6.])
    A3 = np.array([[1., 2., 3.],
                   [4., 5., 6.],
                   [7., 8., 9.]])
    print("Cramer's test:\n", cramer_2x2(A, b), '\n', sep='')
    print("3x3 Test:\n", det_3x3(A3), sep='')

if __name__ == '__main__':
    main()