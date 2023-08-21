from main import app
from fastapi import Request
from database.vedio_services import adding_new_video_db, deleting_video_db, changing_video_text_db, \
    getting_videos_db, getting_all_vidieos_db


@app.get('/api/add_video')
async def adding_video(request:Request):
    data=await request.json()

    vedio_id=data.get('id')
    duration=data.get('duration')
    name=data.get('name')
    user_id=data.get('user_id')
    video_path=data.get('video_path')
    description=data.get('description')

    if vedio_id and duration and name and user_id and video_path and description:
        adding_new_video_db(id, duration, name, user_id, video_path, description)
        return {'statsus': 1, 'message': 'new video has been added'}
    return {'status': 0, 'message': 'Please check data entry'}

@app.delete('/api/delete_video')
async def deleting_video(request: Request):
    data=await request.json()

    video_id=data.get('id')
    if video_id:
        deleting_video_db(video_id)
        return {'status': 1, 'message': 'video has been deleted'}
    return {'status': 0, 'message': 'Wrong data entry'}

@app.put('/api/video')
async def getting_all_video(request: Request):
    data=await request.json()

    video_name=data.get('video_name')
    if video_name:
        getting_all_vidieos_db(video_name)
        return {'status': 1, 'message': getting_all_vidieos_db}
    return {'status': 1, 'message': f'No video with {video_name} was found'}

@app.get('/api/video')
async def getting_video_by_id(request: Request):
    data=await request.json()

    video_id=data.get('id')
    if video_id:
        getting_videos_db(video_id)
        return {'status': 1, 'message': getting_videos_db}
    return {'status': 0, 'message': 'Video was not found'}

@app.put('/api/change_video')
async def changing_video_name_description(id: int, change_info: str, new_data: str):
    data=changing_video_text_db(id, change_info, new_data)
    return {'status': 1, "message": data}


