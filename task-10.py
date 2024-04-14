class Audio:
    id_counter = 1

    def __init__(self, name, url):
        self.id = Audio.id_counter
        Audio.id_counter += 1
        self.name = name
        self.url = url
        self.rating = 0

    def get_rating(self):
        return self.rating


class Playlist:
    id_counter = 1

    def __init__(self, name):
        self.id = Playlist.id_counter
        Playlist.id_counter += 1
        self.name = name
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)


class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)

    def search_audio_by_name(self, name):
        result = []
        for playlist in self.playlists:
            found = [audio for audio in playlist.audios if name.lower() in audio.name.lower()]
            result.extend(found)
        return result

    def search_playlist_by_name(self, name):
        return [playlist for playlist in self.playlists if name.lower() in playlist.name.lower()]

    def rate_playlist(self, playlist_id, rating):
        playlist = next((playlist for playlist in self.playlists if playlist.id == playlist_id), None)
        if playlist:
            playlist.ratings.append(rating)

    def rate_audio(self, audio_id, rating):
        for playlist in self.playlists:
            audio = next((audio for audio in playlist.audios if audio.id == audio_id), None)
            if audio:
                audio.rating = rating
                break


# Example usage:
music_player = MusicPlayer()
music_player.create_playlist("Rock")
music_player.create_playlist("Jazz")

audio1 = Audio("Song1", "http://example.com/song1.mp3")
audio2 = Audio("Song2", "http://example.com/song2.mp3")

music_player.playlists[0].add_audio(audio1)
music_player.playlists[1].add_audio(audio2)

print([audio.name for audio in music_player.search_audio_by_name("Song")])  # ['Song1', 'Song2']
print([playlist.name for playlist in music_player.search_playlist_by_name("Rock")])  # ['Rock']
music_player.rate_playlist(1, 5)
music_player.rate_audio(1, 4)
