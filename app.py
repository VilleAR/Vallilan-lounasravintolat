from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/registration")
def registration():
    choices=["yes", "no"]
    occupations=["Student", "Employed", "Both"]
    return render_template("registration.html", choices=choices, occupations=occupations)

@app.route("/register", methods=["POST"])
def register():
    username=request.form["username"]
    password=request.form["password"]
    hash_value = generate_password_hash(password)
    if "admin" and "occupation" in request.form:
        admin=request.form["admin"]
        occupation=request.form["occupation"]
        sql = "INSERT INTO users (username,password, admin, occupation) VALUES (:username,:password, :admin, :occupation)"
        db.session.execute(sql, {"username":username,"password":hash_value, "admin":admin, "occupation":occupation})
        db.session.commit()
    return redirect("/")
@app.route("/adlogged")
def adlogged():
    return render_template("adlogged.html")
@app.route("/logged")
def index2():
    sql = "SELECT id, topic, created_at FROM polls ORDER BY id DESC"
    result = db.session.execute(sql)
    polls = result.fetchall()
    return render_template("index2.html", polls=polls)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user==None:
        return redirect("/")
    else:
        hash_value=user[0]
        if check_password_hash(hash_value, password):
            session["username"]=username
        else:
            return redirect("/")
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/new")
def new():
    return render_template("new.html")  

@app.route("/answer", methods=["POST"])
def answer():
    poll_id = request.form["id"]
    if "answer" in request.form:
        choice_id = request.form["answer"]
        sql = "INSERT INTO answers (choice_id, sent_at) VALUES (:choice_id, NOW())"
        db.session.execute(sql, {"choice_id":choice_id})
        db.session.commit()
    return redirect("/result/"+str(poll_id))

@app.route("/poll/<int:id>")
def poll(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT id, choice FROM choices WHERE poll_id=:id"
    result = db.session.execute(sql, {"id":id})
    choices = result.fetchall()
    return render_template("poll.html", id=id, topic=topic, choices=choices)

@app.route("/result/<int:id>")
def result(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT c.choice, COUNT(a.id) FROM choices c LEFT JOIN answers a " \
          "ON c.id=a.choice_id WHERE c.poll_id=:poll_id GROUP BY c.id"
    result = db.session.execute(sql, {"poll_id":id})
    choices = result.fetchall()
    return render_template("result.html", topic=topic, choices=choices)

@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    sql = "INSERT INTO polls (topic, created_at) VALUES (:topic, NOW()) RETURNING id"
    result = db.session.execute(sql, {"topic":topic})
    poll_id = result.fetchone()[0]
    choices = request.form.getlist("choice")
    for choice in choices:
        if choice != "":
            sql = "INSERT INTO choices (poll_id, choice) VALUES (:poll_id, :choice)"
            db.session.execute(sql, {"poll_id":poll_id, "choice":choice})
    db.session.commit()
    return redirect("/logged")