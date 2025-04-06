# Imports
import requests
import re
import time
import threading
import sys
from bs4 import BeautifulSoup, NavigableString, Tag
from datetime import datetime

# Preloads
session = requests.Session()

# Constants
base = "chat.jonazwetsloot.nl"
url = f"https://{base}"
api_url = f"{url}/api/v1"
login_url = f"{url}/login"
actionlogin_url = f"{url}/actionlogin"
timeline_url = f"{url}/timeline"
profile_url = f"{url}/users"
inbox_url = f"{url}/inbox"
list_dms_url = f"{url}/messages"
send_message_url = f"{api_url}/message"
dm_url = f"{api_url}/direct-message"
group_url = f"{api_url}/group-message"
like_url = f"{api_url}/like"
follow_url = f"{api_url}/contact.php"

version = "Selfbot V1.0.0"

headers = { 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,application/json,text/plain,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Host": base,
    "Origin": url,
    "Referer": login_url,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Content-Type": "application/x-www-form-urlencoded",
}

# Variables
message_cache = {}
dm_cache = {}
dm_cache_user = {}
saved_key = None
first_run = True
show_http = False
user = None

# Universal functions:
def check_type(value, class_, argnumber, argname, funcname):
    if value is None:
        args = ", ".join("..." for _ in range(argnumber - 1))
        args = f"{args}, {argname}:{class_.__name__}" if args else f"{argname}:{class_.__name__}"
        show_message(f"Expected arg{argnumber} in {funcname}({args}) (was None)", "Error")
        return False

    if type(value) != class_:
        args = ", ".join("..." for _ in range(argnumber - 1))
        args = f"{args}, {argname}:{class_.__name__}" if args else f"{argname}:{class_.__name__}"
        show_message(f"Expected arg{argnumber} to be class {class_.__name__} instead of {value.__class__.__name__} in {funcname}({args})", "Error")
        return False
    
    return True

def show_message(message:str=None, mtype:str="Standard"):
    if not check_type(message, str, 1, "message", "show_message"): return
    
    if mtype == "Standard":
        print(f"[{version}] {message}")
    elif mtype == "Error":
        print(f"[{version}] Error: {message}")
    elif mtype == "Http" and show_http:
        print(f"[{version}] Http: {message}")
    else:
        show_message("Ignored show_message due to invalid mtype")

allowed = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
def username_to_id(username:str=None):
    if not check_type(username, str, 1, "username", "ProfileService.username_to_id"): return
    return ''.join([char if char in allowed or char == ' ' else '' for char in username]).replace(' ', '-')

def http_request(method:str=None, url:str=None, data:any=None):
    if not check_type(method, str, 1, "method", "http_request"): return
    if not check_type(url, str, 2, "url", "http_request"): return

    if method.lower() not in ["get", "post", "put", "delete", "patch", "head", "options"]:
        show_message(f"Invalid HTTP method for http_request: {method}", "Error")
        return
        
    response
    if data:
        response = session[method.lower()](url, headers=headers, data=data)
    else:
        response = session[method.lower()](url, headers=headers)
    return response

def get_key():
    global saved_key
    if saved_key:
        return saved_key
    
    response = session.get(timeline_url, headers=headers)
    match = re.search(r'<input[^>]+name="key"[^>]+value="([^\"]+)"', response.text)
    saved_key = match.group(1) if match else None
    if saved_key is None:
        show_message("Failed to retrieve key.", "Error")
    return saved_key

def extract_messages(html:str=None):
    if not check_type(html, str, 1, "html", "extract_messages"): return

    def parse_message(message_container:Tag=None, parent_id:str=None):
        if not check_type(message_container, Tag, 1, "message_container", "parse_message"): return
        if not parent_id is None:
            if not check_type(parent_id, str, 2, "parent_id", "parse_message"): return

        message_div = None
        if parent_id:
            message_div = message_container
        else:
            message_div = message_container.find('div', class_='message')
        
        if not message_div:
            show_message("Message div doesn't exist!", "Error")
            return None

        bar_div = message_div.find('div', class_='bar')
        if not bar_div:
            show_message("Bar div doesn't exist!", "Error")
            return None

        time_element = bar_div.find('p', class_='time')
        content_element = message_div.find('div', class_='content')
        user_element = bar_div.find('a', class_='username')
        message_id_element = bar_div.find('button', class_='submit inverted message-menu-share-button')

        message_id = message_id_element['data-id'] if message_id_element else "0"
        time_text = time_element.text.strip() if time_element else ""
        content_text = get_text_from_message(content_element)
        markdown_text = get_text_from_message(content_element, True)
        user_text = user_element.text.strip() if user_element else "Unknown"

        reactions_container = message_container.find('div', class_='reactions')
        reactions = []
        if reactions_container:
            reactions = [parse_message(reaction_div, message_id) for reaction_div in reactions_container.find_all('div', class_='reaction') if reaction_div]

        return PublicMessage(format_time(time_text), content_text, markdown_text, user_text, message_id, reactions, parent_id)

    soup = BeautifulSoup(html, 'html.parser')
    messages = [parse_message(message_container) for message_container in soup.find_all('div', class_='message-container')]

    return [msg for msg in messages if msg is not None]

