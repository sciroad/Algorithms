package main

import "fmt"

func gridlandMetro(n int32, m int32, k int32, track [][]int32) int32 {
	// Write your code here
	resultArr := make([][]int32, n, m)

	mark := func(r, c1, c2 int32) {
		for i := c1; i <= c2; i++ {
			resultArr[r][i] = 0
			fmt.Println(i)
		}
	}
	var result int32 = 0
	for _, arr := range resultArr {
		for i := 0; i < len(arr); i++ {
			arr[i] = 1
		}
	}
	fmt.Println(resultArr)
	for _, v := range track {
		mark(v[0]-1, v[1]-1, v[2]-1)
	}
	for _, arr := range resultArr {
		for _, v := range arr {
			result += v
		}
	}
	return result

}

func main() {
	matrix := [][]int32{
		{2, 1, 5}, {2, 2, 4}, {2, 8, 8},
	}
	n := int32(2)
	m := int32(9)
	k := int32(3)
	println(gridlandMetro(n, m, k, matrix))
}
