class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let isValid = true;

        // traverse through each row
        for(let i = 0; i < 9; i++){
            let hashmap = {};

            for(let j = 0; j < 9; j++){
                if(hashmap[board[i][j]]){
                    isValid = false;
                    break;
                }
                if(board[i][j] === '.') continue;
                hashmap[board[i][j]] = (hashmap[board[i][j]] || 0) + 1;
            }
        }

        // traverse through each column
        for(let i = 0; i < 9; i++){
            let hashmap = {};

            for(let j = 0; j < 9; j++){
                if(hashmap[board[j][i]]){
                    isValid = false;
                    break;
                }
                if(board[j][i] === '.') continue;
                hashmap[board[j][i]] = (hashmap[board[j][i]] || 0) + 1;
            }
        }

        let m = 0;
        let n = 0;
        // check each boxes
        while(m < 9){
        
        let hashmap = {}
        for(let i = m; i < m+3; i++){
            for(let j = n; j < n+3; j++){
                if(hashmap[board[i][j]]){
                    isValid = false;
                    break;
                }
                if(board[i][j] === '.') continue;
                hashmap[board[i][j]] = (hashmap[board[i][j]] || 0) + 1;
            }
        }
        if(n+3 < 9){
            n = n+3;
        }else{
            m = m + 3;
            n = 0;
        }
        
        }

        return isValid;
    }
}
