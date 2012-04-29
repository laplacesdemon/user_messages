from django import template

register = template.Library()

@register.filter
def unread(thread, user):
    """
    Returs true if there is unread messages for the user on the thread
    """
    return bool(thread.userthread_set.filter(user=user, unread=True))