package easy

func catAndMouse(x int32, y int32, z int32) string {
	var zx int32 = z - x
	var zy int32 = z - y
	if zy < 0 {
		zy = -zy
	}
	if zx < 0 {
		zx = -zx
	}
	result := zy - zx
	if result < 0 {
		return "Cat B"
	} else if result > 0 {
		return "Cat A"
	} else {
		return "Mouse C"
	}

}
