from django.http import HttpResponse
def handler404(request, exception):
    return HttpResponse("<h1 style='color:red'> 💀 404: The page You were Looking is not found kindly enter perfect URL 💀</h1>", status = 404)