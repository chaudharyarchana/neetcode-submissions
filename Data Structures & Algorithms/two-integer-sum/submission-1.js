class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hashmap = {}; // to store indices of nums
        let ans = [];
        
        for(let i = 0; i < nums.length; i++){
            if(!Object.hasOwn(hashmap, nums[i])) hashmap[nums[i]] = [];
            hashmap[nums[i]].push(i);
        }

        nums.sort((a,b) => a - b); // sort in ascending order

        let i = 0;
        let j = nums.length - 1;

        while(i < j){
            let sum = nums[i] + nums[j];
            if(sum === target){
                ans[0] = nums[i];
                ans[1] = nums[j];
                break;
            }else if(sum < target) i++;
            else j--;
        }
        
        if(ans[0] === ans[1]){
            return hashmap[ans[0]].sort((a,b) => a-b).slice(0,2);
        }
        return [...hashmap[ans[0]].sort((a,b) => a-b).slice(0,1) , ...hashmap[ans[1]].sort((a,b) => a-b).slice(0,1)];
    }
}
