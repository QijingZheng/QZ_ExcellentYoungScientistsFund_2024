#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import matplotlib as mpl
mpl.use('agg')

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# from matplotlib import font_manager
#
# fontP = font_manager.FontProperties()
# fontP.set_family('SimHei')
# fontP.set_size(14)

# plt.style.use('ggplot')
# plt.style.use('dark_background')

pub_year = np.arange(2016, 2025)
pub_nums = np.array([1, 3, 7, 12, 16, 26, 37, 53, 15])

# x0 = np.linspace(pub_year.min(), pub_year.max(), 300)
x0 = np.linspace(pub_year.min(), 2023, 300)
fx = interp1d(pub_year, pub_nums, kind='quadratic')
y0 = fx(x0)

figure = plt.figure(
    # figsize=(4.0, 6.0),
    figsize=(4.8, 3.6),
    dpi=300,
)
ax = plt.subplot()

# ax.plot(pub_year, pub_nums, '-', color='y', lw=1, zorder=8, alpha=0.8)
# ax.plot(pub_year, pub_nums, ls='none',
#         marker='o', color='b',
#         mew=1.5, mfc='w', ms=7)

ax.plot(x0, y0, '-', color='gold', lw=1, zorder=8, alpha=0.8)
ax.scatter(pub_year, pub_nums,
           s=pub_nums*60,
           c=pub_nums,
           cmap='hot',
           marker='*', 
           # lw=0,
           edgecolor='w',
           # facecolor='w', linewidths=2.5,
           zorder=10,
           # alpha=0.7,
          )

ax.grid('on', ls='--')
ax.tick_params(which='both', labelsize='large')
ax.tick_params(axis='x', labelrotation=30)

ax.set_xlim(2015.5, 2024.5)
ax.set_xticks(np.arange(2016, 2025))

ax.set_ylim(-1, 72)

# ax.set_xlabel(r'年份', labelpad=5, fontsize='large')
# ax.set_ylabel(r'文章数', labelpad=5)

ax.set_xlabel(r'Year', labelpad=10, fontsize='xx-large')
ax.set_ylabel(r'#No', labelpad=10, fontsize='xx-large')

plt.tight_layout()
plt.savefig('hefei-namd_pub.pdf')
plt.savefig('hefei-namd_pub.png')

from subprocess import call
call('feh -xdF hefei-namd_pub.png'.split())

# plt.show()
