import kivy
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.core.window import Window




class MainGridLayout(GridLayout):
    pass

class packageAPK(App):   
    def build(self):
        return MainGridLayout()

if __name__=='__main__':
    packageAPK().run()