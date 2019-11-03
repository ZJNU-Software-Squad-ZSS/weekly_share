# 前端开发
**前端开发学习路线** 先放一张web开发者学习路线摘自菜鸟编程  
![前端开发路线](https://www.runoob.com/wp-content/uploads/2018/01/weblearnpath2.png)  

因为在之前的项目开发中，都会涉及到排版的问题所以我先总结一下
>* float
>* display 
## float  
float属性可能是我们在制作网页前端的时候用到的最多的css属性，尽管常用值就只有left、right、none,但是不见得我们真的了解它的特性。在css中设置float属性可以使元素脱离标准文档流（指的是HTML页面在没有任何css布局的情况下，块级元素从上到下，行内元素从左到右依次排序的情况）,但在最开始的时候,float属性只是为达到文字环绕。  
### 1.子元素添加float属性会造成父元素的高度塌陷
上个html码清晰一点
```html
<div class="father">
   <div class="box1"></div>
   <div class="box2"></div>
</div>

```
再上一个css码
```css
div{
     outline:1px solid black;
}
.father{
    width: 300px;
    background-color: aliceblue;
    text-align:center;
    line-height:150px;
    color:red;
}
.box1{
     height:150px;
     width:150px;
     background-color: antiquewhite;
    }
.box2{
     height:150px;
     width:150px;
     background-color:beige;
    }
```
你会发现呈现出来的结果是这样的  

![效果](https://images2017.cnblogs.com/blog/1216287/201708/1216287-20170827194612964-1813959962.png)  

这很正常，但是你在box1中或者box2中都设置了float:left之后，你会发现效果是这样的  

![效果](https://images2017.cnblogs.com/blog/1216287/201708/1216287-20170827195417574-806176804.png)  
乍看一下好像没有毛病老铁，但是通过检查工具你会发现父元素的高度塌陷了  

![效果](https://images2017.cnblogs.com/blog/1216287/201708/1216287-20170827195556308-323921540.png)  

so你肯定会问你bb这么久，父元素塌陷对我们到底有什么影响？扎心了老铁，**父亲元素高度塌陷，会让所有标准流中的元素位置上移，导致整个页面布局的混乱。**

所以这里给出几种解决的方法
>* 1、给父元素设置overflow:hidden;
>* 2、给父元素设置一个合适的高度
>* 3、在浮动元素的末尾增加一个空的div设置clear:both;

方法一中为什么设置了overflow属性就能够解决浮动带来的这个效果呢，是因为构成了BFC
BFC的定义为(block formatting context)意思就上格式化上下文。BFC的表现原则就是：如果一个元素具有BFC，那么它内部的子元素，都不会影响外部元素，结合上例来说，只要我父元素上了BFC，你子元素再怎么骚都翻不起什么大浪。  
触发BFC的条件是：  
1.HTML根元素  
2.float的值不为none  
3.overflowd的值为auto、scroll或者hidden  
4.display的值为table-cell,table-caption and inline-block中的任意一个  
5.position的值不为relative and static  

---
扎心了老铁，到点了，要去背单词了，下次整理










