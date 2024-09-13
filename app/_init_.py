# app/__init__.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui.home_screen import HomeScreen
from ui.log_screen import LogScreen
from ui.graph_screen import GraphScreen
from ui.settings_screen import SettingsScreen
from data import setup_data

class WeightWiseApp(App):
    def build(self):
        setup_data()  # Initialize the database
        sm = ScreenManager()
        
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(LogScreen(name='log'))
        sm.add_widget(GraphScreen(name='graph'))
        sm.add_widget(SettingsScreen(name='settings'))
        
        return sm
