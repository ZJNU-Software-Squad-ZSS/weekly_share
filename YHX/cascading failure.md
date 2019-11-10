在很多实际网络中，一个或几个节点的故障，会通过节点之间的耦合关系引发其他节点的故障，产生连锁反应，最终导致相当一部分节点故障甚至是整个网络的崩溃，这就是级联失效的过程。衡量网络的鲁棒性一般有两个参量：级联失效过程中的最大连通子团大小以及渗流阈值。第一个参量的值越大，则网络的鲁棒性就越好，这是比较直观的。 在网络级联失效过程中，网络整体的连通性会随之改变，当故障节点达到一定比例时，网络完全破碎， 发生由完全连通态(有序)到完全分裂态(无序)的一个非连续或者连续的相变过程。此时的故障节点比例阈值就是渗流阈值，这个参量间接地反映了网络的鲁棒性。 通过以往的研究发现，在单层网络中，网络的级联失效呈现出渗流中的连续的二级相变的现象，这很类似于水在发生气液相变时的临界现象。然而， 在相互依存网络中，由于两个网络之间存在相互依存关系，网络的级联失效表现为一级相变，这时存在一个渗流阈值，渗流阈值越小，网络的鲁棒性越高。  

用python构造渗流模型

```python
from pylab import *
from scipy.ndimage import measurements
import statsmodels.api as sm
 
L = 100
r = rand(L,L)
p = 0.4
z = r < p
    
imshow(z, origin='lower', interpolation='nearest')
colorbar()
title("Matrix")
    
lw, num = measurements.label(z)
imshow(lw, origin='lower', interpolation='nearest')
colorbar()
title("Labeled clusters")

b = arange(lw.max() + 1)
shuffle(b)
shuffledLw = b[lw]
imshow(shuffledLw, origin='lower', interpolation='nearest')
colorbar()
title("Labeled clusters")
    
area = measurements.sum(z, lw, index=arange(lw.max() + 1))
areaImg = area[lw]
im3 = imshow(areaImg, origin='lower', interpolation='nearest')
colorbar()
title("Clusters by area")
    
im3 = imshow(areaImg, origin='lower', interpolation='nearest')
colorbar()
title("Clusters by area")
sliced = measurements.find_objects(areaImg == areaImg.max())
if(len(sliced) > 0):
    sliceX = sliced[0][1]
    sliceY = sliced[0][0]
    plotxlim=im3.axes.get_xlim()
    plotylim=im3.axes.get_ylim()
    plot([sliceX.start, sliceX.start, sliceX.stop, sliceX.stop, sliceX.start], \
         [sliceY.start, sliceY.stop, sliceY.stop, sliceY.start, sliceY.start], \
         color="red")
    xlim(plotxlim)
    ylim(plotylim)
        
        
def RankOrderPlot(data):
    d=array(data)
    d = d[d>0]
    t=array(sorted(d,key=lambda x:-x))
    r=array(range(1,len(d)+1))   
    y = log(t)
    x = log(r)
    X = sm.add_constant(x, prepend=True)
    res = sm.OLS(y,X).fit()
    C,beta = res.params
    plt.plot(r,t,"o",color="b")
    plt.plot(r,exp(C)*r**beta,"r-")
    plt.xscale('log')
    plt.yscale('log')
    plt.text(max(r)/2,max(t)/100,"beta = " + str(round(beta,2)))
    print beta
 
RankOrderPlot(area)
```