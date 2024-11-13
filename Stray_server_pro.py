import socket
import threading
import time
import requests as req
import datetime

print("Welcome to Stray Host!")

try:
    with open(f'settings.settings', 'r') as a:
        print("Reading settings.settings file.")
        a.readline()
        a.readline()
        a.readline()
        label = a.readline().replace("    label : ", "")
        server_name = a.readline().replace("    server-name : ", "")
        server_name_to_show = a.readline().replace("    server-name-to-show : ", "")
        a.readline()
        a.readline()
        connect_to_main_server = a.readline().replace("    connect-to-main-server : ", "")
        a.readline()
        a.readline()
        buttonframe_bg = a.readline().replace("    buttonframe-background : ", "")
        opacity = a.readline().replace("    opacity : ", "")
        label_color = a.readline().replace("    label-color : ", "")
        label_background_color = a.readline().replace("    label-background-color : ", "")
        label_size = a.readline().replace("    label-size : ", "")
        background = a.readline().replace("    background : ", "")
        font_color = a.readline().replace("    font-color : ", "")
        font_background_color = a.readline().replace("    font-background-color : ", "")
        result_text_box_color = a.readline().replace("    result-text-box-color : ", "")
        result_text_box_edge_color = a.readline().replace("    result-text-box-edge-color : ", "")
        result_text_box_edge_color_selected = a.readline().replace("    result-text-box-edge-color-selected : ", "")
        result_text_box_edge_size = a.readline().replace("    result-text-box-edge-size : ", "")
        searchbar_color = a.readline().replace("    searchbar-color : ", "")
        searchbar_edge_color = a.readline().replace("    searchbar-edge-color : ", "")
        searchbar_edge_color_selected = a.readline().replace("    searchbar-edge-color-selected : ", "")
        searchbar_edge_size = a.readline().replace("    searchbar-edge-size : ", "")
        send_command_background_color = a.readline().replace("    send-command-background-color : ", "")
        send_command_text_color = a.readline().replace("    send-command-text-color : ", "")
        send_command_pressed_background_color = a.readline().replace("    send-command-pressed-background-color : ", "")
        send_command_pressed_text_color = a.readline().replace("    send-command-pressed-text-color : ", "")
        refresh_list_background_color = a.readline().replace("    refresh-list-background-color : ", "")
        refresh_list_text_color = a.readline().replace("    refresh-list-text-color : ", "")
        refresh_list_pressed_background_color = a.readline().replace("    refresh-list-pressed-background-color : ", "")
        refresh_list_pressed_text_color = a.readline().replace("    refresh-list-pressed-text-color : ", "")
        create_new_background_color = a.readline().replace("    create-new-background-color : ", "")
        create_new_text_color = a.readline().replace("    create-new-text-color : ", "")
        create_new_pressed_background_color = a.readline().replace("    create-new-pressed-background-color : ", "")
        create_new_pressed_text_color = a.readline().replace("    create-new-pressed-text-color : ", "")
        a.readline()
        a.readline()
        whitelist = a.readline().replace("    whitelist : ", "")
        a.readline()
        a.readline()
        start_text = a.readline().replace("    start-text : ", "")
        not_found = a.readline().replace("    not-found : ", "")
        got_admin = a.readline().replace("    got-admin : ", "")
        maintenance = a.readline().replace("    maintenance : ", "")
        not_on_whitelist = a.readline().replace("    not-on-whitelist : ", "")
        help = a.readline().replace("    help : ", "")
        added_someone_to_admins = a.readline().replace("    added-someone-to-admins : ", "")
        failed_to_add_someone_to_admins = a.readline().replace("    failed_to_add_someone_to_admins : ", "")
        added_someone_to_whitelist = a.readline().replace("    added-someone-to-whitelist : ", "")
        failed_to_add_someone_to_whitelist = a.readline().replace("    failed_to_add_someone_to_whitelist : ", "")
        command_disabled = a.readline().replace("    command-disabled : ", "")
        a.readline()
        a.readline()
        rules = a.readline().replace("    rules : ", "")
        create_new_articles = a.readline().replace("    create-new-articles : ", "")
        only_admins_create_new_articles = a.readline().replace("    only-admins-create-new-articles : ", "")
        a.readline()
        a.readline()
        private = a.readline().replace("    private : ", "")
        premium = a.readline().replace("    premium : ", "")
        price_if_premium = a.readline().replace("    price_if_premium : ", "")
        print("DONE!")
