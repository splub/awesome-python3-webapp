#!/usr/bin/env python3
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Hello</h1>')
#协程修饰器
@asyncio.coroutine
def 
