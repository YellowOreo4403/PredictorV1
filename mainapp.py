import customtkinter as ctk
import numpy as np
import pickle
from tkinter import messagebox
import sys
import os

# ONLY USE IF YOU WANT .EXE FILE (PYINSTALLER)!!
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# put your .pkl file here!
with open(resource_path("prediction_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(resource_path("scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)

# Change appearance 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Predictor")
        self.geometry("1080x720")
        self.resizable(False, False)

        # Font
        self.font_title = ctk.CTkFont(family="Roboto", size=22, weight="bold")
        self.font_label = ctk.CTkFont(family="Roboto", size=14)
        self.font_entry = ctk.CTkFont(family="Roboto", size=14)
        self.font_button = ctk.CTkFont(family="Roboto", size=16)

        # Put your title here
        self.label_title = ctk.CTkLabel(self, text="Example", font=self.font_title)
        self.label_title.pack(pady=20)

        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=10, fill="both", expand=True)

        # put your input (X) here
        self.entries = {}
        fields = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",

        ]

        for i, field in enumerate(fields):
            label = ctk.CTkLabel(self.frame, text=field, font=self.font_label)
            label.grid(row=i, column=0, sticky="e", padx=(10, 5), pady=8)

            entry = ctk.CTkEntry(self.frame, width=200, font=self.font_entry)
            entry.grid(row=i, column=1, sticky="w", padx=(5, 10), pady=8)

            self.entries[field] = entry

        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=1)

        # Modify your button
        self.btn_prediksi = ctk.CTkButton(self.frame, text="Predict height", font=self.font_button, command=self.prediksi)
        self.btn_prediksi.grid(row=len(fields), column=0, columnspan=2, pady=20)

    def prediksi(self):
        try:
            values = []
            for key in self.entries:
                val = self.entries[key].get()
                if not val:
                    raise ValueError(f"Field '{key}' must be filled")

                if "Luas" in key:
                    values.append(float(val))
                else:
                    values.append(int(val))

            data_input = np.array(values).reshape(1, -1)
            data_scaled = scaler.transform(data_input)
            result = model.predict(data_scaled)[0]

            #change "m" and "meter" as your liking
            messagebox.showinfo("Prediction result", f"Prediction: m {result:.2f} Meter")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = App()
    app.mainloop()
