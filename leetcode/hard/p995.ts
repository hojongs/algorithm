/*
995. Minimum Number of K Consecutive Bit Flips
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

python에서 Time limit exceeded 발생해서 TypeScript로 시도 및 성공
실행 시간은 오락가락함 (1.6s ~ 2.7s)

sudo npm install -g typescript
tsc --target es6 p995.ts
*/
function minKBitFlips(nums: number[], k: number): number {
    let cnt = 0;

    for (const [i, v] of nums.entries()) {
        if (i + k > nums.length) {
            for (let h = i; h < nums.length; h++) {
                if (nums[h] == 0)
                    return -1;
            }
            break;
        }
        if (v == 0) {
            for (let h = i; h < i + k; h++) {
                nums[h] ^= 1;
            }
            cnt++;
        }
    };

    return cnt;
};
