from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/', book_list, name='home_page'),
    path('books/details/<int:id>/', book_details, name='book_details'),
    path('publishing_house/create/', publishing_house_create, name = 'create_publishing_house_page'),

    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),

    path('index/', home, name='Homepage'),

    path('anon/', anonim, name = 'anon'),
    path('auth/', auth, name='auth'),
    path('publishing_house/suppliers/', supplier, name='suppliers')
    #path('can_change_publishing_house/', can_change_publishing_house, 'change_house'),
    #path('can_add_change_publishing_house', can_add_change_publishing_house, 'change_add_house'),
    #path('can_change_only_telephone/', change_only_telephone, name='change telephone')


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
