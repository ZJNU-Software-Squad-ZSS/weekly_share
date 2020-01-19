# 2x0_Unity3D
很久以前就在看的Unity3D，一直因为项目原因搁置，寒假到了，再补一补

# 主界面下的按键操作
Z 切换中心-轴心
X 切换世界坐标系-自身坐标系 
QWERTY-左上角操作游戏的快捷键
Ctrl+S-保存场景
Ctrl+N-新建场景
滚轮-拉远拉近
滚轮按下-平移视角
双击层级面板的游戏对象/单机选中层级面板游戏对象，在场景中按F-定位对象位置
选定层级某一对象后，ctrl+shift+home-全选该对象及其上面所有对象
选定层级某一对象后，ctrl+shift+end-全选该对象及其上面所有对象
### 方向未锁定下
右键-绕自身旋转视角
Alt+左键-绕左键位置旋转视角
### 方向锁定下
右键-平移

# 预制件和模型
### 预制件
（一）、将某个对象以文件形式保存——从层级拖到项目，生成prefab文件
（二）、用来批量管理游戏对象——对预制件的部分修改会反映在对象实例上
&emsp;&emsp;1、缩放-若修改了对象实例的某一值，则该值和预制件脱离关系
&emsp;&emsp;2、添加组件
（三）、用预制件生成的对象在检查器第一栏里会多出预制件一行
&emsp;&emsp;1、select按钮-跳转到项目里对应的预制件文件
&emsp;&emsp;2、Overrides按钮-显示当前和预制件不同的组件
&emsp;&emsp;&emsp;&emsp;（1）、Revert All-还原成和预制件相同
&emsp;&emsp;&emsp;&emsp;（2）、Apply All-预制件应用成该对象实例
&emsp;&emsp;&emsp;&emsp;（3）、组件可以被单独的Apply和Revert
&emsp;&emsp;&emsp;&emsp;（4）、被应用和还原的对象实例将继续和预制件一起改变
### 模型
（一）、是一种可以有动作的对象
（二）、文件格式常为fbx
（三）、推荐模型的朝向为Z正轴，上方为Y正轴，右方为X正轴  
（四）、用模型生成的对象在检查器第一栏里会多出模型一行
&emsp;&emsp;1、select按钮-跳转到项目里对应的模型文件
&emsp;&emsp;2、Overrides按钮-显示当前和模型不同的组件

# 层级
### 父子关系
（一）子对象的Transform的结果是和父对象有关的
（二）改变父对象的Transform不改变子对象的Transform值
（三）改变父对象的Transform会使子对象发生改变
# 项目
（一）可以新建材质
（二）可以导出资源包-unitypackage文件
（三）可以导入资源包
（四）可以新建物理材质
&emsp;&emsp;1、动态摩擦力
&emsp;&emsp;2、静态摩擦力
&emsp;&emsp;3、弹力-取值区间[0,1]
&emsp;&emsp;4、摩擦组合-和其他物体发生摩擦时摩擦力的大小
&emsp;&emsp;5、反弹合并-和其他物体发生碰撞时弹力大小

# 检查器
### 组件
（一）除了Transform外其他的组件都可以被删除添加，组件是某一类型功能的集合。
（二)选中多个对象后，将展示公有的组件
1、Mesh Filter 网格过滤器-决定形状
2、Mesh Renderer 网格渲染器-决定外观展示
&emsp;&emsp;（1）、材质
&emsp;&emsp;（2）、光照和阴影
3、Terrain 地形-改变地形
&emsp;&emsp;（1）、Create Neighobr Terrain 创建相邻地形-在已有的地形四周新建一块地形
&emsp;&emsp;（2）、Raise or Lower Terrain 升高或降低地形
&emsp;&emsp;（3）、Set Height 高度设置-让地形高度趋于某一高度值
&emsp;&emsp;（4）、Smooth Height 平滑高度-让地形起伏变得平滑
&emsp;&emsp;（5）、Paint Texture 纹理填充-为地形添加纹理，纹理间可以用笔刷进行覆盖
&emsp;&emsp;（6）、Add Tree 添加树-可以添加、删除树-树笔刷缩小为1可以一颗颗添加树
&emsp;&emsp;（7）、Add Detials 添加细节-可以添加、删除草和细节网格
&emsp;&emsp;（8）、Terrain 地形设置
&emsp;&emsp;&emsp;&emsp;设置地形最基本的属性
&emsp;&emsp;&emsp;&emsp;进一步细化树和细节
&emsp;&emsp;&emsp;&emsp;地形碰撞量
&emsp;&emsp;&emsp;&emsp;风对草地的影响
&emsp;&emsp;&emsp;&emsp;设置地形大小，最大上升高度、分辨率
&emsp;&emsp;&emsp;&emsp;纹理、光照细化
4、Rigidbody 刚体-产生物理效果
&emsp;&emsp;（1）、质量-
&emsp;&emsp;（2）、阻力-
&emsp;&emsp;（3）、角阻力-旋转阻力
&emsp;&emsp;（4）、使用重力-选择物体是否受到重力作用-还是会受到别的力作用
&emsp;&emsp;（5）、是运动学的-勾选后物体的质量为无限大（且不受重力）
&emsp;&emsp;（6）、冻结位置
&emsp;&emsp;（7）、冻结旋转
5、Collider 碰撞器-有各种形状的碰撞器
&emsp;&emsp;（1）、是触发器
&emsp;&emsp;（2）、物理材质
&emsp;&emsp;（3）、其他修改大小、中心
5、Animation 动画-产生动作效果-有动画的物体z轴最好指向前方，否则用一个Object包裹
&emsp;&emsp;（1）、Animation-控制当前动作
&emsp;&emsp;（2）、Animations-显示对象所有动画