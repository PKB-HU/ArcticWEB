import threading
import time
import os
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import socket
import requests as req
from tkinter import scrolledtext
from tkinter import ttk
import platform

print(platform.system())

opsys = platform.system()

charset = '@&#'

admin = False

VERSION = '2.0'

clear_command = "cls" if opsys == "Windows" else "clear"


def send_username(username_):
    username_command = f'usr{username_}'
    q.send(bytes(username_command, 'utf-8'))
    message = q.recv(1024).decode("utf-8")
    if message == "1":
        admin = True
        tk.messagebox.showinfo('Stray',
                                'Rendszergazdai jogosultságok megadva.')


connect = False

url: str = 'https://checkip.amazonaws.com'
req = req.get(url)
ip: str = req.text

def update_checker():
    try:
        new_update_code = q.recv(1024).decode('utf-8')
        print(new_update_code)
        with open('version', 'r') as k:
            old_update_code = VERSION
            print(f'Program is running on {old_update_code}')
            print(f'Server is running on {new_update_code}')
            if str(old_update_code) != str(new_update_code):
                if new_update_code == 'MAINTANCE':
                    tk.messagebox.showerror('Karbantartási Szünet!',
                                            'Karbantartási Szünet! Kérjük próbálja meg később.')
                    quit()
                else:
                    tk.messagebox.showerror('Frissítés',
                                            'Nem a legújabb verziót használja!\nKérjük telepítse az új verziót a weboldalunkról.')
    except:
        print("Error sending version request! [Check it manually on the website] ")

def update_gui(text, mode):
    text_box.config(state='normal')
    if mode == "del":
        text_box.delete(1.0, tk.END)

    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state='disabled')


while connect is False:
    if True:
        try:
            main_server = input("IP : ")
            q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            q.connect((main_server, 5667))
            q.settimeout(None)
            connect = True
            q.send("0".encode("utf-8"))
            time.sleep(0.1)
            print("Waiting for list...")
            os.system(clear_command)
            server_list = q.recv(1024).decode("utf-8")
            print("\n")
            print("\n")
            print("\n")
            print(server_list)
            print("\n")
            server = input("Choose server >> : ")
            print(server)
            q.send(server.encode("utf-8"))
            time.sleep(0.1)
            ip_to_connect = q.recv(1024).decode("utf-8")
            time.sleep(1)
            os.system(clear_command)
            print(f"IP : {ip_to_connect}")
            q.close()
        except:
            print("Can't connect to server!")



# username = askstring('Stray', 'Username : ')
username = input("Nickname : ")

os.system(clear_command)




connect = False

# HOST_IP = askstring('ArcticWEB', 'IP : ')

