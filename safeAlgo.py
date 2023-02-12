n = int(input("Enter No of Processes"))
pr = []
for i in range(n):
    print("Enter Process no ",i+1)
    prno = input()
    pr.append(prno)
    print(pr)

    # Taking Allo
    print("Allocation for A B C for Process",pr[0])
    pr = list(map(int,input().split(' ')))
