class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        if(s.length <= 1) return s.length;

        let map = new Map();
        let start = 0;
        let maxFreqChar = 0;
        let ans = 0;

        for(let end = 0; end < s.length; end++){
            let char = s[end];
            map.set(char,(map.get(char) || 0) + 1);
            maxFreqChar = Math.max(maxFreqChar, map.get(char));

            while((end - start + 1) - maxFreqChar > k){
                let char = s[start]
                map.set(char, map.get(char)-1);
                start++;
            }
            ans = Math.max(ans,(end - start + 1));
        }
        return ans;
    }
}
