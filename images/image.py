# This module initalizes all images using the PILLOW librari and CTkImage from Customtkinter

import customtkinter
from PIL import Image


# Menu-bar Image:
logo_ui = customtkinter.CTkImage(light_image=Image.open("images\yblocker.png"), dark_image=Image.open("images\yblocker.png"),size=(128,128))

# "Change Theme" button Image:
theme_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-night-mode-24.png"), dark_image=Image.open("images\icons8-night-mode-24.png"),size=(20,20))

# "Start" button Image:
start_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-spielen-26.png"), dark_image=Image.open("images\icons8-spielen-26.png"),size=(20,20))

# "Stop" button Image:
stop_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-stop-26.png"), dark_image=Image.open("images\icons8-stop-26.png"),size=(20,20))

# "Home" button Image:
home_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-zuhause-26.png"), dark_image=Image.open("images\icons8-zuhause-26.png"),size=(20,20))

# "Settings" button Image:
settings_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-einstellungen-50.png"), dark_image=Image.open("images\icons8-einstellungen-50.png"),size=(20,20))

# "About" button Image:
about_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-info-50.png"), dark_image=Image.open("images\icons8-info-50.png"),size=(20,20))

# "Sync" button Image:
sync_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-synchronisieren-48.png"), dark_image=Image.open("images\icons8-synchronisieren-48.png"),size=(20,20))

# "Remove" button Image:
remove_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-entfernen-24.png"), dark_image=Image.open("images\icons8-entfernen-24.png"),size=(20,20))

# "Remove" button Image:
search_image = customtkinter.CTkImage(light_image=Image.open("images\icons8-suche-50.png"), dark_image=Image.open("images\icons8-suche-50.png"),size=(20,20))

# Welcomepage Image:
logo_welcome = customtkinter.CTkImage(light_image=Image.open("images\yblocker.png"), dark_image=Image.open("images\yblocker.png"),size=(128,128))