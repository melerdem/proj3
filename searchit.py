import tkinter as tk
from tkinter import scrolledtext

# --- Just example data ---
sample_results = {
    "Wikipedia": {
        "preview": "An apple is a round, edible fruit...",
        "full": "Wikipedia: An apple is a round, edible fruit produced by an apple tree (Malus spp.). Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus."
    },
    "Dictionary": {
        "preview": "1: the usually round, red or yellow...",
        "full": "Dictionary: 1: the usually round, red or yellow, edible fruit of a small tree of the rose family."
    },
    "Thesaurus": {
        "preview": "(No preview available)",
        "full": "Thesaurus: synonym suggestions not implemented."
    }
}

# --- Root window ---
root = tk.Tk()
root.title("Search It!")
root.geometry("600x500")

# --- Page 1: Search Screen ---
search_frame = tk.Frame(root)
search_frame.grid(row=0, column=0, sticky="nsew")

tk.Label(search_frame, text="Please enter a search query:", font=('Arial', 14)).pack(pady=20)
query_entry = tk.Entry(search_frame, font=('Arial', 12), width=40)
query_entry.pack(pady=10)

def go_to_results():
    query = query_entry.get()
    if query:
        query_label.config(text=query)
        results_frame.tkraise()

tk.Button(search_frame, text="Search", command=go_to_results).pack(pady=20)

# --- Page 2: Results List ---
results_frame = tk.Frame(root)
results_frame.grid(row=0, column=0, sticky="nsew")

query_label = tk.Label(results_frame, text="", font=('Arial', 14, 'bold'))
query_label.pack(pady=10)

tk.Label(results_frame, text="Choose a source:", font=('Arial', 12)).pack()

def show_full_result(source):
    full_result_title.config(text=source)
    full_result_text.delete("1.0", tk.END)
    full_result_text.insert(tk.END, sample_results[source]["full"])
    full_result_frame.tkraise()

for source in sample_results:
    preview = sample_results[source]["preview"]
    btn = tk.Button(results_frame, text=f"{source}\n\"{preview}\"", justify="left",
                    command=lambda s=source: show_full_result(s), wraplength=550, anchor="w")
    btn.pack(fill="x", padx=20, pady=5)

tk.Button(results_frame, text="← Back", command=lambda: search_frame.tkraise()).pack(pady=20)

# --- Page 3: Full Result Display ---
full_result_frame = tk.Frame(root)
full_result_frame.grid(row=0, column=0, sticky="nsew")

full_result_title = tk.Label(full_result_frame, text="", font=('Arial', 14, 'bold'))
full_result_title.pack(pady=10)

full_result_text = scrolledtext.ScrolledText(full_result_frame, wrap="word", width=70, height=15)
full_result_text.pack(padx=10, pady=10)

tk.Button(full_result_frame, text="← Back", command=lambda: results_frame.tkraise()).pack(pady=10)

# Start with the search page
search_frame.tkraise()
root.mainloop()
