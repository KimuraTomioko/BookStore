from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import Publishing_houseForm, RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

def book_list(request):
    list_books = Books.objects.filter(exists=True)
    context = {
        'list_books': list_books
    }
    return render(request, 'libary/books/catalog.html', context)

def supplier(request):
    suppliers = Publishing_house.objects.all()
    return render(request, 'libary/books/supplier.html', {'suppliers': suppliers})

def book_details(request, id):
    book = get_object_or_404(Books, pk=id)
    context = {
        'book_object': book
    }
    return render(request, 'libary/books/details.html', context)

@login_required
def publishing_house_create(request):
    if request.method == "POST":
        form_published_house = Publishing_houseForm(request.POST)
        if form_published_house.is_valid():
            new_publishing_house = Publishing_house(**form_published_house.cleaned_data)
            new_publishing_house.save()
            return redirect('product_filter_page')
        else:
            context = {
                'form': form_published_house
            }
            return render(request, 'libary/publishing_house/create.html', context)
    else:
        form_published_house = Publishing_houseForm()
        context = {
            'form': form_published_house
        }
        return render(request, 'libary/publishing_house/create.html', context)

def user_registration(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            messages.success(request, 'Вы успешно зарегистрированны!')
            return redirect('log in')
        messages.error(request, 'Что-то пошло не так')
        return redirect('product_filter_page')
    else:
        reg_form = RegistrationForm()
    return render(request, 'libary/auth/registration.html', {'form': reg_form})

def user_login(request):
    if request.method == 'POST':
        form_login = LoginForm(data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()
            print('anonim', request.user.is_anonymous)
            print('auth', request.user.is_authenticated)
            login(request, user)

            print('anonim', request.user.is_anonymous)
            print('auth', request.user.is_authenticated)
            print(user)

            messages.success(request, 'Вы успешно авторизованы')
            return redirect('product_filter_page')
        messages.error(request, "Данные введены неверно")
    else:
        form_login = LoginForm()
    return render(request, 'libary/auth/login.html', {'form': form_login})


def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('log in')

def home(request):
    return render(request, 'index.html')

def anonim(request):
    print('is_active: ', request.user.is_active)
    print('is_staff: ', request.user.is_staff)
    print('is_admin: ', request.user.is_superuser)
    print('is_anonymous: ', request.user.is_anonymous)
    print('is_auth: ', request.user.is_authenticated)

    print('Может ли изменять издательство: ', request.user.has_perm('libary.change_publishing_house'))
    print('Может ли изменять и добавлять издательства?: ', request.user.has_perms(['libary.change_publishing_house', 'libary.add_publishing_house']))

    return render(request, 'libary/test/anonim.html')


@login_required()
def auth(request):
    return render(request, 'libary/test/auth.html')

#@permission_required('libary.change_publishing_house')
#def can_change_publishing_house(request):
    #return render(request, 'libary/test/change_publishing_house.html')

#@permission_required(['libary.change_publishing_house', 'libary.add_publishing_house'])
#def can_add_change_publishing_house(request):
    #return render(request, 'libary/test/add_change_publishing_house.html')

#@permission_required('libary.change_only_telephone')
#def change_only_telephone(request):
    #return render(request, 'libary/test/change_only_telephone')

