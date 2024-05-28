import os
from models.base import session
from models.note import Note
from app import app
from flask import render_template, request, redirect
from dotenv import load_dotenv


load_dotenv()

@app.route("/")
def all():
    return render_template("read_all.html")

@app.route("/read/<int:id>")
def read(id):
    note = session.query(Note).get(id)
    return render_template("read_detail.html", note=note)

@app.route("/delete/<int:id>")
def delete(id):
    note = session.query(Note).filter_by(id=id).first()
    if note:
        session.delete(note)
        session.commit()
    session.close()
    return redirect("/")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        task = request.form["task"]

        notes = Note(
            task=task
        )

        try:
            session.add(notes)
            session.commit()
            return  redirect('/')
        except Exception as exc:
            return exc
        finally: session.close()
    else:
        return render_template("create.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    note = session.query(Note).get(id)
    if request.method == "POST":
        task = request.form["task"]

        note.task = task
        session.commit()
        session.close()
        return redirect("/")
    else:
        return render_template("edit.html", note=note)