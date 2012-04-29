from user_messages.models import Thread


def user_messages(request):
    c = {}
    if request.user.is_authenticated():
        c["inbox_count"] = Thread.objects.inbox(request.user).count()
        c["unread_count"] = Thread.objects.unread(request.user).count()
    return c

