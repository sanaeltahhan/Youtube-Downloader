from flask import Flask, render_template, request, url_for, redirect, send_file
from pytube import YouTube
import os



app = Flask(__name__)


@app.route('/')
def hello():
    url = request.args.get('url')
    choice = request.args.get('choice')

    if url:
        yt = YouTube(str(url))
        videos = yt.streams.all()
        videos_str = [str(var) for var in videos]
        if not choice:
            return render_template('home.html', videos = videos_str, loading = True, checked = True, url=url)
        else:
            choice=int(choice)
            vid = videos[choice]
            destination = os.getcwd()+'\\static\\downloads\\'
            vid.download(destination)
            return redirect(url_for('downloads'))

    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/downloads')
def downloads():
    filename = str(os.listdir("D:\Documents\Projects\YoutubeDownloader\YoutubeDownloader\static\downloads")[-1])
    path =f'D:\Documents\Projects\YoutubeDownloader\YoutubeDownloader\static\downloads\{filename}'
    return send_file(path, as_attachment = True)


if __name__ == '__main__':
    app.run(debug = True)
