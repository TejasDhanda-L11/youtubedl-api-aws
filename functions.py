import youtube_dl as you


def YoutubeDLPlaylistSpec(url,playlistend=-1,playliststart=1):
    y = you.YoutubeDL(params={'playliststart':playliststart,"playlistend":playlistend,"ignoreerrors":True})
    r = y.extract_info(url=url, download=False)
    return r
# print(YoutubeDL('https://www.youtube.com/playlist?list=PLCOOUY9uAnn82EnBxCXpN6uF9pYVTvBqQ'))

# playlist url
# https://www.youtube.com/playlist?list=PLCOOUY9uAnn82EnBxCXpN6uF9pYVTvBqQ



def playlistRawDataModifierDiff_AUD_VID(playlistUrl,playlistend=-1,playliststart=1):
    playlistRawData = YoutubeDLPlaylistSpec(playlistUrl,playlistend=playlistend, playliststart=playliststart)
    mapDataToBeReturned ={}
    # title playlist
    title_playlist = playlistRawData['title']
    print('title_playlist = '+ str(title_playlist))
    mapDataToBeReturned['title'] = title_playlist
    mapDataToBeReturned['video'] = {}

    # individual video stuff

    listIndividualVideos = []

    entriesInPlaylist = playlistRawData['entries']
    numEntryVideo = -1
    for eachEntry in entriesInPlaylist:
        print('eachEntry = '+str(eachEntry))
        numEntryVideo += 1
        # print(eachEntry)
        # video title
        returnabletitleVideo = eachEntry['title']
        print('titleVideo '+ str(returnabletitleVideo))
        # link highest quality
        listOfFormats = eachEntry['formats']
        # print('listOFFFFFFFFFF' +str(listOfFormats))
        curentHighestQualityVid = {}
        curentHighestQualityAud = {}

        # getting to know best format datas
        for eachFormatNum in range(len(listOfFormats)):
            currentFormat = listOfFormats[eachFormatNum]
            # VIDEO
            if currentFormat['vcodec'] != 'none' and currentFormat['acodec'] == 'none':
                curentHighestQualityVid[str(eachFormatNum)] = int(currentFormat['format_note'][:-1])
            # Audio
            if currentFormat['acodec'] != 'none' and currentFormat['vcodec'] == 'none':
                # print(str(eachFormatNum)+'/n/n/n/n/n/n/n/n/n'+str(currentFormat)+'/n/n/n/n/n/n/n/n/n/n/n')

                curentHighestQualityAud[str(eachFormatNum)] = float(currentFormat['tbr'])

        sortedcurentHighestQualityVid_List = sorted(
            curentHighestQualityVid.items(),
            key=
            lambda qual: -qual[1]
        )
        sortedcurentHighestQualityAud_List = sorted(
            curentHighestQualityAud.items(),
            key=
            lambda qual: -qual[1]
        )
        bestAudFormatNumber = int(sortedcurentHighestQualityAud_List[0][0])
        bestVidFormatNumber = int(sortedcurentHighestQualityVid_List[0][0])

        returnableVidURL = listOfFormats[bestVidFormatNumber]['url']
        returnableAudURL = listOfFormats[bestAudFormatNumber]['url']

        mapDataToBeReturned['video'][numEntryVideo] = {
            'titleVid':(returnabletitleVideo),
            'URLVid': (returnableVidURL),
            'URLAud':(returnableAudURL)
        }
        # print(sortedcurentHighestQualityVid_List)
        # print(bestVidFormatNumber)
        # print(sortedcurentHighestQualityAud_List)
        # print(bestAudFormatNumber)
    print(mapDataToBeReturned)
    return (mapDataToBeReturned)
# playlistRawDataModifier(YoutubeDL('https://www.youtube.com/playlist?list=PLCOOUY9uAnn82EnBxCXpN6uF9pYVTvBqQ'))

