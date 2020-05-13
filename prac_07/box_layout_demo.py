from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """"An App to take name for input and greets"""
    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display Hello + name and test in console"""
        print("test")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def press_clear(self):
        """Clear both textbox and Label"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"



BoxLayoutDemo().run()
