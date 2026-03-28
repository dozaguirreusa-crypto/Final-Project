from flask import Flask, request, jsonify, render_template, redirect, url_for
from src.models import UserModel

app = Flask(__name__)

# ===============================
# PÁGINA PRINCIPAL
# ===============================
@app.route("/")
def home():
    return render_template("home.html")


# ===============================
# HEALTHCHECK (Render)
# ===============================
@app.route("/health")
def health():
    return jsonify(status="ok"), 200


# ===============================
# LISTAR USUARIOS
# ===============================
@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        users = UserModel.get_all()
        return render_template("users_list.html", users=users)
    except Exception as e:
        return render_template(
            "users_list.html",
            users=[],
            error=str(e)
        )


# ===============================
# FORMULARIO CREAR USUARIO
# ===============================
@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")

            if not name or not email:
                return render_template(
                    "user_form.html",
                    error="Todos los campos son obligatorios"
                )

            UserModel.create_user(name, email)
            return redirect(url_for("get_all_users"))

        except Exception as e:
            return render_template(
                "user_form.html",
                error=str(e)
            )

    return render_template("user_form.html")


# ===============================
# FORMULARIO EDITAR USUARIO
# ===============================
@app.route("/users/edit/<int:user_id>", methods=["GET", "POST"])
def update_user(user_id):
    try:
        user = UserModel.get_user(user_id)
        if not user:
            return redirect(url_for("get_all_users"))

        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")

            if not name or not email:
                return render_template(
                    "user_form.html",
                    user=user,
                    error="Todos los campos son obligatorios"
                )

            UserModel.update_user(user_id, name, email)
            return redirect(url_for("get_all_users"))

        return render_template("user_form.html", user=user)

    except Exception as e:
        return render_template(
            "user_form.html",
            error=str(e)
        )


# ===============================
# ELIMINAR USUARIO
# ===============================
@app.route("/users/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    try:
        UserModel.delete_user(user_id)
    except Exception:
        pass
    return redirect(url_for("get_all_users"))
