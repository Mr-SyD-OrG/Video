from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/syd", allow_head=True)
async def root_route_handler(request):
    return web.json_response("MrSyD")



from pyrogram import Client
import aiofiles
import os
from .screenshotbot import ScreenShotBot as app

  # Your Pyrogram client

@routes.get("/file/{chat_id:\d+}/{message_id:\d+}")
async def stream_hdler(request):
    # Your existing stream_handler logic here
    chat_id = int(request.match_info["chat_id"])
    message_id = int(request.match_info["message_id"])

    if request.headers.get("IAM") != Config.IAM_HEADER:
        return web.Response(text="Unauthorized", status=403)

    try:
        message = await app.get_messages(chat_id, message_id)
        file = message.document or message.video or message.audio

        if not file:
            return web.Response(text="Unsupported media type", status=400)

        file_path = f"/tmp/{file.file_id}"
        if not os.path.exists(file_path):
            await app.download_media(message, file_name=file_path)

        file_stat = os.stat(file_path)
        headers = {
            "Content-Type": file.mime_type or "application/octet-stream",
            "Content-Length": str(file_stat.st_size),
            "Accept-Ranges": "bytes",
        }

        async def file_stream():
            async with aiofiles.open(file_path, "rb") as f:
                chunk = await f.read(8192)
                while chunk:
                    yield chunk
                    chunk = await f.read(8192)

        return web.Response(body=file_stream(), headers=headers)

    except Exception as e:
        return web.Response(text=f"Error: {str(e)}", status=500)
