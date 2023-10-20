import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font as tkfont

#database connection

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootuser",
    database="restaurant_supply_express"
)
mycursor = mydb.cursor()

class DatabaseGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Restaurant Supply Express! Drone Delivery")
        self.geometry("1200x1000")
        icon = PhotoImage(file="chick.png")
        self.iconphoto(True, icon)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LogIn, Summary, AddOwner, AddEmployee, AddPilotRole, AddWorkerRole, AddIngredient, AddDrone, AddRestaurant, AddService, AddLocation, \
                StartFunding, HireEmployee, FireEmployee, ManageService, TakeoverDrone, JoinSwarm, LeaveSwarm, LoadDrone, RefuelDrone, FlyDrone, \
                PurchaseIngredient, RemoveIngredient, RemoveDrone, RemovePilotRole, \
                DisplayOwnerView, DisplayEmployeeView, DisplayPilotView, DisplayLocationView, DisplayIngredientView, DisplayServiceView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LogIn")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
'''
[1] add_owner() ✅
[2] add_employee() ✅
[3] add_pilot_role() ✅
[4] add_worker_role() ✅
[5] add_ingredient() ✅
[6] add_drone() ✅
[7] add_restaurant() ✅
[8] add_service() ✅
[9] add_location() ✅
[10] start_funding() ✅
[11] hire_employee() ✅
[12] fire_employee() ✅
[13] manage_service() ✅
[14] takeover_drone() ✅
[15] join_swarm() ✅
[16] leave_swarm() ✅
[17] load_drone() ✅
[18] refuel_drone() ✅
[19] fly_drone() ✅
[20] purchase_ingredient() ✅
[21] remove_ingredient() ✅
[22] remove_drone() ✅
[23] remove_pilot_role() ✅
[24] display_owner_view() ✅
[25] display_employee_view() ✅
[26] display_pilot_view() ✅
[27] display_location_view() ✅
[28] display_ingredient_view() ✅
[29] display_service_view() ✅
'''

class LogIn(tk.Frame):
    # def __init__(self, parent, controller):
    #     tk.Frame.__init__(self, parent)
    #     self.controller = controller
    #     label2 = tk.Label(self, text="Restaurant Supply Express! Drone Delivery", font=('Times', 45)).pack()
    #     label = tk.Label(self, text="Please enter your username", font=controller.title_font)
    #     label.pack(side="top", fill="x", pady=10)
    #     input = Entry(self, width=50)
    #     input.pack()
    #     suc = Label(self, text = "You have the access!", fg="green", font = 14)
    #     fail = Label(self, text = "No authority to access the datebase!", fg = "red", font = 14)
    #     sumBtn = tk.Button(self, text="Go to the summary page",
    #                         command=lambda: self.controller.show_frame("Summary"))
    #     button = Button(self, text="submit", command=lambda: LogIn.openDash(self,input, fail, suc,sumBtn))
    #     button.pack()
        
    # def openDash(self, input, fail, suc, button):
    #     username = input.get()
    #     #print(username)
    #     sql = "SELECT count(*) FROM users Where username = '{username}'".format(username = username)
    #     #print(sql)
    #     mycursor.execute(sql)
    #     res = mycursor.fetchone()
    #     #print(res)
    #     #print(res[0])
    #     if (res[0] == 0):     
    #         fail.pack()
    #         suc.pack_forget()
    #         button.pack_forget()
    #     else:
    #         suc.pack()
    #         fail.pack_forget()
    #         button.pack()
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.first_click = True
        self.user_list = []
        self.username_hint = 'Users: '

        label2 = tk.Label(self, text="Restaurant Supply Express! Drone Delivery", font=('Times', 45)).pack()
        label = tk.Label(self, text="Please enter your username", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        input = Entry(self, width=50, background= '#FFFFFF')
        input.pack()

        suc = Label(self, text = "Logged in!", fg="green", font = 14)
        fail = Label(self, text = "No authority to access the datebase!", fg = "red", font = 14)
        sumBtn = tk.Button(self, text="Go to the summary page",
                            command=lambda: self.controller.show_frame("Summary"))
        button = Button(self, text="submit", command=lambda: self.button_onclick(input, fail, suc,sumBtn))
        button.pack()

    def make_user_list(self):
        sql = "SELECT * FROM users"
        # run sql and fetch result
        mycursor.execute(sql)
        res = mycursor.fetchall()
        usernames = [name[0] for name in res]
        self.user_list = usernames
        self.name_hint = 'authorized users: '
        for ind, itm in enumerate(usernames):
            self.username_hint += str(itm)
            if ind < len(usernames) - 1:
                self.username_hint += ', '

    def button_onclick(self, input, fail, suc, button):
        username_input = input.get()

        # if first time clicked, run sql querry
            # sql = "SELECT count(*) FROM users Where username = '{username}'".format(username=username_input)
        if self.first_click:
            self.first_click = False
            self.make_user_list()
        
        # if not first time, check if input in list
        if username_input in self.user_list:
            suc.pack()
            fail.pack_forget()
            button.pack()
        else:
            hint_text = self.username_hint
            hint = Label(self, text =  hint_text, fg = "red", font = 14)
            fail.pack()
            hint.pack()
            suc.pack_forget()
            button.pack_forget()
        
        print(self.user_list)



class Summary(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight =1)
        self.columnconfigure(3, weight=1)
        label = tk.Label(self, text="Summary procedures", font=controller.title_font)
        label.grid(row = 0, column = 0, padx =50, pady= 50)
        sv = Label(self, text="Summary view", font=controller.title_font)
        sv.grid(row = 10, column = 0, padx =50, pady= 50)

        button1 = tk.Button(self, text="Add Owner",
                            command=lambda: controller.show_frame("AddOwner"))
        button2 = tk.Button(self, text="Add Employee",
                            command=lambda: controller.show_frame("AddEmployee"))
        button3 = tk.Button(self, text="Add Pilot Role",
                            command=lambda: controller.show_frame("AddPilotRole"))
        button4 = tk.Button(self, text="Add Worker Role",
                            command=lambda: controller.show_frame("AddWorkerRole"))
        button5 = tk.Button(self, text="Add Ingredient",
                            command=lambda: controller.show_frame("AddIngredient"))
        button6 = tk.Button(self, text="Add Drone",
                            command=lambda: controller.show_frame("AddDrone"))
        button7 = tk.Button(self, text="Add Restaurant",
                            command=lambda: controller.show_frame("AddRestaurant"))
        button8 = tk.Button(self, text="Add Service",
                            command=lambda: controller.show_frame("AddService"))
        button9 = tk.Button(self, text="Add Location",
                            command=lambda: controller.show_frame("AddLocation"))
        button10 = tk.Button(self, text="Start Funding",
                            command=lambda: controller.show_frame("StartFunding"))
        button11 = tk.Button(self, text="Hire Employee",
                            command=lambda: controller.show_frame("HireEmployee"))
        button12 = tk.Button(self, text="Fire Employee",
                            command=lambda: controller.show_frame("FireEmployee"))
        button13 = tk.Button(self, text="Manage Service",
                            command=lambda: controller.show_frame("ManageService"))
        button14 = tk.Button(self, text="Takeover Drone",
                            command=lambda: controller.show_frame("TakeoverDrone"))
        button15 = tk.Button(self, text="Join Swarm",
                            command=lambda: controller.show_frame("JoinSwarm"))
        button16 = tk.Button(self, text="Leave Swarm",
                            command=lambda: controller.show_frame("LeaveSwarm"))
        button17 = tk.Button(self, text="Load Drone",
                            command=lambda: controller.show_frame("LoadDrone"))
        button18 = tk.Button(self, text="Refuel Drone",
                            command=lambda: controller.show_frame("RefuelDrone"))
        button19 = tk.Button(self, text="Fly Drone",
                            command=lambda: controller.show_frame("FlyDrone"))
        button20 = tk.Button(self, text="Purchase Ingredient",
                            command=lambda: controller.show_frame("PurchaseIngredient"))
        button21 = tk.Button(self, text="Remove Ingredient",
                            command=lambda: controller.show_frame("RemoveIngredient"))
        button22 = tk.Button(self, text="Remove Drone",
                            command=lambda: controller.show_frame("RemoveDrone"))
        button23 = tk.Button(self, text="Remove Pilot Role",
                            command=lambda: controller.show_frame("RemovePilotRole"))
        button24 = tk.Button(self, text="Display Owner View",
                            command=lambda: controller.show_frame("DisplayOwnerView"))
        button25 = tk.Button(self, text="Display Employee View",
                            command=lambda: controller.show_frame("DisplayEmployeeView"))
        button26 = tk.Button(self, text="Display Pilot View",
                            command=lambda: controller.show_frame("DisplayPilotView"))
        button27 = tk.Button(self, text="Display Location View",
                            command=lambda: controller.show_frame("DisplayLocationView"))
        button28 = tk.Button(self, text="Display Ingredient View",
                            command=lambda: controller.show_frame("DisplayIngredientView"))
        button29 = tk.Button(self, text="Display Service View",
                            command=lambda: controller.show_frame("DisplayServiceView"))
        
        butList = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                button11, button12, button13, button14, button15, button16, button17, button18, button19,
                button20, button21, button22, button23]
        r = 3
        c =0
        for bl in butList:
            bl.grid(row = r,column = c)
            c = c +1
            if (c%4 == 0):
                r =r+1
                c = 0
        butList1 = [button24,button25,button26,button27,button28,button29]
        x = 11
        y = 0
        for bbl in butList1:
            bbl.grid(row = x,column = y)
            y = y +1
            if (y%4 == 0):
                x =x+1
                y = 0


