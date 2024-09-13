# ui/settings_screen.py

"""
WeightWise Settings Screen

Manage user profiles and application settings.
"""

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class SettingsScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # User name input
        self.name_label = Label(text="Name:")
        self.add_widget(self.name_label)
        
        self.name_input = TextInput(multiline=False, size_hint_y=0.2)
        self.add_widget(self.name_input)
        
        # User email input
        self.email_label = Label(text="Email:")
        self.add_widget(self.email_label)
        
        self.email_input = TextInput(multiline=False, size_hint_y=0.2)
        self.add_widget(self.email_input)
        
        # Save button
        self.save_button = Button(text="Save Profile", size_hint_y=0.2)
        self.save_button.bind(on_press=self.save_profile)
        self.add_widget(self.save_button)
        
        # Status or information label
        self.status_label = Label(text="Update your profile information.", size_hint_y=0.2)
        self.add_widget(self.status_label)
        
    def save_profile(self, instance):
        """
        Handle profile saving and show confirmation popup.
        """
        name = self.name_input.text
        email = self.email_input.text
        
        if name and email:
            # Here you should include the logic to save the user profile
            self.show_popup("Success", "Profile saved successfully!")
        else:
            self.show_popup("Error", "Please enter valid name and email.")
        
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
