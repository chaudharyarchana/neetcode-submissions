class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        // sliding window
    
       if(s.length === 0) return 0;
       if(s.length === 1) return 1;

       let maxL = 0;
       let map = new Map();
       let start = 0;
       let end = 0;

       while(end < s.length){
          let char = s[end];
          if(map.has(char)){
            let dupIdx = map.get(char);
            let i = start;
            while(i <= dupIdx){
                map.delete(s[i]);
                i++;
            }
            start = dupIdx+1;
          }
          map.set(char,end);
          maxL = Math.max(maxL,end - start + 1);
          end++;
       }

       return maxL;
    }
}
