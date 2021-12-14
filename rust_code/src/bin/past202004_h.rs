#![allow(unused_imports)]

use std::cmp::min;

use num::abs;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn get_dist(x0: usize, y0: usize, x1: usize, y1: usize) -> usize {
    let res = abs(x0 as i64 - x1 as i64) + abs(y0 as i64 - y1 as i64);
    res as usize
}

fn solve() {
    input! {
        n: usize,
        m: usize,
        al: [Chars; n]
    }
    let mut nums = vec![vec![]; 11];
    for y in 0..n {
        for x in 0..m {
            let c = al[y][x];
            let v = if c == 'S' {
                0
            } else if c == 'G' {
                10
            } else {
                c.to_digit(10).unwrap() as usize
            };
            nums[v].push((y, x));
        }
    }
    let inf = 1e18 as usize;
    let mut dp = vec![vec![inf; n * m + 1]; 11];
    dp[0][0] = 0;
    for v in 0..10 {
        for (i, (y0, x0)) in nums[v].iter().enumerate() {
            for (j, (y1, x1)) in nums[v + 1].iter().enumerate() {
                dp[v + 1][j] = min(dp[v + 1][j], dp[v][i] + get_dist(*x0, *y0, *x1, *y1));
            }
        }
    }
    let ans = if dp[10][0] == inf {
        -1
    } else {
        dp[10][0] as i64
    };
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
