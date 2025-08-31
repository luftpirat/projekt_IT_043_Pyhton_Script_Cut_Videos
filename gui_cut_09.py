import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.simpledialog import askstring as simple_input
import subprocess
import os
import sqlite3
from datetime import datetime
import threading
import json

# Datenbank in der die Jobs gespeichert werden. 
DB_FILE = "ffmpeg_jobs5.db"




CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Default-Werte falls keine Config existiert
        return {
            "column_widths": {
                "ID": 50,
                "Eingabe-Datei": 200,
                "Eingabe-Verzeichnis": 250,
                "Ausgabe-Datei": 200,
                "Start": 80,
                "Ende": 80,
                "Beschreibung": 250,
                "Gruppe": 120,
                "Untergruppe": 120,
                "Erstellt_am": 150
            }
        }

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)









# --- Datenbankfunktionen ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Jobs Tabelle
    c.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            eingabe_datei TEXT NOT NULL,
            eingabe_verzeichnis TEXT NOT NULL,
            ausgabe_datei TEXT NOT NULL,
            startzeit TEXT NOT NULL,
            endzeit TEXT NOT NULL,
            beschreibung TEXT,
            gruppe TEXT,
            untergruppe TEXT,
            erstellt_am TEXT NOT NULL
        )
    """)
    # Gruppen Tabelle
    c.execute("""
        CREATE TABLE IF NOT EXISTS gruppen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)
    # Untergruppen Tabelle
    c.execute("""
        CREATE TABLE IF NOT EXISTS untergruppen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gruppe_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY(gruppe_id) REFERENCES gruppen(id)
        )
    """)
    conn.commit()
    conn.close()

