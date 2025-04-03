from typing import Union, Tuple, Optional

from customtkinter import CTkLabel
from customtkinter import CTkButton
from customtkinter import CTkEntry
from customtkinter import CTkInputDialog
from .SamplingListView import SamplingListView as SamplingListView

class SamplingNameListWindow(CTkInputDialog):
    """
    Dialog with extra window, message, entry widget, cancel and ok button.
    For detailed information check out the documentation.
    """

    def __init__(self, *args,
                 step_index: 0,
                 bound_index: 0,
                 option_manager: None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        win_width = 400
        win_height = 800
        if screen_width < win_width:
            win_width = screen_width * 0.9

        if screen_height < win_height:
            win_height = screen_height * 0.9

        # Calculate the x and y coordinates to center the window
        x_coord = (screen_width // 2) - (win_width // 2)
        y_coord = (screen_height // 2) - (win_height // 2)

        self.geometry(f"{win_width}x{win_height}+{x_coord}+{y_coord}")
        
        self.step_index = step_index
        self.bound_index = bound_index  
        self.option_manager = option_manager
        self.bounds = None

    def _create_widgets(self):

        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self.bounds = SamplingListView(
                self, step_index=self.step_index, bound_index=self.bound_index, option_manager=self.option_manager)
        self.bounds.grid(row=0, column=0, columnspan=2, padx=(10, 10),
                    pady=(10, 10), sticky="nsew")
        self.bounds.grid_columnconfigure(0, weight=1)

        self._ok_button = CTkButton(master=self,
                                    width=100,
                                    border_width=0,
                                    fg_color=self._button_fg_color,
                                    hover_color=self._button_hover_color,
                                    text_color=self._button_text_color,
                                    text='Save',
                                    command=self._ok_event)
        self._ok_button.grid(row=2, column=0, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew")

        self._cancel_button = CTkButton(master=self,
                                        width=100,
                                        border_width=0,
                                        fg_color=self._button_fg_color,
                                        hover_color=self._button_hover_color,
                                        text_color=self._button_text_color,
                                        text='Cancel',
                                        command=self._cancel_event)
        self._cancel_button.grid(row=2, column=1, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew")
        
    def _ok_event(self, event=None):
        # Save values in bounds editor...
        
        self.bounds.push_to_option_manager()
        
        self.grab_release()
        self.destroy()

    def _on_closing(self):
        self.grab_release()
        self.destroy()

    def _cancel_event(self):
        self.grab_release()
        self.destroy()