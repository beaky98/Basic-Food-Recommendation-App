import pygame
from operator import itemgetter
from tkinter import *

NUMBER = 14  #initialise the global constant of the number of canteens

data=[]  #initialise a global list for the following options to append values in

root = Tk()

#Canteen's information = Food, price, location, opening and closing hours and rating 
canteen = [{'canteen_name':'Canteen 1',
            'food_list' : [['Chicken Rice', 3.00], ['Fishball Noodles', 3.50], ['Mixed Rice',3.00]],
            'location' : [490, 450],
            'openhr' : "0700",
            'closehr' : "2100", 
            'rating' : 2.8},  #Can1
           
            {'canteen_name':'Canteen 2',
            'food_list' : [['Mixed Rice', 3.50], ['Xiao Long Bao', 4.30], ['Chicken Rice', 2.80], ['Takoyaki', 2.40], ['Pasta', 4.50]],
            'location' : [541, 370],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 5.0},  #Can2
           
            {'canteen_name':'Canteen 9',
            'food_list' : [['Mala', 5.00], ['Ramen', 4.50], ['Mixed Rice',3.00], ['Drinks', 1.10], ['Chicken Rice', 3.50]],
            'location' : [697, 212],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 4.0},  #Can9
           
            {'canteen_name':'Canteen 11',
            'food_list' : [['Mixed Rice', 3.00], ['Waffle', 1.40], ['Naan',1.50], ['Tze Char', 5.00], ['Mala', 5.00]],
            'location' : [832, 152],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 4.3}, #Can11

            {'canteen_name':'Canteen 13',
            'food_list' : [['Mixed Rice', 3.00], ['Ramen', 4.50]],
            'location' : [489, 71],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 3.5},  #Can13

            {'canteen_name':'Canteen 14',
            'food_list' : [['Chicken Rice', 3.00], ['Ban Mian', 3.50], ['Mixed Rice', 3.00]],
            'location' : [585, 77],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 3.7},  #Can14

            {'canteen_name':'Canteen 16',
            'food_list' : [['Chicken Rice', 3.00], ['Fishball Noodles', 3.50], ['Roti Prata', 1.00]],
            'location' : [437, 129],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 3.2}, #Can16

            {'canteen_name':'Ananda Kitchen',
            'food_list' : [['Chicken Briyani', 5.00], ['Murtabak', 6.00], ['Roti Prata', 1.00]],
            'location' : [846, 237],
            'openhr' : "1200",
            'closehr' : "2230",
            'rating' : 3.8},  #Ananda Kitchen

            {'canteen_name':'Foodgle',
            'food_list' : [['Chicken Rice', 3.50], ['Fishball Noodles', 3.50], ['Roti Prata', 1.00], ['Kimchi Fried Rice', 3.50], ['Mala', 5.00]],
            'location' : [762, 93],
            'openhr' : "1200",
            'closehr' : "2230",
            'rating' : 4.9},  #Foodgle

            {'canteen_name':'North Hill',
            'food_list' : [['Mixed Rice', 3.50], ['Tze Char', 5.50], ['Fishball Noodles', 3.50]],
            'location' : [859, 265],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 4.1},  #North Hill

            {'canteen_name':'Pioneer',
            'food_list' : [['Chicken Rice', 3.00], ['Fishball Noodles', 3.50], ['Mixed Rice',3.50]],
            'location' : [565, 568],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 3.4},  #Pioneer

            {'canteen_name':'Quad Cafe',
            'food_list' : [['Bibimbap', 3.50], ['Ginseng Chicken Soup', 5.00], ['Yong Tau Foo', 4.50]],
            'location' : [156, 274],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 3.6},  #Quad

            {'canteen_name':'Koufu',
            'food_list' : [['Pasta', 4.20], ['Chicken Poke Bowl', 3.90], ['Chicken Fuyong',3.50], ['Chicken Rice', 3.00]],
            'location' : [180, 481],
            'openhr' : "0700",
            'closehr' : "2100",
            'rating' : 4.2}, #Koufu

            {'canteen_name':'Northspine',
            'food_list' : [['Chicken Rice', 3.00], ['Fishball Noodles', 3.30], ['Vegeterian', 3.50], ['Mixed Rice', 3.50], ['Mala', 5.00]],
            'location' : [247, 219],
            'openhr' : "0700",
            'closehr' : "2359",
            'rating' : 3.0}] #Northspine

