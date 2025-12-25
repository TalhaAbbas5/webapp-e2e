from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash
import re

app_routes = Blueprint("app_routes", __name__)

# Dummy user for now
VALID_USER = {
    "username": "admin",
    "password": "1234"
}

@app_routes.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == VALID_USER["username"] and password == VALID_USER["password"]:
            session["user"] = username
            return redirect(url_for("app_routes.dashboard"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app_routes.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("app_routes.login"))
    return render_template("dashboard.html")

@app_routes.route("/form", methods=["GET", "POST"])
def form_page():
    if "user" not in session:
        return redirect(url_for("app_routes.login"))

    error = None
    success = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")

        # Validation
        if not name or not email or not age:
            error = "All fields are required"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error = "Invalid email address"
        elif not age.isdigit() or int(age) <= 0:
            error = "Age must be a positive number"
        else:
            success = "Form submitted successfully!"

    return render_template("dashboard.html", error=error, success=success)
