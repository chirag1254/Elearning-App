from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import ScreenManager,NoTransition,CardTransition
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.list import OneLineListItem
from kivy.uix.image import AsyncImage
from kivy.uix.button import ButtonBehavior
from time import sleep
from kivy.uix.widget import Widget
from kivy.clock import Clock
from functools import partial
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image



Window.size = (350,600)



class StartingScreen(MDScreen):
    pass

class LogoScreen(MDScreen):
    pass

class LoginChoice(MDScreen):
    pass


class StudentSignupScreen(MDScreen): 
    pass

class StudentSigninScreen(MDScreen):
    pass

class StudentHomeScreen(MDScreen):
    pass

class StudentSearchScreen(MDScreen):
    pass
# class TeacherLoginChoice(MDScreen):
#     pass







class ELearningApp(MDApp):
    
    
    
    def __init__(self, **kwargs):
        super(ELearningApp,self).__init__(**kwargs)
        self.internet = False
        
        
        

    def on_start(self):
        
        self.event = Clock.schedule_once(self.check_internet,5)
        self.event
        Clock.schedule_once(self.start_app,5)
        self.event = Clock.schedule_interval(self.check_internet,10)
        self.event
        
        
        
        
        

    

    def check_internet(self,*args): 
         
        try:
            import socket
            IPaddress=socket.gethostbyname(socket.gethostname())
            if IPaddress=="127.0.0.1":
                self.no_internet()
                self.internet = False
                
                
            else:
                self.internet = True
                
                
        except:          
            pass
    
    def no_internet(self,*args):
        self.snackbar = Snackbar(text="No Internet Connection!")
        self.snackbar.show()
        
    def start_app(self,*args):
        
        if  self.internet == False:
            self.root.ids['starting_screen'].ids['spinner'].active = True
            self.root.ids['screen_manager'].transition = NoTransition()
            self.change_screen('starting_screen')
            self.root.ids['screen_manager'].transition = CardTransition()
            
        else:  
            self.change_screen("login_choice")
            


            
        
        


    def Search(self):
        self.root.ids['screen_manager'].transition = NoTransition()
        self.change_screen("search_screen")
        self.root.ids['screen_manager'].transition = CardTransition() 
        
        
        
        

    def build(self):
        
        
        self.icon = "images/Logo 2020-10-08 08 09 32.jpg"
        GUI = Builder.load_file('main.kv')

        return GUI

    def change_screen(self, screen_name):
        sm = self.root.ids['screen_manager']
        sm.current = screen_name
        pass

    def callback_for_menu_items(self):
        print("hlo")

    def show_example_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet()
        data = ["View Photo","Change Photo","Remove Photo"]
        for item in data:
            bottom_sheet_menu.add_item(
                item,
                lambda x: self.callback_for_menu_items()
            )
        bottom_sheet_menu.open()
    
    



if __name__ == "__main__":

    ela = ELearningApp()
    ela.run()
    
