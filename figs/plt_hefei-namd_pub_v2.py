#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

mpl.use('agg')

def PubNum(x, a):
    return a * (x - 2016)**2 + 1


# from matplotlib import font_manager
#
# fontP = font_manager.FontProperties()
# fontP.set_family('SimHei')
# fontP.set_size(14)

# plt.style.use('ggplot')
# plt.style.use('dark_background')

pub_year = np.arange(2016, 2025)
pub_nums = np.array([1, 3, 7, 12, 16, 26, 39, 54, 15])

o, v = curve_fit(PubNum, pub_year[:-1], pub_nums[:-1])

# x0 = np.linspace(pub_year.min(), pub_year.max(), 300)
x0 = np.linspace(pub_year.min(), 2024, 300)
# fx = interp1d(pub_year, pub_nums, kind='quadratic')
y0 = PubNum(x0, *o)

figure = plt.figure(
    # figsize=(4.0, 6.0),
    figsize=(5.4, 3.2),
    dpi=300,
)
ax = plt.subplot()

ax.grid('on', which='both',
        ls='--', lw=0.5,
        color='gray', alpha=0.5,
        zorder=-100)

ax.xaxis.set_minor_locator(AutoMinorLocator(n=2))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=2))

ax.plot(pub_year, pub_nums, ls='none',
        marker='h', color='b',
        mew=1.5, mfc='w', ms=8,
        zorder=2,
        label='Raw Data')
ax.plot(x0, y0, ls='-', lw=10.0, color='gray', alpha=0.4,
        zorder=1,
        label='Quadratic Fitting')
ax.plot([2024], [15],
        marker='*', color='r',
        mew=0.8, mfc='w', ms=20)

ax.legend(loc='upper left')

for ii in range(pub_year.size):
    px = pub_year[ii] - 0.1
    py = pub_nums[ii] + 2.0
    ax.text(px, py, '{}'.format(pub_nums[ii]),
            ha="right",
            va="bottom",
            fontsize='x-small',
            # family='monospace',
            fontweight='bold',
            color='tab:red',
            transform=ax.transData
            # bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    )
    


ax.tick_params(which='both', labelsize='medium')
ax.tick_params(axis='x', labelrotation=0)

ax.set_xlim(2015.5, 2024.5)
ax.set_ylim(-2, 60)

ax.set_xticks(np.arange(2016, 2025, 2))



ax.set_xlabel(r'Year', labelpad=5, fontsize='large')
ax.set_ylabel(r'No. of Publications', labelpad=10, fontsize='large')

plt.tight_layout()
plt.savefig('hefei-namd_pub_v2.pdf')
plt.savefig('hefei-namd_pub_v2.png')

from subprocess import call
call('feh -xdF hefei-namd_pub_v2.png'.split())

# plt.show()
