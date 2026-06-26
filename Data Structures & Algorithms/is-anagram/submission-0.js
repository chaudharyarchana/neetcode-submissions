class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) return false;

        const hashmap = {};

        for(let i = 0; i < s.length; i++){
           hashmap[s.charAt(i)] =  (hashmap[s.charAt(i)] || 0) + 1;
           hashmap[t.charAt(i)] =  (hashmap[t.charAt(i)] || 0) - 1;
        }

        for(let key in hashmap){
            if(hashmap[key] !== 0) return false;
        }
        
        return true;
    }
}