#[3] add_pilot_role
class AddPilotRole(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Pilot Role", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        aprU = tk.Label(self, text = "Username: ")
        aprUE = tk.Entry(self, font = 14)
        aprLID = tk.Label(self, text = "License ID: ")
        aprLIDE = tk.Entry(self, font = 14)
        aprEx = tk.Label(self, text = "Experience: ")
        aprExE =  tk.Entry(self, font = 14)
        aprSuc = tk.Label(self, text = "You have successfully added a pilot!", fg = "green", font = 14)
        aprFail = tk.Label(self,text = "Warning! The pilot can not be added!", fg = "red", font = 14)
        aprSub = tk.Button(self, text = "Submit", command= lambda: AddPilotRole.aprSubFuc(apr_entry_list,aprSuc, aprFail))
        aprDone = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        apr_label_list = [aprU, aprLID,aprEx, aprSuc, aprFail,aprSub,aprDone]
        apr_entry_list = [aprUE, aprLIDE, aprExE]
        aprU.pack()
        aprUE.pack()
        aprLID.pack()
        aprLIDE.pack()
        aprEx.pack()
        aprExE.pack()
        aprSub.pack()
        aprDone.pack()

    def aprSubFuc(apr_entry_list,aprSuc, aprFail):
        mycursor.execute("select count(*) from pilots")
        aprOld = mycursor.fetchall()
        apr_args = []
        
        try:
            for en in apr_entry_list:
                apr_args.append(en.get())
            mycursor.callproc('add_pilot_role', apr_args)
            mydb.commit()
            argNew = mycursor.execute("select count(*) from pilots")

            if (aprOld == argNew):
                aprFail.pack()
            else:
                aprSuc.pack()
        except Exception:
            aprFail.pack()        
        finally:
            for en in apr_entry_list:
                en.delete(0, END)

#[19] fly_drone
class FlyDrone(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Fly Drone", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        myLabel = Label(self, text="Enter the service id and the tag of the drone you want to fly.")
        myLabel.pack()
        myLabel2 = Label(self, text="service id:")
        input = Entry(self, width=50)
        myLabel2.pack()
        input.pack()
        myLabel3 = Label(self, text="tag:")
        input2 = Entry(self, width=50)
        myLabel3.pack()
        input2.pack()
        myLabel5 = Label(self, text="Enter the destination:")
        input3 = Entry(self, width=50)
        myLabel5.pack()
        input3.pack()

        myButton = Button(self, text="Submit", command=lambda: FlyDrone.submit(self, input, input2, input3))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input2, input3):
        ip_id = input.get()
        ip_tag = input2.get()
        ip_dest = input3.get()
        sql = "call fly_drone('{id}', '{tag}', '{dest}')".format(id = ip_id, tag = ip_tag, dest = ip_dest)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This drone is not able to fly to this destination: {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This drone is not able to fly to this destination.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This drone is heading to {dest}, {rows} record(s) affected".format(dest = ip_dest, rows = count), fg="green")
                myLabel2.pack()

    
#[15] join_swarm
class JoinSwarm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Join Swarm", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the service id and the tag of the drone that you want it to leave its swarm.")
        myLabel.pack()
        myLabel2 = Label(self, text="service id:")
        input2 = Entry(self, width=50)
        myLabel2.pack()
        input2.pack()
        myLabel3 = Label(self, text="tag:")
        input3 = Entry(self, width=50)
        myLabel3.pack()
        input3.pack()

        myLabel4 = Label(self, text="Enter the tag of the swarm's leader drone:")
        input4 = Entry(self, width=50)
        myLabel4.pack()
        input4.pack()

        myButton = Button(self, text="Submit", command=lambda: JoinSwarm.submit(self, input2, input3, input4))
        myButton.pack()

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input2, input3, input4):
        ip_id = input2.get()
        ip_tag = input3.get()
        ip_swm_tag = input4.get()
        sql = "call join_swarm('{id}', '{tag}', '{swm_tag}')".format(id = ip_id, tag = ip_tag, swm_tag = ip_swm_tag)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This drone is not a valid drone to join the swarm: {err}".format(err = err), padx=30, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=30, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This drone is not a valid drone to join the swarm.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This drone has joined the swarm, {rows} record(s) affected".format(rows = count), fg="green")
                myLabel2.pack()

