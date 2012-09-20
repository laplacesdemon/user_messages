from django import template

register = template.Library()

@register.filter
def unread(thread, user):
    """
    Returs true if there is unread messages for the user on the thread
    """
    return bool(thread.userthread_set.filter(user=user, unread=True))

@register.filter
def other_user(thread, user):
    """
    Returns the other user in the thread
    """
    for u in thread.users.all():
        if u != user:
            return u
    return None

@register.filter
def other_user_profile(thread, user):
    """
    Returns the other user in the thread
    """
    for u in thread.users.select_related().all():
        if u != user:
            return u
    return None