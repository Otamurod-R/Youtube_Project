from api import app
from fastapi import Request
from database.vedio_services import adding_new_video_db, deleting_video_db, changing_video_name_db, \
    changing_video_description_db, getting_videos_db, getting_all_vidieos_db


@app.get('/api/add_video')
async def adding_video(id: int=0, user_id: int=0):