def get_text_from_message(message_div:Tag=None, markdown:bool=False):
    if not check_type(message_div, Tag, 1, "message_div", "get_text_from_message"): return ""
    if not check_type(markdown, bool, 2, "markdown", "get_text_from_message"): return ""

    def handle_node(node:NavigableString|Tag=None):
        if isinstance(node, NavigableString):
            return str(node)

        if not check_type(node, Tag, 1, "node", "handle_node"): return ""

        name = node.name
        classes = node.get("class", [])

        if name == "p":
            raw = node.get_text(strip=True)
            if raw.startswith("### "):
                return f"### {raw[4:]}\n"
            if raw.startswith("## "):
                return f"## {raw[3:]}\n"
            if raw.startswith("# "):
                return f"# {raw[2:]}\n"
            return handle_children(node) + "\n"
        if name == "br":
            return "\n"
        if name == "a" and "mention" in classes:
            return node.get_text()
        if name == "span":
            if "inline-code" in classes:
                content = node.get_text()
                return f"`{content}`" if markdown else content
            if "spoiler" in classes or node.get("class") == [""]:
                content = node.get_text()
                return f"||{content}||" if markdown else content
        if name == "strong":
            only_child = list(node.children)
            if len(only_child) == 1 and isinstance(only_child[0], Tag) and only_child[0].name == "em":
                content = only_child[0].get_text()
                return f"***{content}***" if markdown else content
            else:
                content = handle_children(node)
                return f"**{content}**" if markdown else content
        if name == "em":
            content = handle_children(node)
            return f"*{content}*" if markdown else content
        if name == "ins":
            content = handle_children(node)
            return f"__{content}__" if markdown else content
        if name == "del":
            content = handle_children(node)
            return f"~~{content}~~" if markdown else content
        if name == "blockquote":
            content = handle_children(node)
            return f"> {content.strip()}\n" if markdown else content
        if name == "h1":
            content = handle_children(node)
            return f"# {content.strip()}\n" if markdown else f"{content}\n"
        if name == "h2":
            content = handle_children(node)
            return f"## {content.strip()}\n" if markdown else f"{content}\n"
        if name == "h3":
            content = handle_children(node)
            return f"### {content.strip()}\n" if markdown else f"{content}\n"
        if name == "sub":
            content = handle_children(node)
            return f"-# {content.strip()}\n" if markdown else content
        if name == "div" and "code" in classes:
            content = node.get_text().strip("\n")
            lines = content.splitlines()
            if len(lines) > 1:
                lang = lines[0].strip()
                code = "\n".join(lines[1:])
                return f"```{lang}\n{code}\n```" if markdown else content
            return f"```\n{content}\n```" if markdown else content
        if name == "img":
            return node.get("alt", "")

        return handle_children(node)

    def handle_children(tag):
        return "".join(handle_node(child) for child in tag.children)

    result = handle_children(message_div)
    return result.strip()

# MessageService functions:
def reply(message_id:str=None, message:str=None):
    if not check_type(message_id, str, 1, "message_id", "MessageService.reply"): return
    if not check_type(message, str, 2, "message", "MessageService.reply"): return
    
    key = get_key()
    if not key:
        return

    data = {
        "message": message,
        "id": message_id,
        "name": user,
        "key": key
    }
    response = session.post(send_message_url, data=data, headers=headers)
    show_message(f"Response Status Code (Send Reply): {response.status_code}", "Http")

