def Histogram():
    import matplotlib.pyplot as plt
    x = []
    n = int(input('Enter the bins range :- '))
    r = int(input("Enter number of elements you want to add : "))
    print('Now Enter the',r,'elements :-')
    for i in range(0, r):
        ele = float(input())

        x.append(ele)
    plt.hist(x, bins=n)
    plt.show()
