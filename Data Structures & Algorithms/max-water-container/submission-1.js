class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let max = 0;
        let l = 0;
        let r = heights.length - 1;

        while(l < r){
            // we have to inc. the min value to get the maximum area - use 2 pointer to get max value;
            let area = Math.min(heights[l],heights[r])*(r-l); 
            max = Math.max(max,area);
            // move the pointer which is lesser
            if(heights[l] < heights[r]) l++;
            else r--;
        }
        return max;
    }
}
