from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.textinput import TextInput
import re
import subprocess
import sys
import math

from mpmath import *
from math import *
from numpy import *
import numpy



Builder.load_file('./scientific.kv')
Window.size = (800, 550)

class CalculatorWidget(Widget):
    # Clear the screen
    def clear(self):
        self.ids.input_box.text = "0"

    # Remove the last character
    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    # Getting the button value
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"

        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    # Getting the sings
    def sings(self, sing):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sing}"

    # Getting decimal value
    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", prev_number)

        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number) and "." not in num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number

        elif '.' in prev_number:
            pass

        else:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number


    def tang(self, sing):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('tan(r)', {'__builtins__': None}, {'r': r, 'tan': tan})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong "
            print(prev_number)

    def ctang(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('cot(r)', {'__builtins__': None}, {'r': r, 'cot': cot})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong "
            print(prev_number)
        
    def sin(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('sin(r)', {'__builtins__': None}, {'r': r, 'sin': sin})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)
    
    def cos(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('cos(r)', {'__builtins__': None}, {'r': r, 'cos': cos})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)

        
    def log(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('log(r)', {'__builtins__': None}, {'r': r, 'log': log})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)
        
    def arctang(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('atan(r)', {'__builtins__': None}, {'r': r, 'atan': atan})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)
        
    def arctang(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('atan(r)', {'__builtins__': None}, {'r': r, 'atan': atan})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)
    
    def arcctg(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('atan(r)', {'__builtins__': None}, {'r': r, 'atan': atan})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)
    
    def arsin(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('arcsin(r)', {'__builtins__': None}, {'r': r, 'arcsin': numpy.arcsin})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)

    def arcos(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('arccos(r)', {'__builtins__': None}, {'r': r, 'arccos': numpy.arccos})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)

    def rad(self):
        prev_number = self.ids.input_box.text
        
        try :
            r=int(prev_number)
            e=eval('sqrt(r)', {'__builtins__': None}, {'r': r, 'sqrt':sqrt})
            self.ids.input_box.text = str(e)

        except:
            self.ids.input_box.text= "wrong"
            print(prev_number)


    # Calculate the result
    def results(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    # Positive to negative
    def positive_negative(self):
        prev_number = self.ids.input_box.text
        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"

    def drop(self):
        
        subprocess.call(['python', 'calc.py'])

    def tg(self):
        print("working")
    

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == "__main__":
    CalculatorApp().run()