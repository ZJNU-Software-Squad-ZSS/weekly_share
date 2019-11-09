# TensorRT在python中的接口使用
## 2 Python初始化TensorRT
* 创建IBuilder对象去优化网络（创建后可生成序列化文件）
* 创建IRuntime对象去执行优化网络（从序列化文件导入） 
以下代码显示了如何实现日志记录接口。 在这种用例中，他已经禁止了信息性消息，只打印警告性和错误性消息。简单地调用trt.infer.ConsoleLogger获得句柄即可。
   >G_LOGGER = trt.infer.ConsoleLogger(trt.infer.LogSeverity.ERROR)
## 3 Python创建网络定义
使用TensorRT首先需要将训练好的模型转换成TensorRT的表示形式，然后再构建优化的运行时。 
　　下面将在Python中使用两种方式导入模型，一种是通过解析器导入，一种从框架导入现有模型。

#### 3.1 Python使用解析器导入模型
　　要使用Python 解析器API导入模型，你需要执行以下主要步骤： 
　　　1.创建构建器和网络 
　　　2.针对指定格式，创建相应的解析器 
　　　3.使用解析器解析导入的模型并填充网络。 
　　先创建构建器（作为网络工厂），再创建网络。 不同的解析器有不同的标记网络输出机制。

#### 3.2 使用Python导入Caffe模型
　　这个例子介绍使用NvCaffeParser和Python API直接导入Caffe模型

###### 1.导入TensorRT包和其他包
>Import tensorrt as trt

###### 2.定义数据类型，这里使用float32

>datatype = trt.infer.DataType.FLOAT

###### 3.传入所需文件路径

>MODEL_PROTOTXT = ‘/data/mnist/mnist.prototxt’
CAFFE_MODEL = ‘/data/mnist/mnist.caffemodel’

###### 4.创建构建器

>builder = trt.infer.create_infer_builder(G_LOGGER)

###### 5.创建网络

>network = builder.create_network()

###### 6.创建解析器

>parser = parsers.caffeparser.create_caffe_parser()

###### 7.解析Caffe网络和权重，然后生成TensorRT网络

>blob_name_to_tensor = parser.parse(CAFFE_MODEL,MODEL_PROTOTXT,network,datatype)

* 输出是填充好的TensorRT网络（作为参数传递给解析器）。 此外，解析器返回blob_name_to_tensor - 一个包含从张量名称到ITensor对象的映射表。
#### 3.3 使用Python导入TensorFlow模型
　　这个例子教你使用NvCaffeParser和Python API直接导入TensorFlow模型，例子在/tensorrt/examples/tf_to_trt中，更多信息，请参考示例tf_to_trt。 
###### 1.导入TensorRT和UFF解析器的Python包：

>import tensorrt as trt
from tensorrt.parsers import uffparser

###### 2.使用UFF转换器将冻结图转换为UFF文件。 

>import uff
uff.from_tensorflow_frozen_model(frozen_file, ["fc2/Relu"])

###### 3.使用UFF解析器将UFF文件解析为TensorRT网络，并指定输入节点（维度）和输出节点：

>parser = uffparser.create_uff_parser()
 
* 这可以通过以下方式完成：

>parser.register_input("Placeholder", (1, 28, 28), 0)
parser.register_output("fc2/Relu")

***注：TensorRT默认输入张量是CHW，从TensorFlow（默认NHWC）导入时，确保输入张量也是CHW，如果不是先转换为CHW。*** 
###### 4.创建引擎
```
engine = trt.utils.uff_to_trt_engine(G_LOGGER,
                                    uff_model,
                                    parser,
                                    MAX_BATCHSIZE,
                                    MAX_WORKSPACE)
 ```
#### 3.4使用Python导入ONNX模型
* 这是一个展示如何使用NvOnnxParser和Python API直接导入ONNX模型。
###### 1.导入TensorR包：

>import tensorrt as trt

###### 2.导入NvOnnxParser包并将ONNX模型直接转换为TensorRT网络。sample_onnx 的Python示例是通过配置文件将用户参数传递给解析器对象。

>from tensorrt.parsers import onnxparser
apex = onnxparser.create_onnxconfig()

###### 3.解析图像分类模型，然后生成TensorRT引擎进行推理。这里我们解析用户输入参数并生成配置对象：
```
apex.set_model_filename("model_file_path")
apex.set_model_dtype(trt.infer.DataType.FLOAT)
apex.set_print_layer_info(True) # Optional debug option
apex.report_parsing_info() # Optional debug option
```

　*提高或降低调试输出信息的冗余级:*

>apex.add_verbosity()
apex.reduce_verbosity()

　*或者直接设置冗余级别:*

>apex.set_verbosity_level(3)

###### 4.创建并配置对象后，然后创建解析器，并从配置对象中检索参数并解析输入模型文件：

>trt_parser = onnxparser.create_onnxparser(apex)
data_type = apex.get_model_dtype()
onnx_filename = apex.get_model_file_name()
###### 5.解析模型文件，生成TensorRT网络：
```
trt_parser.parse(onnx_filename, data_type)
retrieve the network from the parser
trt_parser.convert_to_trt_network()
trt_network = trt_parsr.get_trt_network()
```
