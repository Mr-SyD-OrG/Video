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

@routes.get("/file/{chat_id}/{message_id}")
async def stream_handler(request):
    chat_id = int(request.match_info["chat_id"])
    message_id = int(request.match_info["message_id"])

    
    try:
        message = await app.get_messages(chat_id, message_id)

        if not message or not message.media:
            return web.Response(text="No media in message", status=404)

        file = message.document or message.video or message.audio
        if not file:
            return web.Response(text="Unsupported media type", status=400)

        # Temporary success response
        return web.Response(text="Media found!", status=200)

    except Exception as e:
        return web.Response(text=f"Error: {str(e)}", status=500)
