class CommaSeperatedString:

    def __init__(self,value):
        self.value=value

    def seperate(self):
        ab=self.value.split(",")
        lines=0
        for a in ab:
            lines=lines+1
            print(a)
        return lines
