class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();
        let ans = [];

        for(let i = 0; i < strs.length; i++){
            let key = strs[i].split('').sort().join('');

            if(!map.has(key)){
                 map.set(key,[]);
            }
            map.get(key).push(strs[i]);
        }
      for (const [key, value] of map) {
        ans.push(value);
      }

      return ans;
    }
}