#In this class we have functions for...
#  ->initialising the buttons for the GUI
#  ->the different commands that will be executed accordingly
#  ->the link to another class so as to pop-up a new window to show the lists accordingly
class Main_GUI:

    #Initialise the program as it exexutes
    def __init__(self, master):

        #initialise and the style of the buttons to make choices
        self.master = master
        self.frame = Frame(self.master)
        self.b_menu = Label(self.master, text='MAIN MENU', bg='grey', fg='white', relief=RAISED, width=25,font=('Arial', 36, 'bold'), pady=25)
        self.b1 = Button(self.master, text="1. Search by Distance", width=50, height=1, font=32, command=self.group_function_1)
        self.b2 = Button(self.master, text="2. Search by Food", width=50, height=1, font=32, pady=10, command=self.group_function_2)
        self.b3 = Button(self.master, text="3. Search by Food Price", width=50, height=1, font=32, pady=10, command=self.group_function_3)
        self.b4 = Button(self.master, text="4. Search by Rank", width=50, height=1, font=32, pady=10, command=self.group_function_4)
        self.b5 = Button(self.master, text="5. Search by Opening and Closing Hours", width=50, height=1, font=32, pady=10, command=self.group_function_5)
        self.b6 = Button(self.master, text="6. Exit", width=50, height=1, font=32, pady=10, command=quit)
        
        #to display the buttons
        self.b_menu.grid()
        self.b1.grid()
        self.b2.grid()
        self.b3.grid()
        self.b4.grid()
        self.b5.grid()
        self.b6.grid()
        self.frame.grid()

#FUNCTIONS FOR OPTION 1
        
    #If user click button 1, it will invoke this function
    def group_function_1(self):
        
        self.main()
        self.distance_location()
        self.data_1()
        self.popup_1()

    #Initialising pygame
    def main(self):
        
        self.display_map()
        self.MouseClick()

    #Map of NTU and the respective canteens
    def display_map(self):
        
        introScreenImage = pygame.image.load("NTU Map.jpg")
        screen = pygame.display.set_mode((883,617))
        screen.blit(introScreenImage, (0,0))
        pygame.display.flip()

    #Get user's mouseclick input
    def MouseClick(self):
        
        keep_clicking = True
        while keep_clicking:
            ## pygame.event.get() retrieves all events made by user
            for event in pygame.event.get():
                #Close program once click exit(X) button        
                if event.type == pygame.QUIT:
                    keep_clicking = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Assigning x and y - coordinates from tuple to variables
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    keep_clicking = False
                    

        return (mouseX, mouseY)

    #Ask User for current location
    def distance_location(self):
        
        x_u, y_u = self.MouseClick()  #get user's location with just one click from the mouse
        dist_list = []   #initialise empty list for the values to be appended
        
        #Compare and calculate the distance between the user's location and all the foodcourts
        for i in range (NUMBER):
            
            diff_dist_x = (x_u- int(canteen[i]['location'][0]))**2
            diff_dist_y = (y_u- int(canteen[i]['location'][1]))**2
            diff_dist = (diff_dist_x + diff_dist_y)**0.5
            dist_list += [diff_dist]
            
        #Append new key into individual canteen dictionary
            canteen[i]['diff_dist'] = dist_list[i]

            #print(canteen[i]['diff_dist'])  #debugging

    #Function to sort the list of canteens from the nearest to the furthest from the user's location
    def data_1(self):
        
        global data
        self.data=list(self.sort_distance())
        

    #Sort according to distance
    def sort_distance(self):
        
        canteen_distance=[]
        canteen_distance.append('Ranked by nearest canteen from user')
        global canteen
        
        #Sort in ascending order
        canteen=sorted(canteen,key=itemgetter('diff_dist'),reverse=False)
        for i in range(NUMBER):
            canteen_distance.append(canteen[i]['canteen_name'])
        return canteen_distance

    #to initiate the pop-up window after the first button is pressed from the MENU
    def popup_1(self):
        
        #self.master.withdraw()  #exit the main program after clicking any button from the MENU
        self.newWindow = Toplevel(self.master)
        p1 = option_1(self.newWindow)


