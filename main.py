import logging
from aiogram import Bot, Dispatcher, executor, types
from menuKeyboard import menu
from menuKeyboards2 import *
from menuKeyboards2 import *
from aiogram import bot

API_TOKEN = 'Token'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

user_id = 844256927
async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(user_id, "Bot ishga tushdi")

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Assalomu aleykum! \nIslomiy audio kitoblar botiga\nXush kelibsiz!")
    await message.answer("Audio kitobni tanlang", reply_markup=menu)


@dp.message_handler(text="🏠Bosh sahifa")
async def send_link(message: types.Message):
    await message.answer('🏠Bosh sahifa', reply_markup=menu)


#Button1 ####### Jangchi - Akrom Malik #################
@dp.message_handler(text="📕Jangchi - Akrom Malik")
async def send_link(message: types.Message):
    await message.answer('📕Jangchi - Akrom Malik', reply_markup=Button1)

@dp.message_handler(text="🎧Jangchi 1-2-3")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/187")

@dp.message_handler(text="🎧Jangchi 4-5-6")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/189")

@dp.message_handler(text="🎧Jangchi 7-8-9")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/194")

@dp.message_handler(text="🎧Jangchi 10-11")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/197")

@dp.message_handler(text="🎧Jangchi 12")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/203")

@dp.message_handler(text="🎧Jangchi 13")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/205")

@dp.message_handler(text="🎧Jangchi 14")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/208")

@dp.message_handler(text="◀Orqaga")
async def send_link(message: types.Message):
    await message.answer("Tanlang", reply_markup=menu)

#Button ####### 📕Halqa - Akrom Malik #################
@dp.message_handler(text="📕Halqa - Akrom Malik")
async def send_link(message: types.Message):
    await message.answer('📕Halqa - Akrom Malik', reply_markup=Button21)

@dp.message_handler(text="🎧Halqa 1-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/222")

@dp.message_handler(text="🎧Halqa 2-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/224")

@dp.message_handler(text="🎧Halqa 3-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/227")

@dp.message_handler(text="🎧Halqa 4-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/229")

@dp.message_handler(text="🎧Halqa 5-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/231")

@dp.message_handler(text="🎧Halqa 6-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/235")

@dp.message_handler(text="🎧Halqa 7-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/237")

@dp.message_handler(text="🎧Halqa 8-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/240")

@dp.message_handler(text="🎧Halqa 9-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/242")

@dp.message_handler(text="🎧Halqa 10-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/245")

@dp.message_handler(text="🎧Halqa 11-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/246")

@dp.message_handler(text="🎧Halqa 12-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/248")

@dp.message_handler(text="🎧Halqa 13-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/250")

@dp.message_handler(text="🎧Halqa 14-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/253")

@dp.message_handler(text="🎧Halqa 15-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/255")

@dp.message_handler(text="🎧Halqa 16-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/256")

@dp.message_handler(text="🎧Halqa 17-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/258")

@dp.message_handler(text="🎧Halqa 18-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/260")

@dp.message_handler(text="🎧Halqa 19-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/265")

@dp.message_handler(text="🎧Halqa 20-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/267")

@dp.message_handler(text="🎧Halqa 21-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/268")

@dp.message_handler(text="🎧Halqa 22-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/269")

@dp.message_handler(text="🎧Halqa 23-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/270")

@dp.message_handler(text="🎧Halqa 24-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/271")

@dp.message_handler(text="🎧Halqa 25-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/273")

@dp.message_handler(text="🎧Halqa 26-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/274")

@dp.message_handler(text="🎧Halqa 27-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/275")

@dp.message_handler(text="🎧Halqa 28-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/276")

@dp.message_handler(text="🎧Halqa 29-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/277")

@dp.message_handler(text="🎧Halqa 30-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/278")

@dp.message_handler(text="🎧Halqa 31-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/279")

@dp.message_handler(text="🎧Halqa 32-qism")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/280")

@dp.message_handler(text="▶Halqa keyingi 2/4")
async def send_link(message: types.Message):
    await message.answer("▶Halqa keyingi 2/4", reply_markup=Button22)

@dp.message_handler(text="◀Halqa orqaga 1/4")
async def send_link(message: types.Message):
    await message.answer("◀Halqa orqaga 1/4", reply_markup=Button21)

@dp.message_handler(text="▶Halqa keyingi 3/4")
async def send_link(message: types.Message):
    await message.answer("▶Halqa keyingi 3/4", reply_markup=Button23)

