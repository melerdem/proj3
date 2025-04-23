import tkinter as tk
from tkinter import scrolledtext
from API import get_wikipedia, get_dictionary, get_thesaurus  # Make sure API_PyTest.py is in same folder

# --- GUI Root Window ---
root = tk.Tk()
root.title("Search It!")
root.geometry("600x500")

# --- Search Frame (Page 1) ---
search_frame = tk.Frame(root)
search_frame.grid(row=0, column=0, sticky="nsew")

tk.Label(search_frame, text="Please enter a search query:", font=('Arial', 14)).pack(pady=20)
query_entry = tk.Entry(search_frame, font=('Arial', 12), width=40)
query_entry.pack(pady=10)

# --- Results Frame (Page 2) ---
results_frame = tk.Frame(root)
results_frame.grid(row=0, column=0, sticky="nsew")

#query_label = tk.Label(results_frame, text="", font=('Arial', 14, 'bold'))
#query_label.pack(pady=10)

tk.Label(results_frame, text="Choose a source:", font=('Arial', 12)).pack()

# --- Full Result Frame (Page 3) ---
full_result_frame = tk.Frame(root)
full_result_frame.grid(row=0, column=0, sticky="nsew")

full_result_title = tk.Label(full_result_frame, text="", font=('Arial', 14, 'bold'))
full_result_title.pack(pady=10)

full_result_text = scrolledtext.ScrolledText(full_result_frame, wrap="word", width=70, height=15)
full_result_text.pack(padx=10, pady=10)

tk.Button(full_result_frame, text="← Back", command=lambda: results_frame.tkraise()).pack(pady=10)

# --- Function to Show Full Result ---
def show_full_result_from_dict(source, results):
    full_result_title.config(text=source)
    full_result_text.delete("1.0", tk.END)
    full_result_text.insert(tk.END, results[source]["full"])
    full_result_frame.tkraise()

# --- Function to Populate Buttons Dynamically ---
def update_results_ui(results, query):
    # Clear all widgets from results_frame
    for widget in results_frame.winfo_children():
        widget.destroy()

    # Create a new label for the query
    label = tk.Label(results_frame, text=query, font=('Arial', 14, 'bold'))
    label.pack(pady=10)

    tk.Label(results_frame, text="Choose a source:", font=('Arial', 12)).pack()

    for source in results:
        preview = results[source]["preview"]
        btn = tk.Button(results_frame, text=f"{source}\n\"{preview}\"", justify="left",
                        command=lambda s=source: show_full_result_from_dict(s, results),
                        wraplength=550, anchor="w")
        btn.pack(fill="x", padx=20, pady=5)

    tk.Button(results_frame, text="← Back", command=lambda: search_frame.tkraise()).pack(pady=20)


# --- API Fetching Logic ---
def fetch_all_results(query):
    results = {
        "Wikipedia": {"preview": "", "full": ""},
        "Dictionary": {"preview": "", "full": ""},
        "Thesaurus": {"preview": "", "full": ""}
    }

    # Wikipedia
    try:
        page = get_wikipedia(query)
        if page.exists():
            results["Wikipedia"]["preview"] = page.summary[:60] + "..."
            results["Wikipedia"]["full"] = f"Wikipedia:\n\n{page.summary}"
        else:
            results["Wikipedia"]["preview"] = "(No entry)"
            results["Wikipedia"]["full"] = "Wikipedia page not found."
    except Exception as e:
        results["Wikipedia"]["preview"] = "(Error)"
        results["Wikipedia"]["full"] = f"Error fetching Wikipedia: {str(e)}"

    # Dictionary
    definitions = get_dictionary(query)
    results["Dictionary"]["preview"] = definitions[0][:60] + "..." if definitions else "(No preview)"
    results["Dictionary"]["full"] = "Dictionary:\n\n" + "\n\n".join(definitions)

    # Thesaurus
    synonyms, antonyms = get_thesaurus(query)
    results["Thesaurus"]["preview"] = ", ".join(synonyms[:3]) if synonyms else "(No preview)"
    thesaurus_text = "Thesaurus:\n\n"
    thesaurus_text += "Synonyms:\n" + ", ".join(synonyms) if synonyms else "No synonyms found.\n"
    thesaurus_text += "\n\nAntonyms:\n" + ", ".join(antonyms) if antonyms else "\nNo antonyms found."
    results["Thesaurus"]["full"] = thesaurus_text

    return results

# --- Search Button Action ---
def go_to_results():
    query = query_entry.get().strip()
    if query:
        results = fetch_all_results(query)
        update_results_ui(results, query)
        results_frame.tkraise()


tk.Button(search_frame, text="Search", command=go_to_results).pack(pady=20)

# --- Start with Search Page ---
search_frame.tkraise()
root.mainloop()
