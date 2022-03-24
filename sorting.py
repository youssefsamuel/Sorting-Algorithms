import random
import time
import sys
sys.setrecursionlimit(2000)
def quicksort(x):
    lo = 0
    hi = len(x) - 1
    quicksort2(x, lo, hi)

def quicksort2(x, low, high):
    if low < high:
        pivotIndex=partition(x,low,high)
        quicksort2(x,low,pivotIndex-1)
        quicksort2(x,pivotIndex+1,high)

def partition(x, low, high):
    i=low # i will be used to represent the index of the first element higher than the pivot, in the beginning initialized to the first element in the given array.
    randIndex=random.randint(low,high)
    pivot=x[randIndex]
    x[high],x[randIndex]=x[randIndex],x[high]
    for j in range(low,high): #compare elements with pivot, if the element is lower than the pivot swap it with the first element higher than the pivot.
        if x[j]<=pivot:
            x[i],x[j]=x[j],x[i] 
            i+=1 #increment i to be the index of the first element higher than the pivot.
    x[i],x[high]=x[high],x[i] 
    return i #correct position of the pivot in the sorted array.

def mergeSort(x):
    n = len(x)
    lo = 0
    hi = n-1
    x = mergeSort2(x, lo, hi)

def mergeSort2(x, lo, hi):
    if lo >= hi:
        return
    mid = int((lo+hi) / 2)
    mergeSort2(x, lo, mid)
    mergeSort2(x, mid+1, hi)        
    if x[mid] < x[mid+1]:
        return
    merge(x, lo, mid, hi)

def merge(x, lo, mid, hi):
    n = hi - lo + 1
    a = [0] * n
    i = lo
    j = mid+1
    k = lo
    for h in range(0, n):
        a[h] = x[h+lo]
    while i <= mid and j <= hi:
        if a[i-lo] <= a[j-lo]:
            x[k] = a[i-lo]
            k += 1
            i += 1
        else:
            x[k] = a[j-lo]
            k += 1
            j += 1
    while i <= mid:
        x[k] = a[i-lo]
        k += 1
        i += 1
    while j <= hi:
        x[k] = a[j-lo]
        k += 1
        j += 1 

def hybridMergeSort(x, THRESHOLD):
    n = len(x)
    lo = 0
    hi = n-1
    x = hybridMergeSort2(x, lo, hi, THRESHOLD)

def hybridMergeSort2(x, lo, hi, THRESHOLD):
    if lo >= hi:
        return
    if hi-lo+1 <= THRESHOLD:
        selectionSort2(x, lo, hi)
        return;    
    mid = int((lo+hi) / 2)
    hybridMergeSort2(x, lo, mid, THRESHOLD)
    hybridMergeSort2(x, mid+1, hi, THRESHOLD)        
    if x[mid] < x[mid+1]:
        return
    merge(x, lo, mid, hi)

def selectionSort2(x, lo, hi):
    for i in range(lo, hi):
        imin = i
        for j in range(i+1, hi+1):
            if x[j] < x[imin]:
                imin = j
        x[i], x[imin] = x[imin], x[i]        
  
def insertionSort(x):
    n = len(x)
    for i in range(1, n):
        hole = i
        key = x[i]
        while hole > 0 and x[hole-1] > key:
            x[hole] = x[hole-1]
            hole = hole - 1
        x[hole] = key    

def selectionSort(x):
    n = len(x)
    for i in range(0, n-1):
        imin = i
        for j in range(i+1, n):
            if x[j] < x[imin]:
                imin = j
        x[i], x[imin] = x[imin], x[i]        

def bubbleSort(x):
    sorted = False
    p = 1
    i = 0
    n = len(x)
    while p < n and not sorted:
        sorted = True
        for i in range(0, n-p):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                sorted = False
        p = p+1 

def smallest(x, k):
    n = len(x)
    if k >= n:
        print("k must be smaller than the size of the array")
        return
    lo = 0
    hi = n-1    
    while True:
        q = partition(x, lo, hi)
        if q == k:
            return x[q]
        elif q < k:
            lo = q+1
        elif q > k:
            hi = q-1
        if lo == hi:
            return x[lo]    

def main():
    sortingName = ["Quick Sort"," Hybrid Merge Sort", "Normal Merge Sort", "Selection Sort", "Insertion Sort", "Bubble Sort"]
    n = [1000, 5000, 10000, 50000, 100000]
    for i in range(0, len(n)):
        print(f"Array size = {n[i]}: \n")
        x = [0]*n[i]
        for p in range(0, n[i]):
            x[p] = random.randint(-50000,50000)
        for k in range(0, 6):
            copy = [0] * len(x)
            for b in range(0, len(x)):
                copy[b] = x[b]
            begin = time.time()
            if k == 0:
                quicksort(copy)
            elif k == 1:
                hybridMergeSort(copy, 7)
            elif k == 2:
                mergeSort(copy)
            elif k == 3:
                selectionSort(copy)
            elif k == 4:
                insertionSort(copy)   
            else:
                bubbleSort(copy)             
            end = time.time()
            print(f"Running time for {sortingName[k]} is {(end-begin)*1000} ms\n")
            
main()



