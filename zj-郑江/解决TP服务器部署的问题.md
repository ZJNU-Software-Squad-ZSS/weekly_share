# 解决TP服务器部署的问题

## 阿里云注册二级域名（TP项目根域名问题）

```
1. 进入域名解析页面
	https://dns.console.aliyun.com/?spm=a2c1d.8251892.aliyun_sidebar.10.543c5b76cBg5ng#/dns/domainList
	
2. 点击主域名 zhengjiang.online

3. 点击添加记录

4. 主机记录填写：{二级域名}.zhengjiang.online
   记录值填写服务器IP地址 ：106.14.173.104
   
5. 点击确定之后，ping {二级域名}.zhengjiang.online，ping的通就说明二级域名解析成功

6. nginx服务器添加一个server，用来把二级域名指向对应的项目
	 server {
            listen       80 ;
            server_name  ocean.zhengjiang.online;
            root         /usr/share/nginx/html/myCompany/public/;

            # Load configuration files for the default server block.
            include /etc/nginx/default.d/*.conf;

          location / {
    	  index index.php index.html index.htm; #默认首页
    	  if (!-e $request_filename) {
               rewrite ^(.*)$ /index.php?s=$1 last;
               break;
             }
            }
    	location ~ \.php/ {
               if ($request_uri ~ ^(.+\.php)(/.+?)($|\?)) { }
               fastcgi_pass 127.0.0.1:9000;
               include fastcgi_params;
               fastcgi_param SCRIPT_NAME     $1;
               fastcgi_param PATH_INFO       $2;
               fastcgi_param SCRIPT_FILENAME $document_root$1;
            }
            location ~ \.php$ {
                fastcgi_pass 127.0.0.1:9000;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
            }

    	location ~\.(jpeg|jpg|png)$ {
            #设置缓存时间（d:天；h:小时）
            expires 1h;
        }
            error_page 404 /404.html;
                location = /40x.html {
            }

            error_page 500 502 503 504 /50x.html;
                location = /50x.html {
            }
        }
        
7. 重启nginx服务
	systemctl restart nginx
	OK
```

目前的nginx配置文件内容(包括https以及二级域名配置)

```
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;     #配置用户或组
worker_processes auto;  #允许生成的进程数，默认为1
error_log /var/log/nginx/error.log; #指定日志路径
pid /run/nginx.pid;     #指定nginx进程运行文件存放位置

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024; #最大链接数，默认为512
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"'; #自定义格式

    access_log  /var/log/nginx/access.log  main;    #main为自定义的日志文件格式

    sendfile            on; #允许以sentfile方式传输文件，默认为off，可以在http块，server块，location块
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65; #连接超时时间，默认75s
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;  #文件扩展名于文件类型映射表
    default_type        application/octet-stream;   #默认文件类型，默认为text/plain

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;
    #配置gzip压缩
    gzip on;
    #http的协议版本
    gzip_http_version 1.0;
    #如果是IE的话，就关闭压缩
    gzip_disable "MSIE [1-6].";
    #需要压缩的文件格式
    gzip_types image/jpeg;

    #每个虚拟主机的共用的根目录文件

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html/;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

      location / {
	  index index.php index.html index.htm; #默认首页
	  if (!-e $request_filename) {
           rewrite ^(.*)$ /index.php?s=$1 last;
           break;
         }
        }
	location ~ \.php/ {
           if ($request_uri ~ ^(.+\.php)(/.+?)($|\?)) { }
           fastcgi_pass 127.0.0.1:9000;
           include fastcgi_params;
           fastcgi_param SCRIPT_NAME     $1;
           fastcgi_param PATH_INFO       $2;
           fastcgi_param SCRIPT_FILENAME $document_root$1;
        }
        location ~ \.php$ {
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            include fastcgi_params;
        }

	location ~\.(jpeg|jpg|png)$ {
        #设置缓存时间（d:天；h:小时）
        expires 1h;
    }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

    server {
            listen       80 ;
            server_name  ocean.zhengjiang.online;
            root         /usr/share/nginx/html/myCompany/public/;

            # Load configuration files for the default server block.
            include /etc/nginx/default.d/*.conf;

          location / {
    	  index index.php index.html index.htm; #默认首页
    	  if (!-e $request_filename) {
               rewrite ^(.*)$ /index.php?s=$1 last;
               break;
             }
            }
    	location ~ \.php/ {
               if ($request_uri ~ ^(.+\.php)(/.+?)($|\?)) { }
               fastcgi_pass 127.0.0.1:9000;
               include fastcgi_params;
               fastcgi_param SCRIPT_NAME     $1;
               fastcgi_param PATH_INFO       $2;
               fastcgi_param SCRIPT_FILENAME $document_root$1;
            }
            location ~ \.php$ {
                fastcgi_pass 127.0.0.1:9000;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
            }

    	location ~\.(jpeg|jpg|png)$ {
            #设置缓存时间（d:天；h:小时）
            expires 1h;
        }
            error_page 404 /404.html;
                location = /40x.html {
            }

            error_page 500 502 503 504 /50x.html;
                location = /50x.html {
            }
        }




server {
 listen 443;
 server_name localhost;
 ssl on;
 root         /usr/share/nginx/html;    #项目目录
 index index.html index.htm;
 ssl_certificate   cert/a.pem;
 ssl_certificate_key  cert/a.key;
 ssl_session_timeout 5m;
 ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
 ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
 ssl_prefer_server_ciphers on;
 location / {
 	  index index.php index.html index.htm; #默认首页
 	  if (!-e $request_filename) {  #很重要，没了它框架路由无法成功
            rewrite ^(.*)$ /index.php?s=$1 last;
            break;
          }
         }

 	location ~ .php$ {
 	 fastcgi_pass 127.0.0.1:9000;
 	 fastcgi_index index.php;
 	 fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
 	 include fastcgi_params;
 	}

 	location ~\.(jpeg|jpg|png)$ {
         #设置缓存时间（d:天；h:小时）
         expires 1h;
     }

         error_page 404 /404.html;
             location = /40x.html {
         }

         error_page 500 502 503 504 /50x.html;
             location = /50x.html {
         }
}
# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2 default_server;
#        listen       [::]:443 ssl http2 default_server;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers HIGH:!aNULL:!MD5;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        location / {
#        }
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}


```

## TP5 模板文件找不到

```
tp5中在引入模板时，会去找当前控制器名小写的模板名，在使用驼峰命名法时，在nginx上就会出现找不到模板文件的错误。
例如：控制器为adminAdd，那么模板文件为adminAdd.html，但是tp就会去找adminadd.html，就会找不到模板文件。


 // 是否自动转换URL中的控制器和操作名
'url_convert'            => false,

配置项中的"url_convert"参数默认为True，会将url控制器名转换为小写形式，当使用驼峰命名法时，adminAdd会被转化为adminadd，从而造成模板文件找不到，这时只需要将"url_convert"的值置为False即可，不自动转换大小写。
我猜想自动转换大小写的作用是，统一管理模板，不管你的控制器叫什么，我都把你转化成小写，比较好管理。
但是这对于像linux这种大小写区分的操作系统来说，就会爆出很多错误。

解决方案：
1. “url_convert”配置项改为false，在写代码的时候任然可以使用“小驼峰法”。

2. 下次在写模板名的时候，注意模板名要全部小写。
```

