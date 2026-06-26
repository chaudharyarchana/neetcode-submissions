class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = '';
        for(let str of strs){
            encoded = encoded + str.length + '#' + str;
        }
        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let decoded = [];
        let i = 0;

        while( i < str.length){
             let j = i;

             while(str[j] !== '#') j++;

             let length = parseInt(str.slice(i,j));
             i = j+1;

             let word = str.slice(i,i+length);
             i = i + length;
             decoded.push(word);
        }
        return decoded;
    }
}
