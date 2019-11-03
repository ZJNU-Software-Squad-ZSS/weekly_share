# 1 TensorRT安装

tensorrt的安装方式很简单，只需要注意一些环境的依赖关系就可以，截止目前tensorrt最新版本是5.0.4，参考官网安装教程，这里简单总结一下步骤

### 1.1 环境确认

确认CUDA版本是9.0或者10.0，可通过运行nvcc -V指令来查看CUDA，如果不是9.0以上，则需要先把CUDA版本更新一下nn
	cudnn版本是7.3.1，如果不满足要求，按照《Linux之cudnn升级方法》进行升级
	需安装有tensorflow，uff模块需要
### 1.2 安装pycuda

如果要使用python接口的tensorrt，则需要安装pycuda

>pip install 'pycuda>=2017.1.1'

### 1.3 下载安装包

进入下载链接
点击Download Now（需要登录英伟达账号，没有的注册一个）
选择下载的版本（最新TensorRT5）
完成问卷调查
选择同意协议
根据自己的系统版本和CUDA版本，选择安装包，如图所示（如果是完整安装，建议选择Tar File Install Packages，这样可以自行选择安装位置）


### 1.4 安装指令
```
#在home下新建文件夹，命名为tensorrt_tar，然后将下载的压缩文件拷贝进来解压
tar xzvf TensorRT-5.0.2.6.Ubuntu-16.04.4.x86_64-gnu.cuda-9.0.cudnn7.3.tar 
#解压得到TensorRT-5.0.2.6的文件夹，将里边的lib绝对路径添加到环境变量中
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/lthpc/tensorrt_tar/TensorRT-5.0.2.6/lib 
#安装TensorRT
cd TensorRT-5.0.2.6/python
#if python2
sudo pip2 install tensorrt-5.0.2.6-py2.py3-none-any.whl
#if python3
sudo pip3 install tensorrt-5.0.2.6-py2.py3-none-any.whl 
#安装UFF
cd TensorRT-5.0.2.6/uff
#if python2
sudo pip2 install uff-0.5.5-py2.py3-none-any.whl
#if python3
sudo pip3 install uff-0.5.5-py2.py3-none-any.whl 
#安装graphsurgeon
cd TensorRT-5.0.2.6/graphsurgeon
#if python2
sudo pip2 install graphsurgeon-0.3.2-py2.py3-none-any.whl
#if python3
sudo pip3 install graphsurgeon-0.3.2-py2.py3-none-any.whl
```

### 1.5 环境测试

运行python测试，导入模块不报错就表明安装正确
*需要安装好numpy、Pillow、pycuda、tensorflow等环境，如果都有可以跳过*
#### 这边有个tensorRT在win10上面安装的一个例子
>https://blog.csdn.net/yangzzguang/article/details/85570663

*我正开始刚刚学习,有想法的可以和我交流*