from django.shortcuts import render

# Create your views here.
def home_screen_veiw(request):
    return render(request, 'BlogApp/Home.html')
