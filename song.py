
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        songs = set()
        next_song = self
        while next_song:
            if next_song.name in songs:
                return True
            else:
                songs.add(next_song.name)
                next_song = next_song.next or None

        return False


first = Song('Hello')
second = Song('Eye of the tiger')
third = Song('Third Eye')

first.next_song(second);
second.next_song(third);
third.next_song(first)

print(first.is_repeating_playlist())
