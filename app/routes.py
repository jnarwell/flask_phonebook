from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import PhonebookForm
from app.models import Phonebook

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = PhonebookForm()
    if form.validate_on_submit():
        first=form.first.data
        last=form.last.data
        phone=form.phone.data
        address=form.address.data

        new_contact = Phonebook(first=first,last=last,phone=phone,address=address)
        db.session.add(new_contact)
        db.session.commit()
        flash('New contact added')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)
