# Excel文件上传

```html
前端
<!--只显示label，吧丑陋的input file 给隐藏起来，会稍微好看点-->
<label for="upload" class="subexcel">导入excel表格</label>
<!--这边 accept 表示在打开文件选择器的时候，会默认选择 .xlsx文件 -->
<input type="file" id="upload"  class="hidden" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" />

```

```js
后端
  //当文件组件的状态发生改变即用户已上传文件来了，触发回调函数
        $('#upload').change(function(){
            //获得文件
            var file = document.getElementById("upload").files;
            console.log(file);
            // //上次修改时间
            // alert(f[0].lastModifiedDate);
            // //名称
            // alert(f[0].name);
            // //大小 字节
            // alert(f[0].size);
            // //类型
            // alert(f[0].type);
            var filename=file[0].name;
            layer.confirm("确定上传 "+filename,{
                title:"上传文件",
                icon:3,
                anim:3
            },function(index){
                layer.close(index);
                $.ajax({
                    url:
                })
            })
        })
```

