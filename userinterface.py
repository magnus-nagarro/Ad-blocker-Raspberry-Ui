from  __init__ import *

# --> Initalizing Elements of Home-Frame:
class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initalizing Tabview Widget:
        self.tabview = customtkinter.CTkTabview(self,width=440, border_color=("#1F538D"), border_width=1, anchor="nw")
        self.tabview.place(x=5,y=0)
        self.tabview.add("Statistics")  
        self.tabview.add("Import/Export")  
        self.tabview.set("Statistics")  

        self.tabview1 = customtkinter.CTkTabview(self,width=440, height = 300, border_color=("#1F538D"), border_width=1, anchor="nw")
        self.tabview1.place(x=5,y=250)
        self.tabview1.add("blocked Links")



        # --> Initalizing Elements of Tabview

        self.link_entry = customtkinter.CTkEntry(self.tabview.tab("Import/Export"), placeholder_text="Please enter a Link", width= 350)
        self.link_entry.place(x=10,y=10)

        self.import_button = customtkinter.CTkButton(self.tabview.tab("Import/Export"), width= 50, text="Add", command = self.import_button_action)
        self.import_button.place(x=365,y=10)

        self.import_status_label = customtkinter.CTkLabel(self.tabview.tab("Import/Export"), width = 405, fg_color="transparent", corner_radius=5, text = "")
        self.import_status_label.place(x=10, y=45)

        self.export_button = customtkinter.CTkButton(self.tabview.tab("Import/Export"), width= 450, text="Export Links", command = self.export_button_action)
        self.export_button.place(x=10,y=80)



        # --> Initalizing Elements of Tabview 1:

        # Erstelle einen ttk-Stil
        self.style = ttk.Style ()

        # Ändere die Schriftart und die Schriftgröße der Überschriften
        self.style.configure("Treeview.Heading", font=(None, 15))
        self.style.configure("Treeview", font=(None, 13))

        self.table = ttk.Treeview(self.tabview1.tab("blocked Links"))
        self.table['columns'] = ('link_id', 'link_name')

        self.table.column("#0", width=0, stretch="no")
        self.table.column("link_id",anchor="center", width=20)
        self.table.column("link_name",anchor="center",width=395)

        self.table.heading("#0",text="",anchor="center")
        self.table.heading("link_id",text="Id",anchor="center")
        self.table.heading("link_name",text="Link",anchor="center")

        self.table.bind("<ButtonRelease-1>", self.on_select)

        self.table.place(x=5,y=50, width=600, height=320)

        # create scrollbar for Table
        self.table_scrollbar = customtkinter.CTkScrollbar(self.tabview1.tab("blocked Links"), command=self.table.yview)
        self.table_scrollbar.pack(side='right', fill='y')

        self.table.configure(yscrollcommand= self.table_scrollbar.set)

        self.sync_button = customtkinter.CTkButton(self.tabview1.tab("blocked Links"), width= 50, text="Sync", command = self.getlinks, image=images.sync_image)
        self.sync_button.place(x=5,y=0)

        self.remove_button = customtkinter.CTkButton(self.tabview1.tab("blocked Links"), width= 175, text="Remove selected Row", command = self.remove_rows, image = images.remove_image, fg_color="red")
        self.remove_button.place(x=85,y=0)

        self.search_entry = customtkinter.CTkEntry(self.tabview1.tab("blocked Links"), placeholder_text="Search", width= 100)
        self.search_entry.place(x=268,y=0)

        self.search_button = customtkinter.CTkButton(self.tabview1.tab("blocked Links"), width= 15, text="", command = self.search_button_action, image = images.search_image)
        self.search_button.place(x=375,y=0)

    # Import Links to the Database:
    def import_button_action(self):
        with open('ip.cfg', "r") as f:
            Host_url = json.load(f)

        background_thread = threading.Thread(target=self.reset)
        link= self.link_entry.get()
        url= f"http://{Host_url}/add?link={link}"
        
        try:
            response = requests.post(url)
            buffer = json.loads(response.text)
            print(buffer)
            
            if buffer['success'] == True:
                self.import_status_label.configure(text="Link imported successfully", fg_color="green")
            elif buffer["success"] == False:
                self.import_status_label.configure(text=f"Error during importing: {buffer["error"]}", fg_color="red")
            self.import_status_label.place(x=10, y=45)
            self.getlinks()
    
        except:
            self.import_status_label.configure(text="Error during importing", fg_color="red")
            self.import_status_label.place(x=10, y=45)
            self.getlinks()

        background_thread.start()
        
    # Get all links from Database:
    def getlinks(self):
        with open('ip.cfg', "r") as f:
            Host_url = json.load(f)

        url = f"http://{Host_url}/blocked"

        response = requests.get(url)
        data = json.loads(response.text)
        id=1
        if self.table.get_children():
            self.table.delete(*self.table.get_children())
        for element in data:
            self.table.insert(parent='',index='end',text='', values=(id,element))
            id = id +1

    # Remove selected row from the table:
    def remove_rows(self):
        with open('ip.cfg', "r") as f:
            Host_url = json.load(f)

        background_thread = threading.Thread(target=self.reset)
        item_id = self.table.selection()[0]
        link = self.table.item(item_id)["values"][1]

        url= f"http://{Host_url}/delete?link={link}"
        
        try:
            response = requests.delete(url)
            buffer = json.loads(response.text)
            
            if buffer['success'] == True:
                self.remove_button.configure(text="Deleted", fg_color="red")
            elif buffer["success"] == False:
                self.remove_button.configure(text=f"Error: {buffer["error"]}", fg_color="red")

            self.table.delete(item_id)
            self.getlinks()
        
    
        except:
            self.remove_button.configure(text="Error", fg_color="red")
            self.getlinks()

        background_thread.start()

    # Search for a link:
    def search(self,value_to_find):
        for i, row in enumerate(self.table.get_children()):
            row_value = self.table.item(row)["values"][1]  # Ändern Sie den Index basierend auf der Spalte, in der Sie suchen möchten
            if row_value == value_to_find:
                self.table.selection_set(row)
                self.table.yview(i)  # Scrollen Sie zur Zeile

    # "Search" Button Action:
    def search_button_action(self):
        value = self.search_entry.get()
        self.search(value)

    # Reset Action after Thread has finished
    def reset(self):
        self.import_button.configure(state="disabled")
        self.remove_button.configure(state="disabled")
        time.sleep(1)
        self.remove_button.configure(text="Remove selected Row")
        self.import_status_label.place_forget()
        self.import_button.configure(state="normal")
        self.remove_button.configure(state="normal")

    # "Export" Button Action:
    def export_button_action(self):
        with open('ip.cfg', "r") as f:
            Host_url = json.load(f)

        url = f"http://{Host_url}/blocked"

        response = requests.get(url)
        data = json.loads(response.text)
        with open('meine_datei.txt', 'w') as f:
            json.dump(data, f)

        os.system('meine_datei.txt')

