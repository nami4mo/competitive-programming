#![allow(unused_imports)]
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};
use std::collections::{HashMap, VecDeque};

fn solve() {
    input! {
        n: usize, l: usize,
        xl: [usize; n],
        t1: usize,
        t2: usize,
        t3: usize,
    }

    let mut dp = vec![1e18 as usize; l + 10];
    dp[0] = 0;

    let mut hardle = vec![false; l + 10];
    for &x in &xl {
        hardle[x] = true;
    }

    for i in 0..l {
        if hardle[i + 1] {
            dp[i + 1] = dp[i + 1].min(dp[i] + t1 + t3);
        } else {
            dp[i + 1] = dp[i + 1].min(dp[i] + t1);
        }
        if hardle[i + 2] {
            dp[i + 2] = dp[i + 2].min(dp[i] + t1 + t2 + t3);
        } else {
            dp[i + 2] = dp[i + 2].min(dp[i] + t1 + t2);
        }
        if hardle[i + 4] {
            dp[i + 4] = dp[i + 4].min(dp[i] + t1 + t2 * 3 + t3);
        } else {
            dp[i + 4] = dp[i + 4].min(dp[i] + t1 + t2 * 3);
        }
    }
    let mut ans = dp[l];
    if l > 2 {
        ans = ans.min(dp[l - 3] + t1 / 2 + t2 * 5 / 2);
    }
    ans = ans.min(dp[l - 2] + t1 / 2 + t2 * 3 / 2);
    ans = ans.min(dp[l - 1] + t1 / 2 + t2 * 1 / 2);
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
