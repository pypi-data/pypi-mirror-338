from customtkinter import CTkScrollableFrame
from customtkinter import CTkFrame
from customtkinter import CTkLabel
from customtkinter import CTkButton
from customtkinter import CTkEntry
import tkinter as tk
import subprocess
import platform
import os

global option_manager

class SamplingListView(CTkScrollableFrame):
    def __init__(self, *args,
                 option_manager: None,
                 step_index: 0,
                 bound_index: 0,
                 **kwargs):
        super().__init__(*args, **kwargs)
        
        self.option_manager = option_manager
        self.step_index = step_index
        self.bounds_index = bound_index
        self.key_values = []
        self.visual_name = tk.StringVar()
        self.visual_name.set("name")
        
        
        self.name = self.option_manager.get_steps()[self.step_index]["parameter_objects"][bound_index]["name"].get()
        self.default = self.option_manager.get_steps()[self.step_index]["parameter_objects"][bound_index]["default_value"].get()
        try:
            if self.name != "" and self.default != "":
                
                self.visual_name.set(self.name.rsplit('/', 1)[0] + '/')
                self.names = self.name.split('/')
                self.rows = self.names[-1].split(';')
                self.defaults = self.default.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(" ", "").split(",")
                
                print("rows", self.rows)
                print("defaults", self.defaults)
                index = 0
                
                for name in self.rows:
                    obj = {"name": tk.StringVar(), "value": tk.StringVar()}
                    obj['name'].set(name)
                    obj['value'].set(self.defaults[index])
                    self.key_values.append(obj)
                    index += 1
        except Exception as e:
            print(e)
        
        if (len(self.key_values) == 0):
            self.add_key()
        
        self.edit_mode = False
        
        self.render()

    def clear(self):
        self.containerFrame.destroy()
        
    def toggle_edit_mode(self):
        self.clear()
        self.edit_mode = not self.edit_mode
        self.render()
        
    def add_key(self, key="0000", value="0"):
        obj = {"name": tk.StringVar(), "value": tk.StringVar()}
        obj['name'].set(key)
        obj['value'].set(value)
        self.key_values.append(obj)
        
    def remove_key(self, index):
        self.key_values.pop(index)
        
    def render(self):
        row = 0
        index = 0
        
        self.containerFrame = CTkFrame(self)
        self.containerFrame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.containerFrame.grid_columnconfigure((0, 1), weight=1)
        
        
        CTkLabel(self.containerFrame, text="Row:").grid(row=row, column=0, columnspan=1, padx=5, pady=5, sticky="")
        CTkLabel(self.containerFrame, text="Default:").grid(row=row, column=1, columnspan=1, padx=5, pady=5, sticky="")
        row += 1
        
        for key_value_pair in self.key_values:
            CTkEntry(self.containerFrame, textvariable=self.key_values[index]["name"]).grid(row=row, column=0, padx=(5, 5), pady=(5, 5), sticky="ew")
            
            if self.edit_mode:
                return_func = lambda index=index: (self.clear(), self.remove_key(index), self.render())
                CTkButton(self.containerFrame, text="Remove", command=return_func).grid(row=row, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
            else:
                bb = CTkEntry(self.containerFrame)
                bb.grid(row=row, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
                bb.configure(textvariable=self.key_values[index]["value"])
            row += 1
            index += 1
            
        if self.edit_mode:
            CTkButton(self.containerFrame, text="Exit", command=self.toggle_edit_mode).grid(row=row, column=0, padx=(5, 5), pady=(5, 5), sticky="ew")
        else:
            CTkButton(self.containerFrame, text="Edit", command=self.toggle_edit_mode).grid(row=row, column=0, padx=(5, 5), pady=(5, 5), sticky="ew")
            
        add_key_func = lambda: (self.clear(), self.add_key(), self.render())
        CTkButton(self.containerFrame, text="Add", command=add_key_func).grid(row=row, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
        
        row += 1
        
    def push_to_option_manager(self):
        visual_name = self.visual_name.get()
        default_values = "["
        first = True
        for key_value_pair in self.key_values:
            if first:
                visual_name += key_value_pair['name'].get()
                first = False
            else:
                visual_name += ";" + key_value_pair['name'].get()
            default_values += key_value_pair['value'].get() + ","
            
        default_values = default_values[:-1] + "]"
            
        self.option_manager.get_steps()[self.step_index]["parameter_objects"][self.bounds_index]["name"].set(visual_name)
        self.option_manager.get_steps()[self.step_index]["parameter_objects"][self.bounds_index]["default_value"].set(default_values)