# --> Initalizing Elements of the Settings-Frame:
class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #h1:
        self.settings_header = customtkinter.CTkLabel(self, text="Settings", width=440, fg_color="transparent",font=("",40))
        self.settings_header.place(x=5,y=10)

        #Theme text:
        self.theme_text = customtkinter.CTkLabel(self, text="Theme:", width=140, fg_color="transparent",font=("",20))
        self.theme_text.place(x=5,y=70)

        #Theme Drop-Down:
        self.theme_optionmenu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light", "Auto (System default)"], command=self.theme_change)
        self.theme_optionmenu.place(x=155,y=70)

        #Window-sclaing text:
        self.window_scaling_text = customtkinter.CTkLabel(self, text="Scaling:", width=140, fg_color="transparent",font=("",20))
        self.window_scaling_text.place(x=5,y=105)

        #Windwos-scaling Drop-Down:
        self.window_scaling_optionmenu = customtkinter.CTkOptionMenu(self, values=["75","100","125","150","175","200","225","250"], command=self.change_window_scaling)
        self.window_scaling_optionmenu.place(x=155,y=105)

        #IP change text:
        self.ip_change_text = customtkinter.CTkLabel(self, text="Change IP:", width=140, fg_color="transparent",font=("",20))
        self.ip_change_text.place(x=5,y=140)

        #Ip Change button
        self.ip_change_button = customtkinter.CTkButton(self, text="change Ip Adress", width=140, command=self.change_ip_button_action)
        self.ip_change_button.place(x=155,y=140)

    # Theme Change Function:
    def theme_change(self,choice):

        print("optionmenu dropdown clicked:", choice)

        if choice == "Auto (System default)":
            customtkinter.set_appearance_mode("system")

        if choice == "Dark":
            customtkinter.set_appearance_mode("dark")

        if choice == "Light":
            customtkinter.set_appearance_mode("light")
    
    def change_window_scaling(self,choice):
        scale = int(choice)
        scale = scale /100
        customtkinter.set_window_scaling(scale)
        customtkinter.set_widget_scaling(scale)
        # self.table.column_stretch = 1.25
        # self.table.row_stretch = 1.25

    def change_ip_button_action(self):
        dialog = customtkinter.CTkInputDialog(text="Type in your new Ip Adress:", title="IP change")

        newip = dialog.get_input()

        with open('ip.cfg', 'w') as config:
            json.dump(newip, config)

