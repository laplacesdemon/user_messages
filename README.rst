User messaging
==============

``user-messages`` is an application for allowing users of your Django site to
send messages to each other.


Quick Start
-----------

Include ``user-messages`` in your requirements file and add
``"user_messages"`` to your INSTALLED APPS setting.

Once you have the ``user-messages`` installed, hook up the URLs::
    
    urlpatterns = patterns("",
        # some cool URLs
        
        (r"^messages/", include("user_messages.urls")),
        
        # some other cool URLs
    )

Now all you need to do is wire up some templates.

My additions
------------

I've added a couple of template tags

other_user: Returns the other user in the thread
other_user_profile: Returns the other user in the thread
