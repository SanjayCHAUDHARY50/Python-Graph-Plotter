def ScatterPlot():
    import matplotlib.pyplot as plt

    x = []
    y = []
    r = int(input("Enter number of elements you want to add : "))
    print('Now Enter the X and Y Coordinates of elements :-')
    for i in range(0, r):
        ele = float(input())
        k = float(input())
        y.append(k)
        x.append(ele)
    plt.scatter(x, y)
    plt.show()