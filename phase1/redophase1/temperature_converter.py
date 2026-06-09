class TemperatureConverter:

    def __init__(self,value):
        self.value=value

    def calculate_cel_to_feh(self):
        return (self.value*1.8)+32
    def calcualte_feh_to_cel(self):
        return (self.value-32)/1.8