#[16] leave_swarm
class LeaveSwarm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Leave Swarm", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the service id and the tag of the drone that you want it to leave its swarm.")
        myLabel.pack()
        myLabel2 = Label(self, text="service id:")
        input2 = Entry(self, width=50)
        myLabel2.pack()
        input2.pack()
        myLabel3 = Label(self, text="tag:")
        input3 = Entry(self, width=50)
        myLabel3.pack()
        input3.pack()

        myButton = Button(self, text="Submit", command=lambda: LeaveSwarm.submit(self, input2, input3))
        myButton.pack()

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input2, input3):
        ip_id = input2.get()
        ip_tag = input3.get()
        sql = "call leave_swarm('{id}', '{tag}')".format(id = ip_id, tag = ip_tag)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This drone is not a valid drone to leave its swarm: {err}".format(err = err), padx=30, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=30, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This drone is not a valid drone to leave its swarm.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This drone has left its swarm, {rows} record(s) affected".format(rows = count), fg="green")
                myLabel2.pack()

#[9] add_location
class AddLocation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Location", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the label of the location:")
        myLabel.pack()

        myLabel2 = Label(self, text="location's label:")
        input = Entry(self, width=50)
        myLabel2.pack()
        input.pack()

        myLabel3 = Label(self, text="Enter the x coordinate:")
        myLabel3.pack()

        myLabel4 = Label(self, text="x:")
        input2 = Entry(self, width=50)
        myLabel4.pack()
        input2.pack()

        myLabel5 = Label(self, text="Enter the y coordinate:")
        myLabel5.pack()

        myLabel6 = Label(self, text="y:")
        input3 = Entry(self, width=50)
        myLabel6.pack()
        input3.pack()

        myLabel7 = Label(self, text="Enter the space(s) of this location:")
        myLabel7.pack()

        myLabel8 = Label(self, text="space(s):")
        input4 = Entry(self, width=50)
        myLabel8.pack()
        input4.pack()

        myButton = Button(self, text="Submit", command=lambda: AddLocation.submit(self, input, input2, input3, input4))
        myButton.pack()

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input2, input3, input4):
        ip_label = input.get()
        ip_x_coord = input2.get()
        ip_y_coord = input3.get()
        ip_space = input4.get()
        sql = "call add_location('{label}', '{x_coord}', '{y_coord}', '{space}')".format(label = ip_label, x_coord = ip_x_coord, y_coord = ip_y_coord, space = ip_space)

        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This location cannot be added. {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This location cannot be added.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="Location {label} is added to ({x_coord}, {y_coord}) with {space} spaces.".format(label = ip_label, x_coord = ip_x_coord, y_coord = ip_y_coord, space = ip_space), fg="green")
                myLabel2.pack()

#[10] start_funding
class StartFunding(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start Funding", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the username of the owner:")
        myLabel.pack()

        myLabel2 = Label(self, text="owner's username:")
        input = Entry(self, width=50)
        myLabel2.pack()
        input.pack()

        myLabel3 = Label(self, text="Enter the restaurant's name:")
        myLabel3.pack()

        myLabel4 = Label(self, text="restaurant's name:")
        input2 = Entry(self, width=50)
        myLabel4.pack()
        input2.pack()

        myButton = Button(self, text="Submit", command=lambda: StartFunding.submit(self, input, input2))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input2):
        ip_owner = input.get()
        ip_long_name = input2.get()
        sql = "call start_funding('{username}', '{long_name}')".format(username = ip_owner, long_name = ip_long_name)

        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This funding cannot be created. {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This funding cannot be created.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="Now, {long_name} is funded by {username}".format(long_name = ip_long_name, username = ip_owner), fg="green")
                myLabel2.pack()

#[11] hire_employee
class HireEmployee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hire Employee", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the username of the employee:")
        myLabel.pack()

        myLabel2 = Label(self, text="employess's username:")
        input = Entry(self, width=50)
        myLabel2.pack()
        input.pack()

        myLabel3 = Label(self, text="Enter the service's id:")
        myLabel3.pack()

        myLabel4 = Label(self, text="service's id:")
        input2 = Entry(self, width=50)
        myLabel4.pack()
        input2.pack()

        myButton = Button(self, text="Submit", command=lambda: HireEmployee.submit(self, input, input2))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input2):
        ip_username = input.get()
        ip_id = input2.get()
        sql = "call hire_employee('{username}', '{id}')".format(username = ip_username, id = ip_id)

        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This employment cannot be created. {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This employment cannot be created.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="Now, {username} works for service {id}".format(username = ip_username, id = ip_id), fg="green")
                myLabel2.pack()

#[12] fire_employee
class FireEmployee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Fire Employee", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the username of the employee:")
        myLabel.pack()

        myLabel2 = Label(self, text="employess's username:")
        input = Entry(self, width=50)
        myLabel2.pack()
        input.pack()

        myLabel3 = Label(self, text="Enter the service's id:")
        myLabel3.pack()

        myLabel4 = Label(self, text="service's id:")
        input2 = Entry(self, width=50)
        myLabel4.pack()
        input2.pack()

        myButton = Button(self, text="Submit", command=lambda: FireEmployee.submit(self, input, input2))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input2):
        ip_username = input.get()
        ip_id = input2.get()
        sql = "call fire_employee('{username}', '{id}')".format(username = ip_username, id = ip_id)

        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This employment cannot be ended. {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This employment cannot be ended.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="Now, {username} is fired from service {id}".format(username = ip_username, id = ip_id), fg="green")
                myLabel2.pack()

