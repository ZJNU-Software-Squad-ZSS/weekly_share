# 番外——计算机硬件基础复习
从开学到现在基本都没好好学计算机硬件基础
临近期末，防火防盗防挂科
这是第二章
## 寄存器
### 通用寄存器
#### 数据寄存器
AX：常用来字节乘除和IO，分为AH,AL，AH常用来字节乘除、IO、转换、十进制运算，AL常用来字节乘除
BX：常用来转换，分为BH,BL
CX：常用来数据串操作，循环，分为CH，CL
DX：字节乘除、IO
#### 指针、变址寄存器
SP：栈顶指针，用来堆栈段的弹出和压入
BP：基址指针，用来堆栈段的随机存储
SI：源变址寄存器，存源操作数的偏移地址
DI：目标变址寄存器，存目标的偏移地址
### 段寄存器
CS：代码段寄存器
DS：数据段寄存器
SS：堆栈段寄存器
ES：附加段寄存器
### 控制寄存器
F：控制寄存器。16位，分为状态标志位和控制标志位
#### 状态标志位：存储当前运算后的结果
CF：进位标志，等于1时说明加减法的最高位产生进位/借位
PF：奇偶性标志，等于1时说明结果的低8位中有偶数个1
AF：辅助进位标志，等于1时说明结果的D3位产生进位/借位
ZF：零标志，等于1时说明运算结果为0
SF：符号标志，等于1时说明运算结果或负数的最高位为1，等于0时说明运算结果或正数的最高位为0
OF：溢出标志，等于1时说明运算结果超出表示范围
#### 控制标志位
DF：方向标志，用来循环时的方向（自增/自减）
IF：中断允许标志
TF：跟踪标志
### 额外
IP：程序指针，指向当前的运行代码

## 段
### 任意段之间的关系
段之间的位置关系可能为：重叠、排列、断开
重叠：部分重叠，完全重叠，完全重叠即段的起始地址和长度都相同
排列：一个段的起始地址+长度为另一个段的起始地址
断开：两个段之间有间距
### 逻辑地址
逻辑地址是指段的起始地址和偏移地址
如DS段起始地址为1123H，一个位置的偏移量为0004H
则上述为逻辑地址
### 实际地址
实际地址=起始地址*16+偏移地址
一个实际地址可以对应多个逻辑地址
即变化实际地址和偏移地址可得出相同的实际地址
### 段的段地址、偏移地址与操作的对应关系
|                    | 段地址 | 其他段地址 | 偏移地址 |
| ------------------ | ----- | --------- | ------- |
| 取指令              | CS    | \          | IP      |
| 堆栈操作            | SS    | \          | SP      |
| 变量                | DS    | CS、ES、SS | 有效地址 |
| 源数据串            | DS    | CS、ES、SS | SI      |
| 目标数据串          | ES    | \          | DI      |
| 作为堆栈基址使用的BP | SS    | CS、DS、ES | 有效地址 |

### 堆栈段的存储
堆栈段的栈底的地址是最大的
从栈底到栈顶(SP)逐渐减小
每层占一个字（16位）
需要注意的是SS并不指向栈底，指向栈底的上方的某个位置，不过SP的偏移量是根据SS来的，所以不用管栈底