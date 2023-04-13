import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

from matplotlib import pyplot as plt
import numpy as np
import math 
#needed for definition of pi
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')

fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly(fig)
py.iplot(plotly_fig)