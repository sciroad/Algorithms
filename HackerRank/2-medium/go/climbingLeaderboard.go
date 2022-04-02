package medium

func climbingLeaderboard(ranked []int32, player []int32) []int32 {
	var result []int32 = []int32{}
	rank := int32(1)
	iRanked := 0
	iPlayer := len(player) - 1
	// maxL := len(player)
	currentScore := ranked[iRanked]
	if player[iPlayer] >= currentScore {
		result = append(result, rank)
		iPlayer--
	} else {
		iRanked++
		if currentScore > ranked[iRanked] {
			currentScore = ranked[iRanked]
			rank++
		}

	}
	for iPlayer > -1 {
		if player[iPlayer] >= ranked[iRanked] {
			result = append(result, rank)
			iPlayer--
		} else {
			iRanked++
			if currentScore > ranked[iRanked] {
				currentScore = ranked[iRanked]
				rank++
			}

		}
	}
	finalResult := []int32{}
	for i := len(result) - 1; i > -1; i-- {
		finalResult = append(finalResult, result[i])
	}
	return finalResult
}
