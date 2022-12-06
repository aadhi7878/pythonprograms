n=int(input("enter the numbers count :"))
a=[]
for i in range(n):
    p=int(input("enter the number"))
    a.append(p)
def insertionSort(a,n):

    for step in range(1,n):
        key = a[i]
        j = i-1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        a[j + 1] = key
insertionSort(a,n)
print(a)    

