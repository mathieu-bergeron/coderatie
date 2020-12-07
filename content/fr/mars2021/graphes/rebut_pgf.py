
plt.rcParams.update({
    "font.family": "serif",  
    "font.serif": ["Times", "Times New Roman", "times"],
    "text.usetex": True,     # use inline math for ticks
    "pgf.rcfonts": False,    # don't setup fonts from rc parameters
    "pgf.preamble": [
        "\\usepackage{times}",
        #"\\setmainfont{times}",  # serif font via preamble
        #"\\usepackage{unicode-math}",   # unicode math setup
    #    r"\setmathfont{xits-math.otf}",
    ]
})