@dp.message_handler(text="◀Halqa orqaga 2/4")
async def send_link(message: types.Message):
    await message.answer("◀Halqa orqaga 2/4", reply_markup=Button22)

@dp.message_handler(text="▶Halqa keyingi 4/4")
async def send_link(message: types.Message):
    await message.answer("▶Halqa keyingi 4/4", reply_markup=Button24)

@dp.message_handler(text="◀Halqa orqaga 3/4")
async def send_link(message: types.Message):
    await message.answer("◀Halqa orqaga 3/4", reply_markup=Button23)

#CHUNKI SEN ALLOHSAN
@dp.message_handler(text="📕Chunki sen Allohsan - Ali Jobir Fifiy")
async def send_link(message: types.Message):
    await message.answer("📕Chunki sen Allohsan - Ali Jobir Fifiy", reply_markup=Button31)

@dp.message_handler(text="▶Chunki sen Allohsan keyingi")
async def send_link(message: types.Message):
    await message.answer("Keyingi", reply_markup=Button32)

@dp.message_handler(text="◀Chunki sen Allohsan orqaga")
async def send_link(message: types.Message):
    await message.answer("Oldingi", reply_markup=Button31)

@dp.message_handler(text="🎧01 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/285")

@dp.message_handler(text="🎧02 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/287")

@dp.message_handler(text="🎧03 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/288")

@dp.message_handler(text="🎧04 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/289")

@dp.message_handler(text="🎧05 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/290")

@dp.message_handler(text="🎧06 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/291")

@dp.message_handler(text="🎧07 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/292")

@dp.message_handler(text="🎧08 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/293")

@dp.message_handler(text="🎧09 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/294")

@dp.message_handler(text="🎧10 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/295")

@dp.message_handler(text="🎧11 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/296")

@dp.message_handler(text="🎧12 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/297")

@dp.message_handler(text="🎧13 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/298")

@dp.message_handler(text="🎧14 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/300")

@dp.message_handler(text="🎧15 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/301")

@dp.message_handler(text="🎧16 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/302")

@dp.message_handler(text="🎧17 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/303")

@dp.message_handler(text="🎧18 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/304")

@dp.message_handler(text="🎧19 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/305")

@dp.message_handler(text="🎧20 Chunki sen Allohsan")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/307")

###########Qiyomat va Oxirat#########################
@dp.message_handler(text="📕Qiyomat va oxirat - Imom Abu Xomid G'azzoliy")
async def send_link(message: types.Message):
    await message.answer("Qiyomat va oxirat - Imom Abu Xomid G'azzoliy", reply_markup=Button41)

@dp.message_handler(text="▶Qiyomat va oxirat keyingi")
async def send_link(message: types.Message):
    await message.answer("▶Keyingi", reply_markup=Button42)

@dp.message_handler(text="◀Qiyomat va oxirat oldingi")
async def send_link(message: types.Message):
    await message.answer("◀Oldingi", reply_markup=Button41)

@dp.message_handler(text="🎧01 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/309")

@dp.message_handler(text="🎧02 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/310")

@dp.message_handler(text="🎧03 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/311")

@dp.message_handler(text="🎧04 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/313")

@dp.message_handler(text="🎧05 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/314")

@dp.message_handler(text="🎧06 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/315")

@dp.message_handler(text="🎧07 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/316")

@dp.message_handler(text="🎧08 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/317")

@dp.message_handler(text="🎧09 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/318")

@dp.message_handler(text="🎧10 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/320")

@dp.message_handler(text="🎧11 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/321")

@dp.message_handler(text="🎧12 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/324")

@dp.message_handler(text="🎧13 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/325")

@dp.message_handler(text="🎧14 Qiyomat va oxirat")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/326")

############## Peshonamdagi nur #############################
@dp.message_handler(text="📕Peshonamdagi nur - Mahmud Olaqosh")
async def send_link(message: types.Message):
    await message.answer("Peshonamdagi nur", reply_markup=Button51)

@dp.message_handler(text="🎧01 Peshonamdagi nur")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/93")

@dp.message_handler(text="🎧02 Peshonamdagi nur")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/94")

@dp.message_handler(text="🎧03 Peshonamdagi nur")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/95")

@dp.message_handler(text="🎧04 Peshonamdagi nur")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/96")

@dp.message_handler(text="🎧05 Peshonamdagi nur")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/97")

@dp.message_handler(text="🎧06 Peshonamdagi nur")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/98")