#FUNCTIONS FOR OPTION 2

    #If user click button 2, it will invoke this function
    def group_function_2(self):
        
        self.popup_2()

    #to initiate the pop-up window after the second button is pressed from the MENU
    def popup_2(self):
        
        self.newWindow = Toplevel(self.master)
        p2 = option_2(self.newWindow)
        

#FUNCTIONS FOR OPTION 3
        
    #If user click button 3, it will invoke this function
    def group_function_3(self):
        
        self.popup_3()
        
    #to initiate the pop-up window after the third button is pressed from the MENU     
    def popup_3(self):
        
        self.newWindow = Toplevel(self.master)
        p3 = option_3(self.newWindow)

#FUNCTIONS FOR OPTION 4
        
    #If user click button 4, it will invoke this function
    def group_function_4(self):
        
        self.data_4()
        self.popup_4()
        
    #Function to sort the list of canteens from the nearest to the furthest from the user's location
    def data_4(self):
        
        global data
        self.data=list(self.sort_rating())
        return self.data

    #Sort according to distance
    def sort_rating(self):
        
        canteen_rate=[]
        global canteen
        #Sort in descending order
        canteen=sorted(canteen,key=itemgetter('rating'),reverse=True)
        canteen_rate.append('Ranked by rating')
        for i in range (NUMBER): 
            canteen_rate.append(canteen[i]['canteen_name'])
        return canteen_rate

    #to initiate the pop-up window after the fourth button is pressed from the MENU
    def popup_4(self):
        
        #self.master.withdraw()  #exit the main program after clicking any button from the MENU
        self.newWindow = Toplevel(self.master)
        p4 = option_4(self.newWindow)



#FUNCTIONS FOR OPTION 5
        
    #If user click button 5, it will invoke this function    
    def group_function_5(self):

        self.popup_5()
        
    #to initiate the pop-up window after the fifth button is pressed from the MENU    
    def popup_5(self):
        
        self.newWindow = Toplevel(self.master)
        p5 = option_5(self.newWindow)        

    
#Open a new window to show the sorted list of the nearest foodcourt from the user's location
class option_1(Main_GUI):   

    #Method to be called automatically
    def __init__(self,master):
        
        #initialise the frame of the popup window
        self.master = master
        self.frame = Frame(self.master)

        #Make a call to a class method from another class Main_GUI
        self.DATA = Main_GUI.data_1(self)

        #ensure data is accessible and modifiable 
        global data

        #orientation of the GUI
        self.one_1 = Label(self.master,text='Canteen',bg='white', relief=RAISED,width=50).grid(row=0,column=1)
        self.one_2 = Label(self.master,text=self.data[0],bg='white', relief=RAISED,width=50).grid(row=0,column=0)
        r=1
        for m in self.data[1:]:
            self.one_3 = Label(self.master,text=r,bg='white', relief=RIDGE,width=50).grid(row=r,column=0)
            self.one_4 = Label(self.master,text=m,bg='white', relief=RIDGE,width=50).grid(row=r,column=1)
            r=r+1

