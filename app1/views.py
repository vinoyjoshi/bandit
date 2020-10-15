from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from .models import Contact

# Create your views here.
def contactPage(request):
    form = ContactForm()
    user = Contact.objects.all().values("name")
    return render(request, 'contact.html',{'contactForm':form,'user':user})

def contact_submit(request):
    if(request.method == 'POST' and request.is_ajax()):
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({'success':True},status = 200)
    return JsonResponse({'success':False},status = 400)

def get_contact_info(request):
    if(request.is_ajax()):
        username = request.GET.get('username')
	print(username)

        try:
            user = Contact.objects.get(name = username)

        except:
            return JsonResponse({'success':False},status = 400)
        print(username)
        data = {
        "username":user.name,
        "email" : user.email,
        'message' : user.message
        }
        print(data['email'])
        return JsonResponse(data)
    return JsonResponse({'success':False},status = 400)
