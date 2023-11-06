from django.shortcuts import render

# Create your views here.
def home(request):
    products = [('Apple',120),('Orange',80),('Mango',60),('Dragon',200)]
    context = {"items": products}
    return render(request,'myself/home.html',context)
def about(request):
    return render(request,'myself/about.html')
def contact(request):
    return render(request,'myself/contact.html')
def submited_data(request):
    if (request.method == 'get'):
        # print('form submitted')
        name=request.GET.get('txt_name')
        print(name)
        email=request.GET.get('txt_email')
        print(email)
        phone=request.GET.get('txt_mob')
        print(phone)
    return render(request,'myself/response.html')


