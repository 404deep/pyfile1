import requests

print("running...")
base_url = "https://api.telegram.org/bot5356277967:AAGkvXNg4Q3TeC2fqz-oKFrqbkPQ0yM3xmo/sendMessage?chat_id=1103836710&text=hello2"


parameters = {
    "chat_id" : "1103836710",
    "text" : "hello"
}

resp = requests.get(base_url, data = parameters)
