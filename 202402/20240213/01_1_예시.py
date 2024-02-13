top = -1
stack = [0]*100
icp = {'(':3,'+':1,'-':1,'*':2,'/':2}
isp = {'(':0,'+':1,'-':1,'*':2,'/':2}

fx = '(6+5*(2-8)/2)'
postfix = ''
for tk in fx:
    if tk == '(' or (tk in '+-*/' and isp[stack[top]] < icp[tk]):
        top += 1
        stack[top] = tk
    elif tk in '+-*/' and isp[stack[top]] >= icp[tk]:
        while isp[stack[top]] >= icp[tk]:
            top -= 1
            postfix += stack[top+1]
        top += 1
        stack[top] = tk
    elif tk == ')':
        while stack[top] != '(':
            top -= 1
            postfix += stack[top + 1]
        top -= 1
    else:
        postfix += tk

print(postfix)
