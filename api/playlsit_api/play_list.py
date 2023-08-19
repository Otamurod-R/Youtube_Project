from api import app
from fastapi import Request
from database.playlist_services import create_playlist_db, deleting_playlist_db, deleting_video_from_playlist_db

@app.put('/api/create')
async def creating_playlist(request:Request):
    data=await request.json()

    id=data.get('id')
    name=data.get('name')
    category=data.get('category')
    user_name=data.get('user_id')
    user_video=data.get('video_id')

    if id and name and category and user_name and user_video:
        create_playlist_db(id=id, name=name, category=category, user_id=user_name, video_id=user_video)
        return {'statsus': 1, 'message': 'new playlist has been created'}
    return {'status': 0, 'message': 'Please check data entry'}

@app.delete('/api/delete_video')
async def delete_video_from_playlist(request:Request):
    data=await request.json()

    video_id=data.get('videos_id')
    if video_id:
        deleting_video_from_playlist_db(video_id)
        return {'status': 1, 'message': 'video has been deleted'}
    return {'status': 0, 'message': 'Wrong data entry'}

@app.delete('/api/delete_playist')
async def delete_playlist(request:Request):
    data=await request.json()

    playlist_id=data.get('playlist_id')
    if playlist_id:
        deleting_playlist_db(playlist_id)
        return {'status': 1, 'message': 'Playlist has been deleted'}
    return {'status': 0, 'message': 'Wrong data entry'}

