from django.shortcuts import render
from .models import Post
from marketing.models import Signup

def index(request):
    featured = Post.objects.filter(featured=True)
    #latest = Post.object.order_by('-timestamp')[0:3]

    context = {
        'object_list': featured,
        #'latest': latest
    }
    return render(request, 'html/index.html', context)

def indexx(request):
    return render(request, 'html/index.html', {})

def blog(request):
    return render(request, 'html/blog.html', {})

def error(request):
    return render(request, 'html/404.html', {})

def contacts(request):
    return render(request, 'html/contacts.html', {})

def blogpost(request):
    return render(request, 'html/blog-post.html', {})

def confirm(request):
    return render(request, 'html/confirm.html', {})

def detail(request):
    return render(request, 'html/detail-restaurant.html', {})

def detail2(request):
    return render(request, 'html/detail-restaurant-2.html', {})

def detail3(request):
    return render(request, 'html/detail-restaurant-3.html', {})

def gridlistingfilterscolmap(request):
    return render(request, 'html/grid-listing-filterscol-map.html', {})

def gridlistingfilterscolstreet(request):
    return render(request, 'html/grid-listing-filterscol-openstreetmap.html', {})

def gridlistingfilterscol(request):
    return render(request, 'html/grid-listing-filterscol.html', {})

def gridlistingmasonrystreet(request):
    return render(request, 'html/grid-listing-masonry-openstreetmap.html', {})

def gridlistingmasonry(request):
    return render(request, 'html/grid-listing-masonry.html', {})

def headercart(request):
    return render(request, 'html/header-cart-top.html', {})
    
def headeruserlog(request):
    return render(request, 'html/header-user-logged.html', {})

def iconpack(request):
    return render(request, 'html/icon-pack-1.html', {})    

def index2(request):
    return render(request, 'html/index-2.html', {})

def index3(request):
    return render(request, 'html/index-3.html', {})

def index4(request):
    return render(request, 'html/index-4.html', {})

def index5(request):
    return render(request, 'html/index-5.html', {})



def help(request):
    return render(request, 'html/help.html')

def iconpack2(request):
    return render(request, 'html/icon-pack-2.html', {})

def review(request):
    return render(request, 'html/leave-review.html', {})

def listingmapopenstreetcopy(request):
    return render(request, 'html/listing-map-openstreetmap copy.html', {})

def listingmapopenstreet(request):
    return render(request, 'html/listing-map-openstreetmap.html', {})

def listingmap(request):
    return render(request, 'html/listing-map.html', {})

def order(request):
    return render(request, 'html/order.html', {})


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    return render(request, 'html/register.html', {})

def shortcodes(request):
    return render(request, 'html/shortcodes.html', {})

def submitrestaurant(request):
    return render(request, 'html/submit-restaurant.html', {})

def submitrider(request):
    return render(request, 'html/submit-rider.html', {})

def gridfullwidth(request):
    return render(request, 'html/grid-listing-filterscol-full-width.html', {})


def gridfullmasonry(request):
    return render(request, 'html/grid-listing-filterscol-full-masonry.html', {})

def about(request):
    return render(request, 'html/about.html', {})

def account(request):
    return render(request, 'html/account.html', {})

def soon(request):
    return render(request, 'html/coming_soon/index.html', {})