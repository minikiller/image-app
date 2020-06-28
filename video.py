import ffmpeg


input_video = ffmpeg.input("resource/video_with_audio.mp4")
added_audio = ffmpeg.input("resource/dance_beat.ogg").audio.filter('adelay', "100|100")

merged_audio = ffmpeg.filter([input_video.audio, added_audio], 'amix')

(
    ffmpeg
    .concat(input_video, merged_audio, v=1, a=1)
    .output("mix_delayed_audio.mp4")
    .run(overwrite_output=True)
)