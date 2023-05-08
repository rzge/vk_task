from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Friend_Request

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'main/about_you.html') #возможность видеть личную информацию
# Create your views here.

@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = CustomUser.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request was already sent')

@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')

# @login_required
# def send_friend_request(request, to_user_id):
#     from_user = request.user
#     to_user = CustomUser.objects.get(id=to_user_id)
#
#     friend_request = FriendRequest(from_user=from_user, to_user=to_user)
#     friend_request.save()
#
# @login_required()
# def accept_friend_request(request, from_user_id):
#     to_user = request.user
#     from_user = CustomUser.objects.get(id=from_user_id)
#
#     friend_request = FriendRequest.objects.get(from_user=from_user, to_user=to_user)
#     friend = Friend(user=to_user, friend=from_user)
#
#     friend_request.delete()
#     friend.save()