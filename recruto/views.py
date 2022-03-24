from django.http import HttpResponse

def index(request):
    name = request.GET.get("name")
    msg = request.GET.get("message")
    if name is None or msg is None:
        return HttpResponse("Parameters not found! tip :  ?name=myName&message=myMessage ")
    else:
        return HttpResponse(f"Hello {name}! {msg}!")
