# ui/home_screen.py

"""
WeightWise Home Screen

Provide navigation and an overview of the application features.
"""

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Title label
        self.title = Label(text="WeightWise", font_size=32, size_hint_y=0.2)
        self.add_widget(self.title)
        
        # Navigation buttons
        self.log_button = Button(text="Log Weight", size_hint_y=0.2)
        self.add_widget(self.log_button)

        self.graph_button = Button(text="View Progress", size_hint_y=0.2)
        self.add_widget(self.graph_button)

        self.settings_button = Button(text="Settings", size_hint_y=0.2)
        self.add_widget(self.settings_button)

        # Status or information label
        self.status_label = Label(text="Welcome to WeightWise!", size_hint_y=0.2)
        self.add_widget(self.status_label)
