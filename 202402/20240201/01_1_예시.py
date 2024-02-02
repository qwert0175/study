# 비정렬 순차검색

def sequential_search(a,n,key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1
    if i < n:
        return i
    else:
        return -1
    
# 정렬 순차검색

def sequential_search2(a,n,key):
    i = 0
    while i < n and a[i] < key:
        i = i + 1
    if i < n and a[i] == key:
        return i
    else:
        return -1
    
# 이진검색

def binary_search(a,n,key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

# 선택정렬

def selection_sort(a,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

# 셀렉션 알고리즘
        
def select(a,k):
    for i in range(k):
        min_idx = i
        for j in range(i+1,len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[k-1]