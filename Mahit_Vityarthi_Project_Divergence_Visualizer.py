import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.colors as mcolors


plt.style.use('dark_background')

def plot_divergence(X, Y, F_x, F_y):

    Divergence = np.gradient(F_x, (X[1, 0] - X[0, 0]), axis=0) + np.gradient(F_y, (Y[0, 1] - Y[0, 0]), axis=1)

    fig, ax = plt.subplots(figsize=(10, 9))
    
    ax.set_title('DIVERGENCE FIELD\n(Sources & Sinks)', fontsize=14, color='orange', fontweight='bold')
    
 
    max_val = np.max(np.abs(Divergence))
    norm = mcolors.Normalize(vmin=-max_val, vmax=max_val)
    contour = ax.contourf(X, Y, Divergence, levels=50, cmap='plasma', norm=norm, alpha=0.9)
    
    cbar = fig.colorbar(contour, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Divergence Magnitude (∇ · F)', color='white')
    cbar.ax.yaxis.set_tick_params(color='white')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')


    annot = ax.annotate("", xy=(0,0), xytext=(20,20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="black", ec="orange", alpha=0.9),
                        arrowprops=dict(arrowstyle="->", color='orange'), color='white')
    annot.set_visible(False)

    def update_annot(event):
        distances = (X - event.xdata)**2 + (Y - event.ydata)**2
        min_idx = np.unravel_index(np.argmin(distances), X.shape)
        val = Divergence[min_idx]
        annot.xy = (event.xdata, event.ydata)
        annot.set_text(f"Div: {val:.3f}\nPos: ({event.xdata:.2f}, {event.ydata:.2f})")

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            update_annot(event)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        elif vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    step = 3
    ax.quiver(X[::step, ::step], Y[::step, ::step], 
              F_x[::step, ::step], F_y[::step, ::step], 
              pivot='mid', color='white', alpha=0.8)
    
    ax.grid(False)
    ax.axis('off')    
    plt.tight_layout()
    plt.show()


print("VISUALIZER TOOL")
print("----------------")
print("Suggested Cool Inputs for Divergence:")
print("  Fx: sin(x) + x")
print("  Fy: cos(y)")

try:
    while True:
        n = int(input("Enter \n1 for DIVERGENCE: \n2 to exit"))
        
        x_range = (-5, 5)
        y_range = (-5, 5)
        grid_size = 50 

        x = np.linspace(x_range[0], x_range[1], grid_size)
        y = np.linspace(y_range[0], y_range[1], grid_size)
        X, Y = np.meshgrid(x, y, indexing='ij')

        u_str = input("Enter Fx(x,y): ")
        v_str = input("Enter Fy(x,y): ")

        x_sym, y_sym = sp.symbols('x y')
        try:
            fx_func = sp.lambdify((x_sym, y_sym), sp.sympify(u_str), modules='numpy')
            fy_func = sp.lambdify((x_sym, y_sym), sp.sympify(v_str), modules='numpy')

            F_x = fx_func(X, Y)
            F_y = fy_func(X, Y)

            if np.isscalar(F_x): F_x = np.full_like(X, F_x)
            if np.isscalar(F_y): F_y = np.full_like(Y, F_y)

            if n == 1:
                plot_divergence(X, Y, F_x, F_y)
            elif n == 2:
                break
            else:
                print("Invalid input. Please enter 1 or 2.")
        except Exception as e:
            print(f"Error parsing function: {e}")
except ValueError:
    print("Please enter a valid integer.")
except EOFError:
    print("Input stream closed. (If running in a non-interactive preview, hardcode the inputs to test!)")


