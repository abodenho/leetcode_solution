var lengthOfLongestSubstring = function(s) {
    let chars = new Set();
    let left = 0;
    let maximal_value = 0;

    for (let right = 0; right < s.length; right++) {

        while (chars.has(s[right])) {
            chars.delete(s[left]);
            left++;
        }

        chars.add(s[right]);

        maximal_value = Math.max(
            maximal_value,
            right - left + 1
        );
    }

    return maximal_value;
};

console.log(lengthOfLongestSubstring("pwwkew")); // 3