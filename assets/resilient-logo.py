#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:15:09 2021

@author: fabian
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

x = [0, .5, 1]
y = [0, 0.85, 0]
colors = ['#cddd9c', '#9dd9a4', '#4f759a'] #'#e6efd0'

def add_triangle(ax):
    for i in range(3):
        ax.plot([x[i], x[(i+1)%3]], [y[i], y[(i+1)%3]], c='#e6efd0', zorder=1,
                lw=30, alpha=1)
    ax.scatter(x, y, c=colors, zorder=3, s=10000, edgecolor='white', linewidths=5)
    ax.axis('off')
    ax.set_xlim(-.2, 1.2)
    ax.set_ylim(-.2, 1.)

#%% trianlge only
fig,ax = plt.subplots(1,1, subplot_kw={"projection":ccrs.PlateCarree()}, figsize=(10,10))
add_triangle(ax)

plt.savefig(f'logo.pdf', bbox_inches='tight', transparent=True)
plt.savefig(f'logo.png', bbox_inches='tight', transparent=True, dpi=100)
plt.show()
