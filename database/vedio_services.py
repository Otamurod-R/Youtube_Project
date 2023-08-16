from database import get_db
from database.models import Video
from datetime import datetime


def adding_new_video_db(id:int, duration:int, name:str, user_id: int, video_path: str, description:str):
    db=next(get_db())

    new_video=Video(id=id, name=name, duration=duration,
                    user_id=user_id, video_path=video_path, description=description, reg_date=datetime.now())
    db.add(new_video)
    db.commit()

    return 'New video has been added'

def deleting_video_db(video_id):
    db=next(get_db())

    exact_video=db.query(Video).filter_by(id=video_id).first()
    if exact_video:
        db.delete(exact_video)
        db.commit()
        return f'{Video.name} has been deleted'
    return 'No such video file was found'

def getting_video_db(video_id):
    db=next(get_db())

    exact_vedio=db.query(Video).filter_by(id=video_id).first()

    if exact_vedio:
        return exact_vedio
    return 'No such video file was found'

def getting_all_vidieos_db(video_name):
    db=next(get_db())

    all_vedio=db.query(Video).filter_by(name=video_name).all()
    if all_vedio:
        return all_vedio
    return f'No video with {video_name} has been found'

def changing_video_discription(id, new_data):
    db=next(get_db())
    pass


