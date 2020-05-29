import sys
import os
import glob
import hdf5_getters
import re
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = self

        self.albumName = None
        self.albumID = None
        self.artistID = None
        self.artistLatitude = None
        self.artistLocation = None
        self.artistLongitude = None
        self.artistName = None
        self.danceability = None
        self.duration = None
        self.genreList = []
        self.keySignature = None
        self.keySignatureConfidence = None
        self.lyrics = None
        self.popularity = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.title = None
        self.year = None
        self.hotness = None
        self.mfcc = None

def main():
    basedir = "D:/Master K"
    ext = ".H5"  # Set the extension here. H5 is the extension for HDF5 files.
    songs = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root, '*' + ext))
        #songs = {}
        #keys = list()
        #values = list()
        for f in files:
            print (f)
            songH5File = hdf5_getters.open_h5_file_read(f)
            song = Song(str(hdf5_getters.get_song_id(songH5File)))
            item = {"song_id": song.id.replace('b', '')}
            song.artistID = str(hdf5_getters.get_artist_id(songH5File))
            song.artistID = song.artistID.replace('b', '',1)
            item["song_artistID"] = song.artistID
            song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
            song.albumID = song.albumID.replace('b', '',1)
            item["song_albumID"] = song.albumID
            song.albumName = str(hdf5_getters.get_release(songH5File))
            song.albumName = song.albumName.replace('b', '',1)
            item["song_albumName"] = song.albumName
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
            song.artistLatitude = song.artistLatitude.replace('b', '',1)
            item["song_artistLatitude"] = song.artistLatitude
            song.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
            song.artistLocation =song.artistLocation.replace('b', '',1)
            item["song_artistLocation"] = song.artistLocation
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
            song.artistLongitude = song.artistLongitude.replace('b', '',1)
            item["song_artistLongitude"] = song.artistLongitude
            song.artistName = str(hdf5_getters.get_artist_name(songH5File))
            song.artistName = song.artistName.replace('b', '',1)
            item["song_artistName"] = song.artistName
            song.danceability = str(hdf5_getters.get_danceability(songH5File))
            song.danceability = song.danceability.replace('b', '',1)
            item["song_danceability"] = song.danceability
            song.duration = str(hdf5_getters.get_duration(songH5File))
            song.duration = song.duration.replace('b', '', 1)
            item["song_duration"] = song.duration
            song.keySignature = str(hdf5_getters.get_key(songH5File))
            song.keySignature = song.keySignature.replace('b', '', 1)
            item["song_keySignature"] = song.keySignature
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            song.keySignatureConfidence = song.keySignatureConfidence.replace('b', '', 1)
            item["song_keySignatureConfidence"] = song.keySignatureConfidence
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.tempo = song.tempo.replace('b', '', 1)
            item["song_tempo"] = song.tempo
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignature = song.timeSignature.replace('b', '', 1)
            item["song_timeSignature"] = song.timeSignature
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.timeSignatureConfidence = song.timeSignatureConfidence.replace('b', '', 1)
            item["song_timeSignatureConfidence"] = song.timeSignatureConfidence
            song.title = str(hdf5_getters.get_title(songH5File))
            song.title = song.title.replace('b', '', 1)
            item["song_title"] = song.title
            song.year = str(hdf5_getters.get_year(songH5File))
            song.year = song.year.replace('b', '', 1)
            item["song_year"] = song.year
            #song.mfcc = str(hdf5_getters.get_segments_timbre(songH5File))
            #item["song_mfcc"] = song.mfcc
            item["song_mfcc"] = list(hdf5_getters.get_segments_timbre(songH5File))
            song.hotness= str(hdf5_getters.get_artist_hotttnesss(songH5File))
            item["song_hotness"] = song.hotness
            songs.append(item)
            songH5File.close()
            #song_dict= dict(zip(keys, values))
    with open("D:\data_file_k.json", "w") as write_file:
        json.dump(songs, write_file, cls=NumpyEncoder)


    #with open("data_file.json", "r") as read_file:
    #   json_song = json.load(write_file)

main()
