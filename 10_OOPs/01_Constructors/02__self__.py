class computer:
    price = 10
    processors ={
        "intel":"i3",
        "amd":"threadriper"
    }

    ram ={
        "2gb":"2GB DDR3",
        "4gb":"4GB DDR4"
    }

    motherboard={
        "msi":"MSI-mx2000",
        "intel":"intel QX"
    }

    def comp1(self):
        print("You have chosen",self.processors["amd"],"and",self.ram["4gb"],"Memory with",self.motherboard["msi"],"Motherboard")

    def comp2(self):
        print("You have chosen",self.processors["intel"],"and",self.ram["2gb"],"Memory with",self.motherboard["intel"],"Motherboard")

    def comp3(self):
        print("You have chosen",self.processors["amd"],"and",self.ram["2gb"],"Memory with",self.motherboard["intel"],"Motherboard")

comp=computer()
comp.comp1()
comp.comp2()
comp.comp3()