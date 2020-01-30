## Javascript

学习网站 [w3school]("https://www.w3school.com.cn/html/html_attributes.asp")

Head First JavaScript p1-172 笔记整理

如何将JavaScript代码加入到网页：使用<script>元素

```
<script>
  setTimeOut(wakeUpUSer,5000);
  function wakeUpUSer(){
    alert("are you gong to stare at");
  }
</script>
```

#### 1.变量和值

```
var winners =2;
var losers;
```

与HTML不同，JavaScript区分大小写

#### 2.表达式

```
var total=price-(price*(discount/100));
//字符串表达式
"dear"+"reader"+","
//布尔表达式
age<14
```

#### 3.循环和选择

while,for,for in ,forEach,if...elseif

#### 4.与用户交流

创建提醒框——alert

直接写入文档——document.write

使用控制台——console.log（查看代码输出以及调试代码）

```
var message="howdy"+" "+"partner";
console.log(message)
```

直接操作文档——文档对象模型

*******

练习：

```
var word="bottles";
var count=99;
while(count>0){
   console.log(count+" "+word+" of beer on the war");
   console.log(count+" "+word+" of beer");
   console.log("take one down ,pass it around");
   count=count-1;
   if(count>0){
   console.log(count+" "+word+" of beer on the war");
   }else{
   console.log("no more "+word+" of beer on the war");
   }
}
```

******

**JavaScript代码放置：**

```
<head>
 <script>
 statement;
 </script>        //1
 <script src="mycode.js"></script>      //2
```

```
<body>
 <script>
 statement;
 </script>      //3
 <script src="mycode.js"></script>       //4，这中最后
```

添加一个src特性来指定JavaScript文件的URL

******

编写战舰游戏

第一步：创建循环并获取输入：

```
//变量声明
var loction1=3;
var loction2=4;
var loction3=5;
var guess;
var hits=0;
var guessses=0;
var isSunk=false;
//循环，只有战舰没被击沉
while (isSunk==false){
guess=prompt(“Ready ,aim,fire!(enter a number 0-6)”); //获取用户输入
}
```

**prompt:**浏览器提供的一个内置函数，可以用来获取用户输入；它会显示一个对话框，并提供让用户输入的响应的区域。

第二步：检查用户的猜测：

```
while (isSunk==false){
guess=prompt(“Ready ,aim,fire!(enter a number 0-6)”); //获取用户输入
if(guess<0||guess>6){
   alert("please enter a valid cell number");
}else{
    guessses=guesses+1;
    
    if(guess==location1||guess==location2||guess==location3){
       hits=hits+1;
       
       if(hits==3){
        isSunk=true;
        
        alert("you sank my battleship");
       }
    }
}
}
```

完整代码：

```
//变量声明
var loction1=3;
var loction2=4;
var loction3=5;
var guess;
var hits=0;
var guessses=0;
var isSunk=false;
//循环，只有战舰没被击沉
while (isSunk==false){
guess=prompt(“Ready ,aim,fire!(enter a number 0-6)”); //获取用户输入
if(guess<0||guess>6){
   alert("please enter a valid cell number");
}else{
    guessses=guesses+1;
    
    if(guess==location1||guess==location2||guess==location3){
       hits=hits+1;
       
       if(hits==3){
        isSunk=true;
        
        alert("you sank my battleship");
       }
    }
}
}
var stats="you took"+guess+" guesses to sink the battleship"+"which means your shooting accuracy was "+(3/guesses);
alerts(stats);
```

改善代码：

```var loction1=
var randomLoc = Math.floor(Math.random()*5);
var loction1=randomLoc;
var loction2=loction1+1;
var loction3=loction1+2;
```

**随机数**：Math.random();返回0-1不包括1；

要返回0-4的值：Math.random()*5

Math.floor();向下取整

要去掉小数点部分：Math.floor(Math.random()*5)；



#### 5.函数

要声明函数，使用关键字function，并在它后面指定函数名

```
function makeTea(cups,tea){
  console.log("brewing"+cups+" cups of"+tea);
}
makeTea(3,2);
```

函数还可返回值return

```
funtion bake(degrees){
 var message;
 ...
 statement;
 ...
 return message;
}
```

**全局变量和局部变量**



#### 6.数组

```
var scores={60,50,30,24,48,985,3,15,315,26,2,6};
var soluton2=scores[2];
```

创建数组[ ]

```
var flavors=["vanilla","butter","lavander","chocolate","cookies"]
```

访问数组元素

```
var flavorOfTheDay=flavors[2];
```

修改数组元素

```
flavors[3]="vanilla chocolate";
```

确定数组长度

```
var numFlavors=flavors.length;
```

tips：JS里可以用count++ ,count--



**创建空数组并在其中添加元素：**

```
//方法1
var genres=[];
genres[0]="rock";
genres[1]="ambi";
var size = genres.length;
//方法2
var genres=[];
genres.push("rock");
genres.push(ambi);
```

**使用push方法无需指定索引**



代码练习：找出得分最高的泡泡配方

```
<!doctype html>
<html lang="en">
<head>
   <meta charset="utf-8">
   <title>Bubble factory test lab</title>
   <script>
     var scores=[60,54,36,90,84,23,65];
     //找出数组中最大值
     function printAndGetHighScore(scores){
        var highScore=0;
        var output;
        for(var i=0;i<scores.length;i++){
          output ="bubble soluton#"+i+"score: "+scores[i];
          console.log(output);
          if(scores[i]>highScore){
            highScore=scores[i];
          }
        }
        return highScore;
     }
    //找出数组中最大值的索引（可能不止一个）
    function getBestResults(scores,highScore){
      var bestsolution=[];
      for(var i=0;i<scores.length;i++){
        if(score[i]==highScore){
          bestsoluton.push(i);
        }
      }
      return bestsoluton;
    }
    
    var highScore=printAndGetHighScore(scores);
    console.log("bubbles tests:" +scores.length);
    console.log("highest bubble score:" +highScore);
    
    var bestsolutions=getBestResults(scores,highScore);
    console.log("solution with the highest score:" +bestsolution);
    </script>
</head>
<body></body>
</html>
```

