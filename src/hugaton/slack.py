def something():
    pass

def get_userid_from_user(user):
    #<@id|nombre>
    return user.split('|')[0].split('@')[1]