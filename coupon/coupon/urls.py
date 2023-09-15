"""coupon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
app_name='coupon'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('cp-admin/',views.cpadmin),
    path('Dashboard/',views.dashboard),
    path('addNewCategoryContent/',views.addCategoryContent),
    path('addCategory/',views.addCategory),
    path('search/',views.searchitem),
    path('EditCategory/<int:id>/',views.EditCategory,name='EditCategory'),
    path('addOffer/',views.addOffer),
    path('Brands/',views.brands),
    path('userlogin/',views.userlogin),
    path('offer/',views.offerpage),
    path('showpage/<int:id>/',views.showpage,name='showpage'),
    path('EditcategoryContent/<int:id>/',views.editcategorycontent,name='editcategorycontent'),
    path('logout/',views.logout_call),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
