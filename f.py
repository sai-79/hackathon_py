a=input()
print(a)
for i in range(0,len(array2[0])):
  for j in range(0,len(array2[0])):
    if(i==j):
      arr1[i][j]=var(array2,i,rmean)
    elif(i>j):
      arr1[i][j]=cov(i,j,arr2)
      arr1[j][i]=arr1[i][j]
#print(arr1)
    
   rmean=np.zeros(len(array2[0]))
for k in range(0,len(array2[0])):
  for i in range(0,len(array2)):
    rmean[k]+=array2[i][k]
for i in range(0,len(array2[0])):##row mean
  rmean[i]=rmean[i]//len(array2) 
    
    
arr2=np.zeros(len(array2[0])*len(array2)).reshape(len(array2),len(array2[0]))##mean matrix
for i in range(0,len(array2)):
  for j in range(0,len(array2[0])):
    arr2[i][j]=array2[i][j]-rmean[j]




eigenvalues, eigenvectors = eig(arr1)
print("\nEigen values\n")
print(eigenvalues)
print("\neigen vectors\n")
print(eigenvectors)
arr_copy=np.copy(eigenvalues)
#print(arr_copy)
arr_copy.sort()
#print(arr_copy)
slice_eig=list(eigenvalues)
slice_arr=list(arr_copy[5:])
print("\nRequired indices of eigen values\n")
print(slice_arr)
print("\nindices\n")
for i in slice_arr:
  print(slice_eig.index(i))