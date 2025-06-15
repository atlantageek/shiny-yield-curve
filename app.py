from shiny.express import input, render, ui
from shiny import App, reactive
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta,timezone

TIMEZONE = timezone(timedelta(hours=-5))  # Adjust to your timezone if needed
result_df=pd.read_csv("filled_curve.csv").sort_index(axis=0)
print(result_df.head())
data = {
     '1Y': 4.1, '2Y': 4.3, '3Y': 4.5, '4Y': 4.7, 
    '5Y': 4.8, '6Y': 4.9, '7Y': 5.0, '8Y': 5.1
}

#df = pd.DataFrame(data)

def create_line_plot():
    target_date=new_date_text()
    print(target_date)

    #target_date=input.date()
    target_row = result_df[result_df['Date'] == target_date]
    print(target_row)
    x = list(['1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','30 Yr'])
    y = list(target_row[x].values[0])
    fig, ax = plt.subplots()
    #fig.title("Yield Curve")
    ax.bar(x, y)
    ax.set_xlabel("Maturity")
    ax.yaxis.set_label_text("Yield (%)")
    ax.set_ylim(bottom=0,top=10)  # Ensures the y-axis starts at 0 # Ensures the y-axis starts at 0
    return fig


start_date=datetime(1991, 1, 2, 0, 0, tzinfo=TIMEZONE)
end_date=datetime(2024, 12, 31, 0, 0, tzinfo=TIMEZONE)


@reactive.calc
def new_date_text():
    #val = input.monthSlider()
    new_date = input.dateslider()
    reformatted_date= new_date.strftime('%m/%d/%Y')
    return reformatted_date
ui.include_css("styles.css")
with ui.card(full_screen=True):
    ui.card_header("Yield Curve Analysis")
    with ui.card_body():
        @render.text
        def value():
            return new_date_text()
        @render.plot
        def my_plot():
            return create_line_plot()

        ui.input_slider("dateslider","Select Date", min=start_date,max=end_date,value=0,step=7,ticks=True,width="100%", time_format='%m/%d/%Y')
