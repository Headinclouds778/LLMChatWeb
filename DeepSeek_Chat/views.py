from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.utils.timezone import now
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import ChatHistory
from django.contrib.auth.decorators import login_required

def hello(request):
    return HttpResponse("Hello world ! ")


from django.shortcuts import render

# def runoob(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)
#使用 render 来替代之前使用的 HttpResponse。render 还使用了一个字典 context 作为参数
#context 字典中元素的键值 hello 对应了模板中的变量 {{ hello }}
def runoob(request):
    views_list = ["Hello", "motherfucking", "world!"]
    return render(request, "runoob.html", {"views_list": views_list})

@login_required(login_url='/login_view/')
def deepseek_chat(request):
    return render(request, "deepseek_chat.html")

# 渲染登录页面
def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('/deepseek_chat/')  # 如果用户已经登录，重定向到首页
    return render(request, 'login.html')

# 渲染注册页面
def register_view(request):
    return render(request, 'register.html')

# 注册用户
@api_view(['POST'])
def register(request):
    print("Register API called")
    username = request.data.get("username")
    password = request.data.get("password")

    # 检查用户名和密码是否为空
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    # 检查用户是否存在
    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # 密码加密存储
    user = User(username=username, password=make_password(password))
    user.save()

    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

# 登录用户
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    # 检查用户名和密码是否为空
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # 验证密码
    if not check_password(password, user.password):
        return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

    # 登录成功，创建 session
    auth_login(request, user)  # 启动 Django session，前端可以根据 session 管理登录状态

    return Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)

# 登出用户
@api_view(['POST'])
def logout(request):
    auth_logout(request)
    return render(request, 'login.html')


def save_chat(request):
    if request.method == 'POST':
        # 从 POST 请求中获取聊天内容
        html_content = request.POST.get('html_content', '')

        # 获取当前用户
        user = request.user

        # 创建并保存聊天记录
        chat = ChatHistory.objects.create(
            user=user,
            timestamp=now(),
            html_content=html_content
        )
        chat.save()

    # 保存成功后，重定向到 deepseek_chat 界面
    return redirect('deepseek_chat')  # 'deepseek_chat' 是 URL 路径的名称