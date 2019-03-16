from django.shortcuts import render


# Create your views here.


posts = [
  {
    'author': 'jenny',
    'title': 'Blog post 1',
    'content':'first post content',
    'date_posted': 'march 16,2019'
  },
  
  {'author': 'Emma',
    'title': 'Blog post 2',
    'content':'second post content',
    'date-posted': 'march 17,2019'
  }
]



def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'home.html',context)

def about(request):
  return render(request, 'about.html')
