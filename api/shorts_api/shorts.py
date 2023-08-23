from main import app
from fastapi import Request
from database.shorts_services import create_shorts_db, deleting_shorts_db, changing_shorts_info_db, getting_all_shorts_db

@app.post('/api/create')
async def creating_shorts(request:Request): #
    data=await request.json()


    name=data.get('name')
    user_id=data.get('user_id')
    video_id=data.get('video_id')

    if id and name and user_id and video_id:
        create_shorts_db(name=name, user_id=user_id, video_id=video_id)
        return {'statsus': 1, 'message': 'new playlist has been created'}
    return {'status': 0, 'message': 'Please check data entry'}

@app.delete('/api/delete_video')
async def delete_shorts(request:Request):
    data=await request.json()

    shorts_id=data.get('id')
    if shorts_id:
        deleting_shorts_db(shorts_id)
        return {'status': 1, 'message': 'video has been deleted'}
    return {'status': 0, 'message': 'Wrong data entry'}

@app.get('/api/shorts')
async def getting_all_shorts(request:Request):
    data=await request.json()

    shorts_id = data.get('id')
    if shorts_id:
        getting_all_shorts_db(shorts_id)
        return {'status': 1, 'message': getting_all_shorts_db}
    return {'status': 0, 'message': 'Video was not found'}

@app.put('/api/change_shorts')
async def changing_shorts_name_desc(id: int, change_info: str, new_data: str):
    data=changing_shorts_info_db(id, change_info, new_data)
    return {'status': 1, "message": data}
