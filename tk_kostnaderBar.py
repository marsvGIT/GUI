
"""
# Matplotlib - BarPlot
https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm
https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
@author: Administrator
"""
from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
# window
window = Tk()
window.title("Bar plot")
window.geometry('800x500')

## ------fig --------------------------------------------
def plot():

 # the figure that will contain the plot 
 fig = Figure(figsize = (5, 5), 
                 dpi = 100
# adding the subplot 
  plot1 = fig.add_subplot(111)


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
hem =     ['lgh', 'grg', 'el','lån', 'inter','mat','Pud', 'fsk','bil']
hemKost = [4860,   1040, 420,  7787, 200,    5000,  2500, 1111,  5528]
ax.bar(hem,hemKost)
plt.xticks(rotation=45)
ax.set_title('tot ' + str(sum(hemKost)))
plt.show()
plt.xticks(rotation=45)
plt.show()
## --------------------------------------------------
window.mainloop()














































