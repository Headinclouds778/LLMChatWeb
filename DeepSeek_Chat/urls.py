# """
# URL configuration for DeepSeek_Chat project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]
from django.urls import path


from . import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path('runoob/', views.runoob),
    path('deepseek_chat/', views.deepseek_chat),
    path('login_view/', views.login_view, name='login_view'),
    path('register_view/', views.register_view, name='register_view'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
"""
urlpatterns 是 Django 约定的一个变量名，用于存放当前应用的所有 URL 路由配置
path("", views.hello, name="hello") 定义了一条 URL 路由，具体含义如下：
    ""：表示根路径，即访问应用的主页（例如 http://127.0.0.1:8000/）。
    views.hello：指定当访问根路径时，调用 views.py 文件中的 hello 视图函数。
    name="hello"：为此 URL 路由设置一个名称 hello。这样可以在 Django 应用中使用 name="hello" 来引用此 URL，方便后续在模板或代码中生成链接。
"""