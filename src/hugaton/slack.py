def something():
    pass

def get_user_info(user):
    #<@id|nombre>
    id, name = user.split('|')
    return id.split('@')[1], name[:-1]

def notify_channel():
    pass