def like(message_id:str=None, value:bool=True):
    if not check_type(message_id, str, 1, "message_id", "MessageService.like"): return
    if not check_type(value, bool, 2, "value", "MessageService.like"): return
    
    key = get_key()
    if not key:
        return
    
    data = {
        "id": message_id,
        "like": str(value).lower(),
        "name": user,
        "key": key
    }
    response = session.post(like_url, data=data, headers=headers)
    show_message(f"Response Status Code (Like Message): {response.status_code}", "Http")

def edit(message_id:str=None, message:str=None):
    if not check_type(message_id, str, 1, "message_id", "MessageService.edit"): return
    if not check_type(message, str, 2, "message", "MessageService.edit"): return
    
    key = get_key()
    if not key:
        return

    data = {
        "message": message,
        "name": user,
        "key": key,
        "id": message_id
    }
    response = session.put(send_message_url, data=data, headers=headers)
    show_message(f"Response Status Code (Edit Message): {response.status_code}", "Http")

def delete(message_id:str=None):
    if not check_type(message_id, str, 1, "message_id", "MessageService.delete"): return
    
    key = get_key()
    if not key:
        return

    data = {
        "name": user,
        "key": key,
        "id": message_id
    }
    response = session.delete(send_message_url, data=data, headers=headers)
    show_message(f"Response Status Code (Delete Message): {response.status_code}", "Http")

def direct_message(username:str=None, message:str=None):
    if not check_type(username, str, 1, "username", "direct_message"): return
    if not check_type(message, str, 2, "message", "direct_message"): return
    
    key = get_key()
    if not key:
        return
    
    data = {
        "attachments": "",
        "name": user,
        "key": key,
        "user": username,
        "message": message
    }
    response = session.post(dm_url, data=data, headers=headers)
    show_message(f"Response Status Code (Direct Message): {response.status_code}", "Http")

    
def group_message(group_id:str=None, message:str=None):
    if not check_type(group_id, str, 1, "group_id", "group_message"): return
    if not check_type(message, str, 2, "message", "group_message"): return
    
    key = get_key()
    if not key:
        return
    
    data = {
        "attachments": "",
        "name": user,
        "key": key,
        "id": group_id,
        "message": message
    }
    response = session.post(group_url, data=data, headers=headers)
    show_message(f"Response Status Code (Group Message): {response.status_code}", "Http")

# ProfileService functions:
def follow(username:str=None, value:bool=True):
    if not check_type(username, str, 1, "username", "ProfileService.follow"): return
    if not check_type(value, bool, 2, "value", "ProfileService.follow"): return
    
    key = get_key()
    if not key:
        return
    
    method = value and "POST" or "DELETE"
    data = {
        "user": username,
        "method": method,
        "name": user,
        "key": key
    }
    response = session.post(follow_url, data=data, headers=headers)
    show_message(f"Response Status Code (Follow User): {response.status_code}", "Http")

# Time functions:
def format_time(timestr:str):
    if not check_type(timestr, str, 1, "timestr", "format_time"): return

    match = re.match(r"(\d+)\s*(second|minute)s?", timestr.strip().lower())
    
    if not match:
        return 0
    
    number = int(match.group(1))
    unit = match.group(2)
    
    if unit == "second":
        return time.time() - number
    elif unit == "minute":
        return time.time() - number * 60
    else:
        return 0
    
from datetime import datetime, timedelta

def format_real_time(timestr:str):
    if not check_type(timestr, str, 1, "timestr", "format_real_time"): return

    if timestr:
        try:
            time_obj = datetime.strptime(timestr, "%H:%M")
            now = datetime.now()
            
            target_time = now.replace(hour=time_obj.hour, minute=time_obj.minute, second=0, microsecond=0)
            
            if target_time < now:
                target_time = target_time + timedelta(days=1)

            time_diff = target_time - now
            return int(time_diff.total_seconds())
        except ValueError:
            show_message(f"Invalid DM time format: {timestr}", "Error")
            return 0
    else:
        return 0

    
def format_date(datestr:str):
    if not check_type(datestr, str, 1, "datestr", "format_data"): return

    if datestr == "Today":
        return datetime.today().strftime("%d/%m/%y")
    elif datestr == "Yesterday":
        return (datetime.today() - timedelta(days=1)).strftime("%d/%m/%y")
    else:
        return datestr