while connect is False:
    if True:

        q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        q.connect((ip_to_connect, 5666))
        q.settimeout(None)

        label = q.recv(1024).decode("utf-8").replace("\n", "")
        print(label)
        server_name = q.recv(1024).decode("utf-8").replace("\n", "")
        print(server_name)
        server_name_to_show = q.recv(1024).decode("utf-8").replace("\n", "")
        print(server_name_to_show)

        buttonframe_bg = q.recv(1024).decode("utf-8").replace("\n", "")
        print(buttonframe_bg)
        opacity = q.recv(1024).decode("utf-8").replace("\n", "")
        print(opacity)
        label_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(label_color)
        label_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(label_background_color)
        label_size = q.recv(1024).decode("utf-8").replace("\n", "")
        print(label_size)
        background = q.recv(1024).decode("utf-8").replace("\n", "")
        print(background)
        font_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(font_color)
        font_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(font_background_color)
        result_text_box_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(result_text_box_color)
        result_text_box_edge_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(result_text_box_edge_color)
        result_text_box_edge_color_selected = q.recv(1024).decode("utf-8").replace("\n", "")
        print(result_text_box_edge_color_selected)
        result_text_box_edge_size = q.recv(1024).decode("utf-8").replace("\n", "")
        print(result_text_box_edge_size)
        searchbar_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(searchbar_color)
        searchbar_edge_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(searchbar_edge_color)
        searchbar_edge_color_selected = q.recv(1024).decode("utf-8").replace("\n", "")
        print(searchbar_edge_color_selected)
        searchbar_edge_size = q.recv(1024).decode("utf-8").replace("\n", "")
        print(searchbar_edge_size)
        send_command_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(send_command_background_color)
        send_command_text_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(send_command_text_color)
        send_command_pressed_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(send_command_pressed_background_color)
        send_command_pressed_text_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(send_command_pressed_text_color)
        refresh_list_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(refresh_list_background_color)
        refresh_list_text_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(refresh_list_text_color)
        refresh_list_pressed_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(refresh_list_pressed_background_color)
        refresh_list_pressed_text_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(refresh_list_pressed_text_color)
        create_new_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(create_new_background_color)
        create_new_text_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(create_new_text_color)
        create_new_pressed_background_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(create_new_pressed_background_color)
        create_new_pressed_text_color = q.recv(1024).decode("utf-8").replace("\n", "")
        print(create_new_pressed_text_color)

        start_text = q.recv(1024).decode("utf-8").replace("\n", "")
        print(start_text)
        not_found = q.recv(1024).decode("utf-8").replace("\n", "")
        print(not_found)
        got_admin = q.recv(1024).decode("utf-8").replace("\n", "")
        print(got_admin)
        maintenance = q.recv(1024).decode("utf-8").replace("\n", "")
        print(maintenance)
        not_on_whitelist = q.recv(1024).decode("utf-8").replace("\n", "")
        print(not_on_whitelist)
        help_ = q.recv(1024).decode("utf-8").replace("\n", "")
        print(help_)
        added_someone_to_admins = q.recv(1024).decode("utf-8").replace("\n", "")
        print(added_someone_to_admins)
        failed_to_add_someone_to_admins = q.recv(1024).decode("utf-8").replace("\n", "")
        print(failed_to_add_someone_to_admins)
        added_someone_to_whitelist = q.recv(1024).decode("utf-8").replace("\n", "")
        print(added_someone_to_whitelist)
        failed_to_add_someone_to_whitelist = q.recv(1024).decode("utf-8").replace("\n", "")
        print(failed_to_add_someone_to_whitelist)
        command_disabled = q.recv(1024).decode("utf-8").replace("\n", "")
        print(command_disabled)
        rules = q.recv(1024).decode("utf-8").replace("\n", "")
        print(f"Rules: {rules}")
        time.sleep(0.1)
        update_checker()
        connect = True
        print(f"Connected to server : {server_name}")
        os.system(clear_command)


    # except:
        # tk.messagebox.showinfo("Failed to connect to the server!",
                               # 'Please consult with the server owner!')
        # exit()

FORMAT = 'utf-8'
send_username(username)

response = q.recv(1024)
response = response.decode('utf-8')

if "let" == str(response):
    pass
else:
    tk.messagebox.showinfo("Whitelist",
                           f'{not_on_whitelist}')
    exit()


def create_():
    websitename = askstring('Create Article', "Article's name :")
    q.send(bytes(f'create{websitename}', 'utf-8'))
    while True:
        website_text = askstring('Create Article', 'Article text : ')
        if website_text is None:
            q.send(bytes(f'//quit', 'utf-8'))
            break
        else:
            q.send(bytes(str(website_text), 'utf-8'))


def go(command):
    search_website = command.replace('go ', '')
    search_website = search_website.replace('\n', ' ')
    q.send(bytes(f'need{search_website}', 'utf-8'))
    time.sleep(0.2)
    length = q.recv(1024).decode(FORMAT)
    data = length
    text_box.insert(tk.END, data)
    update_gui(data, 'del')
    list_websites()


def get_command():
    command = input_area.get('1.0', 'end')
    command = command.replace('\n', '')
    if 'go ' in command:
        go(command)
    elif command == 'help':
        update_gui(help_, 'del')
        list_websites()
    elif 'create' in command:
        create_()
        list_websites()
    elif command == 'getaddr':
        getaddr()
        list_websites()
    elif "addAdmin " in command:
        addAdmin(command.replace("addAdmin ", ""))
        list_websites()
    elif "whitelist " in command:
        whitelist(command.replace("whitelist ", ""))
        list_websites()


def addAdmin(user):
    q.send(bytes('addAdmin', 'utf-8'))
    q.send(bytes(f'{user}', 'utf-8'))
    message = q.recv(1024).decode("utf-8")
    if message == "1":
        update_gui(added_someone_to_admins, "")
    else:
        update_gui(failed_to_add_someone_to_admins, '')


