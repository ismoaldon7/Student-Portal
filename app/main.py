# --- APP ---
from kivy.config import Config
Config.set('graphics','width',1280)
Config.set('graphics','height',720)
from kivy.core.window import Window
Window.clearcolor = (71/255, 93/255, 102/255, 1)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, WipeTransition

# --- TOOLS ---
import os
import sys
import json
from kivy.resources import resource_add_path
from kivy.properties import ListProperty, StringProperty, NumericProperty
if getattr(sys, 'frozen', False):
    from app.screens.modules import resource_path
else:
    from screens.modules import resource_path
resource_add_path(resource_path(os.path.join('data', 'logo')))
resource_add_path(resource_path(os.path.join('data', 'fonts')))
resource_add_path(resource_path(os.path.join('data', 'database')))
resource_add_path(resource_path(os.path.join('screens', 'wikipedia')))
resource_add_path(resource_path(os.path.join('screens', 'mainmenu')))


class StudentPortal(MDApp):

    title = "Student Portal"
    color_theme = 'normal'
    bg_color = ListProperty([71/255, 93/255, 102/255, 1])
    tile_color = ListProperty([133/255, 144/255, 149/255, 1])
    raised_button_color = ListProperty([144/255, 159/255, 165/255, 1])
    text_color = ListProperty([0, 0, 0, 1])
    title_text_color = ListProperty([1, 1, 1, 1])
    accent_color = ListProperty([0.5, 0.7, 0.5, 1])
    app_font = StringProperty(resource_path(os.path.join('data', 'fonts', 'JetBrainsMono-Regular.ttf')))
    mainmenu_icons = resource_path(os.path.join('data', 'icons_dark'))
    cursor_width = NumericProperty(3)

    def build(self):
        if getattr(sys, 'frozen', False):
            from app.screens import mainmenu, wikipedia, notebook
        else:
            from screens import mainmenu, wikipedia, notebook

        self.mainmenu_module = mainmenu
        self.wikipedia_module = wikipedia
        self.notebook_module = notebook

        self.root = ScreenManager()
        self.mainmenu = self.mainmenu_module.MainMenu()
        self.wikipedia = self.wikipedia_module.Wikipedia()
        self.notebook = self.notebook_module.Notebook()
        self.screens = {
            'mainmenu': self.mainmenu,
            'wikipedia': self.wikipedia,
            'notebook': self.notebook
        }
        self.root.switch_to(self.mainmenu)
        return self.root

    def switch_screen(self, screen_name, direction='left'):
        self.root.transition.direction = direction
        self.root.switch_to(self.screens.get(screen_name))

    def unlock_dark_mode(self):
        self.color_theme = 'dark'
        self.bg_color = [29/255, 29/255, 29/255, 1]
        self.tile_color = [40/255, 40/255, 40/255, 1]
        self.raised_button_color = [52/255, 52/255, 52/255, 1]
        self.text_color = [1, 1, 1, 1]

    def color_theme_normal(self):
        self.color_theme = 'normal'
        self.bg_color = [71/255, 93/255, 102/255, 1]
        self.tile_color = [133/255, 144/255, 149/255, 1]
        self.raised_button_color = [144/255, 159/255, 165/255, 1]
        self.text_color = [0, 0, 0, 1]


if __name__ == '__main__':
    StudentPortal().run()
