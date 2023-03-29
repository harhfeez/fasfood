"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post.views import index, blog, error, contacts, blogpost, confirm, detail, detail2, detail3, gridlistingfilterscolmap,gridlistingfilterscolstreet,gridlistingfilterscol,gridlistingmasonrystreet, gridlistingmasonry, headercart,headeruserlog,help, iconpack,iconpack2, index2, index3, index4, index5, review,listingmapopenstreetcopy, listingmapopenstreet, listingmap, order, register, shortcodes, submitrider,submitrestaurant,indexx, about, account,gridfullmasonry,gridfullwidth, soon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('404/', error),
    path('contacts/', contacts),
    path('blog-post/', blogpost),
    path('confirm/', confirm),
    path('detail-restaurant/', detail),
    path('detail-restaurant-2/', detail2),
    path('detail-restaurant-3/', detail3),
    path('grid-listing-filterscol-map/', gridlistingfilterscolmap),
    path('grid-listing-filterscol-openstreetmap/', gridlistingfilterscolstreet),
    path('grid-listing-filterscol/', gridlistingfilterscol),
    path('grid-listing-masonry-openstreetmap/',gridlistingmasonrystreet ),
    path('grid-listing-masonry/',gridlistingmasonry ),
    path('header-cart-top/',headercart ),
    path('header-user-logged/',headeruserlog ),
    path('help/', help),
    path('icon-pack-1/', iconpack),
    path('icon-pack-2/', iconpack2),
    path('index-2/', index2),
    path('index-3/', index3),
    path('index-4/', index4),
    path('index-5/', index5),
    path('leave-review/', review),
    path('listing-map-openstreetmapcopy/', listingmapopenstreetcopy),
    path('listing-map-openstreetmap/', listingmapopenstreet),
    path('listing-map/', listingmap),
    path('order/', order),
    path('register/', register),
    path('shortcodes/', shortcodes),
    path('submit-rider/', submitrider),
    path('submit-restaurant/', submitrestaurant),
    path('index/', indexx),
    path('about/', about),
    path('account/', account),
    path('grid-listing-filterscol-full-masonry/', gridfullmasonry),
    path('grid-listing-filterscol-full-width/', gridfullwidth),
    path('coming_soon/index/', soon),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
 