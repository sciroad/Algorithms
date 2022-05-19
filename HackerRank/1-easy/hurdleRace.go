package easy

func hurdleRace(k int32, height []int32) int32 {
	max := k
	for i := 0; i < len(height); i++ {
		if height[i] > max {
			max = height[i]

		}
	}
	return max - k

}
