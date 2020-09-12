from flask import Flask, request, send_file
from PIL import Image
from dist import Distributor

app = Flask(__name__)

@app.route("/img", methods=["POST"])
def upload_image():
    file = request.files['image']
    img_in = Image.open(file.stream)
    output = Distributor(img_in).result()
    img_out = Image.fromarray(data, 'RGB')

    return send_file(img_out, mimetype='image/gif')

if __name__ == "__main__":
    app.run()