# --> Initalizing Elements of the About-Frame:
class AboutFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        about_text="Adblocker by Alex, Amir and Magnus.\n\nThis software was developed as part of a student project for the Baden-Württemberg Cooperative State University in Lörrach. It is for private use only and is not accessible to the public. The blocking software was primarily developed for and tested on the Rapsberry Pi. The user interface of the blocking software was implemented and tested for Windows devices in the network.\n\nThe mission of this software is simple: the aim is to block as much advertising as possible on any website. To do this, the link of the advertisement must be determined and imported into the blacklist contained in the software. The user therefore has the option of determining the blocked pages himself, but also of blocking links from external sources. The software also shows the user statistics on how many links have been blocked at the moment/total.\n\nCompatibility:\n- Blocker software: The Blocker software is only compatible with Docker-enabled devices. It was primarily tested and developed for Raspberry Pi. Compatibility with other dockers may be given, but is not guaranteed.\n- Please make sure that Docker is installed and working on your host.\n- User interface: The user interface was developed and tested on Windows. Compatibility with other python-enabled devices (Mac/Linux) cannot be guaranteed.\n\nContact:\n\nIf you have any problems installing or using the software, please contact\n\n- Blocker Software: magnus.scherrmann@nagarro.com\n- User interface : alexander.bauer@nagarro.com\n\nFor general questions, requests or suggestions, please contact:\n\namir.gharbi@nagarro.com\n\nThis software is for private use only and should not be made available to the public."

        self.about_h1 = customtkinter.CTkLabel(self, text="About", width=440, fg_color="transparent",font=("",40))
        self.about_h1.pack()

        self.about_textbox = customtkinter.CTkTextbox(self, width=440, height = 510, fg_color="transparent",font=("",14), wrap = "word")
        self.about_textbox.insert("0.0", about_text) 
        self.about_textbox.pack()

