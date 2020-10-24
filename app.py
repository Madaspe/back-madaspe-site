from os import getenv

from dotenv import load_dotenv

import os
from flask import Flask, request, redirect, url_for, flash, send_from_directory, render_template
from werkzeug.utils import secure_filename

from database import db
from database import models

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = f"{os.getcwd()}/upload_files"


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        file = request.files[list(request.files)[0]]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        file_db = models.File(file.filename, os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        db.save_model_in_database(file_db)

        # return send_from_directory(app.config['UPLOAD_FOLDER'], file.filename)
        return redirect(url_for('upload_file', filename=file.filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    load_dotenv()

    try:
        os.mkdir(app.config['UPLOAD_FOLDER'])
    except:
        pass

    app.run(getenv("IP"), port=getenv("PORT"), debug=True)
