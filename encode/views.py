from django.shortcuts import render
import base64

# Create your views here.
def base64view(request):
    if request.method == 'POST':
        string = request['POST'].get('string')
        context = base64.b64encode(string.encode('utf-8'))
        return render(request, 'encode/base64.html', locals())
    else:
        return render(request, 'encode/base64.html')
