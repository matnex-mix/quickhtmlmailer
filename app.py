from flask import Flask, render_template, request, redirect, url_for, make_response, session, flash
from flask_mail import Mail, Message #import mailing system
import os
import json

import time, threading


app = Flask(__name__) #configure flask
app.secret_key = "ITSASECRET" #secret key for username session

#setting up mail
app.config['MAIL_SERVER']='smtp-relay.sendinblue.com' #use gmail
app.config['MAIL_PORT'] = 587 #mail port
app.config['MAIL_USERNAME'] = 'quickhtmlmailer@gmail.com' #email
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = True #security type
app.config['MAIL_USE_SSL'] = False #security type


mail = Mail(app) #include mailing system

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sender = request.form["from"]
        accept = request.form['to']
        subject = request.form["subject"]
        html = request.form["html"]
        result = [x.strip() for x in accept.split(',')]
        for email in result:
            msg = Message(subject, sender=sender, recipients=[email])
            msg.html = html
            mail.send(msg)
            print("sent")
        flash("Message sent")
        return render_template("index.html")
    elif request.method == "GET":
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug="true")