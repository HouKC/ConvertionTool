from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import base64
from .utils import string2unicode_string, unicode_string2string
from .utils import string2ascii_10_string, string2ascii_16_string
from .utils import ascii_string2string, unicode_string2ascii_10_string
from .utils import unicode_string2ascii_16_string, ascii_string2unicode_string

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


class UnicodeView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method_func = {     # 方法名对应的处理函数名
            "中文": {
                "中文 转 Unicode": string2unicode_string,
                "中文 转 ASCII(十进制)": string2ascii_10_string,
                "中文 转 ASCII(十六进制)": string2ascii_16_string,
            },
            "Unicode": {
                "Unicode 转 中文": unicode_string2string,
                "Unicode 转 ASCII(十进制)": unicode_string2ascii_10_string,
                "Unicode 转 ASCII(十六进制)": unicode_string2ascii_16_string,
            },
            "ASCII": {
                "ASCII 转 中文": ascii_string2string,
                "ASCII 转 Unicode": ascii_string2unicode_string,
            },
        }

    def get(self, request):
        method_dict = {}
        for key, value in self.method_func.items():
            method_dict[key] = list(value.keys())
        return render(request, 'encode/unicode_ascii.html', {"method_dict": method_dict})

    def post(self, request):
        string = request.data['string']
        method = request.data['encode_method']
        data = {"status": "403"}
        if string and method:
            for key, value in self.method_func.items():
                if method in value.keys():
                    data["context"] = self.method_func[key][method](string)
                    if data["context"]:
                        data["status"] = "200"
                    break
        return JsonResponse(data)
