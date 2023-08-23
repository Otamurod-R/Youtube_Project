from database import get_db
from database.models import User
from datetime import datetime


def register_user_db(name, email, user_country, phone_number, password):
    db=next(get_db())

    new_user=User(name=name, email=email, user_country=user_country, phone_number=phone_number, password=password,
                  reg_date=datetime.now())

    db.add(new_user)
    db.commit()
    return new_user.user_id


def check_user_data_db(phone_number, email):
    db=next(get_db())

    '''checking database for the user'''
    checker=db.query(User).filter_by(phone_number=phone_number, email=email).first()

    if checker:
        return False
    return True


def check_user_password_email_db(email, password):
    db=next(get_db())

    '''try to find the user by email first'''
    checker=db.query(User).filter_by(email=email).first()


    if checker:
        if checker.password==password:
            return checker.user_id
        else:
            return 'Wrong password '

    return 'Wrong email has been indicated'


def profile_info_db(user_id):
    db=next(get_db())

    exact_user=db.query(User).filter_by(user_id=user_id).first()

    '''if we have the user, we should show all the info'''
    if exact_user:
        return exact_user.email, exact_user.phone_number, \
            exact_user.user_city, exact_user.user_id, exact_user.name, \
            exact_user.reg_date,
    return 'No Such User account'


def change_user_data_db(user_id, change_info, new_data):
    db=next(get_db())

    exact_user=db.query(User).filter_by(user_id=user_id).first()

    '''checking what personal datat user wants to change'''
    if exact_user:
        if change_info=='email':
            exact_user.email=new_data
        elif change_info=='phone_number':
            exact_user.phone_number=new_data
        elif change_info=='name':
            exact_user.name=new_data
        elif change_info=='user_country':
            exact_user.user_country=new_data
        elif change_info=='password':
            exact_user.password=new_data

        db.commit()
        return 'Data has been successfully changed'

    return 'User was not found'