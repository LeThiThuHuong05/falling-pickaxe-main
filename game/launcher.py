import json
import os
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk

CONFIG_FILE = "config.json"
DEFAULT_CONFIG_FILE = "default.config.json"
GAME_EXE = "falling-pickaxe.exe"

class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Falling Pickaxe - Config & Launcher")
        self.root.geometry("600x700")

        self.config_data = {}
        self.entries = {}

        self.load_config()
        self.create_widgets()

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            if os.path.exists(DEFAULT_CONFIG_FILE):
                with open(DEFAULT_CONFIG_FILE, "r", encoding="utf-8") as f:
                    self.config_data = json.load(f)
            else:
                self.config_data = {}
                messagebox.showwarning("Warning", "Configuration files not found!")
        else:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                self.config_data = json.load(f)

    def save_config(self):
        for key, entry in self.entries.items():
            val = entry.get()
            # Convert basic types
            if val.lower() == "true":
                self.config_data[key] = True
            elif val.lower() == "false":
                self.config_data[key] = False
            else:
                try:
                    if "." in val:
                        self.config_data[key] = float(val)
                    else:
                        self.config_data[key] = int(val)
                except ValueError:
                    self.config_data[key] = val

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(self.config_data, f, indent=4)
        messagebox.showinfo("Success", "Configuration saved to config.json!")

    def create_widgets(self):
        # Create a canvas and scrollbar for scrollable content
        canvas = tk.Canvas(self.root)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        # Create form fields
        row = 0
        for key, value in self.config_data.items():
            tk.Label(scrollable_frame, text=key, font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5, padx=5)
            
            entry = tk.Entry(scrollable_frame, width=50)
            if isinstance(value, bool):
                entry.insert(0, str(value).lower())
            else:
                entry.insert(0, str(value))
            
            entry.grid(row=row, column=1, pady=5, padx=5)
            self.entries[key] = entry
            row += 1

        # Action Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=10)

        save_btn = tk.Button(btn_frame, text="Save Config", command=self.save_config, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        save_btn.pack(side="left", padx=5)

        run_btn = tk.Button(btn_frame, text="Run Game", command=self.run_game, bg="#2196F3", fg="white", font=("Arial", 11, "bold"))
        run_btn.pack(side="right", padx=5)

    def run_game(self):
        self.save_config()

        if not os.path.exists(GAME_EXE):
            messagebox.showerror("Error", f"Could not find game executable: {GAME_EXE}")
            return

        try:
            # We open the game exe directly
            subprocess.Popen(
                [GAME_EXE],
                cwd=os.getcwd(),
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run game: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()
