from BoxPlotGraph import *
from ScatterPlotGraph import *
from Histogram import *
from ColumnChart import *
from PieChart import *
def getdata():
    global GraphNo
    GraphNo =  int(input('Enter the Series No. of the graph which you want to use for visualization of your Data : \n 1. Histogram \n 2. Column Chart \n 3. Box Plot Chart \n 4. Pie Chart \n 5. Scatter Plot\n :-'))

while(True):
 getdata()
 if GraphNo == 1:
    Histogram()
    break
 elif GraphNo == 2:
    ColumnChart()
    break
 elif GraphNo == 3:
    BoxPlotGraph()
    break
 elif GraphNo == 4:
    PieChart()
    break
 elif GraphNo == 5:
    ScatterPlot()
    break
 else: print("Invalid Input")
