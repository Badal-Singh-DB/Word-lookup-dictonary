import tkinter as tk
from tkinter import ttk
from trie import Trie
from spelling_correction import get_suggestions
from web_scraping import get_word_definition

class WordLookupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Lookup Dictionary")
        self.trie = Trie()
        self.load_dictionary()

        self.search_var = tk.StringVar()
        self.suggestions = []

        self.create_widgets()

    def load_dictionary(self):
        try:
            with open("words.txt", "r") as f:
                for line in f:
                    word = line.strip()
                    self.trie.insert(word)
            print("Dictionary loaded successfully.")
        except Exception as e:
            print(f"Error loading dictionary: {e}")

    def create_widgets(self):
        self.entry = ttk.Entry(self.root, textvariable=self.search_var)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        self.entry.bind("<KeyRelease>", self.on_key_release)

        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=1, column=0, padx=10, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

        self.text = tk.Text(self.root, wrap=tk.WORD, height=10, width=50)
        self.text.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

    def on_key_release(self, event):
        print("Key released")  # Debug statement
        query = self.search_var.get().strip().lower()
        print(f"Query: {query}")  # Debug statement
        if query:
            self.suggestions = self.trie.auto_suggestions(query)
            self.update_suggestions()

    def update_suggestions(self):
        print("Updating suggestions")  # Debug statement
        self.listbox.delete(0, tk.END)
        for suggestion in self.suggestions:
            self.listbox.insert(tk.END, suggestion)
        print("Suggestions updated")  # Debug statement


    def on_listbox_select(self, event):
        selected_word = self.listbox.get(self.listbox.curselection())
        definition = get_word_definition(selected_word)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, f"{selected_word}\n\n{definition}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordLookupApp(root)
    root.mainloop()
