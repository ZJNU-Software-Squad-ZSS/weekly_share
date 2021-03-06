# Linux

#### Linux cat命令：连接文件并打印输出到标准输出设备

cat 命令可以用来显示文本文件的内容（类似于 DOS 下的 type 命令），也可以把几个文件内容附加到另一个文件中，即连接合并文件。

```
关于此命令，有人认为写 cat 命令的人是因为喜欢猫，因此给此命令起名为“cat”，其实不然，cat 是 concatenate（连接、连续）的简写。
```

cat 命令的基本格式如下：

```
[root@localhost ~]# cat [选项] 文件名
或者
[root@localhost ~]# cat 文件1 文件2 > 文件3
```

这两种格式中，前者用于显示文件的内容，常用选项及各自的含义如表 1 所示；而后者用于连接合并文件。

cat命令常用选项及含义：

| 选项 | 含义                                                     |
| ---- | -------------------------------------------------------- |
| -A   | 相当于 -vET 选项的整合，用于列出所有隐藏符号；           |
| -E   | 列出每行结尾的回车符 $；                                 |
| -n   | 对输出的所有行进行编号；                                 |
| -b   | 同 -n 不同，此选项表示只对非空行进行编号。               |
| -T   | 把 Tab 键 ^I 显示出来；                                  |
| -V   | 列出特殊字符；                                           |
| -s   | 当遇到有连续 2 行以上的空白行时，就替换为 1 行的空白行。 |


注意，cat 命令用于查看文件内容时，不论文件内容有多少，都会一次性显示。如果文件非常大，那么文件开头的内容就看不到了。不过 Linux 可以使用PgUp+上箭头  组合键向上翻页，但是这种翻页是有极限的，如果文件足够长，那么还是无法看全文件的内容。

因此，cat 命令适合查看不太大的文件。  

#### Linux more命令：分屏显示文件内容

more 命令可以分页显示文本文件的内容，使用者可以逐页阅读文件中内容，此命令的基本格式如下：

```
[root@localhost ~]# more [选项] 文件名
```

more 命令比较简单，一般不用什么选项，对于表 1 中所列的选项，读者只需看到认识即可。

表 1 more 命令选项及含义

| 选项 | 含义                                                     |
| ---- | -------------------------------------------------------- |
| -f   | 计算行数时，以实际的行数，而不是自动换行过后的行数。     |
| -p   | 不以卷动的方式显示每一页，而是先清除屏幕后再显示内容。   |
| -c   | 跟 -p 选项相似，不同的是先显示内容再清除其他旧资料。     |
| -s   | 当遇到有连续两行以上的空白行时，就替换为一行的空白行。   |
| -u   | 不显示下引号（根据环境变量 TERM 指定的终端而有所不同）。 |
| +n   | 从第 n 行开始显示文件内容，n 代表数字。                  |
| -n   | 一次显示的行数，n 代表数字。                             |


more 命令的执行会打开一个交互界面，因此读者有必要了解一些交互命令，常用的交互命令如表 2 所示。

表 2 more 命令交互指令及功能

| 交互指令            | 功能                         |
| ------------------- | ---------------------------- |
| h 或 ？             | 显示 more 命令交互命令帮助。 |
| q 或 Q              | 退出 more。                  |
| v                   | 在当前行启动一个编辑器。     |
| :f                  | 显示当前文件的文件名和行号。 |
| !<命令> 或 :!<命令> | 在子Shell中执行指定命令。    |
| 回车键              | 向下移动一行。               |
| 空格键              | 向下移动一页。               |
| Ctrl+l              | 刷新屏幕。                   |
| =                   | 显示当前行的行号。           |
| '                   | 转到上一次搜索开始的地方。   |
| Ctrf+f              | 向下滚动一页。               |
| .                   | 重复上次输入的命令。         |
| / 字符串            | 搜索指定的字符串。           |
| d                   | 向下移动半页。               |
| b                   | 向上移动一页。               |

#### Linux head命令：显示文件开头的内容

head 命令可以显示指定文件前若干行的文件内容，其基本格式如下：

