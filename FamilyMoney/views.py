from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FamilyMember
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def base(request):
    return render(request, 'base.html')


@login_required
def home(request):
    users = User.objects.exclude(id=request.user.id)
    family_members = FamilyMember.objects.filter(user=request.user)
    family_member_ids = family_members.values_list('member_id', flat=True)
    return render(request, 'home.html', {'users': users, 'family_members': family_members, 'family_member_ids': family_member_ids})


@login_required
def add_family_member(request, user_id):
    user = get_object_or_404(User, id=user_id)
    is_family_member = FamilyMember.objects.filter(
        user=request.user, member=user).exists()
    if not is_family_member:
        family_member = FamilyMember.objects.create(
            user=request.user, member=user)
        added_username = family_member.member.username
        return redirect('home')
    else:
        return redirect('home')  # No need for an error message in this case


@login_required
def remove_family_member(request, family_member_id):
    family_member = get_object_or_404(FamilyMember, id=family_member_id)
    family_member.delete()
    return redirect('home')


def list_users(request):
    items = User.objects.all()
    data = {'items': list(items.values())}
    return JsonResponse(data)


# return logged in user data                                Reading data from db
# return my family data                                     Reading data from db
# create a url/api/endpoint/route to add_family_member      Write data from db
# create a url/api/endpoint/route to remove_family_member   Write data from db


"""
C Create POST
R Read   GET
U Update  PUT
D Delete DELETE
"""