def playlistRawDataModifier_SingleVid(playlistUrl,playlistend=-1,playliststart=1):
    playlistRawData = YoutubeDLPlaylistSpec(playlistUrl,playlistend=playlistend, playliststart=playliststart)
    mapDataToBeReturned = {}
    # title playlist
    title_playlist = playlistRawData['title']

    # print('title_playlist = ' + str(title_playlist))
    mapDataToBeReturned['title'] = title_playlist
    mapDataToBeReturned['video'] = {}
    mapDataToBeReturned['uploader'] = playlistRawData['uploader']

    # individual video stuff

    listIndividualVideos = []

    entriesInPlaylist = playlistRawData['entries']
    numEntryVideo = -1
    # print('entriesInPlaylist = '+str(entriesInPlaylist))
    # print('nov = '+str(len(entriesInPlaylist)))
    mapDataToBeReturned['number_of_videos'] = int(len(entriesInPlaylist))
    # print(entriesInPlaylist)
    for eachEntry in entriesInPlaylist:
        if eachEntry !=None:
            print(eachEntry)

            # print('eachEntry = ' + str(eachEntry))
            numEntryVideo += 1
            # print(eachEntry)
            # video title
            returnabletitleVideo = eachEntry['title']
            # print('titleVideo ' + str(returnabletitleVideo))
            # link highest quality
            listOfFormats = eachEntry['formats']
            # print('listOFFFFFFFFFF' +str(listOfFormats))
            curentHighestQualityVid = {}

            # getting to know best format datas
            for eachFormatNum in range(len(listOfFormats)):
                currentFormat = listOfFormats[eachFormatNum]
                # VIDEO
                if currentFormat['vcodec'] != 'none' and currentFormat['acodec'] != 'none':
                    curentHighestQualityVid[str(eachFormatNum)] = int(currentFormat['format_note'].split('p')[0])
                # Audio

            sortedcurentHighestQualityVid_List = sorted(
                curentHighestQualityVid.items(),
                key=
                lambda qual: -qual[1]
            )
            # print(curentHighestQualityVid)
            bestVidFormatNumber = int(sortedcurentHighestQualityVid_List[0][0])

            returnableVidURL = listOfFormats[bestVidFormatNumber]['url']
            returnableFormat = listOfFormats[bestVidFormatNumber]['format_note']

            mapDataToBeReturned['video'][numEntryVideo] = {
                'titleVid': (returnabletitleVideo),
                'URLVid': (returnableVidURL),
                'format': returnableFormat,
                'duration': int(eachEntry['duration']),
                'description': str(eachEntry['description']).replace("'","_").replace('"','_'),
                'thumbnail': eachEntry['thumbnail'],
                'is_live': eachEntry['is_live'],
                'upload_date': eachEntry['upload_date']

            }
            # print(sortedcurentHighestQualityVid_List)
            # print(bestVidFormatNumber)
            # print(sortedcurentHighestQualityAud_List)
            # print(bestAudFormatNumber)
        # print(mapDataToBeReturned)
    return (mapDataToBeReturned)

def YoutubeDlVideoSpec(videourl):
    y = you.YoutubeDL()
    r = y.extract_info(videourl,download=False)
    return r
def getDataOfOnlyParticularVideo(videoUrl):
    mapDataToBeReturned = {}
    eachEntry = YoutubeDlVideoSpec(videourl=videoUrl)
    returnabletitleVideo = eachEntry['title']
    # print('titleVideo ' + str(returnabletitleVideo))
    # link highest quality
    listOfFormats = eachEntry['formats']
    # print('listOFFFFFFFFFF' +str(listOfFormats))
    curentHighestQualityVid = {}

    # getting to know best format datas
    for eachFormatNum in range(len(listOfFormats)):
        currentFormat = listOfFormats[eachFormatNum]
        # VIDEO
        if currentFormat['vcodec'] != 'none' and currentFormat['acodec'] != 'none':
            curentHighestQualityVid[str(eachFormatNum)] = int(currentFormat['format_note'].split('p')[0])
        # Audio

    sortedcurentHighestQualityVid_List = sorted(
        curentHighestQualityVid.items(),
        key=
        lambda qual: -qual[1]
    )
    # print(curentHighestQualityVid)
    bestVidFormatNumber = int(sortedcurentHighestQualityVid_List[0][0])

    returnableVidURL = listOfFormats[bestVidFormatNumber]['url']
    returnableFormat = listOfFormats[bestVidFormatNumber]['format_note']

    mapDataToBeReturned = {
        'titleVid': (returnabletitleVideo),
        'URLVid': (returnableVidURL),
        'format': returnableFormat,
        'duration': int(eachEntry['duration']),
        'description': str(eachEntry['description']).replace("'","_").replace('"','_'),
        'thumbnail': eachEntry['thumbnail'],
        'is_live': eachEntry['is_live'],
        'upload_date': eachEntry['upload_date']

    }
    # print(sortedcurentHighestQualityVid_List)
    # print(bestVidFormatNumber)
    # print(sortedcurentHighestQualityAud_List)
    # print(bestAudFormatNumber)
    return mapDataToBeReturned