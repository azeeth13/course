import logging
import asyncio
import re
import sys
import requests
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher,F,html
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.utils import executor
from aiogram.filters import Command
from aiogram.enums import ParseMode
from states import Registration
from token_1 import TOKEN
from aiogram.types import CallbackQuery,Message
from aiogram.client.default import DefaultBotProperties
from database import get_user_data , save_user_data,create_database
from buttons import *

# from aiogram.exceptions import ChatAdminRequired

from aiogram.types import Message,ContentType
from aiogram.filters import BaseFilter

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())




ADMIN_ID = "1267900230" 





class MediaFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        file = message.content_type in [ContentType.PHOTO]
        return file if file else 'False'






def check_valid_id(user_id):
    # Bu funksiyani haqiqiy foydalanuvchilar ro'yxati yoki bazaga ulashingiz mumkin
    valid_ids = ['-1002328748845', '-1002367829390', '-1002305747603']  # Misol uchun to'g'ri group ID'lar
    return user_id in valid_ids


@dp.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    
    # group_type=await state.update_data(valid_ids=data)
    # Foydalanuvchi start parametrini olish
    if len(message.text.split()) > 1:
        start_param = message.text.split()[1]
        
        # Admin tomonidan yuborilgan ID'larni tekshirish
        if start_param == "group1":
            await state.update_data(group_type="1")
            # Guruh 1 uchun registratsiya jarayonini boshlash
            await message.answer(f"Hurmatli {html.bold(message.from_user.full_name)}! Siz 1-guruh uchun registratsiyadan o'tmoqdasiz.")
            await message.answer(f"Assalomu alaykum, hurmatli {html.bold(message.from_user.full_name)}! Jalol Boltayevning onlayn kursida oʻqimoqchimisiz? Men ustoz Jalol Boltayevning yordamichi botiman! ")
            await message.answer(f"Demak, boshladik.Iltimos, familiya-ismingizni yozing (diqqat! dastlab familiya, keyin ismingizni yozing. Masalan, Boltayev Jalol).")
            await state.set_state(Registration.surname_name)
        elif start_param == "group2":
            await state.update_data(group_type="2")
            # Guruh 2 uchun registratsiya jarayonini boshlash
            await message.answer(f"Hurmatli {html.bold(message.from_user.full_name)}! Siz 2-guruh uchun registratsiyadan o'tmoqdasiz.")
            await message.answer(f"Assalomu alaykum, hurmatli {html.bold(message.from_user.full_name)}! Jalol Boltayevning onlayn kursida oʻqimoqchimisiz? Men ustoz Jalol Boltayevning yordamichi botiman! ")
            await message.answer(f"Demak, boshladik.Iltimos, familiya-ismingizni yozing (diqqat! dastlab familiya, keyin ismingizni yozing. Masalan, Boltayev Jalol).")
            await state.set_state(Registration.surname_name)
        elif start_param == "group3":
            await state.update_data(group_type="3")
            # Guruh 3 uchun registratsiya jarayonini boshlash
            await message.answer(f"Hurmatli {html.bold(message.from_user.full_name)}! Siz 3-guruh uchun registratsiyadan o'tmoqdasiz.")
            await message.answer(f"Assalomu alaykum, hurmatli {html.bold(message.from_user.full_name)}! Jalol Boltayevning onlayn kursida oʻqimoqchimisiz? Men ustoz Jalol Boltayevning yordamichi botiman! ")
            await message.answer(f"Demak, boshladik.Iltimos, familiya-ismingizni yozing (diqqat! dastlab familiya, keyin ismingizni yozing. Masalan, Boltayev Jalol).")
            await state.set_state(Registration.surname_name)
        else:
            await message.answer("Noto'g'ri guruh ID. Iltimos, admin bilan bog'laning.")
    else:
        await message.answer("Botdan foydalanish uchun maxsus start havolasi orqali registratsiyadan o'ting.",reply_markup=admin)