#[1] add_owner
class AddOwner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Owner", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        ao_label_list=[]
        ao_entry_list=[]
        aoUsername = Label(self, text = "username: ")
        aoUsernameE = Entry(self, font = 14)
        aoFName = Label(self, text = "First name: ")
        aoFNE = Entry(self, font = 14)
        aoLName = Label(self, text = "Last name: ")
        aoLNE = Entry(self, font = 14)
        aoAd= Label(self, text = "Address: ", width = 30)
        aoADE = Entry(self, font = 14)
        aoBdate = Label(self, text = "Birthdate: ")
        aoBDE = Entry(self, font = 14)
        aoSuc = Label(self, text = "The restaurant owner is added successfully!", fg = "green",font = 14)
        aoFail = Label(self, text ="Warning! The restaurant owner can not be added!",fg = "red", font = 14)
        aoClose = Button(self, text="Go to the summary page",
                            command=lambda: controller.show_frame("Summary"))
        aoSub = Button(self, text="Submit", command= lambda: AddOwner.subAO(ao_entry_list,aoFail, aoSuc))
        aoUsername.pack()
        aoUsernameE.pack()
        aoFName.pack()
        aoFNE.pack()
        aoLName.pack()
        aoLNE.pack()
        aoAd.pack()
        aoADE.pack()
        aoBdate.pack()
        aoBDE.pack()
        aoSub.pack()
        aoClose.pack()
        ao_label_list = [aoUsername, aoFName, aoLName, aoAd, aoADE, aoBdate,aoSub,aoSuc, aoFail, aoClose]
        ao_entry_list = [aoUsernameE, aoFNE, aoLNE, aoADE, aoBDE]



    def subAO(ao_entry_list, aoFail, aoSuc):
        mycursor.execute("SELECT COUNT(*) FROM restaurant_owners")
        aoOld  = mycursor.fetchall()
        aO_args =[]
        
        try:
            for en in ao_entry_list:
                aO_args.append(en.get())
            mycursor.callproc('add_owner', aO_args )
            mydb.commit()
            mycursor.execute("SELECT COUNT(*) FROM restaurant_owners")
            aoNew = mycursor.fetchall()

            if (aoOld == aoNew):
                aoFail.pack()
            else: 
                aoSuc.pack()
        except Exception:  
            aoFail.pack()
        finally:
            for en in ao_entry_list:
                en.delete(0, END)

#[29] display_service_view
class DisplayServiceView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Service View", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        tree = ttk.Treeview(self)
        
        tree['columns'] = ("c1","c2","c3","c4","c5","c6","c7","c8") 
        tree.column("#0", width=0, minwidth=0)
        tree.column("c1", anchor=W, width=120, minwidth=30)
        tree.column("c2", anchor=W, width=120, minwidth=150)
        tree.column("c3", anchor=W, width=120, minwidth=80)
        tree.column("c4", anchor=W, width=120, minwidth=80)
        tree.column("c5", anchor=W, width=120, minwidth=80)
        tree.column("c6", anchor=W, width=120, minwidth=80)
        tree.column("c7", anchor=W, width=120, minwidth=80)
        tree.column("c8", anchor=W, width=120, minwidth=80)

        tree.heading("c1", text="id", anchor = CENTER)
        tree.heading("c2", text="label", anchor = CENTER)
        tree.heading("c3", text="location", anchor = CENTER)
        tree.heading("c4", text="manager", anchor = CENTER)
        tree.heading("c5", text="revenue", anchor = CENTER)
        tree.heading("c6", text="ingredients", anchor = CENTER)
        tree.heading("c7", text="cost", anchor = CENTER)
        tree.heading("c8", text="weight", anchor = CENTER)
        sql = "select * from display_service_view"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        for row in rows:
            #print(row)
            tree.insert("", tk.END, values=row)
        tree.pack()    
        backButton = Button(self, text="Go to Summary", command=lambda: controller.show_frame("Summary"))
        backButton.pack()

#[2] add_employee
class AddEmployee(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Employee", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        myLabel = Label(self, text="Enter the Username, First Name, Last Name, Address, Birth date, Tax ID, Hire date, "
                                   "Employee experience and Salary")
        myLabel.pack()
        myLabel1 = Label(self, text="username:")
        input1 = Entry(self, width=50)
        myLabel1.pack()
        input1.pack()

        myLabel2 = Label(self, text="first name:")
        input2 = Entry(self, width=50)
        myLabel2.pack()
        input2.pack()

        myLabel3 = Label(self, text="last name:")
        input3 = Entry(self, width=50)
        myLabel3.pack()
        input3.pack()

        myLabel4 = Label(self, text="address:")
        input4 = Entry(self, width=50)
        myLabel4.pack()
        input4.pack()

        myLabel5 = Label(self, text="birth date:")
        input5 = Entry(self, width=50)
        myLabel5.pack()
        input5.pack()

        myLabel6 = Label(self, text="tax ID:")
        input6 = Entry(self, width=50)
        myLabel6.pack()
        input6.pack()

        myLabel7 = Label(self, text="hire date:")
        input7 = Entry(self, width=50)
        myLabel7.pack()
        input7.pack()

        myLabel8 = Label(self, text="employee experience:")
        input8 = Entry(self, width=50)
        myLabel8.pack()
        input8.pack()

        myLabel9 = Label(self, text="salary:")
        input9 = Entry(self, width=50)
        myLabel9.pack()
        input9.pack()

        myButton = Button(self, text="Submit", command=lambda: self.submit(input1, input2, input3,input4, input5, input6, input7, input8, input9))

        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input1, input2, input3, input4, input5, input6, input7, input8, input9):
        ip_username = input1.get()
        ip_fname = input2.get()
        ip_lname = input3.get()
        ip_address = input4.get()
        ip_bdate = input5.get()
        ip_taxid = input6.get()
        ip_hiredate = input7.get()
        ip_experience = input8.get()
        ip_salary = input9.get()

        sql = "call add_employee('{username}', '{fname}', '{lname}', '{address}', '{bdate}', '{taxid}', '{hiredate}', \
        '{experience}', '{salary}' )".format(username=ip_username, fname=ip_fname, lname=ip_lname, address=ip_address, \
                bdate=ip_bdate, taxid=ip_taxid, hiredate=ip_hiredate, experience=ip_experience, salary=ip_salary)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This employee is not able to be added: {err}".format(err=err),
                            padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp=excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This employee is not able to get added.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This employee is added, {rows} record(s) affected".format(
                     rows=count), fg="green")
                myLabel2.pack()

