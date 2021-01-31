def solve(s):
    ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alps = 'abcdefghijklmnopqrstuvwxyz'

    # s=input()
    orig_s=s
    from collections import deque
    q=deque(list(s))
    top=''
    tail=''
    while q:
        if q[0]=='_':
            q.popleft()
            top+='_'
        else:
            break
    while q:
        if q[-1]=='_':
            q.pop()
            tail+='_'
        else:
            break

    s=''.join(list(q))
    if s=='' or '__' in s:
        return orig_s

    s=s.lstrip('_')
    s=s.rstrip('_')
    sl=s.split('_')

    if not s[0] in alps:
        return orig_s

    # print(sl)

    if len(sl)==1:
        if not sl[0][0] in alps:
            return orig_s
        ans=''
        qs=sl[0]
        for si in qs:
            if si in ALPS:
                ans+='_'
                ans+=si.lower()
            else:
                ans+=si
        return top+ans+tail



    for sii in orig_s:
        if sii in ALPS:
            return orig_s

    ans=''
    for i,si in enumerate(sl):
        if not si[0] in alps:
            return orig_s

        if i!=0:
            ans+=si[0].upper()
            ans+=si[1:]
        else:
            ans+=si

    return top+ans+tail


# from random import choice
# CS = 'abcABC012__'
# for i in range(100000):
#     s=''
#     for _ in range(10):
#         s+=choice(CS)
#     if s!=solve(s) and len(s)>len(solve(s)):
#         print(s)
#         print(solve(s))
#         print('-----')

s=input()
print(solve(s))