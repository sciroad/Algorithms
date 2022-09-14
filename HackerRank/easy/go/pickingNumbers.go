package easy

func PickingNumbers() int32 {
	a := []int32{4, 6, 5, 3, 3, 1}
	b := map[int32]int32{}
	for _, i := range a {
		_, ok := b[i]
		if !ok {
			b[i] = 1
		} else {
			b[i]++
		}
	}
	maxL := int32(1)
	for k, v := range b {
		val := b[k+1]
		if val+v > maxL {
			maxL = val + v
		}
	}
	return maxL
}
