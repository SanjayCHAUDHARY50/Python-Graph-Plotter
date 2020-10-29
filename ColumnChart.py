def ColumnChart():
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize = (10, 5))
    x = []
    y = []
    r = int(input("Enter number of elements you want to add : "))
    print('Now Enter the', r, 'elements like Students names.etc :-')
    for i in range(0, r):
        ele = input()

        x.append(ele)

    print('Now Enter the values of', r, 'elements one by one:-')
    for i in range(0, r):
        k = float(input())

        y.append(k)
    plt.bar(x, y, color='maroon',
            width=0.4)
    plt.show()
