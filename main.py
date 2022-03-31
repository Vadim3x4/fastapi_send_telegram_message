from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from fastapi import FastAPI

api_id = ''
api_hash = 'x'
client = TelegramClient('session_name', api_id, api_hash)


def send_code(code, phonenumber):
    contact = InputPhoneContact(client_id=0, phone=phonenumber, first_name="Alexey", last_name=" ")
    result = client.invoke(ImportContactsRequest([contact]))
    client.send_message(result.users[0], f'Code confirmation: {code}')


app = FastAPI()


@app.get("/get_code/")
async def create_item(phone: str, code: str):
    send_code(code, phone)
    return None
