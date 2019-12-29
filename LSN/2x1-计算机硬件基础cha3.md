# 番外——计算机硬件基础复习
总结硬件编程的各项操作
### 寻址
立即寻址： 12H 'AB' 100
寄存器寻址 BX SP
直接寻址：[1680H]  NUM、DATA  AX、AL
寄存器间接寻址：[BX/SI/BX/SP]
基址加变址寻址：[BX/BP+DI/SI] 
寄存器相对寻址：[BX+54H] ARRAY[DI]
相对基址加变址寻址：ARRAY[BX+SI] [BX+SI+ARRRAY] ARRAY[SI][BX]

#### 注意点
只有BX BP SI DI和立即数可以在[]里面，BX对应DS段寄存器，BP对应SS段寄存器
[BX] [1680H] NUM这样统称存储器操作数
### 转移指令
立即数不能给段寄存器
IP不能出现
指令、数据类型相同（8位、16位）
两个操作数不能同时为段寄存器或者存储器操作数
CS不能为目的操作数

MOV d,s s内容送到d
PUSH s s为16位寄存器或者存储器两相邻单位 s入栈
POP d d为16位寄存器或者存储器两相邻单位 出栈，d获取栈顶
XCHG d,s 通用寄存器之间或通用寄存器和存储器/累加器之间 d,s交换数据
XLAT 字节翻译指令 AL<-[BX+AL]，AL一般存储偏移地址
LEA d,s 传送地址指令 比如传送到bx,si中，存储[]里的地址
LDS SI,[DI+100AH] 将[DI+100AH]指向的4个字节，前两个送入SI，后两个送入DS
LES 和LDS相同，传的数据反一反

LAHF AH的D7 D6 D4 D2 D0设置为F的SF ZF AF PF CF
SAHF 和LAHF相反
PUSHF F数据入栈
POPF 数据传入F

IN AL,PORT 端口PORT内容传入AL（若为AH则为PORT+1)
IN AX,DX 从DX和DX+1所指的两个端口读取内容送入AX
OUT PORT AX AX内容输出PORT
OUT DX AL AL内容输出到DX所指端口
### 算数指令
ADD d,s d<-d+s
ADC d,s d<-d+s+CF 
INC d d<-d+1 (不影响CF）
SUB d<-d-s
SBB d<-d-s-CF
DEC d d<-d-1
NEG d d<-!d+1 d各位取反+1 求补码
CMP d,s d-s 只设置标志位，起比大小作用
MUL s 无符号乘法 8* 8时送入AX
IMUL s 有符号乘法 16* 16时送入DX和AX
DIV s 无符号除法AX/s 商存AL，余数存AH
IDIV s 有符号除法 DX和AX/s 商存AX，余数存DX

DAA 十进制调整 跟在ADD/ADL后，AL里数据调整为十进制
DAS 和DAA相似，跟在SUB/SBB后
AAA 和DAA相似
AAS
AAM
AAD

AND d,s 与操作
OR d,s或操作
XOR d,s 异或操作
NOT d,s 取反操作
TEST d,s 与操作，不返回给d

SAL 算数左移 SAR算数右移 有符号 改变标志位
SHL 逻辑左移 SHR 逻辑右移 有符号 改变标志位

### 串操作指令
寻址均为隐藏的
源数据串在DS中，偏移地址由SI提供
目标串在ES中，偏移由DI提供
额外的B代表8位，W代表16位

REP MOVSB 重复传送数据直到CX为0(REP)
REPE CMPSB 重复比较（会设置标志位） 直到ZF=0或CX=0(REPE)
REPNE SCASB 串搜索，源目标地址放DI,关键字放AL，重复比较直到ZF=1或CX=0（REPNE)
LODSW 从源串中取一个字送入AX，自动偏移
STOSB 从AL中送入目标串中，自动偏移
### 程序控制指令
无条件转移
CMP
段内直接 JMP ADD1
段内间接 JMP BX
段间直接 JMP FAR PTR ADD2
段间间接 JMP DWORD PTR [BX+ADD3]

CALL子程序 调用子程序——子程序出口有RET返回主程序

条件转移
JA 高于 CF=0并且ZF=0
JAE 高于或等于 CF=0 OR ZF=1
JB 低于 CF=1 AND ZF=0
JNAE 不高于也不等于 <=> JB
无符号数
A 高 B 低 N 不 E 相等
有符号数
G 大 L 小 N 不 E 相等
