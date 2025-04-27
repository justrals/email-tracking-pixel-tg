from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from telegram import Bot
from dotenv import load_dotenv
import base64, os

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

app = FastAPI()

@app.route("/seen")
async def image(request: Request):
    e = request.query_params.get("e")

    if not e:
        return JSONResponse(content={"error": "Missing 'e' parameter."}, status_code=400)

    email = base64.b64decode(e).decode("utf-8")
    ip = request.client.host
    userAgent = request.headers.get('User-Agent', 'Unknown')
    
    message = f"{email} has read your email.\n\n<b>IP</b>: {ip}\n<b>UserAgent</b>: {userAgent}"
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='HTML')

    response = FileResponse('image.png', media_type='image/gif')

    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response
