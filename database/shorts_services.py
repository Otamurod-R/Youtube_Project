from database import get_db
from database.models import Shorts

def create_shorts_db(id, name, user_id, video_id):
    db=next(get_db())

    new_shorts=Shorts(id=id, name=name, user_id=user_id, video_id=video_id)
    db.add(new_shorts)
    db.commit()

    return new_shorts


def deleting_shorts_db(shorts_id):
    db=next(get_db())

    exact_shorts=db.query(Shorts).filter_by(id=shorts_id).first()
    if exact_shorts:
        db.delete(exact_shorts)
        db.commit()
        return f'{exact_shorts} has been deleted'
    return 'Wrong data detected'

def getting_all_shorts_db(shorts_id):
    db=next(get_db())

    all_shorts=db.query(Shorts).filter_by(name=shorts_id).first()
    if all_shorts:
        return all_shorts
    return 'No video with has been found'

def changing_shorts_info_db(id, changing_info, new_data):
    db=next(get_db())

    exact_video=db.query(Shorts).filter_by(id=id).first()
    if exact_video:
        if changing_info=='description':
            exact_video.description=new_data
        elif changing_info=='name':
            exact_video.name=new_data
        db.commit()
        return 'Data has been changed successfully'
    return 'Changes was not applied'