except:
    print("ERROR reading settings.settings file!")


if False: # nem csinálja meg
    try:
        print("Started indexing...")

        connect = False

        if True:
            if True:

                q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                q.connect(('192.168.1.10', 5667))
                q.settimeout(None)

                q.send("1".encode("utf-8"))
                time.sleep(0.1)
                server_name_to_show_index = server_name_to_show.replace("\n", "")
                q.send(server_name_to_show.encode("utf-8"))
                q.close()
                print("Indexed server to the Stray Network!")
                connect = True
    except:
        print("Error occurred!")


admins = [""]


def get_whitelist():

    with open(f'whitelist.encrypted', 'r') as a:

        whitelist = a.read()
        print("Whitelist read!")
        return whitelist


def log(text):
    pass


print(datetime.datetime.now())

#select * from connection

frequency = 300  # Set Frequency To 2500 Hertz
duration = 150  # Set Duration To 1000 ms == 1 second

indb = False

# if database != '':
    # try:
        # db = mysql.connector.connect(
            # host=database,
            # user='root',
            # password='Mokusors00',
            # database='arcticweb'
        # )
        # indb = True
        # mycursor = db.cursor()
# except:
        # print("Hiba az adatbázishoz való csatlakozáskor!")
        # log("Hiba az adatbázishoz való csatlakozáskor!")
# else:
    # print("Adatbázishoz való csatlakozás kihagyása!")
    # log("Adatbázishoz való csatlakozás kihagyása!")


with open('version', 'r') as k:
    VERSION = k.read()
    print(f"Version : {VERSION}")

url: str = 'https://checkip.amazonaws.com'
req = req.get(url)
ip: str = req.text


HEADER = 64
FORMAT = 'utf-8'

print("Starting...")