#[7] add_restaurant
class AddRestaurant(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Restaurant", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        myLabel = Label(self, text="Enter the restaurant Long Name, Rating, Money Spent, Location")
        myLabel.pack()
        myLabel1 = Label(self, text="longName:")
        input1 = Entry(self, width=50)
        myLabel1.pack()
        input1.pack()

        myLabel2 = Label(self, text="rating:")
        input2 = Entry(self, width=50)
        myLabel2.pack()
        input2.pack()

        myLabel3 = Label(self, text="spent:")
        input3 = Entry(self, width=50)
        myLabel3.pack()
        input3.pack()

        myLabel4 = Label(self, text="location:")
        input4 = Entry(self, width=50)
        myLabel4.pack()
        input4.pack()

        myButton = Button(self, text="Submit", command=lambda: self.submit(input1, input2, input3, input4))

        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input1, input2, input3, input4):
        ip_longName = input1.get()
        ip_rating = input2.get()
        ip_spent = input3.get()
        ip_location = input4.get()

        sql = "call add_restaurant('{input1}', '{input2}', '{input3}', '{input4}' )".format(input1=ip_longName, input2=ip_rating, input3=ip_spent, input4=ip_location)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This restaurant is not able to be added: {err}".format(err=err),
                            padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp=excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This restaurant is not able to get added.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This restaurant is added, {rows} record(s) affected".format(
                     rows=count), fg="green")
                myLabel2.pack()

