# def sortlines(file):
#     try:
#         with open(file,"r") as f:
#             l=[]
#             for line in f:
#                 l.append(line.strip("\n"))
#                 l.sort()
#                 print(l)
#     except FileNotFoundError as e:
#         print(e)
# try:
#     sortlines("aa.txt")
# except:
#     print("give correct parameters")

with open('aadhi.txt',"r") as f:
    # print(f.read())
    print("gap")
    print(f.readline())
    print("gap")
    # print(f.readlines())
    # for  i in (f.readlines()):
    #     print(i)
