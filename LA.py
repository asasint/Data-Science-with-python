# import necessary modules 
from scipy import sparse 
# Row-based linked list sparse matrix 
A = sparse.lil_matrix((1000, 1000)) 
print(A) 
  
A[0,:100] = np.random.rand(100) 
A[1,100:200] = A[0,:100] 
A.setdiag(np.random.rand(1000)) 
print(A) 
