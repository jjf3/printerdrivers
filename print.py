#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:20:29 2023

@author: jjf3
"""

import tkinter as tk
from tkinter import ttk
import webbrowser

# Sample printer brands and models
printer_data = {
    'HP': [' HP LaserJet Pro M404n', 'HP LaserJet Pro M402n', 
            'HP LaserJet Pro M426fdw', 'HP LaserJet Pro M281fdw',
            'HP LaserJet Pro M281fdw', 'HP LaserJet Enterprise M607dn',
            'HP LaserJet Enterprise M609dn', 'HP LaserJet Pro M102w',
            'HP LaserJet Pro M203dw', 'HP LaserJet Enterprise MFP M577dn',
            'HP LaserJet Enterprise MFP M527dn',
],
    'Canon': ['Canon imageCLASS MF743Cdw',
              'Canon imageRUNNER ADVANCE C5535i',
              'Canon PIXMA PRO-100',
              'Canon imagePROGRAF PRO-1000',
              'Canon imageCLASS D1650'],
    'Epson': ['Epson WorkForce Pro WF-C8690', 
              'Epson WorkForce Pro WF-4740',
              'Epson EcoTank ET-4760',]
            
}

# Function to get the printer driver website link
def get_driver_website(model):
    # Add your logic here to get the download link based on the model
    driver_website = {
        "HP LaserJet Pro M404n": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-pro-m404-m405-series/19204305",
        "HP LaserJet Pro M402n": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-pro-m402-m403-series/7089945",
        "HP LaserJet Pro M426fdw": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-pro-mfp-m426-m427-series/7326626",
        "HP LaserJet Pro M281fdw": "https://support.hp.com/us-en/drivers/selfservice/hp-color-laserjet-pro-m280-m281-multifunction-printer-series/16647047",
        "HP LaserJet Enterprise M607dn": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-enterprise-m607-m608-m609-series/18140979",
        "HP LaserJet Enterprise M609dn": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-enterprise-m607-m608-m609-series/18140979",
        "HP LaserJet Pro M102w": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-ultra-m106-m107-p1005-p1006-p1007-p1008-p1009-printer-series/9365377",
        "HP LaserJet Pro M203dw": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-ultra-m206-m207-p1102-p1106-p1108-printer-series/9365381",
        "HP LaserJet Enterprise MFP M577dn": "https://support.hp.com/us-en/drivers/selfservice/hp-color-laserjet-enterprise-mfp-m577-series/6777688",
        "HP LaserJet Enterprise MFP M527dn": "https://support.hp.com/us-en/drivers/selfservice/hp-laserjet-enterprise-mfp-m527-m528-series/6976542",
        "Canon imageCLASS MF743Cdw": "https://www.usa.canon.com/support/p/color-imageclass-mf743cdw",
        "Canon imageRUNNER ADVANCE C5535i": "https://www.usa.canon.com/support/p/imagerunner-advance-c5535i",
        "Canon PIXMA PRO-100": "https://www.usa.canon.com/support/pixma-pro-100",
        "Canon imagePROGRAF PRO-1000": "https://www.usa.canon.com/support/imageprograf-pro-1000",
        "Canon imageCLASS D1650": "https://www.usa.canon.com/support/p/imageclass-d1650",
        "Epson WorkForce Pro WF-C8690": "https://epson.com/Support/Printers/All-In-Ones/WorkForce-Series/Epson-WorkForce-Pro-WF-C8690/s/SPT_C11CG68201",
        "Epson WorkForce Pro WF-474": "https://epson.com/Support/Printers/All-In-Ones/WorkForce-Series/Epson-WorkForce-Pro-WF-4740/s/SPT_C11CF75201",
        "Epson EcoTank ET-4760": "https://epson.com/Support/Printers/All-In-Ones/ET-Series/Epson-ET-4760/s/SPT_C11CG19203",
    }
    return driver_website.get(model)

# Event handler for brand selection
def on_brand_selected(event):
    selected_brand = brand_combobox.get()
    models = printer_data.get(selected_brand, [])
    model_combobox['values'] = models
    model_combobox.current(0)  # Select the first model by default

# Event handler for model selection
def on_model_selected(event):
    selected_model = model_combobox.get()
    driver_website = get_driver_website(selected_model)
    download_button.config(command=lambda: webbrowser.open(driver_website))
    download_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Printer Driver Downloader")

# Brand selection box
brand_label = ttk.Label(window, text="Select Brand:")
brand_label.pack()
brand_combobox = ttk.Combobox(window, values=list(printer_data.keys()))
brand_combobox.bind("<<ComboboxSelected>>", on_brand_selected)
brand_combobox.pack()

# Model selection box
model_label = ttk.Label(window, text="Select Model:")
model_label.pack()
model_combobox = ttk.Combobox(window)
model_combobox.bind("<<ComboboxSelected>>", on_model_selected)
model_combobox.pack()

# Download driver button
download_button = ttk.Button(window, text="Download Driver", state=tk.DISABLED)
download_button.pack()

window.mainloop()
