from ev3dev2.sound import Sound

class Speaker:
    def __init__(self):
        self.speaker = Sound()
        
    def speak(self, text):
        self.speaker.speak(text)
        
    def beep(self):
        self.speaker.beep()
        
    def play_file(self, file):
        self.speaker.play_file(file)
        
    def play_song(self, song):
        self.speaker.play_song(song)
    
    def play_boot(self):
        self.speaker.play_file('xp_startup.wav')