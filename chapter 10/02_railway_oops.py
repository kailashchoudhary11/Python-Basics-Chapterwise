class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

kaisApplication = RailwayForm()

kaisApplication.name = "kai"
kaisApplication.train = "Rajdhani Express"

kaisApplication.printData()