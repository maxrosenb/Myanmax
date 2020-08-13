import csv
import sys
import requests
import tkinter as tk

# Let's create the Tkinter window

window = tk.Tk()
window.geometry("1000x1000")
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
window.title("Myanmax")
search_string = tk.StringVar()
listbox = tk.Listbox(window, yscrollcommand=scrollbar.set, width=150)
# creating a function called DataCamp_Tutorial()
def search_corpus(event=None):
    listbox.delete(0, 'end')
    with open('myanmax.csv') as f:
        s = e.get()
        
        print("SEARCH TERM: ", s)
        reader = csv.DictReader(f)
        next(reader, None) # discard the header
        i = 0
        for row in reader:
            if s in row['Text']:
                listbox.insert(tk.END, row['Text'])
                listbox.insert(tk.END, "source: " + row['Url'])
                i += 1
            listbox.pack(side=tk.LEFT, fill=tk.BOTH)
            if i >= 10:
                    break

window.bind('<Return>', search_corpus)
scrollbar.config(command=listbox.yview)
e = tk.Entry()
e.pack()
tk.Button(window, text = "Search", command = search_corpus).pack()
window.mainloop()