# --- Job-Datenbankfunktionen ---
def save_to_db(eingabe_file, eingabe_dir, ausgabe_file, start, ende, beschreibung, gruppe, untergruppe):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        INSERT INTO jobs 
        (eingabe_datei, eingabe_verzeichnis, ausgabe_datei, startzeit, endzeit, beschreibung, gruppe, untergruppe, erstellt_am)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (eingabe_file, eingabe_dir, ausgabe_file, start, ende, beschreibung, gruppe, untergruppe, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
    load_history()

def load_history(filter_text=""):
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if filter_text:
        like = f"%{filter_text}%"
        c.execute("""
            SELECT id, eingabe_datei, eingabe_verzeichnis, ausgabe_datei, startzeit, endzeit, beschreibung, gruppe, untergruppe, erstellt_am 
            FROM jobs 
            WHERE eingabe_datei LIKE ? OR eingabe_verzeichnis LIKE ? OR ausgabe_datei LIKE ? OR beschreibung LIKE ?
            ORDER BY id DESC
        """, (like, like, like, like))
    else:
        c.execute("""
            SELECT id, eingabe_datei, eingabe_verzeichnis, ausgabe_datei, startzeit, endzeit, beschreibung, gruppe, untergruppe, erstellt_am 
            FROM jobs ORDER BY id DESC
        """)
    for row in c.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()

# --- GUI Helfer ---
def browse_input_dir():
    directory = filedialog.askdirectory()
    if directory:
        entry_input_dir.delete(0, tk.END)
        entry_input_dir.insert(0, directory)

def browse_input_file():
    directory = entry_input_dir.get().strip()
    if not directory or not os.path.exists(directory):
        messagebox.showwarning("Hinweis", "Bitte zuerst ein gültiges Eingabeverzeichnis auswählen.")
        return
    filename = filedialog.askopenfilename(initialdir=directory, filetypes=[("MP4 Dateien", "*.mp4"), ("Alle Dateien", "*.*")])
    if filename:
        entry_input_file.delete(0, tk.END)
        entry_input_file.insert(0, os.path.basename(filename))

def unique_output_path(directory, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    path = os.path.join(directory, filename)
    while os.path.exists(path):
        path = os.path.join(directory, f"{base}_{counter}{ext}")
        counter += 1
    return path

def fill_job_fields(values):
    entry_input_dir.delete(0, tk.END)
    entry_input_dir.insert(0, values[2])
    entry_input_file.delete(0, tk.END)
    entry_input_file.insert(0, values[1])
    entry_output.delete(0, tk.END)
    entry_output.insert(0, values[3])
    entry_start.delete(0, tk.END)
    entry_start.insert(0, values[4])
    entry_end.delete(0, tk.END)
    entry_end.insert(0, values[5])
    text_beschreibung.delete("1.0", tk.END)
    text_beschreibung.insert(tk.END, values[6])
    if values[7]:
        combo_gruppe.set(values[7])
        load_subgroups()
    if values[8]:
        combo_untergruppe.set(values[8])

# --- FFmpeg Funktionen ---
def run_ffmpeg():
    eingabe_dir = entry_input_dir.get()
    eingabe_file = entry_input_file.get().strip()
    ausgabe_name = entry_output.get().strip() or "output.mp4"
    start = entry_start.get()
    ende = entry_end.get()
    beschreibung = text_beschreibung.get("1.0", tk.END).strip()
    gruppe = combo_gruppe.get()
    untergruppe = combo_untergruppe.get()

    if not (eingabe_dir and eingabe_file and start and ende):
        messagebox.showerror("Fehler", "Bitte Eingabeverzeichnis, Eingabedatei, Start- und Endzeit angeben!")
        return

    eingabe_path = os.path.join(eingabe_dir, eingabe_file)
    if not os.path.exists(eingabe_path):
        messagebox.showerror("Fehler", "Eingabedatei existiert nicht!")
        return

    ausgabe_path = unique_output_path(eingabe_dir, ausgabe_name)
    cmd = ["ffmpeg", "-i", eingabe_path, "-ss", start, "-to", ende, ausgabe_path]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        save_to_db(eingabe_file, eingabe_dir, os.path.basename(ausgabe_path), start, ende, beschreibung, gruppe, untergruppe)
        messagebox.showinfo("Erfolg", f"Video erfolgreich exportiert:\n{ausgabe_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Fehler", f"FFmpeg-Fehler:\n{e.stderr}")

def run_ffmpeg_threaded():
    threading.Thread(target=run_ffmpeg, daemon=True).start()

# --- Jobverwaltung ---
def load_selected_job(event=None):
    selected = tree.selection()
    if not selected: return
    values = tree.item(selected[0], "values")
    if values:
        fill_job_fields(values)

def rerun_selected_job():
    selected = tree.selection()
    if not selected: return
    values = tree.item(selected[0], "values")
    if values:
        fill_job_fields(values)
        run_ffmpeg_threaded()

def delete_selected_job():
    selected = tree.selection()
    if not selected: return
    values = tree.item(selected[0], "values")
    job_id = values[0]
    if messagebox.askyesno("Löschen bestätigen", f"Eintrag {job_id} wirklich löschen?"):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
        conn.commit()
        conn.close()
        load_history()
        messagebox.showinfo("Gelöscht", f"Eintrag {job_id} wurde gelöscht.")

def update_selected_job():
    selected = tree.selection()
    if not selected: return
    values = tree.item(selected[0], "values")
    job_id = values[0]

    eingabe_dir = entry_input_dir.get()
    eingabe_file = entry_input_file.get().strip()
    ausgabe_name = entry_output.get().strip() or "output.mp4"
    start = entry_start.get()
    ende = entry_end.get()
    beschreibung = text_beschreibung.get("1.0", tk.END).strip()
    gruppe = combo_gruppe.get()
    untergruppe = combo_untergruppe.get()

    if not (eingabe_dir and eingabe_file and start and ende):
        messagebox.showerror("Fehler", "Bitte Eingabeverzeichnis, Eingabedatei, Start- und Endzeit angeben!")
        return

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        UPDATE jobs
        SET eingabe_datei = ?, eingabe_verzeichnis = ?, ausgabe_datei = ?, startzeit = ?, endzeit = ?, beschreibung = ?, gruppe = ?, untergruppe = ?
        WHERE id = ?
    """, (eingabe_file, eingabe_dir, ausgabe_name, start, ende, beschreibung, gruppe, untergruppe, job_id))
    conn.commit()
    conn.close()
    load_history()
    for item in tree.get_children():
        if tree.item(item, "values")[0] == job_id:
            tree.selection_set(item)
            tree.focus(item)
            tree.see(item)
            break
    messagebox.showinfo("Aktualisiert", f"Eintrag {job_id} wurde aktualisiert und markiert.")

def apply_filter(event=None):
    filter_text = entry_filter.get().strip()
    load_history(filter_text)

# --- Gruppen / Untergruppen ---
def load_groups():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT name FROM gruppen ORDER BY name")
    gruppen = [row[0] for row in c.fetchall()]
    conn.close()
    combo_gruppe['values'] = gruppen
    if gruppen: combo_gruppe.current(0)
    load_subgroups()

def load_subgroups(event=None):
    selected_group = combo_gruppe.get()
    if not selected_group:
        combo_untergruppe['values'] = []
        return
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id FROM gruppen WHERE name = ?", (selected_group,))
    res = c.fetchone()
    if res:
        gruppe_id = res[0]
        c.execute("SELECT name FROM untergruppen WHERE gruppe_id = ? ORDER BY name", (gruppe_id,))
        untergruppen = [row[0] for row in c.fetchall()]
    else:
        untergruppen = []
    conn.close()
    combo_untergruppe['values'] = untergruppen
    if untergruppen: combo_untergruppe.current(0)

def open_groups_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Gruppenverwaltung")
    # Listen
    tk.Label(dialog, text="Gruppen:").grid(row=0, column=0)
    list_gruppen = tk.Listbox(dialog)
    list_gruppen.grid(row=1, column=0, padx=5, pady=5)
    tk.Label(dialog, text="Untergruppen:").grid(row=0, column=1)
    list_untergruppen = tk.Listbox(dialog)
    list_untergruppen.grid(row=1, column=1, padx=5, pady=5)
    # Laden Gruppen
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT name FROM gruppen ORDER BY name")
    for row in c.fetchall(): list_gruppen.insert(tk.END, row[0])
    conn.close()
    # Auswahl zeigt Untergruppen
    def on_group_select(event):
        selected = list_gruppen.curselection()
        if not selected: return
        group_name = list_gruppen.get(selected[0])
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT id FROM gruppen WHERE name = ?", (group_name,))
        gruppe_id = c.fetchone()[0]
        c.execute("SELECT name FROM untergruppen WHERE gruppe_id = ?", (gruppe_id,))
        list_untergruppen.delete(0, tk.END)
        for row in c.fetchall(): list_untergruppen.insert(tk.END, row[0])
        conn.close()
    list_gruppen.bind("<<ListboxSelect>>", on_group_select)
    # Buttons
    def add_group():
        name = simple_input("Neue Gruppe", "Name der Gruppe eingeben:")
        if not name: return
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        try: c.execute("INSERT INTO gruppen (name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            messagebox.showerror("Fehler", "Gruppe existiert bereits.")
            conn.close()
            return
        conn.commit()
        conn.close()
        list_gruppen.insert(tk.END, name)
        load_groups()
    def add_subgroup():
        selected = list_gruppen.curselection()
        if not selected: return
        group_name = list_gruppen.get(selected[0])
        name = simple_input("Neue Untergruppe", "Name der Untergruppe eingeben:")
        if not name: return
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT id FROM gruppen WHERE name = ?", (group_name,))
        gruppe_id = c.fetchone()[0]
        c.execute("INSERT INTO untergruppen (gruppe_id, name) VALUES (?, ?)", (gruppe_id, name))
        conn.commit()
        conn.close()
        list_untergruppen.insert(tk.END, name)
        load_subgroups()
    def delete_group():
        selected = list_gruppen.curselection()
        if not selected: return
        group_name = list_gruppen.get(selected[0])
        if messagebox.askyesno("Löschen bestätigen", f"Gruppe '{group_name}' löschen?"):
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("DELETE FROM gruppen WHERE name = ?", (group_name,))
            conn.commit()
            conn.close()
            list_gruppen.delete(selected[0])
            load_groups()
    tk.Button(dialog, text="Gruppe hinzufügen", command=add_group).grid(row=2, column=0, pady=5)
    tk.Button(dialog, text="Untergruppe hinzufügen", command=add_subgroup).grid(row=2, column=1, pady=5)
    tk.Button(dialog, text="Gruppe löschen", command=delete_group).grid(row=3, column=0, pady=5)

# Export gefilterte Daten
def export_markdown():
    items = tree.get_children()
    if not items:
        messagebox.showwarning("Hinweis", "Keine Daten zum Exportieren vorhanden.")
        return

    # Dateiauswahl für Export
    file_path = filedialog.asksaveasfilename(
        defaultextension=".md",
        filetypes=[("Markdown Dateien", "*.md"), ("Alle Dateien", "*.*")]
    )
    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as f:
        for item in items:
            values = tree.item(item, "values")
            eingabe_datei = values[1]
            eingabe_verzeichnis = values[2]
            ausgabe_datei = values[3]
            beschreibung = values[6] or ""

            # relativer Pfad (z. B. "Video/Datei.mp4")
            video_path = os.path.join(eingabe_verzeichnis, ausgabe_datei).replace("\\", "/")

            f.write(f"## {ausgabe_datei}\n\n")
            f.write(f"<video loop controls width=\"800\">\n")
            f.write(f"<source src=\"{video_path}\" type=\"video/mp4\">\n")
            f.write(f"</video>\n\n")
            if beschreibung.strip():
                f.write(f"{beschreibung}\n\n")

    messagebox.showinfo("Export abgeschlossen", f"Markdown-Datei gespeichert:\n{file_path}")

# Spalten Breiten speichern

def save_current_column_widths():
    config = load_config()
    for col in columns:
        config["column_widths"][col] = tree.column(col)["width"]
    save_config(config)
    messagebox.showinfo("Gespeichert", "Spaltenbreiten wurden gespeichert.")

import csv

def export_database():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Dateien", "*.csv"), ("Alle Dateien", "*.*")],
        title="Datenbank exportieren"
    )
    if not file_path:
        return

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # alle Daten aus jobs lesen
    c.execute("SELECT * FROM jobs")
    rows = c.fetchall()
    column_names = [desc[0] for desc in c.description]

    conn.close()

    # in CSV schreiben
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(column_names)
        writer.writerows(rows)

    messagebox.showinfo("Export abgeschlossen", f"Datenbank wurde exportiert nach:\n{file_path}")



def export_database_sql():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".sql",
        filetypes=[("SQL Dateien", "*.sql"), ("Alle Dateien", "*.*")],
        title="Gesamte Datenbank exportieren"
    )
    if not file_path:
        return

    conn = sqlite3.connect(DB_FILE)

    with open(file_path, "w", encoding="utf-8") as f:
        for line in conn.iterdump():
            f.write(f"{line}\n")

    conn.close()
    messagebox.showinfo("Export abgeschlossen", f"Gesamte Datenbank wurde exportiert nach:\n{file_path}")



# Export seleked Data

def export_selected_to_markdown():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Keine Auswahl", "Bitte wählen Sie mindestens einen Eintrag in der Tabelle aus.")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".md",
        filetypes=[("Markdown Dateien", "*.md"), ("Alle Dateien", "*.*")]
    )
    if not filepath:
        return

    with open(filepath, "w", encoding="utf-8") as f:
        for item in selected_items:
            values = tree.item(item, "values")

            # Werte extrahieren (anpassen an deine Spaltenreihenfolge!)
            eingabe_datei = values[1]
            ausgabe_datei = values[3]
            beschreibung = values[6]
            step = values[7] if len(values) > 7 else ""

            f.write(f"## {beschreibung}\n\n")
            if step.strip():
                f.write(f"**Step:** {step}\n\n")
            f.write(f"**Eingabe:** `{eingabe_datei}`  \n")
            f.write(f"**Ausgabe:** `{ausgabe_datei}`\n\n")
            f.write("---\n\n")

    messagebox.showinfo("Export abgeschlossen", f"Die ausgewählten Einträge wurden nach Markdown exportiert:\n{filepath}")


# --- GUI Setup ---
init_db()
root = tk.Tk()
root.title("FFmpeg Video Cutter mit SQLite + Gruppen/Untergruppen + Filter")

# Eingabefelder
tk.Label(root, text="Eingabeverzeichnis:").grid(row=0, column=0, sticky="w")
entry_input_dir = tk.Entry(root, width=100)
entry_input_dir.grid(row=0, column=1, padx=5, pady=5, sticky="w")
tk.Button(root, text="Verzeichnis wählen", command=browse_input_dir).grid(row=0, column=2, padx=5)

tk.Label(root, text="Eingabedatei:").grid(row=1, column=0, sticky="w")
entry_input_file = tk.Entry(root, width=100)
entry_input_file.grid(row=1, column=1, padx=5, pady=5, sticky="w")
tk.Button(root, text="Datei wählen", command=browse_input_file).grid(row=1, column=2, padx=5)

tk.Label(root, text="Ausgabedatei (nur Name):").grid(row=2, column=0, sticky="w")
entry_output = tk.Entry(root, width=100)
entry_output.grid(row=2, column=1, padx=5, pady=5,  sticky="w")

tk.Label(root, text="Startzeit (HH:MM:SS):").grid(row=3, column=0, sticky="w")
entry_start = tk.Entry(root, width=20)
entry_start.grid(row=3, column=1, sticky="w", padx=5, pady=5)

tk.Label(root, text="Endzeit (HH:MM:SS):").grid(row=4, column=0, sticky="w")
entry_end = tk.Entry(root, width=20)
entry_end.grid(row=4, column=1, sticky="w", padx=5, pady=5)

tk.Label(root, text="Beschreibung:").grid(row=5, column=0, sticky="nw")
text_beschreibung = tk.Text(root, width=50, height=4)
text_beschreibung.grid(row=5, column=1, padx=5, pady=5)

# Gruppe / Untergruppe
tk.Label(root, text="Gruppe:").grid(row=6, column=0, sticky="w")
combo_gruppe = ttk.Combobox(root, state="readonly")
combo_gruppe.grid(row=6, column=1, sticky="w", padx=5, pady=5)
combo_gruppe.bind("<<ComboboxSelected>>", load_subgroups)

tk.Label(root, text="Untergruppe:").grid(row=7, column=0, sticky="w")
combo_untergruppe = ttk.Combobox(root, state="readonly")
combo_untergruppe.grid(row=7, column=1, sticky="w", padx=5, pady=5)

tk.Button(root, text="Gruppen/Untergruppen verwalten", command=open_groups_dialog).grid(row=8, column=0, columnspan=2, pady=5)

# Buttons
tk.Button(root, text="Video schneiden", command=run_ffmpeg_threaded, bg="lightgreen").grid(row=9, column=0, columnspan=3, pady=10)

# Filter
tk.Label(root, text="Suche / Filter:").grid(row=10, column=0, sticky="w")
entry_filter = tk.Entry(root, width=40)
entry_filter.grid(row=10, column=1, padx=5, pady=5, sticky="w")
entry_filter.bind("<KeyRelease>", apply_filter)
tk.Button(root, text="Filter anwenden", command=apply_filter).grid(row=10, column=2, padx=5)

# Treeview
columns = ("ID", "Eingabe-Datei", "Eingabe-Verzeichnis", "Ausgabe-Datei", "Start", "Ende", "Beschreibung", "Gruppe", "Untergruppe")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
config = load_config()
column_widths = config.get("column_widths", {})

for col in columns:
    tree.heading(col, text=col)
    width = column_widths.get(col, 140)  # Fallback
    tree.column(col, width=width, anchor="w")
tree.grid(row=11, column=0, columnspan=3, padx=5, pady=10, sticky="nsew")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=11, column=3, sticky="ns")
tree.bind("<Double-1>", load_selected_job)

# Action Buttons
tk.Button(root, text="Ausgewählten Job erneut ausführen", command=rerun_selected_job, bg="lightblue").grid(row=12, column=0, columnspan=3, pady=5)
tk.Button(root, text="Ausgewählten Job aktualisieren", command=update_selected_job, bg="khaki").grid(row=13, column=0, columnspan=3, pady=5)
tk.Button(root, text="Ausgewählten Job löschen", command=delete_selected_job, bg="salmon").grid(row=14, column=0, columnspan=3, pady=5)
tk.Button(root, text="Gefilterte Daten als Markdown exportieren", command=export_markdown, bg="lightgrey").grid(row=15, column=0, columnspan=3, pady=5)
tk.Button(root, text="Spaltenbreiten speichern", command=save_current_column_widths).grid(row=16, column=0, columnspan=3, pady=5)
tk.Button(root, text="Datenbank exportieren (CSV)", command=export_database, bg="lightgrey").grid(row=17, column=0, columnspan=3, pady=5)
tk.Button(root, text="Gesamte Datenbank als SQL exportieren", command=export_database_sql, bg="lightgrey").grid(row=18, column=0, columnspan=3, pady=5)
tk.Button(root, text="Selektierte exportieren (Markdown)", command=export_selected_to_markdown).grid(row=19, column=0, columnspan=3, pady=5)

# Lade Gruppen und Historie
load_groups()
load_history()

root.mainloop()
