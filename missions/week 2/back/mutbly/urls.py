"""mutbly URL Configuration

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
from django.urls import path, include
import mutbly.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace= 'accounts')), 
    path('cart/', include('cart.urls', namespace='cart')),
    path('', mutbly.views.index, name='index'),
    path('items/<int:id>/', mutbly.views.show, name = 'show'),
    path('search/', mutbly.views.search, name='search'),
    path('items/<int:id>/questions/', mutbly.views.QuestionView.create, name='question_create'),
    path('items/<int:id>/questions/<int:cid>', mutbly.views.QuestionView.delete, name='question_delete'),
    path('social_accounts/', include('allauth.urls')),
    # path('social_accounts/', include('accountapp.urls')),
    # path('update_item/', mutbly.views.updateItem, name='update_item'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

