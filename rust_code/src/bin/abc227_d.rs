#![allow(unused_imports)]

use std::cmp::min;
use std::collections::HashSet;

use num::abs;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n:usize,
        k:i64,
        al:[i64; n],
    }
    let mut ok = 0;
    let mut ng = 1e18 as i64 / k;
    while abs(ok - ng) > 1 {
        let mid = (ok + ng) / 2;
        let mut cnt = 0;
        for a in &al {
            cnt += min(*a, mid);
        }
        if cnt >= mid * k {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    println!("{}", ok);
}

#[fastout]
fn main() {
    solve();
}
