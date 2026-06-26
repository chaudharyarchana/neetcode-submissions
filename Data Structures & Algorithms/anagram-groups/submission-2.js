class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();

        for(let i = 0; i < strs.length; i++){
           let count = new Array(26).fill(0);

           for(let ch of strs[i]){
             count[ch.charCodeAt(0) - 97]++
           }
           const key = count.join('#');

            if(!map.has(key)){
                 map.set(key,[]);
            }
            map.get(key).push(strs[i]);
        }
      

      return Array.from(map.values());
    }
}