@dp.message(Registration.surname_name)
async def process_surname_name(message: Message, state: FSMContext):
    full_name = message.text.strip()
    user_id = message.from_user.id
    username = message.from_user.username  
    
    # fullname ni surname va name ga split qilish
    if " " in full_name:
        surname, name = full_name.split(maxsplit=1)

        # Uzbek familiyani tekshirish
        if re.search(r'(OV|OVA|EV|EVA|ov|ova|ev|eva)$', surname):
            #Lotin harflarda yozishni talab qiladi
            if re.match(r'^[A-Za-z ]+$', full_name):
                await state.update_data(surname=surname, name=name, user_id=user_id, username=username)
                
                await message.answer("Telefon raqamingizni ulashing:", reply_markup=contact)
                await state.set_state(Registration.waiting_for_phone_number)
            else:
                await message.answer("Iltimos, familiya va ismingizni faqat lotin alifbosida kiriting.")
        else:
            await message.answer("Iltimos, to'g'ri familiya va ismni kiriting.")
    else:
        await message.answer("Iltimos, familiya va ismingizni bitta xabar ichida kiriting.")




# @dp.message(Registration.waiting_for_phone_number)
# async def user_surname(message: types.Message, state: FSMContext):
#     await state.update_data(surname=message.text)
#     # await message.answer("Telefon raqamingizni ulashing:", reply_markup=contact)
#     await state.set_state(Registration.new_number)




@dp.message(F.contact,Registration.waiting_for_phone_number)
async def process_phone_number(message: Message, state: FSMContext):
    if message.contact:
        phone_number1 = message.contact.phone_number

        if phone_number1.startswith('998') or phone_number1.startswith('+')  :
            await state.update_data(phone_number=phone_number1)
            await message.answer("Sizda qoʻshimcha telefon raqami bormi? Bor boʻlsa, 972990066 koʻrinishda yozib yuboring. Agar qoʻshimcha raqam mavjud boʻlmasa, “oʻtkazib yuborish” tugmasini bosing.", reply_markup=pass_number)

            await state.set_state(Registration.new_number)
        else:
            await message.answer("Telefon raqami noto'g'ri, iltimos, +998 bilan boshlanuvchi raqamni ulashing.")
    else:
        await message.answer("Iltimos, telefon raqamingizni ulashish uchun tugmani bosing.")

# @dp.callback_query(lambda c: c.data in checkbox_options)
# async def EditBtn(call: CallbackQuery):
#     checkbox_options[call.data] = not checkbox_options[call.data]
#     await bot.edit_message_reply_markup(
#         chat_id=call.message.chat.id, 
#         message_id=call.message.message_id, 
#         reply_markup=GetCheckbox()
#     )


@dp.callback_query(F.data=="o'tkazish")
async def New_profession(callback:CallbackQuery,state:FSMContext):
    await callback.message.delete()
    await state.update_data(proffession=callback)
    await callback.message.answer("Qaysi toifadansiz. Bir yoki birdan ortiq variantni tanlashingiz ham mumkin!",reply_markup=kasblar_tugmasi())
    await state.set_state(Registration.tanlash) 



    
@dp.callback_query(Registration.tanlash)
async def choose_profession(callback: CallbackQuery, state: FSMContext):
    # await callback.message.delete()
    kasblar = ["O'qituvchi 👩‍🏫", "Talaba 👨‍🎓", "Repetitor 🧑‍🏫", "Abituriyent 👩‍🎓"]
    data = await state.get_data()
    tanlangan_kasblar = data.get("tanlangan_kasblar", [])

    if callback.data in kasblar:
        if callback.data in tanlangan_kasblar:
            tanlangan_kasblar.remove(callback.data)
        else:
            tanlangan_kasblar.append(callback.data)

        await state.update_data(tanlangan_kasblar=tanlangan_kasblar)
        await callback.message.edit_text("Qaysi toifadansiz. Bir yoki birdan ortiq variantni tanlashingiz ham mumkin!", reply_markup=kasblar_tugmasi(tanlangan_kasblar))

    elif callback.data == "tasdiqlash":
        await callback.message.delete()
        if tanlangan_kasblar:
            await callback.message.answer(f"Tanlangan kasblar: {', '.join(tanlangan_kasblar)}")
            await callback.message.answer("Tug'ilgan sanangizni kiriting (kun-oy-yil formatida):")
            await state.set_state(Registration.birthday_date)
        else:
            await callback.message.answer("Hech qanday kasb tanlanmadi.")




@dp.message(Registration.birthday_date)
async def process_birthday(message:Message, state: FSMContext):
    birthday = message.text.strip()
    
    try:
        
        birthday_date = datetime.strptime(birthday, '%d-%m-%Y').date()
        await state.update_data(birthday=birthday_date)
        
        
        await message.answer("Yashaydigan viloyatingizni tanlang", reply_markup=provinces_of_uzb)
        



        await state.set_state(Registration.viloyatlar)
        
        
    except ValueError:
        await message.answer("Iltimos, tug'ilgan sanani to'g'ri formatda kiriting (kun-oy-yil).")

