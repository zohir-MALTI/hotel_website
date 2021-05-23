from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs', views.jobs, name='jobs'),
    path('show_CVs', views.show_CVs, name='show_CVs'),
    path('hiring', views.hiring, name='hiring'),
    path('drop_CV', views.drop_CV, name='drop_CV'),
    path('<int:job_id>', views.detail, name='detail'),
    path('<int:job_id>/add_like', views.add_like, name='add_like'),
    path('<int:job_id>/add_comment', views.add_comment, name='add_comment'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('favorites', views.favorites, name='favorites'),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
