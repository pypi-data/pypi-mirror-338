class Track:
	def __init__(self, actor: str, name: str) -> None:
		self.actor = actor
		self.name = name


	def __hash__(self) -> int:
		return hash(self.actor) * hash(self.name)


	def __eq__(self, value: object) -> bool:
		return \
			isinstance(value, Track) \
			and self.actor == value.actor \
			and self.name == value.name


	def __str__(self) -> str:
		return f"{self.actor} - {self.name}"
	

	def __repr__(self) -> str:
		return str(self)


	
class Playback:
	class TrackIsNotSetError(RuntimeError):
		pass

	__isPlaying: bool
	__track: Track | None


	def __init__(self, track: Track|None = None) -> None:
		if track:
			self.setTrack(track)
		else:
			self.resetTrack()


	def setTrack(self, track: Track) -> None:
		self.__track = track
		self.play()


	def resetTrack(self) -> None:
		self.__track = None
		self.__isPlaying = False


	def isTrackSet(self) -> bool:
		return self.__track is not None


	def getTrack(self) -> Track:
		self.validateTrack()
		return self.__track # type: ignore
		
		
	def validateTrack(self) -> None:
		if not self.isTrackSet():
			raise Playback.TrackIsNotSetError()
			
	
	def play(self) -> None:
		self.validateTrack()
		self.__isPlaying = True


	def pause(self) -> None:
		self.validateTrack()
		self.__isPlaying = False


	def toggle(self) -> bool:
		if self.isPlaying():
			self.pause()
			return False

		self.play()
		return True


	def isPlaying(self) -> bool:
		return self.__isPlaying



class Sound:
	def __init__(self) -> None:
		self.__volume = 0.0

	
	def setVolumeRatio(self, ratio: float) -> None:
		self.__volume = ratio

	
	def getLevelRatio(self) -> float:
		return self.__volume



class AudioDevice:
	def __init__(self) -> None:
		self.sound = Sound()
		self.playback = Playback()
