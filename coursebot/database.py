import sqlite3













def create_database():
    conn = sqlite3.connect("user1.db")
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id integer not null,
        registered_date TEXT NOT NULL,
        full_name TEXT NOT NULL,
        username TEXT NOT NULL,
        waiting_for_phone_number TEXT NOT NULL,
        birthday_date TEXT NOT NULL,
        viloyatlar TEXT NOT NULL,
        tanlash TEXT NOT NULL,
        sertifikat TEXT NOT NULL
        
        
        )

"""
    )

    conn.commit()
    conn.close()


try:
    create_database()
    print("database yaratildi")
except:
    print("database yaratilgan")


def save_user_data(
    user_id,
    registered_date=None,
    full_name=None,
    username=None,
    waiting_for_phone_number=None,
    birthday_date=None,
    viloyatlar=None,
    tanlash=None,
    sertifikat=None,
    # paying_user=None,
):

    try:
        conn = sqlite3.connect("user1.db")
        cursor = conn.cursor()

        cursor.execute(
            """
    
            INSERT INTO user (user_id,registered_date,full_name,username,waiting_for_phone_number,birthday_date,viloyatlar,tanlash,sertifikat)
                    
            VALUES (?,?,?,?,?,?,?,?,?)
            
                    
        """,
            (
                user_id,
                registered_date,
                full_name,
                username,
                waiting_for_phone_number,
                birthday_date,
                viloyatlar,
                tanlash,
                sertifikat,
                # paying_user,
            ),
        )

        conn.commit()
        conn.close()
        print(000)
    except Exception as e:
        print("Error: ", e)


def get_user_data(user_id):
    conn = sqlite3.connect("user1.db")
    cursor = conn.cursor()

    cursor.execute(" SELECT * FROM foydalanuvchi WHERE user_id=? ", (user_id,))
    user = cursor.fetchone()

    conn.close()
    return user
