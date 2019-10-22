import requests
import os.path as os
import re


class VkParser(object):

    def __init__(self, server_url, access_token, public_url):
        self.friends_url = server_url
        self.public = public_url
        self.token = access_token

    @staticmethod
    def introducing():
        line = '''
+\t╔═══╗ ╔═══╗ ╔═╗╔═╗ ╔═╗─╔╗ ╔═══╗ ╔════╗\t+
+\t╚╗╔╗║ ║╔═╗║ ╚╗╚╝╔╝ ║║╚╗║║ ║╔══╝ ║╔╗╔╗║\t+
+\t ║║║║ ║║ ║║  ╚╗╔╝  ║╔╗╚╝║ ║╚══╗ ╚╝║║╚╝\t+
+\t ║║║║ ║║ ║║  ╔╝╚╗  ║║╚╗║║ ║╔══╝   ║║  \t+
+\t╔╝╚╝║ ║╚═╝║ ╔╝╔╗╚╗ ║║─║║║ ║╚══╗   ║║  \t+
+\t╚═══╝ ╚═══╝ ╚═╝╚═╝ ╚╝─╚═╝ ╚═══╝   ╚╝  \t+

                @Author: doxn3t
\n\n        
+-------------------Disclaimer------------------------+      
+ Doxnet is a tool that allows you to obtain phone    +
+ numbers from VKontakte through API. All information + 
+ you can get from this tool is legal and in open     +
+ sources. You are absolutely responsible for your    +
+ actions. Hope that tool will be useful for you.     +
+-----------------------------------------------------+
 '''
        print(line, "\n\n")

    def obtaining_request(self):
        new_response = None
        identification = None
        amount = None
        from_where = None
        ids = None

        user_input = str(input("\n[~*] Enter Vk link: "))

        if "public" in user_input:
            from_where = self.public
            ids = "group_id"
            amount = 999

        if "id" in user_input:
            ids = "user_id"
            from_where = self.friends_url
            amount = 5000

        if not from_where:
            print("\n[X] Enter a valid URL address.")
            print("\nExample: https://vk.com/id******")
            raise SystemExit

        a = os.basename(user_input)

        try:
            pattern = re.search(r"\d+", a)
            identification = int(pattern.group())
        except (AttributeError, ValueError, TypeError):
            print("\n[X] Invalid URL address.")
            print("\nExample: https://vk.com/id******")
            raise SystemExit

        print("\n[*~]Processing  /. \n")

        response = requests.get(from_where, params={"access_token": self.token,
                                                    ids: identification,
                                                    "order": "mobile", "count": amount,
                                                    "fields": "contacts", "v": 5.92})

        try:
            new_response = response.json()["response"]["items"]
        except KeyError:
            print("\n[X] Your API key or URL address is incorrect.")
            print("\nExample API: GkN8g5rFj0nj6hLllHXp7y******************************")
            print("\nExample URL: https://vk.com/id******")
        count = 0

        for phone in new_response:
            try:
                if len(phone["home_phone"]) >= 10 and phone["home_phone"][1:].isdigit():
                    if phone["home_phone"].startswith("+7") or phone["home_phone"].startswith("8"):
                        print(f"[^] {phone['home_phone']}  from   [id{phone['id']}]")
                        count += 1
            except KeyError:
                continue

        if not count:
            print("[X] Phone numbers not found.")


VkParser.introducing()
VK_API = str(input("\n[~*] Enter your API service token: \n"))

obj = VkParser(r"https://api.vk.com/method/friends.get",
               VK_API,
               "https://api.vk.com/method/groups.getMembers")
obj.obtaining_request()
print("\nThe program was finished. Have a nice day!")
















            





        


      

    
            
            
            

    
