import tkinter as tk
from tkinter.simpledialog import askstring
import socket
import requests as req
from tkinter import scrolledtext, ttk, messagebox
from time import sleep
from json import load, dump

class ArcticClient:
    def __init__(self):
        self.username = None

        self.root = tk.Tk()
        self.root.title("Arctic Client")

        self.hub_server = "127.0.0.1"
        self.packet_delay = 0.02

        self.cds_ip = ""

        with open("style.json") as style_file:
            self.style = load(style_file)
        self.background_color = self.style["label_background_color"]
        self.font_color = self.style["font_color"]

        self.notebook = ttk.Notebook(self.root)

    
    def setup_window(self):
        def username_entered(event):
            self.username = username_input.get()
            self.root.title(f"Arctic Client - {self.username}")
            setup_widgets.grid_forget()
            self.connect_to_server()
        self.root.geometry("1280x1020")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.root.configure(bg=self.style["background"])

        setup_widgets = tk.Canvas(self.root)
        username_label = tk.Label(setup_widgets, text="Enter username: ", bg=self.background_color, fg=self.font_color)
        username_input = tk.Entry(setup_widgets, bg=self.background_color, fg=self.font_color)
        username_label.grid(column=0, row=0)
        username_input.grid(column=1, row=0)
        setup_widgets.grid(column=0, row=0)
        username_input.bind("<Return>", username_entered)
    
    def connect_to_server(self):
        def server_selection_made(event):
            servername = self.serverlist_widget.get()
            self.serverlist_widget.grid_forget()
            self.serverlist_label.config(text=f"Selected server: {servername}")
            self.socket.send(servername.encode())
            sleep(self.packet_delay)
            self.cds_ip = self.socket.recv(16).decode()
            sleep(self.packet_delay)
            self.socket.close()
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.cds_ip, 5666))
            sleep(self.packet_delay)
            self.socket.send(f"JOIN;{self.username}".encode())
            self.handle_user()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.hub_server, 5667))
        self.socket.settimeout(None)
        self.socket.send(b'0') # We are not a server
        serverlist = self.socket.recv(65535).decode().split("\n")
        self.serverlist_label = tk.Label(self.root, text="Select a server to connect to: ",
                                         bg=self.background_color, fg=self.font_color)
        self.serverlist_widget = ttk.Combobox(self.root, values=serverlist, state="readonly", foreground=self.font_color)
        self.serverlist_label.grid(column=0, row=0)
        self.serverlist_widget.grid(column=1, row=0)
        self.serverlist_widget.current(0)
        self.serverlist_widget.bind("<<ComboboxSelected>>", server_selection_made)

    def handle_user(self):
        self.rules = self.recv_until(";")
        sleep(self.packet_delay)
        self.version = self.recv_until(";")
        sleep(self.packet_delay)
        join_status = self.socket.recv(4096).decode()
        if join_status == "YES":
            self.admin = True
        elif join_status == "NOO":
            self.admin = False
        elif join_status == "403":
            messagebox.showerror("Error", "Access denied.")
            self.on_close()
        self.show_ui(self.admin)

    def get_site_list(self):
        self.socket.send(b'LIST')
        sleep(self.packet_delay)
        sites = self.socket.recv(65535).decode().split(",")
        return sites

    def list_sites(self):
        sites = self.get_site_list()
        text = '\n'.join(sites)
        self.update_textarea(f"Sites: \n{text}")
        self.textarea.grid(row=4, columnspan=4)
    
    def create_site(self):
        sitename = None
        self.clear_ui()
        self.site_create_canvas = tk.Canvas(self.root)
        def sitename_clicked():
            sitename = sitename_entry.get()
            content = sitecontent_entry.get("1.0", "end-1c")
            self.socket.send(f"WRIT;{sitename};{content}".encode())
            sleep(self.packet_delay)
            self.socket.send(b"//quit")
            self.site_create_canvas.grid_forget()
        self.textarea.grid_forget()
        sitename_label = tk.Label(self.site_create_canvas, text="Enter the title of the site: ")
        sitename_entry = tk.Entry(self.site_create_canvas)
        sitename_label.grid(column=0, row=2)
        sitename_entry.grid(column=1, row=2)
        sitecontent_label = tk.Label(self.site_create_canvas, text="Enter site content")
        sitecontent_entry = tk.Text(self.site_create_canvas, height=10, width=50)
        send_site_button = tk.Button(self.site_create_canvas, text="Create site", command=sitename_clicked)
        sitecontent_label.grid(column=0, row=3)
        send_site_button.grid(column=1, row=3)
        sitecontent_entry.grid(column=1, row=4)
        self.site_create_canvas.grid(column=0, row=1)
    
    def view_site(self):
        self.clear_ui()
        self.view_canvas = tk.Canvas(self.root)
        sites = self.get_site_list()
        def view_site_selection_made(event):
            sitename = sitename_combobox.get()
            self.socket.send(f"RECV;{sitename}".encode())
            sleep(self.packet_delay)
            content = self.socket.recv(65535).decode()
            self.update_textarea(f"Site: \n{content}")
        sitename_combobox = ttk.Combobox(self.view_canvas, values=sites, state="readonly")
        sitename_combobox.current(0)
        sitename_combobox.bind("<<ComboboxSelected>>", view_site_selection_made)
        sitename_label = tk.Label(self.view_canvas, text="Select a site to view: ")
        sitename_label.grid(column=0, row=2)
        sitename_combobox.grid(column=1, row=2)
        self.view_canvas.grid(column=0, row=1)
    
    def promote(self):
        self.clear_ui()
        self.promote_canvas = tk.Canvas(self.root)
        def promote():
            username = username_entry.get()
            self.socket.send(f"SUDO;{username}".encode())
            self.promote_canvas.grid_forget()
            result = self.socket.recv(128).decode()
            self.update_textarea(f"Promote result: {result}")
        username_label = tk.Label(self.promote_canvas, text="Enter username to promote:")
        username_entry = tk.Entry(self.promote_canvas)
        promote_button = tk.Button(self.promote_canvas, text="Promote", command=promote)
        username_label.grid(column=0, row=2)
        username_entry.grid(column=1, row=2)
        promote_button.grid(column=2, row=2)
        self.promote_canvas.grid(column=0, row=1)

    def whitelist(self):
        self.clear_ui()
        self.whitelist_canvas = tk.Canvas(self.root)
        def whitelist_add():
            username = username_entry.get()
            self.socket.send(f"WHTL;{username}".encode())
            sleep(self.packet_delay)
            result = self.socket.recv(128).decode()
            self.update_textarea(f"Whitelist result: {result}")
            self.whitelist_canvas.grid_forget()
        username_label = tk.Label(self.whitelist_canvas, text="Enter username to whitelist:")
        username_entry = tk.Entry(self.whitelist_canvas)
        whitelist_add_button = tk.Button(self.whitelist_canvas, text="Add to whitelist", command=whitelist_add)
        username_label.grid(column=0, row=2)
        username_entry.grid(column=1, row=2)
        whitelist_add_button.grid(column=2, row=2)
        self.whitelist_canvas.grid(column=0, row=1)


    def on_close(self):
        if hasattr(self, "socket"):
            self.socket.close()
        self.root.destroy()

    def run(self):
        self.setup_window()
        self.root.mainloop()
    
    def recv_until(self, separator: str):
        data = ""
        while not separator in data:
            data += self.socket.recv(1).decode()
        return data.split(separator)[0]
    
    def show_ui(self, admin):
        self.menu_ui = tk.Canvas(self.root)
        self.server_select_button = tk.Button(self.menu_ui, text="Back to server selection", command=self.server_select)
        self.server_select_button.grid(column=1, row=0)
        self.list_site_button = tk.Button(self.menu_ui, text="List sites", command=self.list_sites)
        self.list_site_button.grid(column=0, row=1)
        self.create_site_button = tk.Button(self.menu_ui, text="Create site", command=self.create_site)
        self.create_site_button.grid(column=1, row=1)
        self.view_site_button = tk.Button(self.menu_ui, text="View site", command=self.view_site)
        self.view_site_button.grid(column=2, row=1)
        if admin:
            self.promote_button = tk.Button(self.menu_ui, text="Promote user", command=self.promote)
            self.promote_button.grid(column=3, row=1)
            self.whitelist_add = tk.Button(self.menu_ui, text="Add user to whitelist", command=self.whitelist)
            self.whitelist_add.grid(column=4, row=1)
        self.textarea = scrolledtext.ScrolledText(self.root, state="disabled")
        self.textarea.grid(row=4, columnspan=4)
        self.menu_ui.grid(row=0)
    
    def server_select(self):
        self.menu_ui.grid_forget()
        self.textarea.grid_forget()
        self.clear_ui()
        self.connect_to_server()
    
    def clear_ui(self):
        try:
            self.site_create_canvas.grid_forget()
        except AttributeError:
            pass
        try:
            self.view_canvas.grid_forget()
        except AttributeError:
            pass
        try:
            self.promote_canvas.grid_forget()
        except AttributeError:
            pass

    def update_textarea(self, message):
        self.textarea.config(state="normal")
        self.textarea.delete("1.0", tk.END)
        self.textarea.insert(tk.END, message + "\n")
        self.textarea.config(state="disabled")

if __name__ == "__main__":
    client = ArcticClient()
    client.run()