#Open a new window to ask what user wants to eat
class option_2(Main_GUI):  

    #Method to be called automatically
    def __init__(self,master):
        self.master = master
        self.t_input_2()

    #Method to ask for user's input   
    def t_input_2(self):
        
        #initialise the frame of the popup window
        self.frame = Frame(self.master)

        Label(self.master, text="What do you want to eat? ",width=100,font=('Arial', 12, 'bold'),bg='grey',fg='white', pady=25).grid(row=0)
        self.e1 = Entry(self.master)
        text = self.e1.get()
        self.e1.grid()
        Button(self.master, text='Enter', command=self.search_by_food).grid(row=3, sticky=W, pady=4)
        
        return text

    
    #Search by food irregardless of rating and distance
    def search_by_food(self):

        self.frame = Frame(self.master)

        #initialise an empty list
        canteen_search_food=[]
        canteen_search_food.append("Canteens that sells what you want: ")

        
        b=0  #initialise the number of canteens if they sell what the user have input
        #Take all the canteen into account
        for i in range (NUMBER):
            
            #Look for individual food in each canteen
            for j in range (len(canteen[i]['food_list'])):
                
                if  self.e1.get() == canteen[i]['food_list'][j][0]:
                    b+=1  #increment if food is found from the user's input :)
                    canteen_search_food.append(canteen[i]['canteen_name'])
                    #print(b)
                    
        if b == 0:  #if canteens do not sell the food the user have input :(
            canteen_search_food.append("-")
            
            #Create blanks in the GUI
            self.two_3 = Label(self.master,text="",bg='white',width=100,relief=RAISED,font=('Arial', 12, 'bold'), pady=10).grid(row=3)

        print (canteen_search_food)
        
        self.two_1 = Label(self.master,text=(canteen_search_food[0]),bg='grey', relief=RAISED,width=100, pady = 25, font=('Arial', 12, 'bold'), fg='white').grid(row=0,column=0)
        r=1
        #Create blanks in the GUI
        self.two_3 = Label(self.master,text="",bg='white',width=100,relief=RAISED,font=('Arial', 12, 'bold'), pady=10).grid(row=3)
        
        for m in (canteen_search_food[1:]):
            self.two_2 = Label(self.master,text=m,bg='white', relief=RAISED,width=100, pady=10, font=('Arial', 12, 'bold')).grid(row=r,column=0)
            r=r+1

        return canteen_search_food
    
#Open a new window to ask user's maximum budget 
class option_3(Main_GUI):
    
    #Method to be called automatically
    def __init__(self,master):
        
        self.master = master
        self.t_input_3()
        
    #Method to ask for user's input 
    def t_input_3(self):
        
        #initialise the frame of the popup window
        self.frame = Frame(self.master)
        Label(self.master, text="What is your maximum budget? $",width=100,font=('Arial', 12, 'bold'),bg='grey',fg='white', pady=20).grid(row=0)
        self.e3 = Entry(self.master)
        self.e3.grid(row=1)
        Button(self.master, text='Enter', command=self.search_by_price).grid(row=2, sticky=W, pady=4)

    
    #Search by food irregardless of rating and distance
    def search_by_price(self):
        
        try:
            self.frame = Frame(self.master)
            canteen_search_price=[]
            canteen_search_price.append("Canteens that sells below your budget: ")
            for i in range(NUMBER):                   
                canteen[i]['food_list']=sorted(canteen[i]['food_list'],key=itemgetter(1))

            #Print price and food by canteen
            a = 0  #initialise the number of canteens that DOES NOT have food that is cheaper than the input max_price
            for i in range(NUMBER):
                if canteen[i]['food_list'][0][1] <= float(self.e3.get()):
                    for j in range(len(canteen[i]['food_list'])):
                        if canteen[i]['food_list'][j][1]<=float(self.e3.get()):
                                    canteen_search_price.append([canteen[i]['canteen_name'],canteen[i]['food_list'][j]])
                else:
                    a+=1
                    if a == NUMBER:  #when all canteens only sell food that are over max_price :(
                        canteen_search_price.append("-")
                        self.three_5 = Label(self.master,text="",bg='white',width=102,relief=RAISED,font=('Arial', 12, 'bold'), pady=5).grid(row=2)
                  
            
            self.three_1 = Label(self.master,text=(canteen_search_price[0]),bg='grey', fg= 'white',relief=RAISED,width=102, font=('Arial', 12, 'bold'), pady = 20).grid(row=0,column=0)
            r=1
            for m in (canteen_search_price[1:]):
                self.three_2 = Label(self.master,text=m,bg='white', width=170, relief=RAISED, font=('Arial', 8, ''), pady=5).grid(row=r,column=0)
                r=r+1

            return canteen_search_price
        except:
            self.three_3 = Label(self.master,text="Invalid input! Try again.",bg='white',fg='red',pady=10,width=100, font=('Arial', 12, 'bold')).grid(row=1,column=0)
            
            self.three_4 = Label(self.master,text="",bg='white',pady=10,width=100, font=('Arial', 12, 'bold')).grid(row=2,column=0)


