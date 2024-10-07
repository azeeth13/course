from aiogram.fsm.state import StatesGroup, State

class Registration(StatesGroup):
    
    surname_name=State()
    waiting_for_phone_number=State()
    new_number=State()
    tanlash = State()
    birthday_date=State()
    viloyatlar=State()
    sertifikat=State()
    tasdiqlov=State()
    new_state=State()
    
    paying_user=State()
    awaiting_admin_approval=State()
