class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let product = 1;
        let zeroCount = 0;
        let ans = [];

        for(let i = 0; i < nums.length; i++){
            if(nums[i] === 0){
                zeroCount++;
                continue;
            };
            product = product*nums[i];
        }
        if(zeroCount > 1){
            return new Array(nums.length).fill(0);
        }
        
        for(let i = 0; i < nums.length; i++){
           if(zeroCount > 0){
           ans[i] =  nums[i] === 0 ? product : 0;
           }else{
            ans[i] = product/nums[i];
           }
        }
        return ans;
    }
}
