import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
from cycler import cycler

def apply_seazen_theme():
    plt.style.use('default')
    sns.set_style("whitegrid")
    
    # Rebuild font cache to ensure JetBrains Mono is detected
    try:
        fm.fontManager.__init__()
    except:
        pass  # If rebuild fails, continue anyway

    # Extended color palette (original 5 + 5 new colors)
    extended_colors = [
        '#118ab2',  # Ocean blue (original)
        '#ef476f',  # Pink/red (original) 
        '#ffd166',  # Golden yellow (original)
        '#06d6a0',  # Mint green (original)
        '#073b4c',  # Dark navy (original)
        '#8b5cf6',  # Purple
        '#00bbf9',  # Sky blue
        '#778da9',  # Blue gray
        '#f59e0b',  # Amber
        '#6366f1'   # Indigo
    ]

    plt.rcParams.update({
        # Figure settings
        'figure.figsize': (4, 4),
        'figure.facecolor': 'white',

        # Font settings
        'font.size': 10,
        'font.family': 'JetBrains Mono',
        'font.sans-serif': ['JetBrains Mono', 'Overpass', 'Helvetica', 'Helvetica Neue', 'Arial', 'Liberation Sans', 'DejaVu Sans', 'Bitstream Vera Sans', 'sans-serif'],

        # Axes settings
        'axes.labelsize': 14,
        'axes.titlesize': 18,
        'axes.titlelocation': 'left',
        'axes.titlepad': 15,
        'axes.titleweight': 'bold',
        'axes.titlecolor': '#495057',
        'axes.labelcolor': '#495057',
        'axes.labelpad': 10,
        'axes.linewidth': 0,
        'axes.edgecolor': 'gray',
        'axes.facecolor': 'white',
        'axes.prop_cycle': cycler(color=extended_colors),
        'axes.spines.left': False,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'axes.spines.bottom': False,
        'axes.grid': True,
        'axes.grid.axis': 'y',

        # Tick settings
        'xtick.color': '#495057',
        'ytick.color': '#495057',
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
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,

        # Grid settings
        'grid.color': '#E0E0E0',
        'grid.linestyle': '-',
        'grid.linewidth': 0.8,
        'grid.alpha': 0.7,

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
