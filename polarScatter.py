# https://stackoverflow.com/questions/40852861/hide-radial-tick-labels-matplotlib

# https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/polar_scatter.html#sphx-glr-gallery-pie-and-polar-charts-polar-scatter-py
# ------------------------------------------

# =============================================================================
# Scatter plot on polar axis¶
# Size increases radially in this example and color increases with angle (just to verify the symbols are being scattered correctly).
# =============================================================================


import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute areas and colorshttps://stackoverflow.com/questions/40852861/hide-radial-tick-labels-matplotlib
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

ax.set_yticklabels([])
ax.set_theta_zero_location('E')

c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75, linewidth=5)