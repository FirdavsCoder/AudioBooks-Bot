from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="📕Jangchi - Akrom Malik"), #Button1
            KeyboardButton(text="📕Halqa - Akrom Malik"), #Button2

        ],
        [
            KeyboardButton(text="📕Chunki sen Allohsan - Ali Jobir Fifiy"), #Button3
            KeyboardButton(text="📕Qiyomat va oxirat - Imom Abu Xomid G'azzoliy"), #Button4
        ],
        [
             KeyboardButton(text="📕Peshonamdagi nur - Mahmud Olaqosh"),
             KeyboardButton(text="📕Halol luqma - Rauf Jilasun"),
        ],
        [
             KeyboardButton(text="📕Dor ostidagi odam - Amina Shengliko'gli"),
             KeyboardButton(text="📕Iskanja - Amina Shengliko'gli"),
        ],
        [
            KeyboardButton(text="📹Shaytonning askarlari"),
        ]
    ],
    resize_keyboard=True
)