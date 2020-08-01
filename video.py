import ffmpeg


def convertVideo(videoName, audioName, targetPath, targetFileName):

    input_video = ffmpeg.input(videoName)
    # added_audio = ffmpeg.input(audioName).audio.filter('adelay', "100|100")
    added_audio = ffmpeg.input(audioName)

    merged_audio = ffmpeg.filter([input_video.audio, added_audio], 'amix')

    (
        ffmpeg
        .concat(input_video, merged_audio, v=1, a=1)
        .output(targetPath+targetFileName)
        .run(overwrite_output=True)
    )

if __name__ == '__main__':
    convertVideo("resource/1.mp4","resource/2.mp3","resource/","result.mp4")
