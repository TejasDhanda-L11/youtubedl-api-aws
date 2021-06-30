from flask import Flask, request, jsonify
import functions

link1 =  'https://www.youtube.com/playlist?list=PLCOOUY9uAnn82EnBxCXpN6uF9pYVTvBqQ'
link2 = 'https://www.youtube.com/playlist?list=PLcNq9x4oCMDvj7Gmhcifsky8T65L7Pdbh'

app = Flask(__name__)

@app.route('/pl', methods=['GET'])
def YoutubeApiPlaylist():
    initialLink = str(request.args['l'])
    #test.playlistRawDataModifier(playlistUrl=initialLink)
    # return jsonify(functions.YoutubeDL(initialLink))
    return jsonify(functions.playlistRawDataModifier_SingleVid(playlistUrl=initialLink))
# just for testing purpose
# @app.route('/pla', methods=['GET'])
# def YoutubeApiPlaylista():
#     initialLink = str(request.args['l'])
#     #test.playlistRawDataModifier(playlistUrl=initialLink)
#     return jsonify(functions.YoutubeDL(initialLink))
#     # return jsonify(functions.playlistRawDataModifier_SingleVid(playlistUrl=initialLink))
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)