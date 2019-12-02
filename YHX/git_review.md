Git会将当前版本和上一个版本进行对比，把所有差异打包到一起作为一个提交记录。

 

| 初始化                                                       | Git  init                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 添加文件到暂存区                                             | Git  add [file]                                              |
| 提交                                                         | Git  commit -m "****"                                        |
| 查看工作区状态                                               | Git  status                                                  |
| 工作区有修改，查看修改内容                                   | Git  diff [file]                                             |
| 丢弃工作区修改                                               | Git  checkout --[file]                                       |
| 丢弃暂存区修改                                               | Git  reset HEAD [file]                                       |
| 版本库删除文件                                               | Git rm  [file]                                               |
| 恢复误删或修改的文件到版本库                                 | rm情况：Git checkout -- [file]  Git rm 情况：git reset HEAD [file],git checkout --  [file] |
| 关联远程库                                                   | Git  remote add origin git@....                              |
| 第一次推送远程分支                                           | Git  push -u origin master                                   |
| 推送最新修改                                                 | Git  push origin master                                      |
| 远程克隆                                                     | Git  clone git@....                                          |
| 查看远程库                                                   | Git  remote  Git remote -v(显示更详细的信息)                 |
| 推送分支                                                     | Git  push origin bugFix                                      |
| 指定本地和远程分支连接                                       | Git branch --set-upstream-to=origin/远程分支名 本地分支名    |
|                                                              |                                                              |
|                                                              |                                                              |
| 分支合并图                                                   | Git  log --graph                                             |
| 将工作现场储藏                                               | Git  stash  Git stash list（查看）                           |
| 恢复工作现场                                                 | stash内容不删除git stash apply,删除git stash drop  stash内容删除git stash pop |
|                                                              |                                                              |
|                                                              |                                                              |
| 创建分支bugFix并切换到新分支                                 | Git  branch bugFix + git checkout bugFix = git checkout -b bugFix  Git branch(查看分支) |
| 删除分支                                                     | Git branch -d bugFix (-D强制删除为合并的分支)                |
| 更加科学的切换分支                                           | Git  switch bugFix  Git switch -c bugFix（包含了创建）       |
| 合并分支方法一：创建分支bugFix提交修改，master也提交修改，合并bugFix到master | Git  checkout -b bugFix  Git  commit  Git  checkout master  Git  commit  Git merge bugFix（master快速向前移动指向了bugFix,Fast-forward）  Git merge --no--ff -m "***"  bugFix（master首先指向了拥有两个父节点的提交记录,master包含了所有的提交记录） |
| 合并分支方法二：rebase，更加线性                             | [master]git  commit  Git  checkout -b bugFix  Git  commit  Git rebase master（此时bugFix在master的最新端,master还没更新,切换到master,git rebase bugFix,因为bugFix继承自master，所以master只是向前移动了一下） |
| 在提交树上移动                                               | Git checkout [某个提交内容]  Git log(查看提交历史)  Git reflog(查看命令历史) |
| 相对引用移动                                                 | Git  checkout HEAD^  Git  checkout HEAD~n                    |
| 移动分支                                                     | Git branch -f [当前指向的提交记录] [目标提交记录]            |
| 撤销变更                                                     | 本地分支Git reset  (--hard) [目标提交记录]  本地分支Git  revert [目标提交记录]再推送到远程仓库 |
| 整理提交记录                                                 | 将别的提交记录中的改变复制到目标提交记录Git cherry-pick c1 c2 c3 …  交互式interactive的rebase  git rebase -i [开始处提交记录]，显示对话框，勾选需要复制的提交记录 |
| 本地栈式提交                                                 | 使用git  cherry-pick [bugFix]只选择复制bug修复的提交，不选择调试控制台输出等修改提交 |
| 提交技巧#1                                                   | 在分支newImage上进行了一次提交，基于它创建了caption分支，又提交了一次，对以前的提交需要做调整  Git rebase -i  [开始处提交记录]将要修改的记录移到最前  Git commit --amend进行小修改  Git rebase -i [开始处提交记录]调回原来的顺序     pick：保留该commit（缩写:p）   reword：保留该commit，但我需要修改该commit的注释（缩写:r）   edit：保留该commit, 但我要停下来修改该提交(不仅仅修改注释)（缩写:e）   squash：将该commit和前一个commit合并（缩写:s）   fixup：将该commit和前一个commit合并，但我不要保留该提交的注释信息（缩写:f）   exec：执行shell命令（缩写:x）   drop：我要丢弃该commit（缩写:d） |