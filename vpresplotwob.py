import matplotlib as mpl

mpl.rc('text', usetex = True, color='w')
mpl.rc('font', family = 'serif')
mpl.rc('figure', figsize=(8, 6))
mpl.rc('xtick', labelsize=18, c='w')
mpl.rc('ytick', labelsize=18, c='w')
mpl.rc('axes', ec='w', titlesize=24, labelsize=20, labelcolor='w')
mpl.rc('legend', fontsize=18, frameon=False)
mpl.rc('savefig', transparent=True)