# Django REST framework 

## 安装

```shell
pip install djangorestframework
```

## 配置

- 在项目**setting.py**文件中注册app

  ```python
  INSTALLED_APPS = (
      ...
      'rest_framework',
  )
  ```

## Token认证

```python
from rest_framework.authentication import TokenAuthentication
```

**rest** **framework** 提供了 **authentication**认证类

可以在类视图中配置**authentication_class**属性

```python
class LoginAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = []
    def post(self,request,*args,**kwargs):
        ret={}
        return Response(ret)

```

也可以在项目**setting.py**文件中配置全局认证类

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}
```

开启**TokenAuthentication**后，rest framework检查请求中的请求头有无token认证属性

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

没有token则返回 **HTTP 401 Unauthorized** 

## 对request和response的二次封装

### request 类

REST framework的 **Request** 类扩展了标准 **HttpRequest**，允许你以与通常处理表单数据相同的方式处理具有JSON数据或其他媒体类型的请求。

### request.data

**request.data** 返回请求主体的以解析的内容。这类似于标准**request.POST**和**request.FILES**属性，除了：

它包括所有已解析的内容，包括文件和非文件输入。
它支持解析除HTTP方法之外的其他内容POST，这意味着您可以访问内容PUT和PATCH请求。
它支持REST框架的灵活请求解析，而不仅仅支持表单数据。例如，您可以像处理传入表单数据一样处理传入的JSON数据。

### request.query_params

建议使用**request.query_params**而不是Django的标准**request.GET**。这样做有助于保持代码库更加正确和明显 - 任何HTTP方法类型都可能包含查询参数，而不仅仅是GET请求。



### response类

参数：

- **data** ：响应的序列化数据
- **status** ： 响应的状态码
- **template_name** ： 模板的名称
- **headers** ： 响应头信息
- **content_type** ：响应的内容类型。一般不需要指定，框架根据前端传递的信息来指定。

## APIView

**APIView** 类它是 **Django** **View** 类的子类。与使用常规View类几乎相同，像往常一样，传入的请求被分派到适当的处理程序方法，如.get()或.post()。

### 与Django View的不同地方：

传递给处理程序方法的请求将是REST框架的Request实例，而不是**Django**的**HttpRequest**实例。
处理程序方法可以返回REST框架Response，而不是**Django** **HttpResponse**。该视图将管理内容协商并在响应上设置正确的渲染器。
任何**APIException**例外都将被捕获并调解为适当的响应。
将对传入的请求进行身份验证，并在将请求分派给处理程序方法之前运行适当的权限和/或限制检查。
