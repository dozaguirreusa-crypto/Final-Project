from .db import get_connection

class UserModel:

    @staticmethod
    def create_user(name, email):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    @staticmethod
    def get_user(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def update_user(user_id, name, email):
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE users SET name=%s, email=%s WHERE id=%s"
        cursor.execute(query, (name, email, user_id))
        conn.commit()
        count = cursor.rowcount
        cursor.close()
        conn.close()
        return int(count) > 0     # ✅ CORREGIDO

    @staticmethod
    def delete_user(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True