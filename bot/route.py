from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/syd", allow_head=True)
async def root_route_handler(request):
    return web.json_response("MrSyD")

async def download_stream(message, offset=0, limit=None, chunk_size=1024 * 512):
    stream = message.download(
        in_memory=True,  # makes it an io.BytesIO
        file_name=None,
        progress=None
    )

    async for chunk in stream.iter_chunks(chunk_size):
        yield chunk





from pyrogram import Client
import aiofiles
import os


  # Your Pyrogram client


routes = web.RouteTableDef()

@routes.get("/file/{chat_id}/{msg_id}")
async def serve_file(request: web.Request):
    try:
        chat_id = int(request.match_info["chat_id"])
        msg_id = int(request.match_info["msg_id"])
    except ValueError:
        return web.Response(status=400, text="Invalid ID format")

    # Now fetch the message and stream it
    from .screenshotbot import ScreenShotBot as client  # make sure client is available globally
    try:
        message = await client.get_messages(chat_id, msg_id)
    except Exception as e:
        return web.Response(status=404, text="404: Not Found")

    if not message or not message.media:
        return web.Response(status=404, text="404: Not Found")

    size = message.file.size
    offset = request.http_range.start or 0
    limit = request.http_range.stop or size

    body = None
    if request.method == "GET":
        ip = request.remote
        log.info(f"Streaming file for {chat_id}/{msg_id} to {ip}")
        # You should write a transfer.download function to get file bytes from Telegram
        body = transfer.download(message.media, file_size=size, offset=offset, limit=limit)

    return web.Response(
        status=206 if offset else 200,
        body=body,
        headers={
            "Content-Type": message.file.mime_type,
            "Content-Range": f"bytes {offset}-{size}/{size}",
            "Content-Length": str(limit - offset),
            "Accept-Ranges": "bytes",
        }
    )
