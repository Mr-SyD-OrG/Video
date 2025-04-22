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

