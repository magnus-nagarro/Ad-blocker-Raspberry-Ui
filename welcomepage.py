import ui

def start_button_action():
    welcomepage.withdraw()

    ui.getlinks()
    ui.update_resources()

    hosturl = ip_entry.get()

    with open('ip.cfg', 'w') as f:
        ui.json.dump(hosturl, f)

    ui.app.mainloop()

def start():
    with open('ip.cfg', "r") as f:
        url = ui.json.load(f)


    print(url)
    if url == "":
        welcomepage.mainloop()
    else:
        ui.getlinks()
        ui.update_resources()
        ui.app.mainloop()
        

def exit():
    ui.sys.exit()

# Initalizing welcome page:
welcomepage = ui.customtkinter.CTk()  # master argument is optional 
welcomepage.geometry("384x308")
welcomepage.title("Welcome")
welcomepage.protocol("WM_DELETE_WINDOW", exit)

# Initalizing elements of the welcome page:
welcome_label = ui.customtkinter.CTkLabel(welcomepage, width=384,text="Welcome to Adblocker!",fg_color=("transparent"),text_color="white", corner_radius= 5, font=("Arial", 20))
welcome_label.place(x=0,y=140)

Ip_text_label = ui.customtkinter.CTkLabel(welcomepage, width=384,text="In order to ensure error-free operation, please enter the IP address \n of the device on which the blocker software is running \n in the field below.",fg_color=("transparent"),text_color="white", corner_radius= 5, font=("Arial", 12))
Ip_text_label.place(x=0,y=175)

ip_entry = ui.customtkinter.CTkEntry(welcomepage, placeholder_text="Enter IP-Adress", width= 128)
ip_entry.place(x=128,y=230)

start_button = ui.customtkinter.CTkButton(welcomepage, width=50, text="Start", command = start_button_action)
start_button.place(x=310,y=275)

start()