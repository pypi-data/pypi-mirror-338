import pytest

from .music import Track, AudioDevice
import crit_est as crest



@pytest.fixture
def audioDevices():
	rockRadio = AudioDevice()
	rockRadio.playback.setTrack(Track("Skillet", "Awake and Alive"))
	rockRadio.sound.setVolumeRatio(0.51)

	gymRadio = AudioDevice()
	gymRadio.playback.setTrack(Track("DEXDBELL", "GYMDOWN"))
	gymRadio.sound.setVolumeRatio(0.3)

	popRadio = AudioDevice()
	popRadio.playback.setTrack(Track("Fight The Fade", "Next Sunrise"))
	popRadio.sound.setVolumeRatio(0.6)

	chillRadio = AudioDevice()
	chillRadio.playback.setTrack(Track("LoFi girl", "Beats to relax"))
	chillRadio.sound.setVolumeRatio(0.3)

	return {
		"turnedOff": AudioDevice(),
		"rock": rockRadio,
		"gym": gymRadio,
		"pop": popRadio,
		"chill": chillRadio
	}



FAVORITE_MUSIC = {
	Track("Skillet", "Awake and Alive"),
	Track("Imagine Dragons", "Radioactive"),
	Track("Imminence", "Black")
}


HATED_MUSIC = {
	Track("Reward For A Dead Man", "Grain of Hope"),
	Track("Smash Stereo", "System Overload"),
	Track("DEXDBELL", "GYMDOWN")
}


BASIC_SUITE = crest.Suite(
	crest.PredicatedCriterion(
		"Let's listen to a music",
		lambda audioDevice:
			not audioDevice.playback.isPlaying()
	),
	crest.PredicatedCriterion(
		"a bit louder, please",
		lambda audioDevice:
			audioDevice.playback.isPlaying() 
			and audioDevice.playback.getTrack() in FAVORITE_MUSIC
			and audioDevice.sound.getLevelRatio() <= 0.5
	),
	crest.PredicatedCriterion(
		"LOUDER",
		lambda audioDevice:
			audioDevice.playback.isPlaying() 
			and audioDevice.playback.getTrack() in FAVORITE_MUSIC
			and audioDevice.sound.getLevelRatio() > 0.5
			and audioDevice.sound.getLevelRatio() < 1
	),
	crest.PredicatedCriterion(
		"I CAN'T HEAR YOU BUT I LIKE IT",
		lambda audioDevice:
			audioDevice.playback.isPlaying() 
			and audioDevice.playback.getTrack() in FAVORITE_MUSIC
			and audioDevice.sound.getLevelRatio() >= 1
	),
	crest.PredicatedCriterion(
		"Skip",
		lambda audioDevice:
			audioDevice.playback.isPlaying() 
			and audioDevice.playback.getTrack() in HATED_MUSIC
	),
	crest.PredicatedCriterion(
		"Quieter",
		lambda audioDevice:
			audioDevice.playback.isPlaying()
			and audioDevice.playback.getTrack() not in \
				FAVORITE_MUSIC | HATED_MUSIC
			and audioDevice.sound.getLevelRatio() > 0.5
	)
)



DEFAULTED_SUITE = crest.DefaultedCriterion(BASIC_SUITE, "Perfect")



@pytest.mark.parametrize("suite, deviceName, expectedReaction",
[
	(BASIC_SUITE, "turnedOff", "Let's listen to a music"),
	(BASIC_SUITE, "rock", "LOUDER"),
	(BASIC_SUITE, "gym", "Skip"),
	(BASIC_SUITE, "pop", "Quieter"),

	(DEFAULTED_SUITE, "turnedOff", "Let's listen to a music"),
	(DEFAULTED_SUITE, "rock", "LOUDER"),
	(DEFAULTED_SUITE, "gym", "Skip"),
	(DEFAULTED_SUITE, "pop", "Quieter"),
	(DEFAULTED_SUITE, "chill", "Perfect")
])
def testBasicSuite(suite, deviceName, expectedReaction, audioDevices):
	assert suite(audioDevice=audioDevices[deviceName]) == expectedReaction



def testBasicSuiteBeyond(audioDevices):
	with pytest.raises(AssertionError):
		BASIC_SUITE(audioDevice=audioDevices["chill"])


