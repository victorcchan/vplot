import matplotlib as mpl

mpl.rc('text', usetex = True, color='w')
mpl.rc('font', family = 'serif')
mpl.rc('figure', figsize=(8, 6))
mpl.rc('xtick', labelsize=24, c='w')
mpl.rc('ytick', labelsize=24, c='w')
mpl.rc('axes', ec='w', titlesize=32, labelsize=28, labelcolor='w')
mpl.rc('legend', fontsize=18, frameon=False)
mpl.rc('savefig', transparent=True)