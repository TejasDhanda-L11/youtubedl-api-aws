from flask import Flask, request, jsonify
import youtube_dl as you


def YoutubeDL(url):
    y = you.YoutubeDL()
    r = y.extract_info(url=url, download=False)
    # for r1 in r:
    #     print(str(r1)+' : '+str(r[r1]))
    return r


app = Flask(__name__)


@app.route('/api', methods=['GET'])
def YoutubeApi():
    initialLink = str(request.args['link'])
    rawData = YoutubeDL(initialLink)
    return jsonify(rawData)