def whitelist(user):
    q.send(bytes('whitelist', 'utf-8'))
    q.send(bytes(f'{user}', 'utf-8'))
    message = q.recv(1024).decode("utf-8")
    if message == "1":
        update_gui(added_someone_to_whitelist, "")
    else:
        update_gui(failed_to_add_someone_to_whitelist, '')


def getaddr():
    update_gui(f'Your IP address: {ip}', 'del')


def list_websites():
    q.send(bytes('list', 'utf-8'))
    time.sleep(0.2)
    data = q.recv(1024).decode('utf-8')
    monthchoosen['values'] = str(data).replace("[", "").replace(",", "").replace("'", "").replace("]", "")
    monthchoosen.pack()

def start_process():
    try:
        update_gui(start_text, "del")
        t = threading.Thread(target=check_selected, args=("DefaultPage",))
        t.start()
    except:
        t = threading.Thread(target=check_selected, args=("start",))
        t.start()

def check_selected(data):
    while True:
        time.sleep(0.1)
        data2 = monthchoosen.get()
        if data != data2 and data2 != "":
            go(str(data2).replace("[", "").replace(",", "").replace("'", "").replace("]", ""))
            t = threading.Thread(target=check_selected, args=(data2,))
            t.start()
            break


root = tk.Tk()
root.title(server_name_to_show)
root.configure(bg=background)
root.attributes('-alpha', float(opacity))
root.geometry(f"1280x1020")


def on_close():
    q.send(bytes(f'###close', 'utf-8'))
    q.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)

label = tk.Label(root, text=label, font=('Arial', int(label_size)))
label.pack(pady=50)
label.configure(bg=label_background_color, fg=label_color, highlightcolor='orange')

buttonframe = tk.Frame(root, bg=buttonframe_bg)
buttonframe.columnconfigure(10, weight=1)

input_area = tk.Text(buttonframe, height=1, font=('Arial', 10), bg=send_command_background_color, fg=send_command_text_color, borderwidth=1)
input_area.config(highlightthickness=1, highlightbackground=send_command_pressed_background_color, highlightcolor=send_command_text_color)
input_area.grid(row=0, column=0, sticky=tk.W + tk.E)

button = tk.Button(buttonframe, text='Send command', font=('Arial', 10), command=get_command, bg=send_command_background_color, fg=send_command_text_color,
                   activebackground=send_command_pressed_background_color, activeforeground=send_command_pressed_text_color, borderwidth=0)
button.config(highlightthickness=12, highlightbackground=send_command_pressed_background_color, highlightcolor=send_command_pressed_text_color)
button.grid(row=0, column=1, sticky=tk.W + tk.E)

list_button = tk.Button(buttonframe, text="Refresh list", font=('Arial', 10), command=list_websites, bg=refresh_list_background_color,
                        fg=refresh_list_text_color, activebackground=refresh_list_pressed_background_color, activeforeground=refresh_list_pressed_text_color, borderwidth=0)
list_button.grid(row=0, column=2, sticky=tk.W + tk.E)
list_button.config(highlightthickness=12, highlightbackground=refresh_list_pressed_background_color, highlightcolor=refresh_list_pressed_text_color)

create_button = tk.Button(buttonframe, text="New Article", font=('Arial', 10), command=create_, bg=create_new_background_color,
                        fg=create_new_text_color, activebackground=create_new_pressed_background_color, activeforeground=create_new_pressed_text_color, borderwidth=0)
create_button.grid(row=0, column=3, sticky=tk.W + tk.E)
create_button.config(highlightthickness=12, highlightbackground=create_new_pressed_background_color, highlightcolor=create_new_pressed_text_color)

buttonframe.pack()
buttonframe.config()

n = tk.StringVar()
monthchoosen = ttk.Combobox(root, width=27,
                            textvariable=n)

monthchoosen.pack()


text_box = tk.scrolledtext.ScrolledText(root, font=('Arial', 20), bg=result_text_box_color, borderwidth=1, width=70)
text_box.pack()
text_box.config(state='disabled', bg=result_text_box_color, fg=send_command_text_color, highlightthickness=float(result_text_box_edge_size), highlightbackground=result_text_box_color,
                highlightcolor=result_text_box_edge_color_selected)

buttonframe.pack(pady=20)

t = threading.Thread(target=list_websites)
t.start()

t = threading.Thread(target=start_process)
t.start()

root.mainloop()
