def enq(n):
    global last
    last += 1
    h[last] = n
    c = last
    p = c // 2
    while p and h[p] < h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = h[1]
    h[1] = h[last]
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c + 1 <= last and h[c] < h[c+1]:
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp

N = 10
h = [0]*(N+1)
last = 0

enq(2)
enq(5)
enq(3)
enq(6)
enq(4)

print(h)

while last:
    print(deq())