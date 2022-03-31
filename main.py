from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from fastapi import FastAPI

api_id = 18161990
api_hash = '4c074998a235071109bad5ef400b14de'
client = TelegramClient('session_name', api_id, api_hash)

phone_number = '+79999999999'
assert client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))


def send_code(code, phonenumber):
    contact = InputPhoneContact(client_id=0, phone=phonenumber, first_name="Alexey", last_name=" ")
    result = client.invoke(ImportContactsRequest([contact]))
    client.send_message(result.users[0], f'Code confirmation: {code}')




app = FastAPI()


@app.get("/get_code/")
async def create_item(phone: str, code: str):
    send_code(code, phone)
    return None