@dp.callback_query(F.data.startswith('province='), Registration.viloyatlar)
async def process_province(callback: CallbackQuery, state: FSMContext):
    selected_province = callback.data.split('=')[1]
    print(callback.data)
    await callback.message.delete()


    try:

        await state.update_data(viloyatlar=selected_province)
            
            
        await callback.message.answer("Sizga Jalol Boltayevning onlayn kursida nima uchun qatnashyapsiz? Bir yoki birdan ortiq variantni tanlashingiz ham mumkin!", reply_markup=sertifikatlar_tugmasi_button())
        await state.set_state(Registration.sertifikat)
    except:
        await callback.message.answer("Iltimos tugmalardan birini tanlang!")
        

@dp.callback_query(Registration.sertifikat)
async def choose_letter(callback: CallbackQuery, state: FSMContext):
    

    qogozlar = ["Milliy sertifikat", "Attestatsiya", "Vazir jamg'armasi", "Olimpiada", "Yozgi kirish imtihoni", "Madrasa"]
    data = await state.get_data()
    tanlangan_sertifikatlar = data.get("tanlangan_sertifikatlar", [])

    if callback.data in qogozlar:
        if callback.data in tanlangan_sertifikatlar:
            tanlangan_sertifikatlar.remove(callback.data)
        else:
            tanlangan_sertifikatlar.append(callback.data)

        await state.update_data(tanlangan_sertifikatlar=tanlangan_sertifikatlar)
        await callback.message.edit_text("Sizga Jalol Boltayevning onlayn kursida nima uchun qatnashyapsiz? Bir yoki birdan ortiq variantni tanlashingiz ham mumkin!", reply_markup=sertifikatlar_tugmasi_button(tanlangan_sertifikatlar))
        
    elif callback.data == "next":
        if tanlangan_sertifikatlar:
            await callback.message.answer(f"Tanlangan sertifikatlar: {', '.join(tanlangan_sertifikatlar)}")
            await callback.message.answer("Malumotni yuborishni xohlaysizmi agar",reply_markup=action_keyboard())
            await state.set_state(Registration.tasdiqlov)
            await callback.message.delete()
        else:
            await callback.message.answer("Iltimos, kamida bitta sertifikat tanlang!")





@dp.message(Registration.new_number)
async def process_new_number(message:Message, state: FSMContext):
    extra_phone_number = message.text.strip()  # Strip whitespace
    
    # Validate extra phone number
    if re.match(r'^\+998\d{9}$', extra_phone_number):
        await state.update_data(new_number=extra_phone_number)
        await state.set_state(Registration.tanlash)
        await message.answer("Qaysi toifadansiz. Bir yoki birdan ortiq variantni tanlashingiz ham mumkin!", reply_markup=kasblar_tugmasi())
    else:
        await message.answer("Iltimos, telefon raqamini to'g'ri formatda kiriting (+998xxxxxxxxx).")





async def send_unique_url(user_id, state: FSMContext):
    valid_ids = ['-1002328748845', '-1002367829390', '-1002305747603']
    data = await state.get_data()

    group_type = data.get("group_type")
    
    if group_type == "1":
        chat_id = valid_ids[0]
    elif group_type == "2":
        chat_id = valid_ids[1]
    elif group_type == "3":
        chat_id = valid_ids[2]
    else:
        await bot.send_message(user_id, "Noto'g'ri guruh tanlandi.")
        return

    invite_link = await bot.create_chat_invite_link(chat_id, member_limit=1)
    await bot.send_message(user_id, f"Guruhga kirish uchun havolangiz: {invite_link.invite_link}")


async def remove_user_after_timeout(user_id, group_id, state, timeout=48):  # callback_data olib tashlandi
    for i in range(timeout):
        # Har bir soatda ogohlantirish yuborish
        await bot.send_message(user_id, "Siz 2 kun ichida to'lov qilishingiz kerak, aks holda guruhdan chiqarilasiz.")
        await asyncio.sleep(7200)  # 1 soat kutamiz

        # Agar holat tasdiqlangan bo'lsa, funksiya tugaydi
        current_state = await state.get_data()
        if current_state.get('payment_confirmed'):
            return

    # 2 kun ichida to'lov qilinmasa, foydalanuvchini guruhdan chiqarish
    await bot.ban_chat_member(chat_id=group_id, user_id=user_id)
    await bot.send_message(user_id, "Afsuski, siz to'lov qilmaganingiz uchun guruhdan chiqarildingiz.")


