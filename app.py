from flask import Flask, render_template, request, redirect, url_for
from src.routes import bp
from src.models import UserModel

app = Flask(__name__)
app.register_blueprint(bp)

# ✅ PAGINA DE PORTADA
@app.route("/")
def home():
    return render_template("home.html")

# ------ VISTA: LISTA DE USUARIOS ------
@app.route("/web/users")
def web_list():
    usuarios = UserModel.get_all()
    return render_template("users_list.html", usuarios=usuarios)

# ------ VISTA: FORMULARIO CREAR ------
@app.route("/web/users/create", methods=["GET", "POST"])
def web_create():
    if request.method == "POST":
        nombre = request.form["name"]
        email = request.form["email"]
        UserModel.create_user(nombre, email)
        return redirect(url_for("web_list"))
    return render_template("user_form.html", action="create")

# ------ VISTA: FORMULARIO EDITAR ------
@app.route("/web/users/update/<int:user_id>", methods=["GET", "POST"])
def web_update(user_id):
    usuario = UserModel.get_user(user_id)

    if request.method == "POST":
        nombre = request.form["name"]
        email = request.form["email"]
        UserModel.update_user(user_id, nombre, email)
        return redirect(url_for("web_list"))

    return render_template("user_form.html", action="update", usuario=usuario)

# ------ ACCIÓN: ELIMINAR ------
@app.route("/web/users/delete/<int:user_id>")
def web_delete(user_id):
    UserModel.delete_user(user_id)
    return redirect(url_for("web_list"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")