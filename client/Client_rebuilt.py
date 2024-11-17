import tkinter as tk
from tkinter import Text, scrolledtext, messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Label, Button, Combobox, Frame
import socket
from time import sleep


class ArcticClient:
    def __init__(self):
        self.username = None
        self.hub_server = "node1.kranem.hu"
        self.packet_delay = 0.02
        self.cds_ip = ""

        # Initialize style and theme
        self.current_theme = "cosmo"  # Default theme (light)
        self.style = Style(theme=self.current_theme)
        self.root = self.style.master
        self.root.title("Arctic Client")
        self.root.geometry("600x400")

        self.main_frame = Frame(self.root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

    def setup_window(self):
        # Function triggered when username is entered
        def username_entered(event=None):
            self.username = username_input.get()
            if not self.username.strip():
                messagebox.showwarning("Warning", "Username cannot be empty!")
                return
            self.root.title(f"Arctic Client - {self.username}")
            username_frame.destroy()
            self.connect_to_server()

        # Username input UI
        username_frame = Frame(self.main_frame)
        username_frame.pack(fill="both", expand=True, pady=30)

        username_label = Label(username_frame, text="Enter Username:", font=("Helvetica", 14))
        username_label.grid(row=0, column=0, padx=10, pady=5)

        username_input = Entry(username_frame, font=("Helvetica", 14))
        username_input.grid(row=0, column=1, padx=10, pady=5)
        username_input.bind("<Return>", username_entered)

        submit_button = Button(username_frame, text="Submit", command=username_entered)
        submit_button.grid(row=0, column=2, padx=10, pady=5)

    def connect_to_server(self):
        def server_selected(event):
            servername = server_combobox.get()
            self.socket.send(servername.encode())
            sleep(self.packet_delay)
            self.cds_ip = self.socket.recv(16).decode()
            self.socket.close()

            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.cds_ip, 6071))
            sleep(self.packet_delay)
            self.socket.send(f"JOIN;{self.username}".encode())
            self.server_frame.destroy()
            self.handle_user()

        # Connect to the hub server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.hub_server, 6081))
        self.socket.settimeout(None)
        self.socket.send(b"0")  # Indicate that this is not a server
        server_list = self.socket.recv(65535).decode().split("\n")

        # Display server selection UI
        self.server_frame = Frame(self.main_frame, padding=10)
        self.server_frame.pack(fill="both", expand=True)

        server_label = Label(self.server_frame, text="Select a Server:", font=("Helvetica", 14))
        server_label.pack(pady=10)

        server_combobox = Combobox(self.server_frame, values=server_list, font=("Helvetica", 12))
        server_combobox.pack(pady=10)
        server_combobox.bind("<<ComboboxSelected>>", server_selected)

    def handle_user(self):
        self.rules = self.recv_until(";")
        sleep(self.packet_delay)
        self.version = self.recv_until(";")
        sleep(self.packet_delay)

        join_status = self.socket.recv(4096).decode()
        if join_status == "403":
            messagebox.showerror("Access Denied", "You are not allowed to join this server.")
            self.on_close()
            return

        self.admin = join_status == "YES"
        self.show_ui()

    def show_ui(self):
        # Main user interface
        self.main_frame.destroy()
        self.main_frame = Frame(self.root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        # Add functional buttons
        Button(self.main_frame, text="List Sites", command=self.list_sites, width=20).pack(pady=10)
        Button(self.main_frame, text="Create Site", command=self.create_site, width=20).pack(pady=10)
        Button(self.main_frame, text="View Site", command=self.view_site, width=20).pack(pady=10)

        if self.admin:
            Button(self.main_frame, text="Promote User", command=self.promote, width=20).pack(pady=10)
            Button(self.main_frame, text="Add to Whitelist", command=self.whitelist, width=20).pack(pady=10)

        # Theme switcher button
        Button(self.main_frame, text="Switch Theme", command=self.switch_theme, width=20).pack(pady=10)

        # Scrolled text area for display
        self.textarea = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, height=10, state="disabled")
        self.textarea.pack(fill="both", expand=True, pady=10)

    def switch_theme(self):
        # Toggle between "cosmo" (light) and "darkly" (dark)
        self.current_theme = "darkly" if self.current_theme == "cosmo" else "cosmo"
        self.style.theme_use(self.current_theme)
        self.root.update()

    def recv_until(self, separator):
        data = ""
        while separator not in data:
            data += self.socket.recv(1).decode()
        return data.split(separator)[0]

    def update_textarea(self, message):
        self.textarea.config(state="normal")
        self.textarea.delete("1.0", tk.END)
        self.textarea.insert(tk.END, message)
        self.textarea.config(state="disabled")

    def list_sites(self):
        self.socket.send(b"LIST")
        sleep(self.packet_delay)
        sites = self.socket.recv(65535).decode().split(",")
        self.update_textarea("Available Sites:\n" + "\n".join(sites))

    def create_site(self):
        def submit_site():
            sitename = sitename_entry.get()
            content = sitecontent_entry.get("1.0", "end-1c")
            self.socket.send(f"WRIT;{sitename};{content}".encode())
            sleep(self.packet_delay)
            result = self.socket.recv(128).decode()
            messagebox.showinfo("Site Creation", result)
            self.update_textarea(f"Site '{sitename}' created successfully.")

        site_window = tk.Toplevel(self.root)
        site_window.title("Create Site")
        site_window.geometry("400x300")

        Label(site_window, text="Site Name:").pack(pady=10)
        sitename_entry = Entry(site_window)
        sitename_entry.pack()

        Label(site_window, text="Site Content:").pack(pady=10)
        sitecontent_entry = Text(site_window, height=8, width=40)  # Use tkinter Text widget
        sitecontent_entry.pack()

        Button(site_window, text="Create Site", command=submit_site).pack(pady=10)

    def on_close(self):
        if hasattr(self, "socket"):
            self.socket.close()
        self.root.destroy()

    def run(self):
        self.setup_window()
        self.root.mainloop()

    def view_site(self):
        # Fetch the list of sites
        self.socket.send(b"LIST")
        sleep(self.packet_delay)
        sites = self.socket.recv(65535).decode().split(",")

        if not sites or sites == [""]:
            messagebox.showinfo("No Sites", "No sites available to view.")
            return

        # Create a new window for site selection
        view_window = tk.Toplevel(self.root)
        view_window.title("View Site")
        view_window.geometry("400x300")
        view_window.resizable(False, False)

        ttk.Label(view_window, text="Select a site to view:", anchor="center").pack(pady=10)

        # Create the dropdown menu (Combobox)
        site_combobox = ttk.Combobox(view_window, values=sites, state="readonly", bootstyle="info")
        site_combobox.pack(pady=10)
        site_combobox.current(0)  # Preselect the first item

        # Function to load and display the site content
        def load_site_content():
            sitename = site_combobox.get()
            if not sitename:
                messagebox.showwarning("Warning", "Please select a site to view.")
                return

            # Request content of the selected site
            self.socket.send(f"RECV;{sitename}".encode())
            sleep(self.packet_delay)
            content = self.socket.recv(65535).decode()

            # Display content in the main text area
            self.update_textarea(f"Site: {sitename}\n\n{content}")
            view_window.destroy()  # Close the view window after content is loaded

        # Add a button to load the selected site
        ttk.Button(view_window, text="View", command=load_site_content, bootstyle="success").pack(pady=20)


if __name__ == "__main__":
    ArcticClient().run()
