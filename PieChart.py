def PieChart():
    import matplotlib.pyplot as plt


    labels = []
    r = int(input("Enter number of labels you want to add : "))
    print('Now Enter the', r, 'labels like C++,Java,Python.etc :-')
    for i in range(0, r):
        ele = input()

        labels.append(ele)
    sizes = []
    print('Now Enter the sizes of', r, 'labels :-')
    for i in range(0, r):
        k = float(input())

        sizes.append(k)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()
