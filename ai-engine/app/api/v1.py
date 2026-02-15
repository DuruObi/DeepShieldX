from app.core.image_forensics import analyze_image
from app.core.url_scanner import inspect_url
from app.core.video_forensics import analyze_video
from fastapi import APIRouter, UploadFile, File
from app.core.voice_detector import analyze_voice
from app.core.message_scanner import scan_message

router = APIRouter()

@router.post("/voice/check")
async def check_voice(audio: UploadFile = File(...)):
    content = await audio.read()
    result = analyze_voice(content)
    return result

@router.post("/message/scan")
async def check_message(payload: dict):
    text = payload.get("text")
    result = scan_message(text)
    return result

@router.post("/video/check")
async def check_video(video: UploadFile = File(...)):
    temp_path = f"/tmp/{video.filename}"

    with open(temp_path, "wb") as f:
        f.write(await video.read())

    result = analyze_video(temp_path)

    return result

@router.post("/url/inspect")
async def check_url(payload: dict):
    url = payload.get("url")
    return inspect_url(url)

@router.post("/image/check")
async def check_image(image: UploadFile = File(...)):
    temp_path = f"/tmp/{image.filename}"
    with open(temp_path, "wb") as f:
        f.write(await image.read())

    return analyze_image(temp_path)
