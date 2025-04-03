from customtkinter import CTkScrollableFrame
from customtkinter import CTkFrame
from customtkinter import CTkLabel
from customtkinter import CTkButton
from customtkinter import CTkEntry
from customtkinter import CTkOptionMenu
from customtkinter import CTkTextbox
from customtkinter import CTkImage
from .BoundsEditorWindow import BoundsEditorWindow as BEW
from ...util.CTkToolTip import CTkToolTip as ctt
import tkinter as tk
import json
import PIL
from PIL import Image
import os
import pandas as pd
from tkinter.filedialog import askopenfilename

class BoundsList(CTkFrame):
    def __init__(self, *args,
                 option_manager = None,
                 step_index = 0,
                 **kwargs):
        super().__init__(*args, **kwargs)
        
        self.option_manager = option_manager

        self.edit_mode = False
        self.tooltip_list = []
        
        self.step_index = step_index 
        self.render()
    
    def clear(self):
        for list in self.tooltip_list:
            for tooltip in list:
                tooltip.destroy()
        self.containerFrame.destroy()
        self.tooltip_list = []
        
    def toggle_edit_mode(self):
        self.clear()
        self.edit_mode = not self.edit_mode
        self.render()
        
    def refresh(self, *args):
        self.clear()
        self.render()
        
    def render(self):
        row = 0
        index = 0
        
        self.tooltip_list = []

        mode = self.option_manager.get_mode()
        bounds = self.option_manager.get_steps()[self.step_index]["parameter_objects"]

        # Load bound parameters depending on the mode
        self.optParams = []
        if mode == "Optimization" or mode == "Sampling: Halton" or mode == "Sampling: Random":
            details = self.option_manager.serialize_data(self.option_manager.get("service_request_data"))
            self.paramMap = {}
            if "parameter" in details:
                for param in details["parameter"]:
                    self.paramMap[param["name"]] = param
                    if "min" in param:
                        self.optParams.append(param["name"])
                        
                self.optParams.sort()
        elif mode == "Sensitivity Analysis":
            file_path = self.option_manager.get("sensitivity_analysis_path").get()
            folder = self.option_manager.get_project_folder()
            file_path = os.path.join(folder, "results", file_path)
            if os.path.exists(file_path):
                try:
                    df = pd.read_csv(file_path)
                    self.optParams = df.columns.tolist()
                except Exception as e:
                    print(f"Error loading CSV file: {e}")
            else:
                print(f"File does not exist: {file_path}")

        
        self.containerFrame = CTkFrame(self, fg_color="transparent")
        self.containerFrame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.containerFrame.grid_columnconfigure(0, weight=1, minsize=20)
        self.containerFrame.grid_columnconfigure(5, weight=1, minsize=20)
        self.containerFrame.grid_columnconfigure((1, 2, 3, 4), weight=5)
        
        CTkLabel(self.containerFrame, text="Type:").grid(row=row, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        CTkLabel(self.containerFrame, text="Name:").grid(row=row, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")


        show_strategy = False
        show_default = False
        show_bounds = True

        if mode == "Sensitivity Analysis":
            show_bounds = False

        for bound in bounds:
            bound_type = bound["type"].get()
            if bound_type == "list":
                show_strategy = True
                show_default = True
                break


        if show_bounds:
            CTkLabel(self.containerFrame, text="Bounds:").grid(row=row, column=2, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")

        if show_default:
            CTkLabel(self.containerFrame, text="Default:").grid(row=row, column=4, padx=(5, 5), pady=(5, 5), sticky="nsew")

        if show_strategy:
            CTkLabel(self.containerFrame, text="Strategy:").grid(row=row, column=5, padx=(5, 5), pady=(5, 5), sticky="nsew")

        row += 1
        
        for bound in bounds:
            tt1 = None
            tt2 = None
            tt3 = None
                        
            options_list = ['custom', 'float', 'list']
            if self.optParams == [] or self.optParams is None:
                options_list = ['custom', 'list']
            
            tt = CTkOptionMenu(self.containerFrame, dynamic_resizing=False, values=options_list, variable=bound["type"], command=self.refresh)
            #command = lambda _, index=index, option=tt: (self.update_type(index, option)) 
            #tt.configure(command=command)
            #tt.set(bound["type"].get())
            tt.grid(row=row, column=0, padx=(5, 5), pady=(5, 5), sticky="new")
            
            cc = None
            
            bound_type = bound["type"].get()

            if self.optParams == [] and bound_type == "float":
                bound["type"].set("custom")
                bound_type = "custom"
            
            if bound_type == "float":
                cc = CTkOptionMenu(self.containerFrame, dynamic_resizing=False, values=self.optParams, variable=bound["name"])
                cc.grid(row=row, column=1, padx=(5, 5), pady=(5, 5), sticky="new")
                
                command = lambda _, index=index: (self.update_values(index), self.update_tooltips(index))  
                cc.configure(command=command)
            else:
                
                cc = CTkEntry(self.containerFrame)
                cc.configure(textvariable=bound["name"])
                cc.grid(row=row, column=1, padx=(5, 5), pady=(5, 5), sticky="new")
                
                        
            if self.edit_mode:
                remove_func = lambda index=index: (self.clear(), self.option_manager.remove_bound(self.step_index, index), self.render())
                bb = CTkButton(self.containerFrame, text="Remove", command=remove_func)
                bb.grid(row=row, column=2, padx=(5, 5), pady=(5, 5), sticky="new")
                ctt(bb, delay=0.1, alpha=0.95, message="Delete this bound...")
            else:
                
                
                if show_bounds:
                    bounds_min = CTkEntry(self.containerFrame)
                    vcmd = (self.register(self.validate_number), '%P', cc, bounds_min)
                    bounds_min.grid(row=row, column=2, padx=(5, 5), pady=(5, 5), sticky="new")
                    bounds_min.configure(textvariable=bound["min_bound"], validate='all', validatecommand=vcmd)
                    self.validate_number(bounds_min.get(), cc, bounds_min)
                                
                    bounds_max = CTkEntry(self.containerFrame)
                    vcmd = (self.register(self.validate_number), '%P', cc, bounds_max)
                    bounds_max.grid(row=row, column=3, padx=(5, 5), pady=(5, 5), sticky="new")
                    bounds_max.configure(textvariable=bound["max_bound"], validate='all', validatecommand=vcmd)
                    self.validate_number(bounds_max.get(), cc, bounds_max)
                
                if show_default:
                    default_value = CTkEntry(self.containerFrame)
                    default_value.grid(row=row, column=4, padx=(5, 5), pady=(5, 5), sticky="new")
                    default_value.configure(textvariable=bound["default_value"])

                if (bound_type == "list"):
                    calibration_strat = CTkOptionMenu(self.containerFrame, dynamic_resizing=False, values=['none', 'mean', 'single'], variable=bound["calibration_strategy"])
                    calibration_strat.grid(row=row, column=5, padx=(5, 5), pady=(5, 5), sticky="new")

                    def button_click_event(bound_index):
                        BEW(title="Edit List Bound", step_index=self.step_index, bound_index=bound_index, option_manager=self.option_manager)

                    open_window = lambda event=None, bound_index=index: (button_click_event(bound_index))
                    expand_image = CTkImage(Image.open(os.path.join("./images", "expand.png")), size=(20, 20))
                    button = CTkButton(self.containerFrame, width=30, text=None, image=expand_image, command=open_window)
                    button.grid(row=row, column=6, padx=(5, 5), pady=(5, 5), sticky="new")
                
                tt1 = ctt(bounds_min, delay=0.1, alpha=0.95, message="...")
                tt2 = ctt(bounds_max, delay=0.1, alpha=0.95, message="...")
                if cc is not None:
                    tt3 = ctt(cc, delay=0.1, alpha=0.95, message="...")
                        
                self.tooltip_list.append([tt3, tt1, tt2])
                        
                self.update_tooltips(index)
            
            row += 1
            index += 1
            
        add_func = lambda: (self.clear(), self.option_manager.add_bound(self.step_index), self.render())
        if len(bounds) > 0:
            if self.edit_mode:
                CTkButton(self.containerFrame, text="Exit", command=self.toggle_edit_mode).grid(row=row, column=0, padx=(5, 5), pady=(5, 5), sticky="new")
            else:
                CTkButton(self.containerFrame, text="Edit", command=self.toggle_edit_mode).grid(row=row, column=0, padx=(5, 5), pady=(5, 5), sticky="new")
        
        CTkButton(self.containerFrame, text="Add Bound", command=add_func).grid(row=row, column=1, padx=(5, 5), pady=(5, 5), sticky="new")

        def import_csv():
            filename = askopenfilename(filetypes=[("CSV", "*.csv")], title="Open Bound CSV", multiple=False)
            print(filename)

            # Open CSV file
            if filename is not None and filename != "":
                df = pd.read_csv(filename)
                for _, row in df.iterrows():
                    if "name" not in row:
                        continue
                    name = row["name"] if "name" in row else "name"
                    type_ = row["type"] if "type" in row else "custom"
                    min_bound = row["min_bound"] if "min_bound" in row else 0
                    max_bound = row["max_bound"] if "max_bound" in row else 1
                    default_value = row["default_value"] if "default_value" in row else 1
                    calibration_strategy = row["calibration_strategy"] if "calibration_strategy" in row else "none"
                    self.option_manager.add_bound(step_index=self.step_index, name=name, min=min_bound, max=max_bound, type=type_, default_value=default_value, calibration_strategy=calibration_strategy)

            self.clear()
            self.render()

        CTkButton(self.containerFrame, text="Import CSV", command=import_csv).grid(row=row, column=2, padx=(5, 5), pady=(5, 5), sticky="new")
            
    def update_type(self, index, option):
        value = option.get()
        self.option_manager.get_steps()[self.step_index]["parameter_objects"][index]["type"].set(value)
        self.refresh()
            
    def update_values(self, index):
        name = self.option_manager.get_steps()[self.step_index]["parameter_objects"][index]["name"].get()
        if name in self.paramMap:
            obj = self.paramMap[name]
            self.option_manager.get_steps()[self.step_index]["parameter_objects"][index]["min_bound"].set(obj["softmin"])
            self.option_manager.get_steps()[self.step_index]["parameter_objects"][index]["max_bound"].set(obj["softmax"])
            
    def update_tooltips(self, index):
        try:
            name = self.option_manager.get_steps()[self.step_index]["parameter_objects"][index]["name"].get()
            bound_type = self.option_manager.get_steps()[self.step_index]["parameter_objects"][index]["type"].get()
            
            tooltips = self.tooltip_list[index]
            t3 = tooltips[0]
            t1 = tooltips[1]
            t2 = tooltips[2]
            
            if (t1 == None or t2 == None or t3 == None):
                if (t1 is not None):
                    t1.configure(message="")
                if (t2 is not None):
                    t2.configure(message="")
                if (t3 is not None):
                    t3.configure(message="")
                print("update skipped")
                return
            
            if bound_type == "list":
                t1.configure(message="")
                t2.configure(message="")
                t3.configure(message="")
            
            if name in self.paramMap:
                obj = self.paramMap[name]
                description = obj["description"]
                default = str(obj["value"])
                min = str(obj["min"])
                max = str(obj["max"])
                softmin = str(obj["softmin"])
                softmax = str(obj["softmax"])
                unit = str(obj["unit"])
                t1.configure(message=description + "\nMin: " + min + "\nSoft Min: " + softmin + "\nUnit: " + unit)
                t2.configure(message=description + "\nMax: " + max + "\nSoft Max: " + softmax + "\nUnit: " + unit)
                t3.configure(message=description + "\nDefault: " + default + "\nUnit: " + unit)
        except:
            pass
        
    def validate_number(self, P, name, entry):
        
        # Get the root window
        root = self.winfo_toplevel()
        
        # Get the entry widget using its internal Tkinter name
        entry_widget = root.nametowidget(entry)
        name_widget = root.nametowidget(name)
        
        if isinstance(name_widget, CTkTextbox):
            return True
        
        # Call the get method on the entry widget
        bound_name = name_widget.get()
        value = entry_widget.get()
        
        # Print the value of the entry widget
        #print(bound_name)
        
        if P == "" or P == "." or P == "-":
            entry_widget.configure(border_color="red")
            return True
        
        try:
            float(P)
            entry_widget.configure(border_color=["#979DA2", "#565B5E"])
            
            if bound_name in self.paramMap:
                obj = self.paramMap[bound_name]
                if "min" in obj and float(P) < float(obj["min"]):
                    entry_widget.configure(border_color="red")
                elif "max" in obj and float(P) > float(obj["max"]):
                    entry_widget.configure(border_color="red")
                elif "softmin" in obj and float(P) < float(obj["softmin"]):
                    entry_widget.configure(border_color="yellow")
                elif "softmax" in obj and float(P) > float(obj["softmax"]):
                    entry_widget.configure(border_color="yellow")
            
            return True
        except ValueError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False