#################Halol luqma ##############################
@dp.message_handler(text="📕Halol luqma - Rauf Jilasun")
async def send_link(message: types.Message):
    await message.answer("Halol luqma", reply_markup=Button61)

@dp.message_handler(text="▶Halol luqma keyingi")
async def send_link(message: types.Message):
    await message.answer("Keyingi", reply_markup=Button62)

@dp.message_handler(text="◀Halol luqma orqaga")
async def send_link(message: types.Message):
    await message.answer("Halol luqma orqaga", reply_markup=Button61)

@dp.message_handler(text="🎧01 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/49")

@dp.message_handler(text="🎧02 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/50")

@dp.message_handler(text="🎧03 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/51")

@dp.message_handler(text="🎧04 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/52")

@dp.message_handler(text="🎧05 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/53")

@dp.message_handler(text="🎧06 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/54")

@dp.message_handler(text="🎧07 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/55")

@dp.message_handler(text="🎧08 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/56")

@dp.message_handler(text="🎧09 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/57")

@dp.message_handler(text="🎧10 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/58")

@dp.message_handler(text="🎧11 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/59")

@dp.message_handler(text="🎧12 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/60")

@dp.message_handler(text="🎧13 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/61")

@dp.message_handler(text="🎧14 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/62")

@dp.message_handler(text="🎧15 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/63")

@dp.message_handler(text="🎧16 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/64")

@dp.message_handler(text="🎧17 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/65")

@dp.message_handler(text="🎧18 Halol luqma")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/69")


##############Dor ostidagi odam########################
@dp.message_handler(text="📕Dor ostidagi odam - Amina Shengliko'gli")
async def send_link(message: types.Message):
    await message.answer("Dor ostidagi odam - Amina Shengliko'gli", reply_markup=Button71)

@dp.message_handler(text="🎧01 Dor ostidagi odam")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/86")

@dp.message_handler(text="🎧02 Dor ostidagi odam")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/87")

@dp.message_handler(text="🎧03 Dor ostidagi odam")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/88")

@dp.message_handler(text="🎧04 Dor ostidagi odam")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/89")

@dp.message_handler(text="🎧05 Dor ostidagi odam")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/90")

@dp.message_handler(text="🎧06 Dor ostidagi odam")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/91")

