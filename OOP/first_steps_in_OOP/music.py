class Music:
    def __init__(self, title : str, artist : str, lyrics : str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(song):
        return f"This is {song.title} from {song.artist}"
    def play(song):
        return song.lyrics

song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
