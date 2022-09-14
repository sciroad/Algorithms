package hard

import "fmt"

func matrixRotation(matrix [][]int32, r int32) {
	min := func(a, b int) int32 {
		if a < b {
			return int32(a)
		}
		return int32(b)
	}
	var l int32 = int32(min(len(matrix[0])/2, len(matrix)/2))
	row := int32(len(matrix))
	col := int32(len(matrix[0]))
	for i := int32(0); i < l; i++ {
		m := row - 2*i - 2
		n := col - 2*i - 2
		times := r % (2 * (m + n))
		rotate(matrix, i, row-i-1, i, col-i-1, times)
	}
	fmt.Println(matrix)

}

func rotate(matrix [][]int32, top, bottom, left, right, times int32) [][]int32 {
	fmt.Println(top, bottom, left, right, times)
	if (top == bottom && right == left) || times == 0 {
		return matrix
	}
	for i := int32(0); i < times; i++ {
		prev := matrix[top][right]
		for k := right - 1; k >= left; k-- {
			temp := matrix[top][k]
			matrix[top][k] = prev
			prev = temp
		}
		for k := top + 1; k <= bottom; k++ {
			temp := matrix[k][left]
			matrix[k][left] = prev
			prev = temp
		}
		for k := left + 1; k <= right; k++ {
			temp := matrix[bottom][k]
			matrix[bottom][k] = prev
			prev = temp
		}
		for k := bottom; k >= top; k-- {
			temp := matrix[top][k]
			matrix[top][k] = prev
			prev = temp
		}
	}
	return matrix
}
