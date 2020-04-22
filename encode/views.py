from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import base64

# Create your views here.
def base64_view(request):
    if request.method == 'POST':
        if 'decode' in request.path_info:
            context = request.POST['context']
            try:
                string = base64.b64decode(context.encode('utf-8')).decode()
            except UnicodeDecodeError:
                message = "输入的字符不是base64编码！请检查字符内容！"
            except Exception:
                message = "无法转换！请检查字符内容！"
        else:
            string = request.POST['string']
            context = base64.b64encode(string.encode('utf-8')).decode()
        return render(request, 'encode/base64.html', locals())
    else:
        return render(request, 'encode/base64.html')


def ascii_view(request):
    if request.method == 'POST':
        if 'decode' in request.path_info:
            context = request.POST['context']
            try:
                # 去除十六进制标识符
                if context.lower().startswith('0x'):
                    context = context.replace('0x', '').replace('0X', '')
                string = ''
                for i in range(0, len(context), 2):
                    if i+1 < len(context):
                        string += chr(int('0x'+context[i:i+2], base=16))
                    else:
                        string += chr(int('0x'+context[i], base=16))
            except Exception:
                message = "无法转换！请检查字符内容！"
        else:
            string = request.POST['string']
            if string:
                context = '0x' + ''.join([str(hex(x).replace('0x', '')) for x in map(ord, string)])
        return render(request, 'encode/ascii.html', locals())
    else:
        return render(request, 'encode/ascii.html')


class UnicodeView(APIView):
    def get(self, request):
        return render(request, 'encode/unicode.html')

    def post(self, request):
        print(request.data)
        data = {"context": '你好'}
        return JsonResponse(data)
