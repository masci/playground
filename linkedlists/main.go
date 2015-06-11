package main

import (
	"fmt"
)

type Node struct {
	data int
	next *Node
}

func NewNode(data int) *Node {
	n := Node{data, nil}
	return &n
}

func hasLoop(head *Node) (has bool, meetIndex int) {
	fast := head
	slow := head
	for i := 0; fast != nil; i++ {
		if fast.next != nil {
			fast = fast.next.next
		} else {
			break
		}
		slow = slow.next

		if fast == slow {
			return true, i
		}
	}
	return false, 0
}

func main() {
	mylist := NewNode(0)
	head := mylist

	// build the list
	for i := 1; i < 50; i++ {
		n := NewNode(i)
		mylist.next = n
		mylist = n
	}

	// print the list
	for n := head; n != nil; {
		fmt.Println(n.data)
		n = n.next
	}
	has, index := hasLoop(head)
	if has {
		fmt.Println("Has loop at index", index)
	} else {
		fmt.Println("No loops here")
	}

	// corrupt the list
	var loopNode *Node
	for n := head; n != nil; {
		if n.data == 38 {
			loopNode = n
		}

		if n.next == nil {
			n.next = loopNode
			break
		}

		n = n.next
	}

	// detect the loop
	has, index = hasLoop(head)
	if has {
		fmt.Println("Has loop, pointers met at index", index)
	} else {
		fmt.Println("No loops here")
	}

	// find the loop node

	// have one pointer to the head
	left := head
	// another to the meeting point
	right := head
	for i := 0; i <= index; i++ {
		right = right.next
	}
	fmt.Println(left, right, loopNode)

	// advance until they meet
	for left != right {
		left = left.next
		right = right.next
	}

	// aaaand the loop starts here:
	fmt.Println(left, right, loopNode)
}
