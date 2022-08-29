# %% setup
# TODO the preamble needs to be moved to another script file, it needs to be made more flexible, probably by the use of optional arguments, also more seamless
'''
Function to set-up the document preamble as an article and other essentials.
'''
def setup():
    global f
    f=open(title+".tex", "w")
    s="\\documentclass[12pt, a4paper]{article}\n\\usepackage[fleqn]{amsmath}\n\\usepackage{amssymb}\n\\usepackage{fullpage}\n\\usepackage{setspace}\n\\usepackage{tikz}\n\n\\everymath{\\displaystyle}\n\\allowdisplaybreaks\n\\setstretch{2}\n\n\\title{"+title+"}\n\\date{}\n\n\\begin{document}\n\\setlength{\\abovedisplayskip}{0pt}\n\\setlength{\\belowdisplayskip}{0pt}\n\\setlength{\\abovedisplayshortskip}{0pt}\n\\setlength{\\belowdisplayshortskip}{0pt}\n\n\n\\maketitle\n\n"
    f.write(s)

# %% diagram
'''
A function to start a diagram.
'''
def diagram():
    s="\\begin{tikzpicture}"
    f.write(s)

# %% axes
'''
Function to draw 2D co-ordinate axes.
'''
def axes():
    s="\\draw (0,0) -- (5,0);\n\\node[label=below:{x}]at(5, 0){};\n\\draw (0,0) -- (0,5);\n\\node[label=left:{y}]at(0, 5){};\n\\node[label=below:{O}]at(0, 0){};"
    f.write(s)

# %% line
# TODO Option to add arrowhead, options to draw from and angle measurement, a way to let use enter data as arguments or to ask interactively, smartly.
'''
Function to draw a line. Takes no arguments. Asks for input of co-ordinates interactively.
'''
def line():
    sx=float(input("Enter starting position x"))
    sy=float(input("Enter starting position y"))
    ex=float(input("Enter ending position x"))
    ey=float(input("Enter ending position y"))
    s=f"\draw ({sx}, {sy}) -- ({ex}, {ey});"
    f.write(s)

# %% draw
'''
A function to finish a diagram.
'''
def diagram():
    s="\\end{tikzpicture}"
    f.write(s)

# %% finish
'''
Function to close the current document.
'''
def finish():
    f.close()

# %% main
'''
The global variables within the scope of this script are declared here. This part is most likely to change drastically as the development of the project progresses.
'''
title=''