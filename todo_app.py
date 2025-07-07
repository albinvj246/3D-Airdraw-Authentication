#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        # List to store tasks
        self.tasks = []
        
        # Create GUI elements
        self.create_header()
        self.create_task_entry()
        self.create_buttons()
        self.create_task_listbox()

    def create_header(self):
        header = tk.Label(
            self.root,
            text="📝 My Task Manager",
            font=("Helvetica", 16, "bold"),
            bg="#f0f0f0",
            pady=10
        )
        header.pack()

    def create_task_entry(self):
        self.task_entry = tk.Entry(
            self.root,
            width=30,
            font=("Helvetica", 12)
        )
        self.task_entry.pack(pady=10)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        add_btn = tk.Button(
            button_frame,
            text="Add Task",
            command=self.add_task,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 10)
        )
        add_btn.pack(side=tk.LEFT, padx=5)

        complete_btn = tk.Button(
            button_frame,
            text="Mark Complete",
            command=self.mark_complete,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 10)
        )
        complete_btn.pack(side=tk.LEFT, padx=5)

        delete_btn = tk.Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task,
            bg="#f44336",
            fg="white",
            font=("Helvetica", 10)
        )
        delete_btn.pack(side=tk.LEFT, padx=5)

    def create_task_listbox(self):
        self.task_listbox = tk.Listbox(
            self.root,
            width=40,
            height=15,
            font=("Helvetica", 11),
            selectmode=tk.SINGLE
        )
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            timestamp = datetime.now().strftime("%H:%M:%S")
            task_with_time = f"[{timestamp}] {task}"
            self.tasks.append(task_with_time)
            self.task_listbox.insert(tk.END, task_with_time)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            if not task.startswith("✓"):
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, f"✓ {task}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()