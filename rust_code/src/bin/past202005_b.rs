#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n:usize,
        m:usize,
        q:usize,
    }
    let mut rem = vec![n; m];
    let mut solve = vec![vec![false; m]; n];
    for _ in 0..q {
        input! {
            s0:i64,
        }
        if s0 == 1 {
            input! {
                s1:usize,
            }
            let mut ans = 0;
            for i in 0..m {
                if solve[s1 - 1][i] {
                    ans += rem[i];
                }
            }
            println!("{}", ans);
        } else {
            input! {
                mut man:usize,
                mut prob:usize
            }
            man -= 1;
            prob -= 1;
            rem[prob] -= 1;
            solve[man][prob] = true;
        }
    }
}
