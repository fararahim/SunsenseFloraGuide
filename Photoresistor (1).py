from tkinter import *
from gpiozero import LightSensor, Buzzer
ldr = LightSensor(5)
import time
"""

plant_dictionary={
    6.1: "Olive Tree",
    8.01: "Lemon Tree",       #6 to 8 
    5.01: "Mint",             #2 to 5 
    7.01: "Basil",            #6 to 8 
    10.01: "Strawberry",      #6 to 20 
    8.01: "Sunflower",
    5.1: "Ginger",           #2 to 5 
    7.1: "Parsley",          #5 to 7 
    3.1: "Chives",           #1 to 3 
    2.1: "Lemon Balm",       #1 to 2
    12.01: "Aloe Vera",       #10 to 12 
    8.1: "Rosemary",         #8 to 10 
    11.1: "Lettuce",         #11 to 15 
    10.1: "Date Palm Tree",   #8 to 11 
    12.1: "Jasmine"
}

# A list of the outputs from the photoresistor
list_of_outputs = []
# Amount of sunlight hours
light_hours = 0

x = 0
while x < 12:
    time.sleep(3)
    currentvalue = ldr.value
    print(currentvalue)
    list_of_outputs.append(int(currentvalue + 0.1))
    x += 1

y = 0
while y < 12:
    if (list_of_outputs[y]) > 0.1:
        light_hours += 1
    y += 1

# creates a list of plants that need the same amount of light as given
matching_plants = [
    plant_dictionary[hours] for hours in plant_dictionary
    if hours >= (light_hours - 0.5) and hours <= (light_hours + 0.5)
]

print(f"The plants you could place here are: {matching_plants}")
"""

class GUITest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
    
    def setupGUI(self):

        title = Label(self.master, text="SunSense Floraguide", font=('Times New Roman', 22))
        title.grid(row=0, column=1,)

        l1 = Label(self.master, text="Press start to begin recording daylight hours:", font=('Times New Roman', 16))
        l1.grid(row=1, column=0, sticky=W)

        b1 = Button(self.master, text="Start", font=('Times New Roman', 16), command=self.startRecording)
        b1.grid(row=2, column=0, sticky=W)

        l2 = Label(self.master, text="Or enter your own daylight hours:", font=('Times New Roman', 16))
        l2.grid(row=3, column=0, sticky=W)

        self.e2 = Entry(self.master, font=('Times New Roman', 18))
        self.e2.insert(END, "6")
        self.e2.grid(row=4, column=0, sticky=W)

        b2 = Button(self.master, text="Enter", font=('Times New Roman', 16), command=self.userHours)
        b2.grid(row=5, column=0, sticky=W)

    def startRecording(self):

        plant_dictionary={
        6.1: "Olive Tree",
        8.01: "Lemon Tree",       #6 to 8 
        5.01: "Mint",             #2 to 5 
        7.01: "Basil",            #6 to 8 
        10.01: "Strawberry",      #6 to 20 
        8.01: "Sunflower",
        5.1: "Ginger",           #2 to 5 
        7.1: "Parsley",          #5 to 7 
        3.1: "Chives",           #1 to 3 
        2.1: "Lemon Balm",       #1 to 2
        12.01: "Aloe Vera",       #10 to 12 
        8.1: "Rosemary",         #8 to 10 
        11.1: "Lettuce",         #11 to 15 
        10.1: "Date Palm Tree",   #8 to 11 
        12.1: "Jasmine"
        }
        
        # A list of the outputs from the photoresistor
        list_of_outputs = []
        # Amount of sunlight hours
        light_hours = 0
        # comment this out on Rasp. pi
        currentvalue = 1.0

        x = 0
        while x < 12:
            time.sleep(1)
            # currentvalue = ldr.value
            print(currentvalue)
            list_of_outputs.append(int(currentvalue + 0.1))
            x += 1

        print(list_of_outputs)
        y = 0
        while y < 12:
            if list_of_outputs[y] > 0.1:
                light_hours += 1
            y += 1

        # creates a list of plants that need the same amount of light as given
        matching_plants = [
            plant_dictionary[hours] for hours in plant_dictionary
            if hours >= (light_hours - 0.5) and hours <= (light_hours + 0.5)
        ]

        label = Label(window, text= f"The plants you could place here are: {matching_plants}", font=('Times New Roman', 16))
        label.grid(row=2, column=2, sticky=W)
        # print(f"The plants you could place here are: {matching_plants}")

    def userHours(self):

        plant_dictionary={
        6.1: "Olive Tree",
        8.01: "Lemon Tree",       #6 to 8 
        5.01: "Mint",             #2 to 5 
        7.01: "Basil",            #6 to 8 
        10.01: "Strawberry",      #6 to 20 
        8.01: "Sunflower",
        5.1: "Ginger",           #2 to 5 
        7.1: "Parsley",          #5 to 7 
        3.1: "Chives",           #1 to 3 
        2.1: "Lemon Balm",       #1 to 2
        12.01: "Aloe Vera",       #10 to 12 
        8.1: "Rosemary",         #8 to 10 
        11.1: "Lettuce",         #11 to 15 
        10.1: "Date Palm Tree",   #8 to 11 
        12.1: "Jasmine"
        }

        light_hours = int(self.e2.get())

        matching_plants = [
            plant_dictionary[hours] for hours in plant_dictionary
            if hours >= (light_hours - 0.5) and hours <= (light_hours + 0.5)
        ]

        label = Label(window, text= f"The plants good for these hours are: {matching_plants}", font=('Times New Roman', 16))
        label.grid(row=4, column=2, sticky=W)



window = Tk()
window.geometry("1300x250")
window.configure(bg="#E0EE5D")
t = GUITest(window)
t.setupGUI()
window.mainloop()