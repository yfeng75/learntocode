# jabber = open("sample.txt",'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line,end='')
    
# jabber.close()

# with open("sample.txt",'r') as jabber:
#     for lines in jabber:
#         if "JAB" in lines.upper():
#             print(lines,end='')

# with open('sample.txt','r') as jabber:
#     line=jabber.readline()
#     while line:
#         print(line,end='')
#         line = jabber.readline()

# with open('sample.txt','r') as jabber:
#     lines=jabber.readlines()
# print(lines)

# for line in lines:
#     print(line,end='')

# with open('sample.txt','r') as jabber:
#     lines=jabber.readlines()
# print(lines)

# for line in lines[::-1]:
#     print(line,end='')

with open('sample.txt','r') as jabber:
    lines=jabber.read()
print(lines)

for line in lines[::-1]:
    print(line,end='')   



   