class computer:
    ram="8gb"
    processor="amd A8"
    Operating_system="Linux"
    def dell(self):
        color="grey"
        model="XPS"
        price="74,000"
        if price<="80000":
            print("Dell has",self.ram,"Memory and color is",color)
        else:
            print("Dell has",self.ram,"Memory and color is",color,"and price of the model",model,"is",price)

    def hp(self):
        color="black"
        model="PS"
        price="25000"
        print("HP has",color,"color variant and the processor is",self.processor,"the latest model is",model,"with price range of",price)

    def asus(self):
        color = "black"
        model = "TUF"
        price = "70000"
        print("The model",model,"with color",color,"and memory",self.ram,"with powerfull processor",self.processor,"in price range of",price)

pcc = computer()
pcc.dell()
pcc.hp()
pcc.asus()

