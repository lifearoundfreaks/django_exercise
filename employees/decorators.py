from django.contrib import messages


def user_access_error(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.warning(
                request,
                'You do not have sufficient rights to view this page.')
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
