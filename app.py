from shiny.express import input, render, ui
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

result_df=pd.read_csv("years35curve.csv")

data = {
     '1Y': 4.1, '2Y': 4.3, '3Y': 4.5, '4Y': 4.7, 
    '5Y': 4.8, '6Y': 4.9, '7Y': 5.0, '8Y': 5.1
}

#df = pd.DataFrame(data)

def create_line_plot():
    target_date=input.date().strftime('%m/%d/%Y')
    #target_date=input.date()
    target_row = result_df[result_df['Date'] == target_date]
    print(target_row)
    x = list(['1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','30 Yr'])
    y = list(target_row[x].values[0])
    print("xxx")
    print(x)
    print(y)
    print("yyy")
    fig, ax = plt.subplots()
    #fig.title("Yield Curve")
    ax.bar(x, y)
    ax.set_xlabel("Maturity")
    ax.yaxis.set_label_text("Yield (%)")
    #ax.set_ylim(bottom=3)  # Ensures the y-axis starts at 0 # Ensures the y-axis starts at 0
    return fig
@render.text
def value():
    return input.date()
@render.plot
def my_plot():
    return create_line_plot()

ui.input_date("date", "Select Date", value="2019-10-01")

#d