################Shaytonning askarlari#####################
@dp.message_handler(text="📹Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("Shaytonning askarlari", reply_markup=Button81)

@dp.message_handler(text="▶Shaytonning askarlari keyingi 2/4")
async def send_link(message: types.Message):
    await message.answer("▶Shaytonning askarlari keyingi 2/4", reply_markup=Button82)

@dp.message_handler(text="◀Shaytonning askarlari orqaga 1/4")
async def send_link(message: types.Message):
    await message.answer("◀Shaytonning askarlari orqaga 1/4", reply_markup=Button81)

@dp.message_handler(text="▶Shaytonning askarlari keyingi 3/4")
async def send_link(message: types.Message):
    await message.answer("▶Shaytonning askarlari keyingi 3/4", reply_markup=Button83)

@dp.message_handler(text="◀Shaytonning askarlari orqaga 2/4")
async def send_link(message: types.Message):
    await message.answer("◀Shaytonning askarlari orqaga 2/4", reply_markup=Button82)

@dp.message_handler(text="▶Shaytonning askarlari keyingi 4/4")
async def send_link(message: types.Message):
    await message.answer("▶Shaytonning askarlari keyingi 4/4", reply_markup=Button84)

@dp.message_handler(text="◀Shaytonning askarlari orqaga 3/4")
async def send_link(message: types.Message):
    await message.answer("◀Shaytonning askarlari orqaga 3/4", reply_markup=Button83)



@dp.message_handler(text="🎧01 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1404") #video
    await message.answer("https://t.me/audiokitoblar_islom/374") #audio

@dp.message_handler(text="🎧02 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1451") #video
    await message.answer("https://t.me/audiokitoblar_islom/375") #audio

@dp.message_handler(text="🎧03 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1470") #video
    await message.answer("https://t.me/audiokitoblar_islom/377") #audio

@dp.message_handler(text="🎧04 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1499") #video
    await message.answer("https://t.me/audiokitoblar_islom/378") #audio

@dp.message_handler(text="🎧05 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1529") #video
    await message.answer("https://t.me/audiokitoblar_islom/379") #audio

@dp.message_handler(text="🎧06 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1562") #video
    await message.answer("https://t.me/audiokitoblar_islom/380") #audio

@dp.message_handler(text="🎧07 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1573") #video
    await message.answer("https://t.me/audiokitoblar_islom/381") #audio

@dp.message_handler(text="🎧08 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1608") #video
    await message.answer("https://t.me/audiokitoblar_islom/382") #audio

@dp.message_handler(text="🎧09 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1641") #video
    await message.answer("https://t.me/audiokitoblar_islom/383") #audio

@dp.message_handler(text="🎧10 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1654") #video
    await message.answer("https://t.me/audiokitoblar_islom/384") #audio

@dp.message_handler(text="🎧11 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1663") #video
    await message.answer("https://t.me/audiokitoblar_islom/390") #audio

@dp.message_handler(text="🎧12 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1672") #video
    await message.answer("https://t.me/audiokitoblar_islom/391") #audio

@dp.message_handler(text="🎧13 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1712") #video
    await message.answer("https://t.me/audiokitoblar_islom/392") #audio

@dp.message_handler(text="🎧14 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1719") #video
    await message.answer("https://t.me/audiokitoblar_islom/393") #audio

@dp.message_handler(text="🎧15 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1740") #video
    await message.answer("https://t.me/audiokitoblar_islom/394") #audio

@dp.message_handler(text="🎧16 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1749") #video
    await message.answer("https://t.me/audiokitoblar_islom/395") #audio

@dp.message_handler(text="🎧17 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1779") #video
    await message.answer("https://t.me/audiokitoblar_islom/396") #audio

@dp.message_handler(text="🎧18 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1792") #video
    await message.answer("https://t.me/audiokitoblar_islom/397") #audio

@dp.message_handler(text="🎧19 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1797") #video
    await message.answer("https://t.me/audiokitoblar_islom/398") #audio

@dp.message_handler(text="🎧20 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1842") #video
    await message.answer("https://t.me/audiokitoblar_islom/399") #audio

@dp.message_handler(text="🎧21 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1840") #video
    await message.answer("https://t.me/audiokitoblar_islom/400") #audio

@dp.message_handler(text="🎧22 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1855") #video
    await message.answer("https://t.me/audiokitoblar_islom/401") #audio

@dp.message_handler(text="🎧23 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1859") #video
    await message.answer("https://t.me/audiokitoblar_islom/402") #audio

@dp.message_handler(text="🎧24 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1925") #video
    await message.answer("https://t.me/audiokitoblar_islom/403") #audio

@dp.message_handler(text="🎧25 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1930") #video
    await message.answer("https://t.me/audiokitoblar_islom/404") #audio

@dp.message_handler(text="🎧26 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1962") #video
    await message.answer("https://t.me/audiokitoblar_islom/405") #audio

@dp.message_handler(text="🎧27 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/1973") #video
    await message.answer("https://t.me/audiokitoblar_islom/406") #audio

@dp.message_handler(text="🎧28 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/2026") #video
    await message.answer("https://t.me/audiokitoblar_islom/407") #audio

@dp.message_handler(text="🎧29 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/2035") #video
    await message.answer("https://t.me/audiokitoblar_islom/408") #audio

@dp.message_handler(text="🎧30 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/2239") #video
    await message.answer("https://t.me/audiokitoblar_islom/409") #audio

@dp.message_handler(text="🎧31 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/2242") #video
    await message.answer("https://t.me/audiokitoblar_islom/410") #audio

@dp.message_handler(text="🎧32 Shaytonning askarlari")
async def send_link(message: types.Message):
    await message.answer("https://t.me/shams_solih/2892") #video
    await message.answer("https://t.me/audiokitoblar_islom/413") #audio

#####################Iskanja########################################

@dp.message_handler(text="📕Iskanja - Amina Shengliko'gli")
async def send_link(message: types.Message):
    await message.answer("📕Iskanja - Amina Shengliko'gli", reply_markup=Button91) 

@dp.message_handler(text="🎧01 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/337") 

@dp.message_handler(text="🎧02 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/338") 

@dp.message_handler(text="🎧03 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/339") 

@dp.message_handler(text="🎧04 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/343") 

@dp.message_handler(text="🎧05 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/346") 

@dp.message_handler(text="🎧06 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/347") 

@dp.message_handler(text="🎧07 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/348") 

@dp.message_handler(text="🎧08 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/350") 

@dp.message_handler(text="🎧09 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/354") 

@dp.message_handler(text="🎧10 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/356") 

@dp.message_handler(text="🎧11 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/358") 

@dp.message_handler(text="🎧12 Iskanja")
async def send_link(message: types.Message):
    await message.answer("https://t.me/audiokitoblar_islom/360") 



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
