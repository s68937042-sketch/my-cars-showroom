from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) # لازم السطر ده يكون كدة
# ... باقي إعدادات قاعدة البيانات ...

# أهم حاجة: في آخر الملف خالص، امسحي سطر app.run() 
# Vercel هو اللي بيشغل التطبيق بنفسه مش محتاج app.run
