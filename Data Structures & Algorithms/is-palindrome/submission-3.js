class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
       let l = 0;
       let r = s.length - 1;

       while(l < r){
        while( l < r && !this.isnumericAlpha(s.charAt(l))) l++;
        while( l < r && !this.isnumericAlpha(s.charAt(r))) r--;

        if( l < r && s.charAt(l).toLowerCase() !== s.charAt(r).toLowerCase()) return false;
        l++; r--;
       }
       return true;
    }

    isnumericAlpha(c){
       return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
    
}
