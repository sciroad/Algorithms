package easy

func utopianTree(n int32) int32 {
	// Write your code here
	var result int32 = 0
	for i := int32(0); i < n+1; i++ {
		if i%2 == 0 {
			result++
		} else {
			result *= 2
		}
	}
	return result

}
