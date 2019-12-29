#【Note】Docker 端口修改（VulHub使用技巧）

在用VulHub搭建测试环境的时候，docker默认端口都为8080，如何修改docker容器的映射端口呢？查了一下，做以下笔记：

## docker-compose

VulHub的镜像使用docker-compose编排，因此可以直接修改```docker-compose.yml```进行修改。e.g.  
```bash
$ more docker-compose.yml
version: '2'
services:
 web:
   image: vulhub/wordpress:4.6
   depends_on:
    - mysql
   environment:
    - WORDPRESS_DB_HOST=mysql:3306
    - WORDPRESS_DB_USER=root
    - WORDPRESS_DB_PASSWORD=root
    - WORDPRESS_DB_NAME=wordpress
# 修改此处的ports属性即可，前面的8080为映射的端口（外部访问的），80为被映射的端口
   ports:
    - "8080:80"
 mysql:
   image: mysql:5
   environment:
    - MYSQL_ROOT_PASSWORD=root
```
修改ports属性即可。


## 使用docker commit新构镜像

```docker commit```命令是把一个容器所有的文件改动和配置信息导入成一个新的docker镜像。然后我们用这个新的镜像重起一个容器（此时修改映射端口）即可。

1. 停止容器
```bash
docker stop [Container_ID_Old]
```

2. commit容器，新构镜像

命令新标签[ContainerTAG_new]

```bash
docker commit [Container_ID_Old] [image_new]:tag
```

3. 使用新构镜像重起一个容器

```bash
docker run --name [Container_tag_new] -p 8081:80 [image_new]:tag
```

注意！VulHub一些靶机服务,例如WordPress，在使用docker-compose时，是附带数据库服务的（MySQL和WP是两个容器），在当初构建容器的时候，已经规定好了服务的端口，此时再修改，会疯狂报错以及一堆问题。（需要多个容器运行的服务，还是直接修改docker-compose.yml就好)


## 修改容器配置文件hostconfig.json

如果容器已经运行了呢？我们也可以通过修改容器对应的配置文件进行修改。  
保险起见，先停止容器：```docker stop [Container_ID]``` 
Linux中，容器的配置文件位置为：
```
/var/lib/docker/containers/[Container_ID]/hostconfig.json
```
使用```sudo docker ps```命令查看容器ID，替换上述路径中的[Container_ID]，编辑修改hostconfig.json文件即可。  
> 注意：docker路径需要root权限才能查看和修改，操作时可直接sudo su切换为root用户编辑，但要“注意安全”。

但注意，最后，我们需要重启整个镜像服务，```systemctl restart docker```，这会影响到其他容器服务，不太推荐此方法。
