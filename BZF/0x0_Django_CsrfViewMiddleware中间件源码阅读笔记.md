## Django CsrfViewMiddleware中间件源码阅读笔记

## CSRF：

CSRF攻击的全称是跨站请求伪造（ cross site request forgery)，是一种对网站的恶意利用，尽管听起来跟XSS跨站脚本攻击有点相似，但事实上CSRF与XSS差别很大，XSS利用的是站点内的信任用户，而CSRF则是通过伪装来自受信任用户的请求来利用受信任的网站。你可以这么理解CSRF攻击：攻击者盗用了你的身份，以你的名义向第三方网站发送恶意请求。 CRSF能做的事情包括利用你的身份发邮件、发短信、进行交易转账等，甚至盗取你的账号

## Token：

Token机制是防止csrf攻击的一种常用手段。 系统开发人员可以在HTTP请求中以参数的形式加入一个随机产生的token，并在服务端进行token校验，如果请求中没有token或者token内容不正确，则认为是CSRF攻击而拒绝该请求。

---



## Django开启csrf认证的方法:

Django内置了开启csrf token认证的中间件**django.middleware.csrf.CsrfViewMiddleware**

可以在项目文件**setting.py**中配置它

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #csrf 认证中间件
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

配置后默认开启全局csrf认证

Django还提供了相应的装饰器来应对单个视图函数或类视图需要**局部启动csrf认证**或**局部禁用csrf认证**的情况

```python
from django.views.decorators.csrf import csrf_protect,csrf_exempt
```

类视图情况特殊，需要使用装饰器**method_decorator**帮助实现

将装饰器**method_decorator**配置在dispatch函数上，dispatch函数使用父类View的实现

```python
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import HttpResponse
from django.views import View
class TestView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET，ok')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post，ok')
```

## 中间件django.middleware.csrf.CsrfViewMiddleware实现分析：

**CsrfViewMiddleware中间件主要结构：**

[![**CsrfViewMiddleware中间件结构]( https://user-images.githubusercontent.com/48949693/68041384-673c8d80-fd0b-11e9-920c-762fb0f2856e.jpg )

Django中间件定义了各种钩子函数（**middleware hooks**）来实现中间件的各种行为。**middleware hooks**在**请求**或**响应**到达特定位置时自动调用。**CsrfViewMiddleware**中的下列函数就是常用的几种之一

**process_request()**，**process_view()**，**process_response()**

### process_request()：

```python
    def process_request(self, request):
        csrf_token = self._get_token(request)
        if csrf_token is not None:
            # Use same token next time.
            request.META['CSRF_COOKIE'] = csrf_token
```

**process_request()**作为最先被调用的钩子函数，调取了**_get_token()**函数，获取了**token**，并将这个**token**放到了**request**的**meta**字典里,前提是**_get_token()**返回了**token**。

在**_get_token()**函数中只是对服务器存贮**token**的位置进行了判断，如果是使用**cookie**存贮**token**，就从**cookie**中调取，如果是用**session**存贮就从**session**中调。

### process_view():

在**process_request()**后，**视图函数**执行前被调用。

**process_view()**中的源码很长，这里就不贴了。主要功能有以下几个：

- 判断**request**对象中**csrf_processing_done**属性是否存在。如果存在，则不执行。
- 判断即将执行的视图函数是否被装饰器**csrf_exempt**装饰。如果被装饰，则不执行。
- 判断请求的类型（**request.method**）是否属于不需要csrf认证的类型（GET，HEAD等）。如果属于，则不执行。
- HTTPS的相关处理
- 将**process_request()**中放入**request.META**字典中的**token**与**request**请求中携带的**token**进行比较，一样则调用**_accept()**函数，不一样则调用**_reject()**函数

#### _accept()：

```python
    def _accept(self, request):
        # Avoid checking the request twice by adding a custom attribute to
        # request.  This will be relevant when both decorator and middleware
        # are used.
        request.csrf_processing_done = True
        return None
```

这里将**csrf_processing_done**属性写入**request**后退出了钩子函数

#### _reject()：

```python
    def _reject(self, request, reason):
        response = _get_failure_view()(request, reason=reason)
        log_response(
            'Forbidden (%s): %s', reason, request.path,
            response=response,
            request=request,
            logger=logger,
        )
        return response
```

这里设置了认证失败后**response**的具体内容,并返回响应

### process_response():

这个钩子函数在响应发送前调用，如果这个响应已经包含了**token**或并没有使用**cookie**存贮**token**则不做修改直接释放响应。反之则为这个**response**加上**token**

```python
    def process_response(self, request, response):
        if not getattr(request, 'csrf_cookie_needs_reset', False):
            if getattr(response, 'csrf_cookie_set', False):
                return response

        if not request.META.get("CSRF_COOKIE_USED", False):
            return response

        # Set the CSRF cookie even if it's already set, so we renew
        # the expiry timer.
        self._set_token(request, response)
        response.csrf_cookie_set = True
        return response
```

#### _set_token():

```python
  def _set_token(self, request, response):
        if settings.CSRF_USE_SESSIONS:
            if request.session.get(CSRF_SESSION_KEY) != request.META['CSRF_COOKIE']:
                request.session[CSRF_SESSION_KEY] = request.META['CSRF_COOKIE']
        else:
            response.set_cookie(
                settings.CSRF_COOKIE_NAME,
                request.META['CSRF_COOKIE'],
                max_age=settings.CSRF_COOKIE_AGE,
                domain=settings.CSRF_COOKIE_DOMAIN,
                path=settings.CSRF_COOKIE_PATH,
                secure=settings.CSRF_COOKIE_SECURE,
                httponly=settings.CSRF_COOKIE_HTTPONLY,
                samesite=settings.CSRF_COOKIE_SAMESITE,
            )
            # Set the Vary header since content varies with the CSRF cookie.
            patch_vary_headers(response, ('Cookie',))
```

这里直接生成了新的**token**并放入了**response**中

## Reference

- https://www.jianshu.com/p/67408d73c66d
- https://docs.djangoproject.com/zh-hans/2.1/
