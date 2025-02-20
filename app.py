"""
Author: Ashwin Nair
Date: 2025-02-20
Project name: app.py
Summary: Main file for the Youtube downloader.
"""

from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.download()
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

