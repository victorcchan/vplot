import matplotlib as mpl

mpl.rc('text', usetex = True, color='k')
mpl.rc('font', family = 'serif')
mpl.rc('figure', figsize=(10, 7.5))
mpl.rc('lines', lw=4, markersize=12)
mpl.rc('xtick', labelsize=24, c='k')
mpl.rc('ytick', labelsize=24, c='k')
mpl.rc('axes', ec='k', titlesize=32, labelsize=28, labelcolor='k')
mpl.rc('legend', fontsize=24)
mpl.rc('savefig', transparent=True)