from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from voyablog.models import Blog
from travel.forms import ContactForm
from travel.models import PackagesAdd, tranding_package, PackagaesState, PackagaesCountry,tranding_package,special_package


# Create your views here.
# class home_view(ListView):
#     model = PackagesAdd

def home_view(request):
    tranding_packages = tranding_package.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all().order_by('-id')[:3]
    special_packages = special_package.objects.all().order_by('-id')[:3]
    parm={
        'tranding_packages':tranding_packages,
        'blogs':blogs,
        'special_packages':special_packages
    }
    return render(request, 'travel/packagesadd_list.html',parm)


def packages(request):
    add_packages = None
    quary = request.GET.get('quary')
    if quary:
        add_packages = PackagesAdd.objects.filter(package_place__icontains=quary)
    else:
        add_packages= PackagesAdd.objects.all()

    return render(request, 'travel/packages.html', {'add_packages': add_packages})


def packagesDetail(request,slug):
    P_Details = get_object_or_404(PackagesAdd,slug=slug)
    qs=P_Details.State.id
    print(qs)
    related_package = PackagesAdd.objects.filter(State__id=qs).order_by('id')[:3]
    parm={
        'Details': P_Details,
        'related_package':related_package

    }
    return render(request, 'travel/packagesdetails.html', parm)


def contact(request):
    Add_contact = ContactForm()
    if request.method == "POST":
        Add_contact = ContactForm(request.POST)
        if Add_contact.is_valid():
            Add_contact.save()
            return redirect("/home/")
    return render(request, 'travel/contact.html', {'Add_contact': Add_contact})


def about(request):
    t = PackagesAdd.objects.all()
    return render(request, 'travel/about-us.html', {'t': t})



# def hello(request):
#     Country = PackagaesCountry.objects.all()

#     Add_Pack = PackagesAdd.objects.all()

#     return render(request, 'voya/exp.html',
#                   {"Country": Country, "State": PackagaesState.objects.all(), "Add_Pack": Add_Pack})
