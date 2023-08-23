from main import app
from fastapi import Request
from database.playlist_services import create_playlist_db, deleting_playlist_db, deleting_video_from_playlist_db
from pydantic import BaseModel

class Playlist(BaseModel):
    name: str
    category: str
    user_name: int
    user_video: int

@app.post('/api/create')
async def creating_playlist(playlist_model: Playlist):

    new_playlist=dict(playlist_model)

    creating_playlist=create_playlist_db(**new_playlist)
    if creating_playlist:
        try:
            new_playlist1=create_playlist_db(**new_playlist)
            return {'statsus': 1, 'message': new_playlist1}
        except Exception as e:
            return {'status': 1, 'message': e}

    return {'status': 0, 'message': 'Please check data entry'}

@app.delete('/api/delete_video')
async def delete_video_from_playlist(video_id: int):
    exact_video = deleting_video_from_playlist_db(video_id=video_id)
    return {'status': 1, 'message': exact_video}

    # try:
    #     exact_video = deleting_video_from_playlist_db(video_id=video_id)
    #     return {'status': 1, 'message': exact_video}
    # except Exception as e:
    #     return {'status': 1, 'message': e}


@app.delete('/api/delete_playist')
async def delete_playlist(id: int):
    delete_all = deleting_playlist_db(id)
    return {'status': 1, 'message': delete_all}

    # try:
    #     delete_all=deleting_playlist_db(id)
    #     return {'status': 1, 'message': delete_all}
    # except Exception as e:
    #     return {'status': 1, 'messaage': e}


