## MVP架构简介
在MVP架构中，UI界面和数据是被隔离的
+ M-Model层，也就是**数据层**。区别于MVC，在这里Model不仅仅是数据模型，它还负责对数据的存取操作，
例如对数据的读写，网络数据的请求
+ V-View层，也就是**视图层**。View层**只负责对数据的展示**，提供友好的界面与用户进行交互。在Android
中通常将Activity或者Fragment作为View层
+ P-Presenter层，是连接View层和Model层的桥梁，并对**业务逻辑**进行处理。在MVP中Model和View无法直
接进行交互。Presenter层从Model层获得所需要的数据，然后进行一些适当的处理后交由View层进行显示。
