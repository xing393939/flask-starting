# coding: utf-8

from flask  import Flask,request,session,g,redirect,url_for,Blueprint
from flask import abort,render_template,flash
import config
from helpers import formatText,getAvatar
from database import db
import markdown

from models import Reply
import base

config = config.rec()

reply = Blueprint('reply', __name__)

@reply.route('/reply/<pid>/add',methods=['POST'])
def add_reply(pid):
    name = request.form["reply[name]"]
    email = request.form["reply[email]"]
    website = request.form["reply[website]"]
    origin_content = request.form["reply[content]"]
    content = markdown.markdown(formatText(origin_content))
    if name == "" or email == "" or origin_content == "":
        return redirect("/post/%d" % int(pid))
    number = db.query(Reply).filter(Reply.pid == pid).count() + 1
    db.add(Reply(pid=int(pid), name=name, email=email, website=website,
        content=content, origin_content=origin_content, number=number))
    db.commit()
    base.replyerSet(name, email, website)
    return redirect("/post/%d" % (int(pid)))
