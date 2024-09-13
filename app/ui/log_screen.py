# ui/log_screen.py

"""
WeightWise Log Screen

Allow users to log their weight manually.
"""

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class LogScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Weight input
        self.weight_label = Label(text="Enter your weight (kg):")
        self.add_widget(self.weight_label)
        
        self.weight_input = TextInput(multiline=False, input_filter='float', size_hint_y=0.2)
        self.add_widget(self.weight_input)
        
        # Submit button
        self.submit_button = Button(text="Submit", size_hint_y=0.2)
        self.submit_button.bind(on_press=self.submit_weight)
        self.add_widget(self.submit_button)

        # Status or information label
        self.status_label = Label(text="Log your weight to track progress.", size_hint_y=0.2)
        self.add_widget(self.status_label)
        
    def submit_weight(self, instance):
        """
        Handle weight submission and show confirmation popup.
        """
        weight = self.weight_input.text
        if weight:
            # Here you should include the logic to save the weight log
            self.show_popup("Success", "Weight logged successfully!")
        else:
            self.show_popup("Error", "Please enter a valid weight.")
        
    def show_popup(self, title, message):
        """
        Display a popup message.
        """
        layout = BoxLayout(orientation='vertical')
        label = Label(text=message)
        ok_button = Button(text="OK")
        layout.add_widget(label)
        layout.add_widget(ok_button)
        
        popup = Popup(title=title, content=layout, size_hint=(0.6, 0.4))
        ok_button.bind(on_press=popup.dismiss)
        popup.open()