```
[root@localhost ~]# head [选项] 文件名
```

表 1 head 命令常用选项及含义：

| 选项 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| -n K | 这里的 K 表示行数，该选项用来显示文件前 K 行的内容；如果使用 "-K" 作为参数，则表示除了文件最后 K 行外，显示剩余的全部内容。 |
| -c K | 这里的 K 表示字节数，该选项用来显示文件前 K 个字节的内容；如果使用 "-K"，则表示除了文件最后 K 字节的内容，显示剩余全部内容。 |
| -v   | 显示文件名；                                                 |

注意，如不设置显示的具体行数，则默认显示 10 行的文本数据。

#### Linux less命令：查看文件内容

less 命令的作用和 more 十分类似，都用来浏览文本文件中的内容，不同之处在于，使用 more 命令浏览文件内容时，只能不断向后翻看，而使用 less 命令浏览，既可以向后翻看，也可以向前翻看。

不仅如此，为了方面用户浏览文本内容，less 命令还提供了以下几个功能：

- 使用光标键可以在文本文件中前后（左后）滚屏；
- 用行号或百分比作为书签浏览文件；
- 提供更加友好的检索、高亮显示等操作；
- 兼容常用的字处理程序（如 Vim、Emacs）的键盘操作；
- 阅读到文件结束时，less 命令不会退出；
- 屏幕底部的信息提示更容易控制使用，而且提供了更多的信息。

less 命令的基本格式如下：

```
[root@localhost ~]# less [选项] 文件名
```

表 1 less 命令选项及含义：

| 选项            | 选项含义                                               |
| --------------- | ------------------------------------------------------ |
| -N              | 显示每行的行号。                                       |
| -S              | 行过长时将超出部分舍弃。                               |
| -e              | 当文件显示结束后，自动离开。                           |
| -g              | 只标志最后搜索到的关键同。                             |
| -Q              | 不使用警告音。                                         |
| -i              | 忽略搜索时的大小写。                                   |
| -m              | 显示类似 more 命令的百分比。                           |
| -f              | 强迫打开特殊文件，比如外围设备代号、目录和二进制文件。 |
| -s              | 显示连续空行为一行。                                   |
| -b <缓冲区大小> | 设置缓冲区的大小。                                     |
| -o <文件名>     | 将 less 输出的内容保存到指定文件中。                   |
| -x <数字>       | 将【Tab】键显示为规定的数字空格。                      |

在使用 less 命令查看文件内容的过程中，和 more 命令一样，也会进入交互界面，因此需要读者掌握一些常用的交互指令，如表 2  less 交互指令及功能所示。

| 交互指令   | 功能                                   |
| ---------- | -------------------------------------- |
| /字符串    | 向下搜索“字符串”的功能。               |
| ?字符串    | 向上搜索“字符串”的功能。               |
| n          | 重复*前一个搜索（与 / 成 ? 有关）。    |
| N          | 反向重复前一个搜索（与 / 或 ? 有关）。 |
| b          | 向上移动一页。                         |
| d          | 向下移动半页。                         |
| h 或 H     | 显示帮助界面。                         |
| q 或 Q     | 退出 less 命令。                       |
| y          | 向上移动一行。                         |
| 空格键     | 向下移动一页。                         |
| 回车键     | 向下移动一行。                         |
| 【PgDn】键 | 向下移动一页。                         |
| 【PgUp】键 | 向上移动一页。                         |
| Ctrl+f     | 向下移动一页。                         |
| Ctrl+b     | 向上移动一页。                         |
| Ctrl+d     | 向下移动一页。                         |
| Ctrl+u     | 向上移动半页。                         |
| j          | 向下移动一行。                         |
| k          | 向上移动一行。                         |
| G          | 移动至最后一行。                       |
| g          | 移动到第一行。                         |
| ZZ         | 退出 less 命令。                       |
| v          | 使用配置的编辑器编辑当前文件。         |
| [          | 移动到本文档的上一个节点。             |
| ]          | 移动到本文档的下一个节点。             |
| p          | 移动到同级的上一个节点。               |
| u          | 向上移动半页。                         |