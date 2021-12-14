#![allow(unused_imports)]

use std::collections::VecDeque;

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

// #[fastout]
fn solve() {
    input! {
        n: usize, k: usize,
        al: [u64; n],
    }
    let mut dp = vec![vec![0; n + 1]; n + 1];
    for i in 0..n {
        dp[i + 1][0] = al[i];
    }
    for j in 0..n {
        let mut c_max = 0;
        if j + 2 > k {
            c_max = *dp[j + 1][0..j + 2 - k].iter().max().unwrap();
        }
        for i in j + 1..n {
            // eprintln!("-- {:?} -- ", (i + 1, j + 1));
            let min_i = if i + 1 >= k { i + 1 - k } else { 0 };
            // eprintln!("{:?}", (j + 1, min_i));
            c_max = c_max.max(dp[j + 1][min_i]);
            dp[i + 1][j + 1] = dp[i + 1][j + 1].max(c_max + al[i]);
        }
    }
    // eprintln!("{:?}", dp);
    let ans = dp.iter().map(|x| x.iter().max().unwrap()).max().unwrap();
    println!("{}", ans);
}

fn main() {
    solve();
}
