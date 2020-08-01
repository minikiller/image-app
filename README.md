# image-app

process image

### image convert

POST http://localhost:4000/api/v1/img
Content-Type: application/json

{
"backImgName": "./img/stage.jpg",
"frontImgName": "./img/woman.jpg",
"targetPath": "./",
"targetImgName": "result.png"
}

### video convert

POST http://localhost:4000/api/v1/video
Content-Type: application/json

{
    "videoName": "resource/1.mp4",
    "audioName": "resource/2.mp4",
    "targetPath": "resource/",
    "targetFileName": "result.mp4"
}
## imgUtil.py

用于去除绿幕

## logo.py

用于两个照片的合成

## video.py

用于视频和音频的合成

## main.py

flask 主程序
支持cors，basicAuth，生成的目标文件发布在static目录中，自动在http中可以访问。
