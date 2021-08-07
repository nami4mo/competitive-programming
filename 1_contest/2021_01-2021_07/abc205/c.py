a,b,c=map(int, input().split())
if c%2==0:c=2
else: c=1
if pow(a,c)>pow(b,c):print('>')
if pow(a,c)<pow(b,c):print('<')
if pow(a,c)==pow(b,c):print('=')

# a,b,c=map(int, input().split())
# if a==0 and b==0:
#     print('=')

# elif a==0 and b!=0:
#     if b>0 or (b<0 and c%2==0):
#         print('<')
#     else:
#         print('>')

# elif a!=0 and b==0:
#     if a>0 or (a<0 and c%2==0):
#         print('>')
#     else:
#         print('<')   

# #-----
# if a>0 and b>0:
#     if a>b:
#         print('>')
#     elif a<b:
#         print('<')
#     else:
#         print('=')

# elif a<0 and b<0:
#     if c%2==1:
#         if a>b:
#             print('>')
#         elif a<b:
#             print('<')
#         else:
#             print('=')
#     else:
#         if a<b:
#             print('>')
#         elif a>b:
#             print('<')
#         else:
#             print('=')

# elif a>0 and b<0:
#     if c%2==1:
#         print('>')
#     else:
#         if abs(a)>abs(b):
#             print('>')
#         elif abs(a)<abs(b):
#             print('<')
#         else:
#             print('=')

# elif a<0 and b>0:
#     if c%2==1:
#         print('<')
#     else:
#         if abs(a)>abs(b):
#             print('>')
#         elif abs(a)<abs(b):
#             print('<')
#         else:
#             print('=')