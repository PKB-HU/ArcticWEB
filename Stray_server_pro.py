import socket
import threading
import time
import requests as req
import datetime
import json

print("Welcome to Stray Host!")

try:
    with open(f'settings.json', 'r') as a:
        print("Reading settings.settings file.")
        settings_dict = json.load(a)

        # Names
        label = settings_dict["names"]["label"]
        server_name = settings_dict["names"]["server_name"]
        server_name_to_show = settings_dict["names"]["server_name_to_show"]

        # Connection
        connect_to_main_server = settings_dict["connect_to_main_server"]

        # Colors
        buttonframe_bg = settings_dict["colors"]["buttonframe_background"]
        opacity = settings_dict["colors"]["opacity"]
        label_color = settings_dict["colors"]["label_color"]
        label_background_color = settings_dict["colors"]["label_background_color"]
        label_size = settings_dict["colors"]["label_size"]
        background = settings_dict["colors"]["background"]
        font_color = settings_dict["colors"]["font_color"]
        font_background_color = settings_dict["colors"]["font_background_color"]
        result_text_box_color = settings_dict["colors"]["result_text_box_color"]
        result_text_box_edge_color = settings_dict["colors"]["result_text_box_edge_color"]
        result_text_box_edge_color_selected = settings_dict["colors"]["result_text_box_edge_color_selected"]
        result_text_box_edge_size = settings_dict["colors"]["result_text_box_edge_size"]
        searchbar_color = settings_dict["colors"]["searchbar_color"]
        searchbar_edge_color = settings_dict["colors"]["searchbar_edge_color"]
        searchbar_edge_color_selected = settings_dict["colors"]["searchbar_edge_color_selected"]
        searchbar_edge_size = settings_dict["colors"]["searchbar_edge_size"]
        send_command_background_color = settings_dict["colors"]["send_command_background_color"]
        send_command_text_color = settings_dict["colors"]["send_command_text_color"]
        send_command_pressed_background_color = settings_dict["colors"]["send_command_pressed_background_color"]
        send_command_pressed_text_color = settings_dict["colors"]["send_command_pressed_text_color"]
        refresh_list_background_color = settings_dict["colors"]["refresh_list_background_color"]
        refresh_list_text_color = settings_dict["colors"]["refresh_list_text_color"]
        refresh_list_pressed_background_color = settings_dict["colors"]["refresh_list_pressed_background_color"]
        refresh_list_pressed_text_color = settings_dict["colors"]["refresh_list_pressed_text_color"]
        create_new_background_color = settings_dict["colors"]["create_new_background_color"]
        create_new_text_color = settings_dict["colors"]["create_new_text_color"]
        create_new_pressed_background_color = settings_dict["colors"]["create_new_pressed_background_color"]
        create_new_pressed_text_color = settings_dict["colors"]["create_new_pressed_text_color"]

        # Whitelist
        whitelist = settings_dict["whitelist"]

        # Messages
        start_text = settings_dict["messages"]["start_text"]
        not_found = settings_dict["messages"]["not_found"]
        got_admin = settings_dict["messages"]["got_admin"]
        maintenance = settings_dict["messages"]["maintenance"]
        not_on_whitelist = settings_dict["messages"]["not_on_whitelist"]
        help = settings_dict["messages"]["help"]
        added_someone_to_admins = settings_dict["messages"]["added_someone_to_admins"]
        failed_to_add_someone_to_admins = settings_dict["messages"]["failed_to_add_someone_to_admins"]
        added_someone_to_whitelist = settings_dict["messages"]["added_someone_to_whitelist"]
        failed_to_add_someone_to_whitelist = settings_dict["messages"]["failed_to_add_someone_to_whitelist"]
        command_disabled = settings_dict["messages"]["command_disabled"]

        # Rules
        rules = settings_dict["rules"]["rules"]
        create_new_articles = settings_dict["rules"]["create_new_articles"]
        only_admins_create_new_articles = settings_dict["rules"]["only_admins_create_new_articles"]

        # Misc
        private = settings_dict["other"]["private"]
        premium = settings_dict["other"]["premium"]
        price_if_premium = settings_dict["other"]["price_if_premium"]
        print("DONE!")
except Exception as e:
    print(f"ERROR reading settings.settings file! Error: {e.with_traceback(None)}")


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
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # SO_REUSEADDR allows the socket to be quickly reused after it has been closed.
    print('[STARTING] Binding sockets...')

    s.bind(('127.0.0.1', 5666))  # socket.gethostname()
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