async def remind_monthly(user_id, group_id, state):
    while True:
        # Hozirgi vaqtni olish
        now = datetime.now()

        # Har oyning 1-kunini topish
        next_month = (now.month % 12) + 1
        next_year = now.year + (now.month // 12)
        first_day_next_month = datetime(next_year, next_month, 1)

        # 1-kungacha qancha vaqt borligini topish
        time_to_next_month = (first_day_next_month - now).total_seconds()

        # 1-kun kelguncha kutish
        await asyncio.sleep(time_to_next_month)

        # Foydalanuvchiga to'lov eslatmasi jo'natish
        await bot.send_message(user_id, "Hurmatli foydalanuvchi, bu oygi to'lovni amalga oshirishingiz kerak.")
        
        # Agar to'lov tasdiqlangan bo'lsa, jarayonni to'xtatish
        current_state = await state.get_data()
        if current_state.get('payment_confirmed'):
            await bot.send_message(user_id, "Rahmat, to'lovingiz tasdiqlandi.")
            return



@dp.callback_query(F.data == "send", Registration.tasdiqlov)
async def send_data(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    # Foydalanuvchi ma'lumotlarini olish
    name = user_data.get("name")
    surname = user_data.get("surname")
    phone_number = user_data.get("phone_number")
    user_id = user_data.get("user_id")                              
    username = user_data.get("username")
    extra_number = user_data.get("new_number", "qo'shimcha raqam yo'q")

    # Tanlangan kasblarni olish
    tanlangan_kasblar = user_data.get("tanlangan_kasblar", [])
    kasb = ', '.join(tanlangan_kasblar) if tanlangan_kasblar else "Ma'lum emas"

    birthday = user_data.get("birthday").strftime("%Y-%m-%d") if user_data.get("birthday") else None
    viloyati = user_data.get("viloyatlar")
    tanlangan_sertifikatlar = user_data.get('tanlangan_sertifikatlar', [])
    sertifikat = ', '.join(tanlangan_sertifikatlar) if tanlangan_sertifikatlar else "Ma'lum emas"
    registered_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Foydalanuvchini Sheets-ga qo'shish
    headers = {'Content-Type': 'application/json'}
    data1 = {
        'data': {
            'ism': name,
            'familiya': surname,
            'nomer': phone_number,
            'telegram_id': user_id,
            'username': username,
            'registratsiya_sanasi': registered_date,
            "qo'shimcha_raqam": extra_number,
            'kasb': kasb,
            'tugilgan_sana': birthday,
            'viloyatlar': viloyati,
            'sertifikat': sertifikat,
        }
    }

    response = requests.post('https://sheetdb.io/api/v1/ikta4qhzjerp8', json=data1, headers=headers)
    
    if response.status_code in (200, 201):
        await callback.message.answer("Ma'lumotlaringiz yuborildi ✅")
        
        # Unikal URL jo'natish va foydalanuvchini qo'shish
        group_url = await send_unique_url(callback.from_user.id, state)
        
        # To'lov haqida eslatmalar va ikki kundan keyin guruhdan chiqarish
        asyncio.create_task(remove_user_after_timeout(callback.from_user.id, group_url, state))

        # To'lov so'raladi
        await request_payment(callback.message, state)
    else:
        await callback.message.answer("Ma'lumotlarni yuborishda xatolik yuz berdi.")
    
    await state.clear()



@dp.message(Registration.new_state)
async def request_payment(message: Message, state: FSMContext):
    
    try:
        await message.answer_photo(
            photo="https://miro.medium.com/v2/resize:fit:789/1*A9YcoX1YxBUsTg7p-P6GBQ.png",
            caption="Toʻlovni amalga oshirgan boʻlsangiz, toʻlov chekini yuboring! (skrinshot yuborsangiz ham boʻladi). Kurs narxi 100000 soʻm."
        )
        
        await state.update_data(payment=message)
        await state.set_state(Registration.paying_user)
        
    except Exception as e:
        await message.answer("Rasmni yuborishda xatolik yuz berdi, iltimos, qayta urinib ko'ring.")
        print(f"Error sending payment request: {e}")

@dp.message(MediaFilter())
async def handle_photo(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    user_id = message.from_user.id  # Foydalanuvchi ID ni to'g'ri olish
    
    # Ma'lumotlarni saqlaymiz
    await state.update_data(photo_id=photo_id, user_id=user_id)


    # Adminga rasm yuboramiz va "Tasdiqlash" va "Bekor qilish" tugmalarini qo'shamiz
    key = InlineKeyboardBuilder()
    key.button(text="Tasdiqlash", callback_data=f"action#confirm#{user_id}")
    key.button(text="Bekor qilish", callback_data=f"action#cancel#{user_id}")

    await bot.send_photo(chat_id=ADMIN_ID, photo=photo_id, caption=f"{html.bold(message.from_user.full_name)} rasm yubordi. Iltimos, tasdiqlang.", reply_markup=key.as_markup())

    await message.answer("Rahmat! Toʻlovingiz Jalol Boltayevga yuborildi. Jalol Boltayev toʻlovni tasdiqlagach, sizga guruh linkini yuboraman! Havotir olmang! Toʻlovingiz tez orada tasdiqlanadi (bu 10 daqiqadan 6 soatgacha vaqt olishi mumkin. Jalol ustoz ishda boʻlsalar kechroq tasdiqlab yuboradi).")
    # await state.set_state(Registration.awaiting_admin_approval)

# Admin tasdiqlaganda yoki bekor qilganda
@dp.callback_query(F.data.startswith("action#"))
async def handle_admin_decision(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split("#")
    user_id = action[2]

    # Admin tasdiqlashi yoki bekor qilishi
    if action[1] == "confirm":
        await state.update_data(payment_confirmed=True)  # To'lov tasdiqlangan holatini o'zgartiramiz
        await bot.send_message(user_id, f"Qadrli {html.bold(callback.from_user.full_name)}, toʻlovingiz tasdiqlandi. Jalol Boltayev ustozga ishonchingiz uchun rahmat! Biz ham jamoamiz bilan sizning ishonchingizni oqlashga qattiq harakat qilamiz. Jalol ustoz test materiallari, taʼlim sifati, metodika bilan shugʻullanadi, toʻlov masalalari bilan esa men shugʻullanaman. Har toʻlov payti kelganda eslatib turaman :)")
        
        # Guruhdan chiqarishni bekor qilamiz (agar hali chiqarilmagan bo'lsa)
        # Bu yerda chiqarishni oldini olish uchun hech qanday narsa qilish kerak emas, chunki taymer tekshiradi.

    elif action[1] == "cancel":
        await bot.send_message(user_id, "To'lovingiz bekor qilindi.")
    
    # Sheets API bilan ishlash (ma'lumotlarni yangilash)
    sheet_data = {
        'payment_status': 'toʻlandi' if action[1] == "confirm" else 'toʻlanmadi'
    }
    
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://sheetdb.io/api/v1/ikta4qhzjerp8/telegram_id/{user_id}', json=sheet_data, headers=headers)
    
    if response.status_code not in (200, 201):
        await callback.message.answer("Ma'lumotlarni yangilashda xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko'ring.")
    
    await callback.message.delete()
    # await state.clear()//



async def add_user_to_group_and_start_timer(user_id, group_id, state, callback_data):
    await bot.send_message(user_id, "Siz guruhga qo'shildingiz. 2 kun ichida to'lov qilishingiz kerak, aks holda guruhdan chiqarilasiz.")
    
    # 2 kun ichida foydalanuvchini chiqarishni rejalashtiramiz (2 kun = 48 soat)
    asyncio.create_task(remove_user_after_timeout(user_id, group_id, state, callback_data))


@dp.callback_query(F.data == "o'tkazish", Registration.new_number)
async def skip_number(callback: CallbackQuery, state: FSMContext):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await state.update_data(new_number="qo'shimcha raqam yo'q")  # No extra number provided
    await state.set_state(Registration.tanlash)
    await callback.message.answer("Qaysi toifadansiz. Bir yoki birdan ortiq variantni tanlashingiz ham mumkin!", reply_markup=kasblar_tugmasi())

@dp.callback_query(F.data=="cancel", Registration.tasdiqlov )
async def cancel_data(callback:CallbackQuery, state: FSMContext):
    await callback.message.answer("Ma'lumotlaringiz bekor qilindi ❌")
    await callback.message.answer("Davom etish uchun qaytadan  /start  tugmasini bosing")
    await state.clear()



async def main() -> None:
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main()) 
