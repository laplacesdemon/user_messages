from django import template
from django.template import Node
from django.template import TemplateSyntaxError
from user_messages.models import Thread

register = template.Library()

###########
# Filters #
###########

@register.filter
def unread(thread, user):
    """
    Returs true if there is unread messages for the user on the thread
    """
    return bool(thread.userthread_set.filter(user=user, unread=True))

########
# Tags #
########

class MessageCountNode(Node):
	"""
	To use in unread_messages tag
	"""
	def __init__(self, asvar=None):
		self.asvar = asvar
	def render(self, context):
	    """
	    Return the count of unread messages for the user found in context,
	    (may be 0) or an empty string.
	    """
	    try:
		user = context['user']
		if user.is_anonymous():
		    count = ''
		else:
		    count = Thread.objects.unread(user).count()
	    except (KeyError, AttributeError):
		count = ''
	    if self.asvar:
		context[self.asvar] = count
		return ''
	    return count

@register.tag
def unread_messages(parser, token):
    bits = token.split_contents()
    if len(bits) > 1:
        if len(bits) != 3:
            raise TemplateSyntaxError("'{0}' tag takes no argument or exactly two arguments".format(bits[0]))
        if bits[1] != 'as':
            raise TemplateSyntaxError("First argument to '{0}' tag must be 'as'".format(bits[0]))
        return MessageCountNode(bits[2])
    else:
        return MessageCountNode()
