import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler

def apply_seazen_theme():
    plt.style.use('default')
    sns.set_style("whitegrid")

    plt.rcParams.update({
        # Figure settings
        'figure.figsize': (4, 4),
        'figure.facecolor': 'white',

        # Font settings
        'font.size': 10,
        'font.family': 'Avenir',
        'font.sans-serif': ['Overpass', 'Helvetica', 'Helvetica Neue', 'Arial', 'Liberation Sans', 'DejaVu Sans', 'Bitstream Vera Sans', 'sans-serif'],

        # Axes settings
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'axes.titlelocation': 'left',
        'axes.titlepad': 15,
        'axes.titleweight': 'bold',
        # 'axes.titlecolor': '#031D25',
        'axes.titlecolor': '#4f5d75',
        'axes.labelpad': 10,
        'axes.linewidth': 0,
        'axes.edgecolor': 'gray',
        'axes.facecolor': '#E5E5E5',
        'axes.prop_cycle': cycler(color=['#118ab2', '#ef476f', '#ffd166', '#06d6a0', '#073b4c']),

        # Tick settings
        'xtick.color': 'black',
        'ytick.color': 'black',
        'xtick.major.size': 3,
        'ytick.major.size': 3,
        'xtick.major.width': 0.5,
        'ytick.major.width': 0.5,
        'xtick.major.pad': 3,
        'ytick.major.pad': 3,
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'xtick.bottom': True,
        'ytick.left': True,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,

        # Grid settings
        'grid.color': 'white',
        'grid.linestyle': '-',
        'grid.linewidth': 1,
        'grid.alpha': 0.5,

        # Patch settings (for histogram and bar plots)
        'patch.edgecolor': 'none',
        'patch.force_edgecolor': False,

        # Boxplot settings
        'boxplot.flierprops.linewidth': 0.5,
        'boxplot.boxprops.linewidth': 0.5,
        'boxplot.whiskerprops.linewidth': 0.5,
        'boxplot.capprops.linewidth': 0.5,
        'boxplot.medianprops.linewidth': 0.5,

        # Error bar settings
        'errorbar.capsize': 0.4,
        'lines.linewidth': 1,
        'lines.solid_capstyle': 'round',

        # SVG settings
        'svg.fonttype': 'none',
    })
