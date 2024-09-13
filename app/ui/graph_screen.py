# ui/graph_screen.py

"""
WeightWise Graph Screen

Display weight logs and analysis results in graphical format.
"""

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import matplotlib.pyplot as plt
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

class GraphScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Initialize Matplotlib Figure
        self.figure = plt.Figure()
        self.plot = self.figure.add_subplot(1, 1, 1)
        
        # Create a FigureCanvasKivyAgg widget for Matplotlib
        self.canvas = FigureCanvasKivyAgg(self.figure)
        self.add_widget(self.canvas)
        
        # Add a label to show additional information
        self.info_label = Label(text="Weight Progress Graph")
        self.add_widget(self.info_label)

    def update_graph(self, dates, weights):
        """
        Update the graph with new data.
        
        :param dates: List of dates for x-axis
        :param weights: List of weights for y-axis
        """
        self.plot.clear()
        self.plot.plot(dates, weights, marker='o')
        self.plot.set_xlabel('Date')
        self.plot.set_ylabel('Weight (kg)')
        self.plot.set_title('Weight Progress Over Time')
        self.figure.tight_layout()
        self.canvas.draw()
