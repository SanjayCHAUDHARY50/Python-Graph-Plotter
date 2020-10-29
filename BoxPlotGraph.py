def BoxPlotGraph():
    import matplotlib.pyplot as plt

    labels = []
    value1 = []
    value2 = []
    value3 = []
    value4 = []
    c = 0
    print('Now Enter the', 4, 'labels like C++,Java,Python.etc :-')
    for i in range(0, 4):
        c += 1
        k = input("Label Name :- ")
        labels.append(k)
        if c==1:
            r = int(input("Enter number of elements you want to add in 1st label : "))
            print('Now Enter the', r, 'elements :-')
            for i in range(0, r):
                ele = float(input())

                value1.append(ele)
        elif c==2:
            r = int(input("Enter number of elements you want to add in 2nd label : "))
            print('Now Enter the', r, 'elements :-')
            for i in range(0, r):
                ele = float(input())

                value2.append(ele)
        elif c==3:
            r = int(input("Enter number of elements you want to add in 3rd label : "))
            print('Now Enter the', r, 'elements :-')
            for i in range(0, r):
                ele = float(input())

                value3.append(ele)
        elif c==4:
            r = int(input("Enter number of elements you want to add in 4th label : "))
            print('Now Enter the', r, 'elements :-')
            for i in range(0, r):
                ele = float(input())

                value4.append(ele)

    box_plot_data = [value1, value2, value3, value4]
    plt.boxplot(box_plot_data, patch_artist=True,labels=labels)
    plt.show()

