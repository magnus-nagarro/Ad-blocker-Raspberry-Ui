from __init__ import *

# --> Initalizes all Elements of the Welcomepage/Ip entry:
class Welcomepage(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("384x308")
        self.title("Welcome")
        
        
        self.image_label = customtkinter.CTkLabel(self, width=128,text="", image= images.logo)
        self.image_label.place(x=128,y=0)

        self.welcome_label = customtkinter.CTkLabel(self, width=384,text="Welcome to Adblocker!",fg_color=("transparent"),text_color="white", corner_radius= 5, font=("Arial", 20))
        self.welcome_label.place(x=0,y=140)

        self.Ip_text_label = customtkinter.CTkLabel(self, width=384,text="In order to ensure error-free operation, please enter the IP address \n of the device on which the blocker software is running \n in the field below.",fg_color=("transparent"),text_color="white", corner_radius= 5, font=("Arial", 12))
        self.Ip_text_label.place(x=0,y=175)

        self.ip_entry = customtkinter.CTkEntry(self, placeholder_text="Enter IP-Adress", width= 128)
        self.ip_entry.place(x=100,y=230)

        self.error_label = customtkinter.CTkLabel(self, text="")
        self.error_label.place(x=0,y=275)

        self.start_button = customtkinter.CTkButton(self, width=50, text="Start", command = self.start_button_action, image= images.start_image)
        self.start_button.place(x=233,y=230)

        self.go_button = ui.customtkinter.CTkButton(self, width=50, text="Start", command = self.go_button_action)
        
        self.toplevel_window = None

    # Starting User Interface if IP already exists:
    def start_button_action(self):
        hosturl = self.ip_entry.get()

        url= f"http://{hosturl}/blocked"

        try:
            response = requests.get(url)
        except:
            self.error_label.configure(width=384,text="It seems, that something went wrong wile connecting to Ad-Blocker. \n Please verify if IP-adress is correct and the blocker is running",fg_color=("red"),text_color="white", corner_radius= 5, font=("Arial", 12))

        if response.status_code == 200:  
            self.withdraw()
            self.error_label.place_forget()

            with open('ip.cfg', 'w') as f:
                json.dump(hosturl, f)

            self.toplevel_window = ui.UserInterface(self)
            ui.UserInterface.start(self.toplevel_window)
        
        else:
            self.error_label.configure(width=384,text="It seems, that something went wrong wile connecting to Ad-Blocker. \n Please verify if IP-adress is correct and the blocker is running",fg_color=("red"),text_color="white", corner_radius= 5, font=("Arial", 12))
    
    # Starting User Interface after IP entry:
    def go_button_action(self):
        self.toplevel_window = ui.UserInterface(self)
        ui.UserInterface.start(self.toplevel_window)
        self.withdraw()

    # Starting the Ip Entry, checking if the Ip-adress is correct, and starting the program if everything is ok
    def start(self):
        with open("ip.cfg", "r") as f:
            url = json.load(f)

        if url == "":
           self.mainloop()
        else:
            link = f"http://{url}/blocked"
            try:
                response = requests.get(link)
            except:
                self.error_label.configure(width=384,text="It seems, that something went wrong wile connecting to Ad-Blocker. \n Please verify if IP-adress is correct and the blocker is running",fg_color=("red"),text_color="white", corner_radius= 5, font=("Arial", 12))
                self.mainloop()

            if response.status_code == 200:  
                self.error_label.place_forget()
                self.ip_entry.place_forget()
                self.Ip_text_label.configure(text="Your Ip Adress is correct. Please press Start to continue")
                self.start_button.place_forget()
                self.go_button.place(x=167,y=230)
                self.mainloop()
        
            else:
                self.error_label.configure(width=384,text="It seems, that something went wrong wile connecting to Ad-Blocker. \n Please verify if IP-adress is correct and the blocker is running",fg_color=("red"),text_color="white", corner_radius= 5, font=("Arial", 12))
                self.mainloop()
    

wp = Welcomepage()
wp.start()