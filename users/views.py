import hashlib
from django.shortcuts import render, redirect
from models import User
from forms import UserForm

def new(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            request.session['current_user'] = new_user
            return redirect(new_user)
    else:
        form = UserForm()

    return render(request, 'users/new.html', locals())

def show(request, user_id):
    user = User.objects.get(id=user_id)
    gravatar_id = hashlib.md5(user.email.lower()).hexdigest()
    gravatar_url = "https://secure.gravatar.com/avatar/%s" % (gravatar_id)
    return render(request, 'users/show.html', locals())

def index(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        # create
        return render(request, 'users/show.html', {})

def edit(request):
    pass
