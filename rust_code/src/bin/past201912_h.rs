#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n:usize,
        mut cl:[i64; n],
        q:usize,
    }
    let mut odd_sum = 0;
    let mut all_sum = 0;
    let mut ans = 0;
    let mut curr_odd_min = 1e18 as i64;
    let mut curr_even_min = 1e18 as i64;
    let odd_cnt = ((n + 1) / 2) as i64;

    for i in 0..n {
        if i % 2 == 1 {
            curr_even_min = min(curr_even_min, cl[i]);
        } else {
            curr_odd_min = min(curr_odd_min, cl[i]);
        }
    }

    for _ in 0..q {
        input! {q0:usize}
        match q0 {
            1 => {
                input! {mut x:usize, a:i64}
                x -= 1;
                let tmp_sum = if x % 2 == 0 {
                    odd_sum + all_sum
                } else {
                    all_sum
                };
                if cl[x] >= tmp_sum + a {
                    cl[x] -= a;
                    ans += a;
                    if x % 2 == 1 {
                        curr_even_min = min(curr_even_min, cl[x]);
                    } else {
                        curr_odd_min = min(curr_odd_min, cl[x]);
                    }
                }
            }
            2 => {
                input! {a:i64}
                if curr_odd_min - odd_sum - all_sum < a {
                    continue;
                }
                odd_sum += a;
                ans += a * odd_cnt;
            }
            3 => {
                input! {a:i64}
                if curr_odd_min - odd_sum - all_sum < a || curr_even_min - all_sum < a {
                    continue;
                }
                all_sum += a;
                ans += a * (n as i64);
            }
            _ => {}
        }
    }
    println!("{}", ans);
}
