/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    ans = 0;
    for (let i = 0; i < text2.length; ++i) {
        if (text1.includes(text2[i])) {
					const idx = text1.indexOf(text2[i]);
						console.log(text2[i])
						console.log('-', text1, `idx=${idx}`)
						text1 = text1.slice(idx+1, text1.length);
						console.log('--', text1)
            ans++;
        }
    }
    return ans;
};

// ans = longestCommonSubsequence("ezupkr", "ubmrapg");
// console.log(ans);
ans = longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy");
console.log(ans);