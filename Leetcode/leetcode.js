var numberOfSubarrays = function(nums, k) {
    let niceCount = 0;
    let foundOdd = 0;
    for(let i=0; i< nums.length; i++){
        for(let j=i; j< nums.length; j++){
            if(nums[j] % 2 == 1) {
                foundOdd++;
            }
            if(foundOdd > k) {
                break;
            }

            if(foundOdd == k){
                console.log(i,j)
                niceCount++
            }
        }
        foundOdd = 0
    }
    return niceCount;
};