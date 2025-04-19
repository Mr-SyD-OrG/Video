from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("MrSyD")


from pyrogram import Client
from pyrogram.raw.functions.messages import GetMessages
from .screenshotbot import ScreenShotBot
 
 @routes.get("/file/{chat_id}/{message_id}")
 async def stream_handler(request):
     chat_id = int(request.match_info["chat_id"])
     message_id = int(request.match_info["message_id"])
 
     # Optional: header auth
     if request.headers.get("IAM") != Config.IAM_HEADER:
         return web.Response(text="Unauthorized", status=403)
 
     try:
         message = await ScreenShotBot.get_messages(chat_id, message_id)
 
         if not message or not message.media:
             return web.Response(text="No media in message", status=404)
 
         file = message.document or message.video or message.audio
 
         if not file:
             return web.Response(text="Unsupported media type", status=400)
 
         # Now you stream this file using its file_id (via Pyrogram's get_file or custom handler)
         # Placeholder:
         return web.Response(text="Media exists!", status=200)
 
     except Exception as e:
         return web.Response(text=f"Error: {str(e)}", status=500)
