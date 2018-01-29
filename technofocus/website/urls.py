from django.conf.urls import url
from . import views
from dash.views import dash_load, admin_login,admin_logout, paper_list,simple,download,upload

urlpatterns = [
	url(r'^$', views.website_load,name='site'),
	url(r'portfolio/', views.portfolio,name='portfolio'),
	url(r'services/', views.portfolio,name='services'),
	url(r'contact/', views.portfolio,name='contact'),
	url(r'about/', views.portfolio,name='about'),
	url(r'dash/', dash_load,name='dash'),
	url(r'login/',admin_login,name='login'),
	url(r'list/',paper_list,name='paperlist'),
	url(r'simple/',simple,name='simple'),
	url(r'logout/',admin_logout,name='logout'),
	url(r'upload/',upload,name='upload'),
	url(r'download/',download,name='download')
]