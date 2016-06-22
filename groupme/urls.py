from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update_db/', views.update_db, name='update database'),
    url(r'^functions/', views.functions, name='functions'),
    url(r'^hilg_attack/', views.hilg_attack, name='hilg attack')
]