def handle_client(clientsocket, address):
    wait_time = 0.01
    print("[CLIENT] Sending settings...")
    time.sleep(wait_time)
    clientsocket.send(label.encode('utf-8'))
    time.sleep(wait_time)
    clientsocket.send(server_name.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(server_name_to_show.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(buttonframe_bg.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(opacity.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(label_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(label_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(label_size.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(background.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(font_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(font_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(result_text_box_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(result_text_box_edge_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(result_text_box_edge_color_selected.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(result_text_box_edge_size.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(searchbar_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(searchbar_edge_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(searchbar_edge_color_selected.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(searchbar_edge_size.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(send_command_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(send_command_text_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(send_command_pressed_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(send_command_pressed_text_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(refresh_list_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(refresh_list_text_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(refresh_list_pressed_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(refresh_list_pressed_text_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(create_new_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(create_new_text_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(create_new_pressed_background_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(create_new_pressed_text_color.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(start_text.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(not_found.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(got_admin.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(maintenance.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(not_on_whitelist.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(help.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(added_someone_to_admins.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(failed_to_add_someone_to_admins.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(added_someone_to_whitelist.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(failed_to_add_someone_to_whitelist.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(command_disabled.encode("utf-8"))
    time.sleep(wait_time)
    clientsocket.send(rules.encode("utf-8"))
    time.sleep(wait_time)
    print("Done!")

    clientsocket.send(bytes(str(VERSION), 'utf-8'))
    print(f'[UPDATER] {VERSION} code sent! | {address} ')
    admin = False
    while True:
        request = clientsocket.recv(1024)
        request = request.decode('utf-8')
        if 'usr' in request:
            addressdata = str(address)
            addressdata = addressdata.replace('(', '')
            addressdata = addressdata.replace(')', '')
            addressdata = addressdata.replace("'", "")
            nickname = request.replace('usr', '')
            print(f'[CLIENT] {addressdata} = {nickname}')
            if nickname in admins:
                admin = True
                clientsocket.send(bytes(str("1"), 'utf-8'))
            else:
                clientsocket.send(bytes(str("0"), 'utf-8'))
            whitelist = get_whitelist()
            whitelist = str(whitelist)
            if nickname in whitelist:
                clientsocket.send(bytes(str("let"), 'utf-8'))
                print(f"[WHITELIST] User let in : {nickname}")
            else:
                if whitelist == "open":
                    clientsocket.send(bytes(str("let"), 'utf-8'))
                else:
                    print(f"[WHITELIST] User was not let in : {nickname}")
                    clientsocket.send(bytes(str("cl"), 'utf-8'))
                    break
        if request != '':
            print(f'[CLIENT] Got : {request} | {nickname} ')
        if 'need' in request:
            request = request.replace('need', '')
            try:
                with open(f'sites/{request}', 'r') as a:
                    website_text = a.readlines()
                    print(f'[OPENING] {request} Opened! | {nickname}')
                    data = a.readlines()
                    data = len(data)
                    clientsocket.send(bytes(data))
                    for i in range(len(website_text)):
                        request = website_text[i]
                        print_request = request.replace('\n', '')
                        clientsocket.send(bytes(str(request), 'utf-8'))
            except:
                message = not_found
                clientsocket.send(bytes(str(message).replace("\n", ""), 'utf-8'))
        if 'create' in request:
            request = request.replace('create', '')
            with open('sites/websites.list', 'a') as a:
                a.write(request)
                print(f'[CREATING] {request} added to list | {nickname}')
                a.write("\n")
                a.close()
            with open(f"sites/{request}", 'w') as f:
                print(f'[CREATING] {request} created! | {nickname}')
                while True:
                    website_text = clientsocket.recv(1024).decode(FORMAT)
                    f.write(website_text)
                    print(f'[CREATING] Writing data : {website_text} | {nickname}')
                    f.write('\n')
                    if website_text == '//quit':
                        print(f'[CREATING] Closing : {request} | {nickname}')
                        f.write(f'Created by : {nickname}')
                        break
        if 'list' in request:
            with open('sites/websites.list', 'r') as a:
                website_list = a.readlines()
                data = a.readlines()
                data = len(data)
                clientsocket.send(bytes(data))
                clientsocket.send(bytes(str(website_list).replace("\n", ""), 'utf-8'))
            print(f"[LIST] Sent list! | {nickname}")
        if '###close' in request:
            print(f'[Disconnecting] Disconnecting | {nickname} ')
            clientsocket.close()
            break
        if "addAdmin" in request:
            adminName = clientsocket.recv(1024)
            if admin:
                admins.append(adminName)
                print(f"[ADMINS] {adminName} added to admins!")
                clientsocket.send(bytes(str("1"), 'utf-8'))
            else:
                clientsocket.send(bytes(str("0"), 'utf-8'))
                print(f"[ADMINS] {nickname} tried adding {adminName} to admins!")
        if "whitelist" in request:
            adminName = clientsocket.recv(1024)
            if admin:
                whitelist = f"{whitelist}{adminName}"
                print(f"[WHITELIST] {adminName} added to whitelist!")
                clientsocket.send(bytes(str("1"), 'utf-8'))
            else:
                clientsocket.send(bytes(str("0"), 'utf-8'))
                print(f"[WHITELIST] {nickname} tried adding {adminName} to whitelist!")
        request = None


def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(None)
    print('[STARTING] Binding sockets...')

    s.bind(('192.168.1.10', 5666))  # socket.gethostname()
    s.listen(10)
    print('[STARTING] Started!')
    print('[LISTENING] Listening for maximum 10 users...')
    while True:
        clientsocket, address = s.accept()
        print(f'[CLIENT] Got connection : {address}')

        t = threading.Thread(target=handle_client, args=(clientsocket, address))
        t.start()


print('[STARTING] Starting...')
listen()

