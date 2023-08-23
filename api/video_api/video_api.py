from main import app
from fastapi import Request
from database.vedio_services import adding_new_video_db, deleting_video_db, changing_video_text_db, \
    getting_videos_db, getting_all_vidieos_db
from pydantic import BaseModel

class Video(BaseModel):
    id: int
    duration: int
    name: str
    user_id: int
    video_path: str
    description: str

@app.post('/api/add_video')
async def adding_video(video_model: Video):
    new_video = dict(video_model)

    adding_video = adding_new_video_db(**new_video)
    if adding_video:
        try:
            new_video1 = adding_new_video_db(**adding_video)
            return {'statsus': 1, 'message': new_video1}
        except Exception as e:
            return {'status': 1, 'message': e}

    return {'status': 0, 'message': 'Please check data entry'}

@app.delete('/api/delete_video')
async def deleting_video(id: int):
    exact_video = deleting_video_db(video_id=id)
    return {'status': 1, 'message': exact_video}

    # try:
    #     exact_video=deleting_video_db(video_id=id)
    #     return {'status': 1, 'message': exact_video}
    # except Exception as e:
    #     return {'status': 1, 'message': e}


    # video_id=data.get('id')
    # if video_id:
    #     deleting_video_db(video_id)
    #     return {'status': 1, 'message': 'video has been deleted'}
    # return {'status': 0, 'message': 'Wrong data entry'}

@app.get('/api/video')
async def getting_all_video(name:str):
    by_name = getting_all_vidieos_db(name)
    return {'status': 1, 'message': by_name}

    # try:
    #     by_name=getting_all_vidieos_db(name)
    #     return {'status': 1, 'message': by_name}
    # except Exception  as e:
    #     return {'status': 1, 'message': e }



    # data=await request.json()
    #
    # video_name=data.get('video_name')
    # if video_name:
    #     getting_all_vidieos_db(video_name)
    #     return {'status': 1, 'message': getting_all_vidieos_db}
    # return {'status': 1, 'message': f'No video with {video_name} was found'}

@app.get('/api/video')
async def getting_video_by_id(id: int):
    by_id = getting_videos_db(id)
    return {'status': 1, 'message': by_id}

    # try:
    #     by_id=getting_videos_db(id)
    #     return {'status': 1, 'message': by_id}
    # except Exception as e:
    #     return {'status': 1, 'message': e}


    # data=await request.json()
    #
    # video_id=data.get('id')
    # if video_id:
    #     getting_videos_db(video_id)
    #     return {'status': 1, 'message': getting_videos_db}
    # return {'status': 0, 'message': 'Video was not found'}

@app.put('/api/change_video')
async def changing_video_name_description(id: int, change_info: str, new_data: str):
    data=changing_video_text_db(id, change_info, new_data)
    return {'status': 1, "message": data}


