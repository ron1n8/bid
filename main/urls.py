from django.urls import path
from main import views



urlpatterns = [
	path('', views.index, name = 'index'),
	path('sign-in', views.sign_in, name = 'sign_in'),
	path('sign-out', views.sign_out, name = 'sign_out'),
	path('history', views.history, name = 'history'),
	path('download', views.download, name = 'download'),
	path('dashboard', views.dashboard, name = 'dashboard'),
	path('dashboard/remove/<int:id>', views.remove, name = 'remove'),


	path('channels', views.channels, name = 'channels'),
	path('channels/add', views.channels_add, name = 'channels_add'),
	path('channels/remove/<int:id>', views.channels_remove, name = 'channels_remove'),
]