#Open a new window to show the sorted list of the nearest foodcourt from the user's location
class option_4(Main_GUI):

    #Method to be called automatically
    def __init__(self,master):
        
        #initialise the frame of the popup window
        self.master = master
        self.frame = Frame(self.master)

        #Make a call to a class method from another class Main_GUI
        self.DATA = Main_GUI.data_4(self)

        #ensure data is accessible and modifiable 
        global data

        #orientation of the GUI
        self.four_1 = Label(self.master,text='Canteen',bg='white', relief=RAISED,width=50).grid(row=0,column=1)
        self.four_2 = Label(self.master,text=self.data[0],bg='white', relief=RAISED,width=50).grid(row=0,column=0)
        r=1
        for m in self.data[1:]:
            self.four_3 = Label(self.master,text=r,bg='white', relief=RIDGE,width=50).grid(row=r,column=0)
            self.four_4 = Label(self.master,text=m,bg='white', relief=RIDGE,width=50).grid(row=r,column=1)
            r=r+1
            
#Open a new window to ask for the timing that the user wants to eat at
class option_5(Main_GUI):

    #Method to be called automatically
    def __init__(self,master):
        self.master = master
        self.t_input_5()
        
    #Method to ask for user's input
    def t_input_5(self):
        
        #initialise the frame of the popup window
        self.frame = Frame(self.master)
        
        Label(self.master,text="What time do you want to eat(HHMM)? ",bg='grey', fg='white',width=102,relief=RAISED,font=('Arial', 12, 'bold'), pady=20).grid(row=0)
        self.e5 = Entry(self.master)
        text_5 = self.e5.get()
        self.e5.grid()
        Button(self.master, text='Enter', command=self.eat_time).grid(row=2, sticky=W, pady=4)

        return text_5

    #Method to detect user's input of the time in HHMM as well as catching all the invalid timings the user have input if there is any
    def eat_time(self):
        
        canteen_eat_time=[]
        timing = self.e5.get()
        try:
            #timing = input("What time do you want to eat?(HHMM) ")
            #filter out all the invalid inputs e.g: 2500 , e123, 1e23, 12e3, 123e, abcd, -123, 2.22, 11111 etc
            if timing[0] < "3" and timing[2] < "6" and len(timing) == 4 and chr(48) <= timing[0] <= chr(50) and chr(48) <= timing[1] <= chr(57) and chr(48) <= timing[2] <= chr(53) and chr(48) <= timing[3] <= chr(57):
                if timing < "2400":

                    c=0 #initialise the number of canteens that are NOT opened
                    global canteen
                    canteen_eat_time.append("Canteen that are open at the time")
                    for i in range(NUMBER):
                        if timing >= canteen[i]['openhr'] and timing <= canteen[i]['closehr']:
                            canteen_eat_time.append(canteen[i]['canteen_name'])
                        else:
                            c += 1
                            if c == NUMBER:  #if all canteens are NOT opened
                                canteen_eat_time.append("-")
                                Label(self.master,text="",bg='white',width=102,relief=RAISED,font=('Arial', 12, 'bold'), pady=10).grid(row=2)
                else:
                    print("Enter a valid time")     
            else:
                print("You have an invalid time.")
        except:
            #to accept index value error
            print("You have an invalid time.")
            
        try:
            self.five_1 = Label(self.master,text=(canteen_eat_time[0]),bg='grey', relief=RAISED,width=102, pady = 20, font=('Arial', 12, 'bold'), fg='white').grid(row=0)
            Label(self.master,text="",bg='white',width=102,relief=RAISED,font=('Arial', 12, 'bold'), pady=10).grid(row=2)
            r=1
            for m in (canteen_eat_time[1:]):
                self.five_2 = Label(self.master,text=m,bg='white', relief=RAISED,width=102, pady=10, font=('Arial', 12, 'bold')).grid(row=r)
                r=r+1
        except:
            self.three_3 = Label(self.master,text="Invalid input! Try again.",bg='white',fg='red',pady=30,width=102, font=('Arial', 12, 'bold')).grid(row=1,column=0)
            
            self.three_4 = Label(self.master,text="",bg='white',pady=10,width=102, font=('Arial', 12, 'bold')).grid(row=2,column=0)

            
        return canteen_eat_time


b = Main_GUI(root)
root.mainloop()
