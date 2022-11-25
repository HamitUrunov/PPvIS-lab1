from models.Way import Ways
from models.Goods import Goods 
from models.Wagone import Wagone, count_dict
from models.Train import Train
from models.PassengerTrain import PassengerTrain
from models.Semaphore import Semophor
from time import sleep
import random
class Controller:
    def __init__(self):
        while True:
            choosed = input("Choose train: 1)Reight train or 2)Passenger train: \n")
            if choosed == "1": 
                self.reightTrain = Train(200, 4, "Reight train")
                print(f"Train's speed: {self.reightTrain.speed}")
                print(f"Max. count wagone: {self.reightTrain.maxWagon}")
                print(f"Current count wagone: {len(count_dict)}")
                while len(count_dict) < self.reightTrain.maxWagon:
                    addtrain = input("Add wagone?: Yes or No ")
                    if addtrain == "Yes":
                        sostav = Wagone()
                        loadCapacity = len(count_dict) * sostav.wagone                        
                        print(f"Сurrent load capacity of the train: {loadCapacity}")
                        self.reightTrain.speed = self.reightTrain.speed - 30
                        print(f"Current train speed: {self.reightTrain.speed}")
                    elif addtrain == "No":
                        break
                    else: continue         
                break

            elif choosed == "2":
                self.passengerTrain = PassengerTrain(100, 50, "Passenger Train")
                print(f"Train's speed: {self.passengerTrain.speed}")
                print(f"Count seats: {50}")
                passenger = random.randint(10,50)
                print(f"Boarded the train {passenger}")
                choose = input("Add freight wagon? Yes or No ")
                if choose == "Yes":
                    sostav = Wagone()
                    loadCapacity = 20
                    print("Freight wagones added")
                    break
                elif choose == "No":
                    print("The train is on the way...")
                    sleep(2)
                    print(f"The train arrived at the station {Ways().firstWay[random.randint(1,3)]}")
                    print("Passenger leave the train")
                    print("Choose train again")         

                  
                
        

        def travel(ways):
            name = input("Enter name goods: ")
            weight = input("Enter weight goods: ")
            destination = input("Enter destination:")
            goods = Goods(name, weight)
            freeCapacity = int(loadCapacity) - int(weight)
            print(f"Remaining free space: {freeCapacity}")
            for i in range(7):
                if i < 3:
                    print("Loading of goods...")
                elif i == 3:
                    semophor = Semophor("Green", False)
                    print("Semaphore open")
                    print(f"{semophor.color} colour")
                else: 
                    print("In the way")
                sleep(3)
            print(f"Arrived in {ways[1]}") 
            unloaded = input("Enter how much to upload: ")
            cargo = int(weight) - int(unloaded)
            print(f"Remaining cargo: {cargo}")

            name = input("Enter name goods: ")
            weight = input("Enter weight goods: ")
            destination = input("Enter destination:")
            goods = Goods(name, weight, destination)
            freeCapacity = int(loadCapacity) - int(weight)
            print(f"Remaining free space: {freeCapacity}")
            print("Отправка...")
            for i in range(5):
                print("In the way")
                sleep(1)  

            print(f"Arrived at the end station {ways[2]}")
            print("Upload all")

        print("Choose pass?")
        print(1, Ways().firstWay, 2, Ways().secondWay, 3, Ways().thirdWay)
        way = input()
        if way == str(1):
            travel(Ways().firstWay)
        elif way == str(2):
            travel(Ways().secondWay)
        elif way == str(3):
            travel(Ways().thirdWay)
            

        


