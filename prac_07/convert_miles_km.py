from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ An App to convert miles into kilometer"""
    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculation_handler(self):
        """ Handles calculation from mile to kilometer and displays the result """
        value = self.validate_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def increment_handler(self, change):
        """Handle increment by being clicked on the button"""
        value = self.validate_input() + change
        self.root.ids.input_miles.text = str(value)
        self.calculation_handler()

    def validate_input(self):
        """Get input from the user and convert it to float and return it, unless input is a number, 0.0 is returned"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()
