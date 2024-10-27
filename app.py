import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from shiny import render

import palmerpenguins  # This package provides the Palmer Penguins dataset

# Add a sidebar
with ui.sidebar(position="left", bg="#f8f8f8", open="open"):  
    ui.h2("Sidebar") # Sidebar header
    # Insert Drop-Down menu
    ui.input_selectize(
        id="selected_attribute",
        label="Selected Attribute",
        choices=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    ) 
    # Insert Numeric Input field
    ui.input_numeric(
        id="plotly_bin_count",
        label="Bin Count (Plotly)",
        value=5
    )
    #Insert a slider input
    ui.input_slider(
        id="seaborn_bin_count",
        label="Bin Count (Seaborn)",
        min=3, max=21, value=7)
    
    #Insert checkbox filter
    ui.input_checkbox_group(
        id="selected_species_list",
        label="Species",
        choices=["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
        inline=False
    )
    #Inster a dividing line
    ui.hr() 
    #Insert a link
    ui.a("Source code on GitHub", href="https://github.com/matthewpblock/cintel-02-data/tree/main", target="_blank")

"Main content"  

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Matt's Penguin Block", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")

   
