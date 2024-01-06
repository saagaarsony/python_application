from kivy.app import App # here we import the App Modules
from kivy.uix.boxlayout import BoxLayout # gere We import Boxlayout For The Box
from kivy.uix.button import Button # that Module we import For Buttons
from kivy.uix.textinput import TextInput # that Module as for The TextInput

# Start The Coding

class MainApp(App): # that Was imported From the Module
    def build(self):# that Variable is set to be a self that y we use self..
        self.icon = "cal.png" # that For Changing The Icons
        self.operators = ["/", "*", "+", "-"] # we Define all Oprtators
        self.last_was_operators = None
        self.last_button = None

        main_layout = BoxLayout(orientation= "vertical")
        self.solution = TextInput(background_color = "black", foreground_color = "white",
                                  multiline = False, halign="right", font_size= 60, readonly = True)# That Is For Screen Of Application

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "c", "-"],
        ]

        # for Adding The Buttons In The Black Screen
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color = "grey",
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                )
                # make Button working And Functions
                button.bind(on_press= self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout) 

        # Foe Equle Button
        equal_button = Button(
            text = "=", font_size = 30, background_color = "grey",
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
        )      
        equal_button.bind(on_press= self.on_solution)  
        main_layout.add_widget(equal_button) 

        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'c':
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operators and button_text in self.operators):
                return 
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operators = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text)) 
            self.solution.text = solution           
                        


# For Running The App.
if __name__ == "__main__":
    app = MainApp()
    app.run()        

