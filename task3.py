class TVController:

    controler = 0

    def __init__(self, channels):
        self.channels = channels


    def first_channel(self):
        return self.channels[self.controler]

    def last_channel(self):
        return self.channels[len(self.channels)-1]

    def turn_channel(self):
        return self.channels[self.controler-1]

    def next_channel(self):
        try:
            next_channel = self.channels[self.controler+1]
        except IndexError:
            next_channel = self.channels[0]
        return next_channel

    def previous_channel(self):
        return self.channels[self.controler-1]

    def current_channel(self):
        return self.channels[self.controler]

    def is_exist(self, a="1"):
        try:
            if int(a) in range(1, len(self.channels)):
                return "YES"
            else:
                return "NO"
        except ValueError:
            if a in self.channels:
                return "YES"
            else:
                return "NO"



if __name__ == '__main__':






    y = ["BBC", "Discovery", "TV1000"]
    j = ["BBC", "Discovery",]

    pult_1 = TVController(y)
    pult_2 = TVController(j)



    print(pult_1.first_channel())
    print(pult_2.first_channel())
    print(pult_1.last_channel())
    print(pult_2.last_channel())
    print(pult_1.turn_channel())
    print(pult_2.turn_channel())
    print(pult_1.next_channel())
    print(pult_2.next_channel())
    print(pult_1.previous_channel())
    print(pult_2.previous_channel())
    print(pult_1.is_exist(1))
    print(pult_2.is_exist("Disc"))

