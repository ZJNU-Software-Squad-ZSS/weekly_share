# golang基础算法练习

用算法来练习最近学的golang

## 冒泡排序：

```go
func bubbleSort(arr []int) {
	for i := 0; i <= len(arr)-1; i++ {
		for j := i; j <= len(arr)-1; j++ {
			if arr[i] > arr[j] {
				arr[i],arr[j]=arr[j],arr[i]
			}
		}
	}
}
```



## 选择排序：

```go
func selctionSort(arr []int) {
	for i := 0; i <= len(arr)-1; i++ {
		temp := arr[i]
		for j := i; j <= len(arr)-1; j++ {
			if temp > arr[j] {
				temp = arr[j]
				arr[j] = arr[i]
				arr[i] = temp
			}
		}
	}
}
```



## 插入排序：

```go
func insertionSort(arr []int) {
	for i := 1; i <= len(arr)-1; i++ {
		if arr[i] < arr[i-1] {
			for j := 0; j <= i-1; j++ {
				if arr[i] < arr[j] {
					arr[i], arr[j] = arr[j], arr[i]
				}
			}
		}
	}
}
```



##  希尔排序：

```go
func shellSort(arr []int)  {
	incre:=len(arr)/2
	for incre>0 {
		insertionSort(arr,incre)
		incre/=2
	}

}
func insertionSort(arr []int,incre int) {
	for i := incre; i <= len(arr)-1; i+=incre {
		if arr[i] < arr[i-incre] {
			for j := 0; j <= i-incre; j+=incre {
				if arr[i] < arr[j] {
					arr[i], arr[j] = arr[j], arr[i]
				}
			}
		}
	}
}
```



## 二分查找：

```go
package main

import "fmt"

func BinarySearch(arr []int,startpoint int,endpoint int,findval int) {
	mid:=(startpoint+endpoint)/2
	if startpoint>endpoint{
		return
	}
	if (arr)[mid]==findval {
		fmt.Println(mid)
	}else if findval<(arr)[mid] {
		BinarySearch(arr,startpoint,mid-1,findval)
	}else{
		BinarySearch(arr,mid+1,endpoint,findval)
	}
}
```



## 双向链表：

```go
package main

import "fmt"

type Node struct {
	number int
	next *Node
	pre *Node
}
func append(head *Node,node *Node)  {
	temp:=head
	for {
		if temp.next==nil {
			break
		}
		temp=temp.next
	}
	temp.next=node
	node.pre=temp
}
func len(head *Node) int  {
	temp:=head
	l:=0
	if temp.next==nil{
		return l
	}
	for {
		temp=temp.next
		l++
		if temp.next==nil{
			return l
		}
	}
}
func delete(head *Node,number int)  {
	temp:=head
	if temp.next==nil {
		return
	}
	for {
		temp=temp.next
		if temp.number==number {
			if temp.next==nil {
				temp.pre.next=nil
				return
			}else {
				temp.next.pre=temp.pre
				temp.pre.next=temp.next
				return
			}
		}
		if temp.next==nil {
			return
		}

	}

}
func showList(head *Node) {
	temp:=head
	if temp.next==nil {
		return
	}
	for {
		temp=temp.next
		fmt.Print(temp.number)
		if  temp.next==nil{
			break
		}
	}
}
func main() {
	head:=&Node{}
	node1:=&Node{
		number: 1,
	}
	node2:=&Node{
		number: 2,
	}
	node3:=&Node{
		number: 3,
	}
	node4:=&Node{
		number: 4,
	}
	append(head,node1)
	append(head,node2)
	append(head,node3)
	append(head,node4)
	fmt.Println(len(head))
	showList(head)
	delete(head,2)
	showList(head)

}
```

