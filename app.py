from flask import Flask, render_template, jsonify, request
import boto3
from botocore.client import Config
import os


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/get-presigned-post', methods=['POST'])
def get_presigned_post():
    if request.method == 'POST':
        key = request.json['fp']
        s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
        post = s3.generate_presigned_post(
            Bucket='myBucket',
            Key=key,
            ExpiresIn=3600,
        )
        return jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)