# Message classes
class PublicMessage:
    def __init__(self, time, text, markdowntext, sender, id, reactions, parent_id):
        self.time = float(time)     # 0 in old public messages
        self.text = text
        self.markdowntext = markdowntext
        self.sender = sender
        self.id = str(id)

        self.reactions = reactions
        self.parent_id = parent_id

    def like(self, value:bool=True):
        like(self.id, value)

    def reply(self, message:str=None):
        reply(self.id, message)

    def edit(self, message:str=None):
        edit(self.id, message)

    def delete(self):
        delete(self.id)

    def bind_to_reply(self, func=None):
        BotService.ConnectionService.bind_to_message_reply(self.id, func)

class DMMessage:
    def __init__(self, time, text, markdowntext, sender, id, groupname, groupid):
        self.time = float(time)     # 0 in any-user dms
        self.text = text
        self.markdowntext = markdowntext
        self.sender = sender
        self.id = str(id)           # "0" in any-user dms
        self.groupname = groupname  # None in normal dms
        self.groupid = groupid      # None in normal dms

    def reply(self, message:str=None):
        if self.groupid:
            group_message(self.groupid, message)
        else:
            direct_message(self.sender, message)

class Profile:
    def __init__(self, username, verified, following, followers, likes, description, markdowndescription, socials, join_date, trophies):
        self.username = username
        self.verified = verified
        self.following = following
        self.followers = followers
        self.likes = likes
        self.description = description
        self.markdowndescription = markdowndescription
        self.socials = socials
        self.join_date = join_date
        self.trophies = trophies

    def follow(self, value:bool=True):
        follow(self.username, value)