#[6] add_drone
class AddDrone(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Drone", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        ad_label_list=[]
        ad_entry_list =[] 
        adId = tk.Label(self, text = "Service ID: ")
        adIdE = tk.Entry(self, font = 14)
        adTag = tk.Label(self, text = "Drone Tag: ")
        adTagE =tk. Entry(self, font = 14)
        adIp = tk.Label(self, text = "Fuel: ")
        adIpE = tk. Entry(self, font = 14)
        adCap = tk.Label(self, text = "Capacity: ")
        adCapE= tk.Entry(self, font = 14)
        adSa = tk.Label(self, text = "Sales: ")
        adSaE = tk.Entry(self, font = 14)
        adFb = tk.Label(self, text = "Flown by ")
        adFbE= tk. Entry(self, font = 14)
        adSuc = tk.Label (self, text = "You have successfully add the drone!", fg = "green", font = 14)
        adFail = tk.Label (self, text = "Warning! The drone can not be added to the list!", fg= "red", font = 14)
        adSub = tk.Button(self, text = "Submit", command = lambda: AddDrone.adSubFuc(ad_entry_list, adSuc, adFail))
        adDone = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        ad_label_list = [adId, adTag, adIp, adCap, adSa, adFb, adSuc, adFail, adSub, adDone]
        ad_entry_list = [adIdE, adTagE, adIpE, adCapE, adSaE, adFbE]
        adId.pack()
        adIdE.pack()
        adTag.pack()
        adTagE.pack()
        adIp.pack()
        adIpE.pack()
        adCap.pack()
        adCapE.pack()
        adSa.pack()
        adSaE.pack()
        adFb.pack()
        adFbE.pack()
        adSub.pack()
        adDone.pack()

    def adSubFuc(ad_entry_list, adSuc, adFail):
        mycursor.execute("select count(*) from drones")
        adOld = mycursor.fetchall()
        ad_args = []
        try:
            for en in ad_entry_list:
                ad_args.append(en.get())

            mycursor.callproc('add_drone', ad_args)
            mydb.commit()
            mycursor.execute("select count(*) from drones")
            adNew = mycursor.fetchall()
            if (adOld == adNew):
                adFail.pack()
            else:
                adSuc.pack()
        except Exception:
            adFail.pack()
        finally:
            for en in ad_entry_list:
                en.delete(0,END)

#[5] add_ingredient
#####[5] add_ingredient add_ingredient (in ip_barcode varchar(40), in ip_iname varchar(100),
##                                    in ip_weight integer)
class AddIngredient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        ai_entry_list = []
        ai_label_list = []
        label = tk.Label(self, text="Add Ingredient", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        aiBar = tk.Label(self, text = "Barcode: ", font = "14")
        aiBarE = tk.Entry(self, font = 14 )
        aii = tk.Label(self, text = "Ingredient Name: ", font = 14)
        aiiE = tk.Entry(self, font = 14)
        aiWei = tk.Label(self, text = "Weight; ", font = 14)
        aiWeiE =tk. Entry(self, font = 14)
        aiSuc = tk.Label (self, text = "You have successfully add the ingredient!", fg = "green", font = 14)
        aiFail =tk. Label (self, text = "Warning! The ingredient can not be added to the list!", fg= "red", font = 14)
        aiSub = tk.Button(self, text = "Submit", command = lambda: AddIngredient.aiSubFuc(ai_entry_list, aiSuc, aiFail))
        aiDone =tk. Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        ai_label_list = [aiBar, aii, aiWei, aiSub, aiDone, aiSuc, aiFail]
        ai_entry_list = [aiBarE, aiiE, aiWeiE]
        aiBar.pack()
        aiBarE.pack()
        aii.pack()
        aiiE.pack()
        aiWei.pack()
        aiWeiE.pack()
        aiSub.pack()
        aiDone.pack()


    def aiSubFuc(ai_entry_list, aiSuc, aiFail):
        mycursor.execute("select count(*) from ingredients")
        aiOld = mycursor.fetchall()
        aiArg = []
        try:
            for en in ai_entry_list:
                aiArg.append(en.get())
            mycursor.callproc('add_ingredient', aiArg)
            mydb.commit()
            mycursor.execute("select count(*) from ingredients")
            aiNew = mycursor.fetchall()
            if (aiOld == aiNew):
                aiFail.pack()
            else:
                aiSuc.pack()
        except Exception:
            aiFail.pack()
        finally:
            for en in ai_entry_list:
                en.delete(0, END)

#[8] add_service
#### [8]add_service()in ip_id varchar(40), in ip_long_name varchar(100),
# in ip_home_base varchar(40), in ip_manager varchar(40)
class AddService(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        as_entry_list=[]
        as_label_list=[]
        label = tk.Label(self, text="Add Service", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        asId = tk.Label(self, text = "ID: ")
        asIDE = tk.Entry(self, font = 14)
        asLN = tk.Label(self, text = "Service name: ")
        asLNE = tk.Entry(self,font = 14 )
        asHb = tk.Label(self, text = "Homebase: ")
        asHbE = tk.Entry(self, font = 14)
        asM = tk.Label(self,text = "Manager: " )
        asME = tk.Entry(self, font = 14)
        asFail =tk. Label(self, text = "Warning! The service can not be added!", fg = "red")
        asSuc =tk. Label(self, text = "The service is added successfully", fg = "green")
        asSub = tk.Button (self, text = 'Submit', command= lambda: AddService.asSubmit(as_entry_list, asSuc, asFail))
        asDone =tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        as_entry_list = [asIDE, asLNE, asHbE, asME]
        as_label_list = [asId, asLN, asHb, asM, asFail, asSuc, asSub, asDone]
        asId.pack()
        asIDE.pack()
        asLN.pack()
        asLNE.pack()
        asHb.pack()
        asHbE.pack()
        asM.pack()
        asME.pack()
        asSub.pack()
        asDone.pack()

    def asSubmit(as_entry_list, asSuc, asFail):
        as_args = []
        mycursor.execute("select count(*) from delivery_services")
        asOld = mycursor.fetchall()
        try:
            for en in as_entry_list:
                as_args.append(en.get())
            #print(as_args)
            mycursor.callproc('add_service', as_args)
            mydb.commit()
            mycursor.execute("select count(*) from delivery_services")
            asNew = mycursor.fetchall()

            if (asNew == asOld):
                asFail.pack()
            else: 
                asSuc.pack()
        except Exception:
            asFail.pack()
        finally:
            for en in as_entry_list:
                en.delete(0, END)

#[17] load_drone
class LoadDrone(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Load Drone", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel2 = Label(self, text="Enter the service id and the tag of the drone that will carry these packages.")
        myLabel2.pack()
        #id 1
        myLabel3 = Label(self, text="service id:")
        input = Entry(self, width=50)
        myLabel3.pack()
        input.pack()
        #tag 2
        myLabel4 = Label(self, text="tag:")
        input2 = Entry(self, width=50)
        myLabel4.pack()
        input2.pack()

        myLabel5 = Label(self, text="Enter the barcode, the number of packaged, and the price of the ingredient being added.")
        myLabel5.pack()
        #barcode 3
        myLabel6 = Label(self, text="barcode:")
        input3 = Entry(self, width=50)
        myLabel6.pack()
        input3.pack()
        #pkg 4
        myLabel8 = Label(self, text="number of added packages:")
        input4 = Entry(self, width=50)
        myLabel8.pack()
        input4.pack()
        #price 5
        myLabel7 = Label(self, text="price:")
        input5 = Entry(self, width=50)
        myLabel7.pack()
        input5.pack()

        myButton = Button(self, text="Submit", command=lambda: LoadDrone.submit(self, input, input2, input3, input4, input5))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input2, input3, input4, input5):
        ip_id = input.get()
        ip_tag = input2.get()
        ip_barcode = input3.get()
        ip_pkg = input4.get()
        ip_price = input5.get()
        sql = "call load_drone('{id}', '{tag}', '{barcode}', '{pkg}', '{price}')".format(\
                id = ip_id, tag = ip_tag, barcode = ip_barcode, pkg = ip_pkg, price = ip_price)
        #print(sql)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="These packages cannot be added to this drone: {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="These packages cannot be added to this drone.", fg="red")
                myLabel2.pack()
            else: 
                myLabel2 = Label(self, text="These packages are added to [{id} {tag}], {rows} record(s) affected".format(\
                    id = ip_id, tag = ip_tag, rows = count), fg="green")
                myLabel2.pack()

#[4] add_worker_role
class AddWorkerRole(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        aw_entry_list = []
        aw_label_list = []
        AWLabel = tk.Label(self, text = "Add worker Role", font = controller.title_font).pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text = "Enter worker username")
        label2 = tk.Label(self, text = "The worker is added successfully", font = 40, fg="green")
        label3 = tk.Label(self, text = "The worker can not be added", font = 40, fg="red")
        entry1 = tk.Entry(self, font = 40)
        subButton = Button(self, text = "submit", command= lambda:AddWorkerRole.sub(aw_entry_list, label2, label3))
        done1 = Button(self, text = "Go to the summary page", command=lambda: controller.show_frame("Summary"))
        aw_label_list = [label1, label2,label3, subButton, done1]
        aw_entry_list = [entry1]
        label1.pack()
        entry1.pack()
        subButton.pack()
        done1.pack()
     
    def sub(aw_entry_list, label2, label3):
        mycursor.execute("select count(* )from workers")
        old = mycursor.fetchall()
        try:
            n = aw_entry_list[0].get()
            mycursor.callproc('add_worker_role', [n])
            mydb.commit()
            mycursor.execute("select count(*)from workers")
            new = mycursor.fetchall()
            if(new == old):
                label3.pack()
            else:
                label2.pack()
        except Exception:
            label2.pack()        
        finally:
            for en in aw_entry_list:
                en.delete(0, END)

#[18] refuel_drone
class RefuelDrone(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Refuel Drone", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        myLabel = Label(self, text="Enter the service id and the tag of the drone you want to refuel.")
        myLabel.pack()
        myLabel2 = Label(self, text="service id:")
        input = Entry(self, width=50)
        myLabel2.pack()
        input.pack()
        myLabel3 = Label(self, text="tag:")
        input2 = Entry(self, width=50)
        myLabel3.pack()
        input2.pack()
        myLabel5 = Label(self, text="Enter the amount of the added fuel:")
        input3 = Entry(self, width=50)
        myLabel5.pack()
        input3.pack()

        myButton = Button(self, text="Submit", command=lambda: RefuelDrone.submit(self, input, input2, input3))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input2, input3):
        ip_id = input.get()
        ip_tag = input2.get()
        ip_fuel = input3.get()
        sql = "call refuel_drone('{id}', '{tag}', '{fuel}')".format(id = ip_id, tag = ip_tag, fuel = ip_fuel)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This drone is not valid to be refueled: {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This drone is not valid to be refueled.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="{fuel} more fuel is added, {rows} record(s) affected".format(fuel = ip_fuel, rows = count), fg="green")
                myLabel2.pack()

#[18] purchase_ingredient
class PurchaseIngredient(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Purchase Ingredient", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the name of the restaurant that makes the purchase:")
        input = Entry(self, width=50)
        myLabel.pack()
        input.pack()

        myLabel2 = Label(self, text="Enter the service id and the tag of the drone that carries the ingredients being purchased.")
        myLabel2.pack()
        myLabel3 = Label(self, text="service id:")
        input3 = Entry(self, width=50)
        myLabel3.pack()
        input3.pack()
        myLabel4 = Label(self, text="tag:")
        input4 = Entry(self, width=50)
        myLabel4.pack()
        input4.pack()

        myLabel5 = Label(self, text="Enter the barcode and the quantity of the ingredient being purchased.")
        myLabel5.pack()
        myLabel6 = Label(self, text="barcode:")
        input6 = Entry(self, width=50)
        myLabel6.pack()
        input6.pack()
        myLabel7 = Label(self, text="quantity:")
        input7 = Entry(self, width=50)
        myLabel7.pack()
        input7.pack()

        myButton = Button(self, text="Submit", command=lambda: PurchaseIngredient.submit(self, input, input3, input4, input6, input7))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input, input3, input4, input6, input7):
        ip_long_name = input.get()
        ip_id = input3.get()
        ip_tag = input4.get()
        ip_barcode = input6.get()
        ip_quantity = input7.get()
        sql = "call purchase_ingredient('{long_name}', '{id}', '{tag}', \
            '{barcode}', '{quantity}')".format(long_name = ip_long_name, \
                id = ip_id, tag = ip_tag, barcode = ip_barcode, quantity = ip_quantity)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This ingredient is not a valid ingredient to purchase: {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This ingredient is not a valid ingredient to purchase.", fg="red")
                myLabel2.pack()
            else: 
                myLabel2 = Label(self, text="This ingredient is purchased by {restaurant}, {rows} record(s) affected".format(\
                    restaurant = ip_long_name, rows = count), fg="green")
                myLabel2.pack()

#[13] manage_service
class ManageService(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Manage Service", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        myLabel = Label(self, text="Enter the Username, Service ID")
        myLabel.pack()
        myLabel1 = Label(self, text="username:")
        input1 = Entry(self, width=50)
        myLabel1.pack()
        input1.pack()

        myLabel2 = Label(self, text="service id:")
        input2 = Entry(self, width=50)
        myLabel2.pack()
        input2.pack()

        myButton = Button(self, text="Submit", command=lambda: self.submit(input1, input2))

        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input1, input2):
        ip_username = input1.get()
        ip_serviceID = input2.get()

        sql = "call manage_service('{input1}', '{input2}')".format(input1=ip_username, input2=ip_serviceID)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This service is not able to be managed due to error: {err}".format(err=err),
                            padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp=excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This service is not able to get managed.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This {username} is managing {serviceID}".format(
                     username=ip_username, serviceID = ip_serviceID), fg="green")
                myLabel2.pack()

#[21] remove_ingredient
class RemoveIngredient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Remove Ingredient", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the barcode of the ingredient that you want to remove:")
        input = Entry(self, width=50)
        myLabel.pack()
        input.pack()

        myButton = Button(self, text="Submit", command=lambda: RemoveIngredient.submit(self, input))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input):
        ip_barcode = input.get()
        sql = "call remove_ingredient('{barcode}')".format(barcode = ip_barcode)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This ingredient is not a valid ingredient to remove: {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This ingredient is not a valid ingredient to remove.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This ingredient is removed, {rows} record(s) affected".format(rows = count), fg="green")
                myLabel2.pack()

#[22] remove_drone
class RemoveDrone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Remove Drone", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the service id and the tag of the drone that you want to remove.")
        myLabel.pack()
        myLabel2 = Label(self, text="service id:")
        input2 = Entry(self, width=50)
        myLabel2.pack()
        input2.pack()
        myLabel3 = Label(self, text="tag:")
        input3 = Entry(self, width=50)
        myLabel3.pack()
        input3.pack()

        myButton = Button(self, text="Submit", command=lambda: RemoveDrone.submit(self, input2, input3))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input2, input3):
        ip_id = input2.get()
        ip_tag = input3.get()
        sql = "call remove_drone('{id}', '{tag}')".format(id = ip_id, tag = ip_tag)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This drone is not a valid drone to remove: {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This drone is not a valid drone to remove.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This drone is removed, {rows} record(s) affected".format(rows = count), fg="green")
                myLabel2.pack()

#[22] remove_pilot_role
class RemovePilotRole(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Remove Pilot Role", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        myLabel = Label(self, text="Enter the username of the person that you want to remove from pilor role:")
        input = Entry(self, width=50)
        myLabel.pack()
        input.pack()

        myButton = Button(self, text="Submit", command=lambda: RemovePilotRole.submit(self, input))
        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input):
        ip_username = input.get()
        sql = "call remove_pilot_role('{username}')".format(username = ip_username)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This person is not a valid pilot to remove: {err}".format(err = err), padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp = excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This person is not a valid pilot to remove.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="This person is removed from pilot, {rows} record(s) affected".format(rows = count), fg="green")
                myLabel2.pack()

#[25] display_employee_view
class DisplayEmployeeView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Employee View", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        tree_frame = Frame(self)
        tree_frame.pack(pady=20)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

        tree_scroll.config(command=tree.yview)
    
        tree['columns'] = ("c1","c2","c3","c4","c5","c6","c7","c8")
        tree.column("#0", width=0, minwidth=0)
        tree.column("c1", anchor=W, width=100, minwidth=100)
        tree.column("c2", anchor=W, width=100, minwidth=100)
        tree.column("c3", anchor=W, width=80, minwidth=80)
        tree.column("c4", anchor=W, width=90, minwidth=90)
        tree.column("c5", anchor=W, width=130, minwidth=130)
        tree.column("c6", anchor=W, width=80, minwidth=80)
        tree.column("c7", anchor=W, width=120, minwidth=120)
        tree.column("c8", anchor=W, width=100, minwidth=100)

        tree.heading("c1", text="username", anchor=CENTER)
        tree.heading("c2", text="taxID", anchor=CENTER)
        tree.heading("c3", text="salary", anchor=CENTER)
        tree.heading("c4", text="hired", anchor=CENTER)
        tree.heading("c5", text="employee_experience", anchor=CENTER)
        tree.heading("c6", text="license_ID", anchor=CENTER)
        tree.heading("c7", text="piloting_experience", anchor=CENTER)
        tree.heading("c8", text="manager_status", anchor=CENTER)

        tree.pack()

        sql = "select * from display_employee_view"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        for row in rows:
            #print(row)
            tree.insert("", tk.END, values=row)

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

#[24] display_owner_view
class DisplayOwnerView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Owner View", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        tree_frame = Frame(self)
        tree_frame.pack(pady=20)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

        tree_scroll.config(command=tree.yview)

        tree['columns'] = ("c1","c2","c3","c4","c5","c6","c7","c8","c9")
        tree.column("#0", width=0, minwidth=0)
        tree.column("c1", anchor=W, width=80, minwidth=80)
        tree.column("c2", anchor=W, width=80, minwidth=80)
        tree.column("c3", anchor=W, width=80, minwidth=80)
        tree.column("c4", anchor=W, width=150, minwidth=150)
        tree.column("c5", anchor=W, width=110, minwidth=110)
        tree.column("c6", anchor=W, width=90, minwidth=90)
        tree.column("c7", anchor=W, width=50, minwidth=50)
        tree.column("c8", anchor=W, width=50, minwidth=50)
        tree.column("c9", anchor=W, width=50, minwidth=50)

        tree.heading("c1", text="username", anchor=CENTER)
        tree.heading("c2", text="firs_name", anchor=CENTER)
        tree.heading("c3", text="last_name", anchor=CENTER)
        tree.heading("c4", text="address", anchor=CENTER)
        tree.heading("c5", text="num_restaurants", anchor=CENTER)
        tree.heading("c6", text="num_places", anchor=CENTER)
        tree.heading("c7", text="highs", anchor=CENTER)
        tree.heading("c8", text="lows", anchor=CENTER)
        tree.heading("c9", text="debt", anchor=CENTER)

        tree.pack()

        sql = "select * from display_owner_view"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        for row in rows:
            #print(row)
            tree.insert("", tk.END, values=row)

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

#[23] display_pilot_view
class DisplayPilotView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pilot View", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        tree_frame = Frame(self)
        tree_frame.pack(pady=20)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

        tree_scroll.config(command=tree.yview)

        tree['columns'] = ("c1","c2","c3","c4","c5")
        tree.column("#0", width=0, minwidth=0)
        tree.column("c1", anchor=W, width=100, minwidth=100)
        tree.column("c2", anchor=W, width=100, minwidth=100)
        tree.column("c3", anchor=W, width=100, minwidth=100)
        tree.column("c4", anchor=W, width=100, minwidth=100)
        tree.column("c5", anchor=W, width=100, minwidth=100)

        tree.heading("c1", text="username", anchor=CENTER)
        tree.heading("c2", text="licenseID", anchor=CENTER)
        tree.heading("c3", text="experience", anchor=CENTER)
        tree.heading("c4", text="num_drones", anchor=CENTER)
        tree.heading("c5", text="num_locations", anchor=CENTER)

        tree.pack()

        sql = "select * from display_pilot_view"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        for row in rows:
            #print(row)
            tree.insert("", tk.END, values=row)

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

#[29] display_ingredient_view
class DisplayIngredientView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ingredient View", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        tree_frame = Frame(self)
        tree_frame.pack(pady=20)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

        tree_scroll.config(command=tree.yview)

        tree['columns'] = ("c1","c2","c3","c4","c5")
        tree.column("#0", width=0, minwidth=0)
        tree.column("c1", anchor=W, width=120, minwidth=120)
        tree.column("c2", anchor=W, width=100, minwidth=100)
        tree.column("c3", anchor=W, width=120, minwidth=120)
        tree.column("c4", anchor=W, width=100, minwidth=100)
        tree.column("c5", anchor=W, width=100, minwidth=100)

        tree.heading("c1", text="ingredient_name", anchor=CENTER)
        tree.heading("c2", text="location", anchor=CENTER)
        tree.heading("c3", text="amount_available", anchor=CENTER)
        tree.heading("c4", text="low_price", anchor=CENTER)
        tree.heading("c5", text="high_price", anchor=CENTER)

        tree.pack()

        sql = "select * from display_ingredient_view"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        for row in rows:
            #print(row)
            tree.insert("", tk.END, values=row)

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

#[28] display_location_view
class DisplayLocationView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Location View", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        tree_frame = Frame(self)
        tree_frame.pack(pady=20)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

        tree_scroll.config(command=tree.yview)
        
        tree['columns'] = ("c1","c2","c3","c4","c5","c6")
        tree.column("#0", width=0, minwidth=0)
        tree.column("c1", anchor=W, width=100, minwidth=100)
        tree.column("c2", anchor=W, width=80, minwidth=80)
        tree.column("c3", anchor=W, width=80, minwidth=80)
        tree.column("c4", anchor=W, width=120, minwidth=120)
        tree.column("c5", anchor=W, width=130, minwidth=130)
        tree.column("c6", anchor=W, width=100, minwidth=100)

        tree.heading("c1", text="label", anchor=CENTER)
        tree.heading("c2", text="x_coord", anchor=CENTER)
        tree.heading("c3", text="y_coord", anchor=CENTER)
        tree.heading("c4", text="num_restaurants", anchor=CENTER)
        tree.heading("c5", text="num_delivery_services", anchor=CENTER)
        tree.heading("c6", text="num_drones", anchor=CENTER)

        tree.pack()

        sql = "select * from display_location_view"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        for row in rows:
            #print(row)
            tree.insert("", tk.END, values=row)

        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

#[14] takeover_drone
class TakeoverDrone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Take over Drone", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        myLabel = Label(self, text="Enter the Username, service id, drone tag")
        myLabel.pack()

        myLabel1 = Label(self, text="username:")
        input1 = Entry(self, width=50)
        myLabel1.pack()
        input1.pack()

        myLabel2 = Label(self, text="service id:")
        input2 = Entry(self, width=50)
        myLabel2.pack()
        input2.pack()

        myLabel3 = Label(self, text="drone tag:")
        input3 = Entry(self, width=50)
        myLabel3.pack()
        input3.pack()

        myButton = Button(self, text="Submit", command=lambda: self.submit(input1, input2, input3))

        myButton.pack()
        button = tk.Button(self, text="Go to the summary page",
                           command=lambda: controller.show_frame("Summary"))
        button.pack()

    def submit(self, input1, input2, input3):
        ip_username = input1.get()
        ip_serviceID = input2.get()
        ip_droneTag = input3.get()

        sql = "call takeover_drone('{input1}', '{input2}', '{input3}')".format(input1=ip_username, input2=ip_serviceID, input3=ip_droneTag)
        try:
            mycursor.execute(sql)
            mydb.commit()
            count = mycursor.rowcount
        except mysql.connector.Error as err:
            myMes = Message(self, text="This drone is not a valid drone to be taken over by the pilot: {err}".format(err=err),
                            padx=70, fg="red")
            myMes.pack()
        except Exception as excp:
            myMes2 = Message(self, text="Something went wrong: {excp}".format(excp=excp), padx=70, fg="red")
            myMes2.pack()
        else:
            if count == 0:
                myLabel2 = Label(self, text="This drone is not a valid drone to be taken over by the pilot.", fg="red")
                myLabel2.pack()
            else:
                myLabel2 = Label(self, text="The pilot {username} has taken over this drone {serviceID} {droneTag}, {count} record(s) affected".format(
                     username=ip_username, serviceID = ip_serviceID, droneTag = ip_droneTag, count = count), fg="green")
                myLabel2.pack()

if __name__ == "__main__":
    app = DatabaseGUI()
    app.mainloop()
