from django.shortcuts import redirect

def notLoggedUsers(view_func):
    def wrapper_func(requst, *args, **kwargs):
        if requst.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(requst, *args, **kwargs)

    return wrapper_func

def allowedUsers(allowedGroups=[]):
    def decoraror(view_func):
        def wrapper_func(requst, *args, **kwargs):
            group = None
            if requst.user.groups.exists():
                group = requst.user.groups.all()[0].name
            if group in allowedGroups:
                return view_func(requst, *args, **kwargs)
            else:
                return redirect('/accounts/profile')
        return wrapper_func
    return decoraror


def PowerUsers(view_func):
        def wrapper_func(requst, *args, **kwargs):
            group = None
            if requst.user.groups.exists():
                group = requst.user.groups.all()[0].name
            if group == 'Power Users':
                return view_func(requst, *args, **kwargs)
            if group == 'Users':
                return redirect('/accounts/profile')
        return wrapper_func
