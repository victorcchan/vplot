import matplotlib as mpl

mpl.rc('text', usetex = True, color='k')
mpl.rc('font', family = 'serif')
mpl.rc('figure', figsize=(8, 6))
mpl.rc('xtick', labelsize=18, c='k')
mpl.rc('ytick', labelsize=18, c='k')
mpl.rc('axes', ec='k', titlesize=24, labelsize=20, labelcolor='k')
mpl.rc('legend', fontsize=18)
mpl.rc('savefig', transparent=True)