# Core services
class ConnectionService:
    # Core:
    def __init__(self):
        self.public_functions = []
        self.reply_functions = {}
        self.is_checking_public = False

        self.anydm_functions = []
        self.userdm_functions = {}
        self.is_checking_dms = False

    # Core public:
    def _run_bound_functions(self, message:PublicMessage=None):
        if not check_type(message, PublicMessage, 1, "message", "ConnectionService._run_bound_functions"): return

        if first_run and message.sender == user:
            return
            
        for func in self.public_functions:
            threading.Thread(target=func, args=(message,), daemon=False).start()

    def _run_bound_functions_to_reply(self, message:PublicMessage=None, parent_id:str=None):
        if not check_type(message, PublicMessage, 1, "message", "ConnectionService._run_bound_functions_to_reply"): return
        if not check_type(parent_id, str, 2, "parent_id", "ConnectionService._run_bound_functions_to_reply"): return

        if first_run and message.sender == user:
            return

        if self.reply_functions.get(parent_id):
            for func in self.reply_functions[parent_id]:
                threading.Thread(target=func, args=(message,), daemon=False).start()

    def start_checking_public(self):
        if not self.is_checking_public:
            self.is_checking_public = True
            threading.Thread(target=self._check_periodically_public, daemon=False).start()

    def _check_periodically_public(self):
        global first_run
        while self.is_checking_public:
            try:
                show_message("Checking public...")
                response = requests.get(timeline_url, headers=headers)
                if response.status_code == 200:
                    messages = extract_messages(response.text)
                    def handle_message_list(messages, first):
                        for message in messages:
                            if message != None:
                                if time.time() - message.time < 600 and message.id not in message_cache:
                                    message_cache[message.id] = message.time
                                    if first:
                                        self._run_bound_functions(message)
                                    else:
                                        self._run_bound_functions_to_reply(message, message.parent_id)
                                handle_message_list(message.reactions, False)
                            else:
                                show_message("Message is None", "Error")
                    
                    handle_message_list(messages, True)

                self.check_public_cache()
                first_run = False
            except Exception as e:
                show_message(f"Error checking for new public posts: {e}", "Error")
            time.sleep(10)

    def stop_checking_public(self):
        self.is_checking_public = False

    def check_public_cache(self):
        to_delete = [id for id, unix in message_cache.items() if time.time() - unix > 600]
        for id in to_delete:
            del message_cache[id]

    # Core DM:
    def _run_dm_functions(self, message:PublicMessage=None):
        if not check_type(message, PublicMessage, 1, "message", "ConnectionService._run_dm_functions"): return

        for func in self.anydm_functions:
            threading.Thread(target=func, args=(message,), daemon=False).start()

    def _run_dm_functions_from_user(self, message):
        if not check_type(message, PublicMessage, 1, "message", "ConnectionService._run_dm_functions_from_user"): return

        for func in self.userdm_functions[message.sender]:
            threading.Thread(target=func, args=(message,), daemon=False).start()

    def start_checking_dms(self):
        if not self.is_checking_dms:
            self.is_checking_dms = True
            threading.Thread(target=self._check_periodically_dms, daemon=False).start()

    def _check_periodically_dms(self):
        while self.is_checking_dms:
            try:
                show_message("Checking DMs...")
                response = session.post(inbox_url, headers=headers)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    for user_contact in soup.find_all('a', class_='user-contact'):
                        name = user_contact.find('h3').text.strip()
                        groupname = None
                        newestmessage_element = user_contact.find('p')
                        b = newestmessage_element.find('b')
                        if b:
                            if name != b.text.strip():
                                groupname = name
                            name = b.text.strip()
                            b.decompose()
                        newestmessage = newestmessage_element.text.strip()
                        if newestmessage == "You have not yet sent any messages to this person.":
                            continue

                        if user_contact.find('img', class_='info'):
                            if not dm_cache.get(name):
                                dm_cache[name] = "[empty]"
                            continue

                        if not dm_cache.get(name):
                            dm_cache[name] = newestmessage
                        elif dm_cache[name] != newestmessage:
                            dm_cache[name] = newestmessage
                            self._run_dm_functions(DMMessage("0", newestmessage, newestmessage, name, "0", groupname))

                for username, functions in self.userdm_functions.items():
                    response = session.get(f'{list_dms_url}/{username}', headers=headers)
                    soup = BeautifulSoup(response.text, "html.parser")
                    offset = 0
                    for message_box in soup.find_all('div', class_='receiver'):
                        offset += 1
                        message_box = message_box.find('div', class_='dm')
                        id = message_box['data-id']
                        if dm_cache_user.get(id):
                            continue

                        time_literal = message_box.find('p', class_='time').text.strip()

                        time_day = ""
                        date_span = message_box.find_previous('span', class_='date')
                        if date_span:
                            time_day = date_span.text.strip()
                        else:
                            time_day = "Today"

                        datestr = f"{format_date(time_day)} {time_literal}"
                        unix = int(datetime.strptime(datestr, "%d/%m/%y %H:%M").timestamp()) + offset

                        if time.time() - unix < 600:
                            dm_cache_user[id] = unix

                            name = message_box.find('a', class_='username').text.strip()
                            text = get_text_from_message(message_box.find('div', class_='content'))
                            markdowntext = get_text_from_message(message_box.find('div', class_='content'), True)

                            message = DMMessage(unix, text, markdowntext, name, id, None)
                            for func in functions:
                                threading.Thread(target=func, args=(message,), daemon=False).start()

                    self.check_dm_cache()
            except Exception as e:
                show_message(f"Error checking for new dm posts: {e}", "Error")
            time.sleep(10)

    def stop_checking_dms(self):
        self.is_checking_dms = False

    def check_dm_cache(self):
        to_delete = [id for id, unix in dm_cache_user.items() if time.time() - unix > 600]
        for id in to_delete:
            del dm_cache_user[id]

    # Public service:
    def bind_to_public_post(self, func=None):
        if not callable(func):
            show_message(f"Expected arg1 to be callable in ConnectionService.bind_to_public_post(func:function)", "Error")
            return

        self.public_functions.append(func)

    def bind_to_message_reply(self, message_id:str=None, func=None):
        if not check_type(message_id, str, 1, "message_id", "ConnectionService.bind_to_message_reply"): return
        if not callable(func):
            show_message(f"Expected arg2 to be callable in ConnectionService.bind_to_message_reply(..., func:function)", "Error")
            return

        if message_id not in self.reply_functions:
            self.reply_functions[message_id] = []
        self.reply_functions[message_id].append(func)

    # DM Service:
    def bind_to_any_dm(self, func=None):
        if not callable(func):
            show_message(f"Expected arg1 to be callable in ConnectionService.bind_to_any_dm(func:function)", "Error")
            return
        
        self.anydm_functions.append(func)

    def bind_to_user_dm(self, username:str=None, func=None):
        if not check_type(username, str, 1, "username", "ConnectionService.bind_to_user_dm"): return
        if not callable(func):
            show_message(f"Expected arg2 to be callable in ConnectionService.bind_to_user_dm(.., func:function)", "Error")
            return

        username = username.replace(' ', '-')
        if username not in self.userdm_functions:
            self.userdm_functions[username] = []
        self.userdm_functions[username].append(func)