# --> Initalizing Elements of the Main-frame:
class UserInterface(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x600")
        self.title("CTk example")
        self.protocol("WM_DELETE_WINDOW", self.exit)

        # Initalizing Menu-bar:
        self.menu = customtkinter.CTkFrame(self, width=150, height=600, border_width=1, border_color="#1F538D")
        self.menu.place(x=0,y=0)

        # Initalizing Main-frame:
        self.main_frame = HomeFrame(self, width=450, height=600, fg_color="transparent")
        self.main_frame.place(x=150,y=0)

        # Initalizing About-frame:
        self.about_frame = AboutFrame(self, width=420, height=540)

        # Initalizing Settings-frame:
        self.settings_frame = SettingsFrame(self, width=440, height=560)

        # Initalizing Progressbar:
        self.status_label = customtkinter.CTkLabel(self, width=440, height=30, text="", corner_radius=5, fg_color=("#3A7EBF", "#1F538D"))
        self.status_label.place(x=155,y=565)


        # --> Initalizing Elements of the Menu-bar:

        # Image:
        self.logo_label = customtkinter.CTkLabel(self.menu, image= images.logo, text="")
        self.logo_label.place(x=11,y=10)

        # "Menu" label:
        self.menu_label = customtkinter.CTkLabel(self.menu, width=140,text="AD Blocker - Menu",fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
        self.menu_label.place(x=5,y=150)

        # "Start" button:
        self.button_start = customtkinter.CTkButton(self.menu, width=140, text="Start", command = self.start_button_action, image=images.start_image, fg_color="green")
        self.button_start.place(x=5, y= 200)

        # "Stop" button:
        self.button_stop = customtkinter.CTkButton(self.menu, width=140, text="Stop", command = self.stop_button_action, image=images.stop_image, fg_color="red")
        self.button_stop.place(x=5, y= 235)

        # "CPU" label:
        self.cpu_label = customtkinter.CTkLabel(self.menu, width=140,fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
        self.cpu_label.place(x=5,y=285)

        # "RAM" label:
        self.ram_label = customtkinter.CTkLabel(self.menu, width=140,fg_color=("#3A7EBF", "#1F538D"),text_color="white", corner_radius= 5)
        self.ram_label.place(x=5,y=320)

        # Button "Light" Theme:
        self.button_light_theme = customtkinter.CTkButton(self.menu, width=140, text="Switch Theme", command=self.theme_change_light, image=images.theme_image)
        self.button_light_theme.place(x=5,y=450)

        # Button "Dark" Theme:
        self.button_dark_theme = customtkinter.CTkButton(self.menu,width=140, text="Switch Theme", command=self.theme_change_dark, image=images.theme_image)

        # "Home" button:
        self.button_home = customtkinter.CTkButton(self.menu, width=140, text="Home", command = self.home_button_action, image=images.home_image)
        self.button_home.place(x=5, y= 495)

        # "About" button:
        self.button_about = customtkinter.CTkButton(self.menu, width=140, text="About", command = self.about_button_action, image=images.about_image)
        self.button_about.place(x=5, y= 530)

        # "Settings" button:
        self.button_settings = customtkinter.CTkButton(self.menu, width=140, text="Settings", command = self.settings_button_action,  image=images.settings_image)
        self.button_settings.place(x=5,y=565)
        
    #start function for starting the Ui
    def start(self):
        self.update_resources()
        self.main_frame.getlinks()

    #stop function called when closing window:
    def exit(self):
        sys.exit()

    # Function showing current System Resoruces:
    def update_resources(self):
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        self.cpu_label.configure(text=f"CPU: {cpu_usage}%")
        self.ram_label.configure(text=f"Memory: {memory_usage}%")
        self.after(1000, self.update_resources)  # Update every second    

    # Setting "Light" Theme:
    def theme_change_light(self):

        customtkinter.set_appearance_mode("light")
        self.button_light_theme.place_forget()
        self.button_dark_theme.place(x=5,y=450)

    # Setting "Dark" Theme:
    def theme_change_dark(self):

        customtkinter.set_appearance_mode("dark")
        self.button_dark_theme.place_forget()
        self.button_light_theme.place(x=5,y=450)

    # "Home" Button Action:
    def home_button_action(self):
        self.about_frame.place_forget()
        self.settings_frame.place_forget()
        self.main_frame.place(x=150,y=0)

    # "About" Button Action:
    def about_button_action(self):
        self.main_frame.place_forget()
        self.settings_frame.place_forget()
        self.about_frame.place(x=155,y=0)

    # "Settings" Button Action:
    def settings_button_action(self):
        self.main_frame.place_forget()
        self.about_frame.place_forget()
        self.settings_frame.place(x=155,y=0)

    # "Start" Button Action:
    def start_button_action(self):
        with open('ip.cfg', "r") as f:
            Host_url = json.load(f)
        
        url= f"http://{Host_url}/start"
        
        try:
            response = requests.post(url)
        
            if response.status_code == 200:
                buffer = json.loads(response.text)
                self.status_label.configure(text=f"Running: {buffer["running"]}", fg_color="green")
        except:
            self.status_label.configure(text=f"Unable to reach Server", fg_color="#990000")

    # "Stop" Button Action:
    def stop_button_action(self):
        with open('ip.cfg', "r") as f:
            Host_url = json.load(f)

        url= f"http://{Host_url}/stop"
        
        try:
            response = requests.post(url)

            if response.status_code == 200:
                buffer = json.loads(response.text)
                self.status_label.configure(text=f"Running: {buffer["running"]}", fg_color="red")
        except:
            self.status_label.configure(text=f"Unable to reach Server", fg_color="#990000")