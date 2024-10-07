from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder



contact = ReplyKeyboardMarkup(
  keyboard=[
    [KeyboardButton(text='📲 Telefon raqamni yuborish', request_contact=True)]
  ],
  resize_keyboard=True, one_time_keyboard=True
)



pass_number=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="O'tkazib yuborish",callback_data="o'tkazish")],
    ]
)



 
def kasblar_tugmasi(tanlangan_kasblar=None):
    builder = InlineKeyboardBuilder()
    kasblar = ["O'qituvchi 👩‍🏫", "Talaba 👨‍🎓", "Repetitor 🧑‍🏫", "Abituriyent 👩‍🎓"]

    if tanlangan_kasblar is None:
        tanlangan_kasblar = []

    for kasb in kasblar:
        if kasb in tanlangan_kasblar:
            builder.button(text=f"{kasb} ✅", callback_data=kasb)
        else:
            builder.button(text=kasb, callback_data=kasb)

    builder.button(text="Tasdiqlash", callback_data="tasdiqlash")
    builder.adjust(2)
    return builder.as_markup()



def sertifikatlar_tugmasi_button(tanlangan_sertifikatlar=None):
    creator=InlineKeyboardBuilder()
    qogozlar=["Milliy sertifikat","Attestatsiya","Vazir jamg'armasi","Olimpiada","Yozgi kirish imtihoni","Madrasa"]


    if tanlangan_sertifikatlar is None:
        tanlangan_sertifikatlar=[]

    for varoq in qogozlar:
        if varoq in tanlangan_sertifikatlar:
            creator.button(text=f"{varoq} ✅",callback_data=varoq)

        else:
            creator.button(text=varoq,callback_data=varoq)

    creator.button(text="Keyingisi",callback_data='next')
    creator.adjust(2)
    return creator.as_markup()
# def create_sertificate_buttons(selected=None):
#     button_builder = InlineKeyboardBuilder()
#     sertificates=["Milliy sertifikat","Attestatsiya","Vazir jamg'armasi","Olimpiada","Yozgi kirish imtihoni","Madrasa"]

#     if selected is None:
#         selected = []

#     for profession in sertificates:
#         if profession in selected:
#             button_builder.button(text=f"{profession} ✅", callback_data=profession)
#         else:
#             button_builder.button(text=profession, callback_data=profession)

#     # Tasdiqlash tugmasini qo'shish
#     button_builder.button(text="Tasdiqlash", callback_data="confirm")
#     button_builder.adjust(2)
#     return button_builder.as_markup()



# serificates=InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Milliy sertifikat",callback_data='diplom=milliy_sertifikat'),InlineKeyboardButton(text="Attestatsiya",callback_data='diplom=attestatsiya')],
#         [InlineKeyboardButton(text="Vazir jamg'armasi",callback_data="diplom=vazir_jamg'armasi"),InlineKeyboardButton(text="Olimpiada",callback_data='diplom=olimpiada')],
#         [InlineKeyboardButton(text="Yozgi kirish imtihoni",callback_data='diplom=yozgi_kirish_imtihon'),InlineKeyboardButton(text="Madrasa",callback_data="diplom=madrasa")],
        
#     ]
# )



admin=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Admin 👨🏼‍💻", url="https://t.me/XAVIERXCK")]
    ]
)

provinces_of_uzb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Toshkent viloyati",callback_data='province=toshkent'),InlineKeyboardButton(text="Andijon viloyati",callback_data='province=andijon')],
        [InlineKeyboardButton(text="Buxoro viloyati",callback_data="province=buxoro"),InlineKeyboardButton(text="Fargʻona viloyati",callback_data="province=fargona")],
        [InlineKeyboardButton(text="Jizzax viloyati",callback_data='province=jizzah'),InlineKeyboardButton(text="Xorazm viloyati",callback_data='province=xorazm')],
        [InlineKeyboardButton(text="Namangan viloyati",callback_data='province=namangan'),InlineKeyboardButton(text='Navoiy viloyati',callback_data='province=navoiy')],
        [InlineKeyboardButton(text='Qashqadaryo viloyati',callback_data='province=qashaqadaryo'),InlineKeyboardButton(text="Surxondaryo viloyati",callback_data="province=surxondaryo")],
        [InlineKeyboardButton(text="Samarqand viloyati",callback_data='province=samarqand'),InlineKeyboardButton(text="Sirdaryo viloyati",callback_data='province=sirdaryo')],
        
    ]
)



def approve_buttons():
    buttons = [
        InlineKeyboardButton(text="✅ Accept", callback_data="accept_payment"),
        InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_payment")
    ]
    return InlineKeyboardMarkup(inline_keyboard=[buttons])








def action_keyboard():
    # Create the inline keyboard markup
    keyboard = InlineKeyboardBuilder()  # Adjust row_width if needed
    # Add buttons to the keyboard
    keyboard.add(
        InlineKeyboardButton(text="Yuborish ✅", callback_data="send"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Bekor qilish ❌", callback_data="cancel")
    )
    keyboard.adjust(2)
    return keyboard.as_markup()