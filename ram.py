## pip3 install psutil ## macos
## pip install psutil ## windows
import psutil
import tkinter as tk
from tkinter import ttk

def format_gb(bytes_value):
    return bytes_value / (1024 ** 3)

def update_ram_info():
    ram = psutil.virtual_memory()

    total_gb = format_gb(ram.total)
    used_gb = format_gb(ram.used)
    free_gb = format_gb(ram.available)
    percent = ram.percent

    label_total_value.config(text=f"{total_gb:.2f} GB")
    label_used_value.config(text=f"{used_gb:.2f} GB")
    label_free_value.config(text=f"{free_gb:.2f} GB")
    label_percent_value.config(text=f"{percent:.1f} %")

    # Progressbar aktualisieren
    progress_used["value"] = percent

    # Alle 1000 ms (1 Sekunde) neu aktualisieren
    root.after(1000, update_ram_info)

# --- GUI erstellen ---
root = tk.Tk()
root.title("RAM Monitor")

# Fenster etwas hübscher machen
root.resizable(False, False)
root.geometry("300x200")

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

# Überschrift
label_title = ttk.Label(main_frame, text="Aktuelle RAM-Nutzung", font=("Segoe UI", 12, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Labels
ttk.Label(main_frame, text="Gesamt:").grid(row=1, column=0, sticky="w")
label_total_value = ttk.Label(main_frame, text="-")
label_total_value.grid(row=1, column=1, sticky="e")

ttk.Label(main_frame, text="Genutzt:").grid(row=2, column=0, sticky="w")
label_used_value = ttk.Label(main_frame, text="-")
label_used_value.grid(row=2, column=1, sticky="e")

ttk.Label(main_frame, text="Frei:").grid(row=3, column=0, sticky="w")
label_free_value = ttk.Label(main_frame, text="-")
label_free_value.grid(row=3, column=1, sticky="e")

ttk.Label(main_frame, text="Auslastung:").grid(row=4, column=0, sticky="w")
label_percent_value = ttk.Label(main_frame, text="-")
label_percent_value.grid(row=4, column=1, sticky="e")

# Progressbar
progress_used = ttk.Progressbar(main_frame, orient="horizontal", mode="determinate", length=250)
progress_used.grid(row=5, column=0, columnspan=2, pady=(10, 0))

# Start-Update
update_ram_info()

root.mainloop()

