# WebBench 网站性能测试工具

## 安装：

这个软件只能在linux下使用

```shell
# 准备环境
yum install -y gcc ctags

# 下载软件包
wget http://www.ha97.com/code/webbench-1.5.tar.gz

# 解压安装包
tar -xvf  webbench-1.5.tar.gz

# 创建安装文件夹
mkdir /usr/local/man
mkdir /usr/local/man/man1

# 运行安装
make &&make install
```

## 命令查看

```
[root@node1 data]# webbench --help
webbench [option]... URL
  -f|--force               Don't wait for reply from server.
  -r|--reload              Send reload request - Pragma: no-cache.
  -t|--time <sec>          Run benchmark for <sec> seconds. Default 30.
  -p|--proxy <server:port> Use proxy server for request.
  -c|--clients <n>         Run <n> HTTP clients at once. Default one.
  -9|--http09              Use HTTP/0.9 style requests.
  -1|--http10              Use HTTP/1.0 protocol.
  -2|--http11              Use HTTP/1.1 protocol.
  --get                    Use GET request method.
  --head                   Use HEAD request method.
  --options                Use OPTIONS request method.
  --trace                  Use TRACE request method.
  -?|-h|--help             This information.
  -V|--version             Display program version.
```

## 基本使用方法

```shell
# 参数 -c表示并发数，-t表示测试时间
webbench -c 10 -t 30 http://www.baidu.com/
```

## 流程

![](https://ocean-oss.oss-cn-beijing.aliyuncs.com/img/20200119203746.png)