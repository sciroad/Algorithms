package easy

func getMoneySpent(keyboards []int32, drives []int32, b int32) int32 {
	/*
	 * Write your code here.
	 */
	var result int32 = -1
	for _, k := range keyboards {
		for _, d := range drives {
			if (d+k) <= b && d+k > result {
				result = d + k
			}
		}
	}
	return result

}
