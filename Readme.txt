This Python application is a scientific visualization tool designed to help users
analyze 2D vector fields. It bridges the gap between abstract mathematical
equations and visual understanding by rendering vector fields in real-time.

It focuses on visualizing Divergence (Scalar Field), which identifies:

"Sources" (Positive flux): Where the field expands or originates.

"Sinks" (Negative flux): Where the field compresses or terminates.

[ KEY FEATURES ]

Symbolic Input: Type mathematical functions directly (e.g., "sin(x) + y")
without writing code.

Interactive Inspection: Hover your mouse over any part of the plot to see
the exact numerical value of Divergence at that coordinate.

Dual Visualization: Combines Quiver plots (arrows showing flow direction)
with Contour plots (color gradients showing flux magnitude).

Dynamic Calculation: Uses numerical differentiation (Finite Difference Method)
to compute derivatives on a 50x50 grid.

[ PREREQUISITES ]
To run this tool, you need Python installed along with the following libraries:

NumPy (for grid generation and gradient calculation)

Matplotlib (for rendering plots and handling mouse events)

SymPy (for parsing string inputs into math functions)

You can install them via pip:
$ pip install numpy matplotlib sympy

[ HOW TO RUN ]

Open your terminal or command prompt.

Navigate to the directory containing the script.

Run the python file:
$ python vector_visualizer.py

[ USAGE GUIDE ]
When the program starts, follow these steps in the console:

Enter Vector Components:
The tool will ask for Fx(x,y) and Fy(x,y).
Use Python/SymPy syntax for mathematical functions:

Addition/Subtraction: +, -

Multiplication: * (e.g., 2x, xy)

Powers: ** (e.g., x**2 for x squared)

Trig functions: sin(x), cos(y), tan(x), exp(x), etc.

Example Inputs:

Scenario          |  Fx Input    |  Fy Input

Simple Source     |  x           |  y
Simple Sink       |  -x          |  -y
Fluid Flow        |  sin(x)      |  cos(y)
Saddle Point      |  x           |  -y

[ INTERACTION ]

The window will open with a dark theme.

The Color Map indicates flux:

Warm Colors (Orange/Yellow) = Positive Divergence (Source)

Cool Colors (Purple/Black)  = Negative Divergence (Sink)

Move your mouse over the plot to see a popup box with exact values.
