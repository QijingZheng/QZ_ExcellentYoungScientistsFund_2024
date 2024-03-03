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
pub_nums = np.array([1, 3, 7, 12, 16, 23, 40, 56, 17])

assert pub_nums.sum() == 175

o, v = curve_fit(PubNum, pub_year[:-1], pub_nums[:-1])

# x0 = np.linspace(pub_year.min(), pub_year.max(), 300)
x0 = np.linspace(pub_year.min(), 2025, 300)
# fx = interp1d(pub_year, pub_nums, kind='quadratic')
y0 = PubNum(x0, *o)

################################################################################
fig= plt.figure(
    # figsize=(4.0, 6.0),
    figsize=(7.5, 3.2),
    dpi=300,
    layout='constrained',
)
# # ax = plt.subplot()
# axes = [plt.subplot(1, 2, ii+1) for ii in range(2)]

# plt.subplots_adjust(
#     left=0.08, right=0.86,
#     bottom=0.15, top=0.98,
#     wspace=0.40,
# )

axes = fig.subplot_mosaic(
    [[0, 1]],
    empty_sentinel=-1,
    gridspec_kw=dict(
        height_ratios=[1.0],
        width_ratios=[1.0, 1.5],
        # hspace=0.0,
        wspace=0.04
    )
)

################################################################################
ax = axes[0]

ax.grid('on', which='both',
        ls='--', lw=0.5,
        color='gray', alpha=0.5,
        zorder=-100)

ax.xaxis.set_minor_locator(AutoMinorLocator(n=2))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=2))

ax.plot(pub_year[:-1], pub_nums[:-1], ls='none',
        marker='h', color='b',
        mew=1.5, mfc='w', ms=8,
        zorder=2,
        label='#Pubs')
ax.plot(x0, y0, ls='-', lw=10.0, color='gray', alpha=0.4,
        zorder=1,
        # label='Quadratic Fitting'
        )
ax.plot([2024], [15],
        marker='*', color='r',
        mew=0.4, mfc='r', ms=20)

ax.legend(loc='upper left', fontsize='medium')

for ii in range(pub_year.size):
    px = pub_year[ii] - 0.0
    py = pub_nums[ii] + 3.5
    ax.text(px, py, '{}'.format(pub_nums[ii]),
            ha="center",
            va="bottom",
            fontsize='x-small',
            # family='monospace',
            fontweight='bold',
            color='tab:green',
            transform=ax.transData
            # bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    )
    


ax.tick_params(which='both', labelsize='medium')
ax.tick_params(axis='x', labelrotation=0)

ax.set_xlim(2015.5, 2024.5)
ax.set_ylim(-2, 75)

ax.set_xticks(np.arange(2016, 2025, 2))

ax.set_xlabel(r'Year', labelpad=5, fontsize='large')
ax.set_ylabel(r'Publications', labelpad=5, fontsize='large')
################################################################################
ax = axes[1]

JournalName = []
JournalCnts = []

TotalCnt = 0
with open('journal_couts.txt', 'r') as inp:
    for line in inp.readlines():
        tmp = line.split()
        cc = int(tmp[0])
        TotalCnt += cc
        if cc > 3:
            JournalCnts.append(cc)
            JournalName.append(' '.join(tmp[1:]))

assert TotalCnt == pub_nums.sum()

JournalCnts.append(TotalCnt - np.sum(JournalCnts))
JournalName.append(
r'''
  Sci. Adv. ->  3
  Phys. Rev. Lett. ->  3
  J. Am. Chem. Soc. ->  2
  Adv. Mater. ->  2
  Nanotechnology ->  2
  npj Comput. Mater. ->  1
  PNAS ->  1
  Nat. Commun. ->  1
  Nat. Comput. Sci. ->  1
  $\ldots$
'''
)

explode = np.zeros_like(JournalCnts, dtype=float)
# explode[-1] = 0.1
# print(explode)
patches, texts, pcts = ax.pie(
    JournalCnts,
    labels=JournalName,
    radius=1.0,
    # autopct='%1.1f%%',
    # autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,int(p * TotalCnt/100)),
    autopct=lambda p : '{:,.0f}'.format(int(np.round(p/100*TotalCnt))),
    textprops={'size': 'x-small', 'weight': 'bold'},
    wedgeprops={'linewidth': 0.8, 'edgecolor': 'white'},
    startangle=45,
    explode=list(explode),
)
plt.setp(patches[-1], facecolor='purple')
plt.setp(pcts, color='white', fontweight='bold')
plt.setp(texts, fontweight=600)
for ii, patch in enumerate(patches):
    # if ii < len(JournalName)-1:
    texts[ii].set_color(patch.get_facecolor())
    # if ii == len(JournalCnts) - 1:
    #     texts[ii].set_size(7)

################################################################################

# plt.tight_layout(pad=1.0)
plt.savefig('hefei-namd_pub_v3.pdf')
plt.savefig('hefei-namd_pub_v3.png')

from subprocess import call
call('feh -xdF hefei-namd_pub_v3.png'.split())

# plt.show()
