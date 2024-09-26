
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('person_detail/',views.person_detail,name="person_detail"),
    path('save_detail/',views.save_detail,name='save_detail'),
    path('doc_detail/',views.doc_detail,name='doc_detail'),
    path('doc_save/',views.doc_save,name='doc_save'),
    path('doc_display/',views.doc_display,name='doc_display'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('profile/',views.profile_detail,name='profile_detail'),
    path('services/',views.services,name='services'),
    path('work/',views.work,name='work'),
    path('check_work/',views.check_work,name="check_work"),
    path('nationality/',views.nationality,name='nationality'),
    path('print_n/<int:id>/',views.print_n,name='print_n'),
    path('print_residential/<int:id>/',views.print_residential,name='print_residential'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
