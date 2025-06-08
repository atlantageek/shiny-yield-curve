from shiny.express import input, render, ui
import matplotlib.pyplot as plt
import numpy as np



data = {
    "Maturity": ['1Y', '2Y', '3Y', '4Y', '5Y', '6Y', '7Y', '8Y'],
    "Yield": [4.1, 4.3, 4.5, 4.7, 4.8, 4.9, 5.0, 5.1]
}
data=np.array([data["Maturity"], data["Yield"]])
#df = pd.DataFrame(data)
print(data[1])
def create_line_plot():
    x = data[0]
    y = data[1]
    fig, ax = plt.subplots()
    #fig.title("Yield Curve")
    ax.bar(x, y)
    ax.set_xlabel("Maturity")
    ax.yaxis.set_label_text("Yield (%)")
    ax.set_ylim(bottom=0)  # Ensures the y-axis starts at 0 # Ensures the y-axis starts at 0
    return fig

@render.plot
def my_plot():
    return create_line_plot()
