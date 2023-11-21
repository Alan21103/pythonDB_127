import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to handle the submit button click
def submit_data():
    # Get values from entry widgets
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    fakultas_prediksi = prediksi_fakultas(nama_siswa, biologi, fisika, inggris)

    cursor.execute('''
      INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
      VALUES (?, ?, ?, ?, ?)
      ''', (nama_siswa, biologi, fisika, inggris, fakultas_prediksi))
    conn.commit()
    conn.close()

    messagebox.showinfo('info', 'Data submitted success successfully')
    result_label.config(text=f'Prodi: {fakultas_prediksi}')

    # Calculate predicted faculty based on highest score
def prediksi_fakultas(nama_siswa, biologi, fisika, inggris):
   if biologi > fisika and biologi > inggris:
      return 'Kedokteran'
   elif fisika > biologi and fisika > inggris:
      return 'Teknik'
   elif inggris > biologi and inggris > fisika:
      return 'Bahasa'
   else:
      return 'Belum dapat diprediksi'
    
# Insert data into SQLite database
conn = sqlite3.connect('jabuk.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY,
    nama_siswa TEXT,
    biologi INTEGER,
    fisika INTEGER,
    inggris INTEGER,
    prediksi_fakultas TEXT
    ) 
''')

# Create the main window
root = tk.Tk()
root.title('Input Nilai Siswa')

label_nama = tk.Label(root, text='Nama Siswa:')
label_biologi = tk.Label(root, text='Nilai Biologi:')
label_fisika = tk.Label(root, text='Nilai Fisika:')
label_inggris = tk.Label(root, text='Nilai Inggris:')

entry_nama = tk.Entry(root)
entry_biologi = tk.Entry(root)
entry_fisika = tk.Entry(root)
entry_inggris = tk.Entry(root)

label_nama.grid(row=0, column=0)
label_biologi.grid(row=1, column=0)
label_fisika.grid(row=2, column=0)
label_inggris.grid(row=3, column=0)

result_label = tk.Label(root,text="Prodi : ")
result_label.grid(row=5,columnspan=2)

entry_nama.grid(row=0, column=1)
entry_biologi.grid(row=1, column=1)
entry_fisika.grid(row=2, column=1)
entry_inggris.grid(row=3, column=1)

button_submit = tk.Button(root, text='Submit', command=submit_data)
button_submit.grid(row=4, column=0, columnspan=2)

root.mainloop()