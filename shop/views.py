from django.shortcuts import render

from .models import Product,Contact
from math import ceil

# Create your views here.
def index(request):
   ## products=Product.objects.all()
    #print(products)
    #n=len(products)
    #nSlides=n//4 + ceil(n/4 -(n//4))
    allProds=[]
    catprods = Product.objects.values('category', 'id')
    print(catprods)
    cats= {item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        print(prod)
        n=len(prod)
        nSlides=n//4 + ceil(n/4 -(n//4))
        allProds.append([prod,range(1,nSlides), nSlides])
    #params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    #allProds = [[products, range(1,nSlides), nSlides],
     #           [products, range(1,nSlides), nSlides]]
    params={'allProds':allProds}
    print(params)

    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method =='POST':
        print("ankesh")
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)
        contact=Contact(name=name, email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"shop/contact.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def ProdView(request, myid):
    # fetch the product using ID
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,"shop/prodview.html",{'product':product[0]})

def Checkout(request):
    return render(request,"shop/checkout.html")