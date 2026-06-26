class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        // brute force
        let maxL = 0;
        if(s.length === 0) return 0;
        if(s.length === 1) return 1;
       
       for(let i = 0; i < s.length-1; i++){
        let map = new Map();
        for(let j = i; j < s.length; j++){
            let char = s.charAt(j);

            if(map.has(char)){
              break;
            }
            map.set(char,j);
            maxL = Math.max(maxL,j - i + 1);
        }
       }
       return maxL;
    }
}
