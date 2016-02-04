from flask import Flask, render_template, request, jsonify
from PIL import Image
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/lsj')#首页
def process():
    return render_template('index.html')


@app.route('/lsj/upload', methods=['POST'])#用于获取获取上传的图片并且处理图片
def upload():
    if request.method == 'POST':
        file = request.files['file']
        hashname = request.form['hash']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(
                os.path.dirname(__file__), 'static', 'img', hashname)
            file.save(file_path)
            im = Image.open(file_path)
            w, h = im.size

            if w > 800 or h > 800:
                scale = min(800 / w, 800 / h)
                neww = int(scale * w)
                newh = int(scale * h)
                im.resize((neww, newh), Image.ANTIALIAS).save(file_path)
    return jsonify(name=filename)

if __name__ == '__main__':
    app.run(debug=True)
