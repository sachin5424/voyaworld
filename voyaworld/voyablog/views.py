from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from  voyablog.models import Blog
from voyablog.forms import ContactForm
# Create your views here.
from  voyablog.models import Blog,Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from voyablog.forms import profileForm
from django.views.generic.edit import UpdateView, CreateView

class blog(ListView):
    model = Blog
#
# def blog(req):
#     add_blog = Blog.objects.all()
#     profile = Profile.objects.all()
#     return render(req, 'voyablog/blog_list.html',{'blog':add_blog,'profile':profile})

class BlogDetail(DetailView):
    model = Blog
# def Blog_Details(request,Blog_name):
#     DetailBlog = Blog.objects.filter(Blog_name=Blog_name)
#     return render(request ,'voyablog/blog_detail.html',{'Detail':DetailBlog})

def Gallery(request):
    img = Blog.objects.all()
    return  render(request,'voyablog/gallery.html',{'img':img})


@login_required
def add_blog(request):
    Add_contact = ContactForm()
    if request.method == "POST":
        Add_contact = ContactForm(request.POST,request.FILES)
        if Add_contact.is_valid():
            Add_contact.save()
            return redirect('/voyablog/blog/')
    return render(request,'voyablog/add_blog.html',{'form':Add_contact})
# @method_decorator(login_required, name="dispatch")
# class Blog_add(CreateView):
#     model = Blog
#     fields = ['Blog_name','img','cat','dec']
#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())


# @method_decorator(login_required, name="dispatch")
# class ProfileUpdateView(UpdateView):
#     model = Profile
#     fields = ['name','Profile_image','phone_no']

@method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView):
    model = Profile

# def ProfileDetailView(request,pk):
#     object_list = get_object_or_404(Profile, id=pk)
#     return render(request,'voyablog/profile_detail.html',{'object_list'})


def ProfileUpdateView(request,pk):
    profile_edit = Profile.objects.filter(id = pk)
    form = profileForm()
    if request.method == 'POST':
        form = profileForm(request.POST)
        if form.is_valid():
            user = request.user
            form.save()
    return render(request,'voyablog/profile_form.html',{'profile':profile_edit,'form':form})
