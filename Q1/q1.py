def main():
    import numpy as np
    arr=np.array([[1,2],[3,4]])
    #print(arr)
    w,v=np.linalg.eig(arr)
    d=np.linalg.det(arr)    
    print("Eigenvalues?: ",w)
    print("Eigenvectors?:\n",v)
    print("Determinant?: ",d)

    vec1=np.array([1,2,3])
    vec2=np.array([4,5,6])
    c=np.cross(vec1,vec2)
    print("Cross product?: ",c)

    A=np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b=np.array([-15,-21,18])
    x=np.linalg.solve(A,b)
    print("Solution?: ",x)    



if __name__ == '__main__':
    main()
