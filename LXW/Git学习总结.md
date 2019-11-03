# 有关git的常用指令

![](https://s2.ax1x.com/2019/10/28/KgKrLT.jpg)

[TOC]

------

#### 常用指令

- ```
  
  mkdir learngit 创建空目录
  pwd  显示当前目录
  git init 把当前目录变成git可以管理的仓库
  git add <file_name>  把文件添加到仓库（文件名要加后缀名）
  git commit -m"注释" 把文件提交到仓库
  （git add命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行git commit就可以一次性把暂存区的所有修改提交到分支。）
  
  git status 查看仓库当前的状态
  git diff <file_name>查看difference
  git log 显示从最近到最远的提交日志
  git log --pretty=online  上面那个命令的优化（显示更加清晰）
  git reset --hard HEAD^ 回退到上一个版本
  git reflog 查看命令历史
  cat <file_name> 查看文件内容
  git diff HEAD -- readme.txt 查看工作区和版本库中最新版本的区别
  ```

------

- #### 版本回退

  在Git中，用`HEAD`表示当前版本，上一个版本就是`HEAD^`，上上一个版本就是`HEAD^^`，往上100个版本写成`HEAD~100`。

- 当版本回退的时候，后悔了想恢复新版本

  - 上面的命令行窗口还没有被关掉，找到那个新版本的`commit id`是88888...`，于是就可以用（git reset --hard 8888）指定回到新版本；---主要是要找到id
  - 或者回退了版本且关掉了电脑 找不到新版本的commit id时可以使用**git reflog** 来找回commit id

------

#### 撤销修改

场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- file名`。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD <file>`，就回到了场景1，第二步按场景1操作。

场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，可以版本回退，不过前提是没有推送到远程库。

------

#### 删除文件

当你删除了一个文件的时候 ，有两个选择：

- 确实要删除该文件，那就用命令`git rm 文件名`删掉，并且`git commit -m`：

- 删错了  可以恢复误删文件到最新版本

  ```
  git checkout -- 文件名
  ```

`git checkout`其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以还原。

------

#### 远程库

```
 git remote add origin git@github.com:theskyhouse/learngit.git
 ----在本地关联远程库   origin代表远程库（默认叫法） 
```

```
$ git remote add origin https://github.com/theskyhouse/testGit2.git
//第二种方式
```

**此处出现了点问题**  用第一种方式关联远程库失败

//廖老师博客上是通过 git@github.com:michaelliao/learngit.git 关联的，经测试推送时不能成功，https的才可以，估计原因跟网络有关系。

如果已经用git@关联，又需要改成https协议，则在.git目录下的config文件中，把  url =  后面的内容改为https类型的即可，也可以通过后面提到的remove指令来解除原关联并重新关联。

```
git push -u origin master
用git push 命令 把当前分支master 推送至远程。由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送成远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令

这之后 只要本地做了提交，就可以直接 git push origin master 把本地分支推送至GitHub 更新！
```

**通过git clone 网址  克隆一个本地库**

PS：Git支持多种协议，包括`https`，但通过`ssh`支持的原生`git`协议速度最快。

------

#### 分支

- `HEAD`指向的就是当前分支，master才是指向提交的。

  （Git用`master`指向最新的提交，再用`HEAD`指向`master`，就能确定当前分支，以及当前分支的提交点）

- 提交一次 master分支前移一步，当我们要创建新的分支，新建指针dev指向master，然后HEAD指向dev，就表示当前分支在dev上。然后每提交一次，dev指针前移一步，master留在原地。（因此完成合并也很方便，只要 master指向dev就好，完成合并后可删除dev 只留下master分支---本来也就是主分支）

```
查看分支：git branch
创建分支：git branch <name>
切换分支：git checkout <name>或者git switch <name>  推荐使用switch 这样比较好理解
创建+切换分支：git checkout -b <name>或者git switch -c <name>
合并某分支到当前分支：git merge <name>(fast forward)
普通模式合并 git merge --no-ff -m"adfada" dev
删除分支：git branch -d <name>
查看分支合并图  git log --graph 

```

当Git 无法自动合并分支时，我们要手动编辑内容，然后提交。

//通常我们合并分支使用的是 Fast forward模式，但是这样一旦删除分支就会丢掉分支信息。

合并分支时，加上`--no-ff`参数就可以用普通模式合并，这样合并后历史中能看出来曾经做过合并，而`fast forward`合并就看不出来曾经做过合并。

#### Bug 分支

在分支下进行的工作，如果不commit的话，回到master，就会显示出你在分支下你添加的工作。这个时候，你在master下修改完bug提交后，正在分支进行的工作也会提交了。为了避免这个情况，你就在分支下，git stash将工作隐藏，这个时候，切换到master时候，修改了bug，提交。分支的内容由于被隐藏了不会被提交上去。

```
概括来讲步骤如下
1.我们在dev分支上进行工作（工作还未完成，没到提交的时候）
2.我们为了防止修复bug时候把进行中的分支工作提交上去，用git stash 来隐藏当前工作（也就是上面具体讲的那些）
3.确定在哪个分支上修复bug，假定在master分支上修复 我们就切换到master分支上去创建新的临时分支（用于修复bug）
4.修复好后提交，并且切回master分支，把临时分支合并过来

这里在测试中遇到了一点问题，经过验证，最终得出：
切换回dev分支后，先不stash pop 而是先git cherry-pick ***，修复dev中的bug，再pop还原工作！！！

5.回到dev分支，git stash list可以查看隐藏的工作
（git stash apply stash@{0或者别的数字} 是恢复工作 但是stash内容不删除  
可以用git stash drop来删除
git stash pop 恢复工作同时删除stash内容）

6.我们的dev分支早期也是从master中分支出来的，所以它上面也有同样的bug，我们可以利用git cherry-pick <commit>（后面加上刚才提交bug的commit id） 在当前分支复制一下刚才的提交

ps：如果丢弃一个没有合并过的分支 要用git branch -D <name> 强行删除不然会报错 

```

举个场景

设A为游戏软件 1、master 上面发布的是A的1.0版本 2、dev 上开发的是A的2.0版本 3、这时，用户反映 1.0版本存在漏洞，有人利用这个漏洞开外挂 4、需要从dev切换到master去填这个漏洞，正常必须先提交dev目前的工作，才能切换。 5、而dev的工作还未完成，不想提交，所以先把dev的工作stash一下。然后切换到master 6、在master建立分支issue101并切换. 7、在issue101上修复漏洞。 8、修复后，在master上合并issue101 9、切回dev，恢复原本工作，继续工作。

#### 多人协作

查看远程库信息 git remote -v

推送分支---git push origin <name> 把该分支上所有本地提交推送到远程库.

假设有一个朋友从远程库clone时，只能看到本地的master分支，要在dev分支上开发，就得使用git checkout -b dev origin/dev

git checkout -b dev//基于本地创建分支 

git checkout -b dev origin/dev //基于远程分支创建本地分支



**当我们要提交的和小伙伴提交的有冲突 我们可以**

1.先设置本地的dev分支与远程origin/dev分支的连接1

git branch --set-upstream-to=origin/dev dev

2.git pull抓取最新的提交

3.手动解决合并的冲突，然后再提交，再push



git rebase 变基操作 ，暂时只知道可以把分叉的提交变成直线，好看清晰一点（只对尚未推送或分享给别人的本地修改执行变基操作清理历史，从不对已推送至别处的提交执行变基操作。 因为rebase会改变提交历史记录，这会影响到别人使用这一远程仓库。）

------

#### 标签管理

```
1.创建标签--- git tag <标签名>
创建带有说明的标签---- git tag -a <标签名> -m "标签说明" commit id（不写id的话默认为HEAD）
2.查看所有标签---git tag(**标签是按字母排序的**)
3.查看标签信息--git show <标签名>

推送标签---git push origin<标签>
推送全部标签---git push origin --tags

4.删除本地标签---git tag -d <标签名>
**5.删除远程标签---git push origin :refs/tags/<标签名>
```

默认标签打在最新的commit 上 ，如果要补充标签可以找到历史中提交的commit id （git log --pretty=oneline --abbrev-commit)然后git tag <标签名> commit id

------

配置别名

```
$ git config --global alias.st status
st 表示 status
$ git config --global alias.unstage 'reset HEAD'
用unstage 表示把暂存区的东西撤销放回工作区
```