"""sample_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.urls import include, path
admin.autodiscover()

urlpatterns = [
    '',
    path(r'^users/(?P<username>\w+)', include('accounts.views.show'), name='user'),
    path(r'^accounts/', include('accounts.urls')),
    path(r'^microposts/', include('microposts.urls')),
    path(r'^$', include('microposts.views.home'), name='home'),
    path(r'', include('static_pages.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path(r'^admin/', include(admin.site.urls)),
]