class MessageService:
    def create_post(self, message:str=None):
        if not check_type(message, str, 1, "message", "MessageService.create_post"): return
    
        key = get_key()
        if not key:
            return

        data = {
            "message": message,
            "attachments": "",
            "name": user,
            "key": key
        }
        response = session.post(send_message_url, data=data, headers=headers)
        show_message(f"Response Status Code (Send Message): {response.status_code}", "Http")

    def reply(self, message_id:str=None, message:str=None):
        reply(message_id, message)

    def like(self, message_id:str=None, value:bool=True):
        like(message_id, value)

    def edit(self, message_id:str=None, message:str=None):
        edit(message_id, message)

    def delete(self, message_id:str=None):
        delete(message_id)

    def direct_message(self, username:str=None, message:str=None):
        direct_message(username, message)

    def get_group_id_by_name(self, group_name:str=None):
        if not check_type(group_name, str, 1, "group_name", "MessageService.get_group_id_by_name"): return
        
        response = session.post(inbox_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            for user_contact in soup.find_all('a', class_='user-contact'):
                name = user_contact.find('h3').text.strip()
                if name == group_name:
                    href = user_contact.get('href')
                    if href:
                        id = href.split("/")[-1]
                        return id

    def message_group_by_name(self, group_name:str=None, message:str=None):
        group_id = self.get_group_id_by_name(group_name)
        if group_id:
            group_message(group_id, message)

    def message_group_by_id(self, group_id:str=None, message:str=None):
        group_message(group_id, message)

class ProfileService:
    def get_profile(self, username:str=None):
        if not check_type(username, str, 1, "username", "ProfileService.get_profile"): return
        username = username_to_id(username)
        if username == username_to_id(user): return # Can't get own profile for now

        response = session.post(f"{profile_url}/{username}", headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            account_info_div = soup.find('div', id='account-info')
            if not account_info_div:
                return
            
            username_div = account_info_div.find('div', id='username')
            username = username_div.find('h1').text.strip()
            verified = username_div.find('h1').find('img') is not None
            following = int(username_div.find('span', id='following-count').text.strip()) or 0
            followers = int(username_div.find('span', id='follower-count').text.strip()) or 0
            likes = int(username_div.find('span', id='like-count').text.strip()) or 0
            description = get_text_from_message(soup.find('div', id='description'))
            markdowndescription = get_text_from_message(soup.find('div', id='description'), True)
            socials = {}
            if soup.find('div', id='socials'):
                for social in soup.find('div', id='socials').children:
                    socialtype = social.find('img').get('src').split('/')[-1].replace('.svg', '')
                    socials[socialtype] = social.get('href')
            join_date = soup.find('p', id='signup-date').text.strip().split(' ')[2]
            trophies = []
            for trophy in soup.find('div', id='trophy-container'):
                trophies.append(trophy.find('h3').text.strip())

            return Profile(username, verified, following, followers, likes, description, markdowndescription, socials, join_date, trophies)

    def username_to_id(self, username:str=None):
        return username_to_id(username)
    
    def id_to_username(self, user_id:str=None):
        # Won't work for other converted chars than space
        if not check_type(user_id, str, 1, "user_id", "ProfileService.id_to_username"): return
        return user_id.replace('-', ' ')
    
    def follow(self, username:str=None, value:bool=True):
        follow(username, value)

class ExportBotService:
    def __init__(self):
        self.ConnectionService = ConnectionService()
        self.MessageService = MessageService()
        self.ProfileService = ProfileService()

    def start_session(self):
        session.get(login_url, headers=headers)

    def login(self, username:str=None, password:str=None, params:dict=None):
        if not check_type(username, str, 1, "username", "BotService.login"): return
        if not check_type(password, str, 2, "password", "BotService.login"): return

        global user
        self.start_session()

        if params:
            if params.get('http-log') == True:
                global show_http
                show_http = True
            if params.get('force-first') == True:
                global first_run
                first_run = False

        user = username
        logindata = {"user": username, "pass": password, "redirect": ""}
        response = session.post(actionlogin_url, data=logindata, headers=headers)
        return response.status_code == 200

show_message("Library succesfully loaded.")

BotService = ExportBotService()
