from .db import get_connection

class UserModel:

    @staticmethod
    def create_user(name, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
            (name, email)
        )
        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return new_id

    @staticmethod
    def get_user(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id=%s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}
        return None

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]

    @staticmethod
    def update_user(user_id, name, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s;",
        (name, email, user_id)
        )
        conn.commit()

    @staticmethod
    def delete_user(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True