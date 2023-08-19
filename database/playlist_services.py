from database import get_db
from database.models import Playlist

def create_playlist_db(id, name, category, user_id, video_id):
    db=next(get_db())

    new_playlist=Playlist(id=id, name=name, category=category, user_name=user_id, user_video=video_id)
    db.add(new_playlist)
    db.commit()

    return new_playlist
def deleting_video_from_playlist_db(video_id):
    db=next(get_db())

    exact_video=db.query(Playlist).filter_by(id=video_id).first()
    if exact_video:
        db.delete(exact_video)
        db.commit()
        return f'{exact_video} has been deleted'
    return 'Wrong data detected'

def deleting_playlist_db(id):
    db=next(get_db())

    playlist=db.query(Playlist).filter_by(id=id).first()
    if playlist:
        db.delete(playlist)
        db.commit()

        return f'{Playlist.name} has been deleted'
    return 'smth went wrong'
