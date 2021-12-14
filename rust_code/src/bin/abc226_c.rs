#![allow(unused_imports)]

use std::collections::HashSet;

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n:usize,
    }
    let mut times = vec![0; n];
    let mut deps = vec![vec![]; n];
    for i in 0..n {
        input! {
            t:usize,
            k:usize,
            al:[Usize1;k],
        }
        deps[i] = al.clone();
        times[i] = t;
    }
    let mut used = vec![false; n];
    used[n - 1] = true;
    let mut ans = 0;
    ans += times[n - 1];
    for i in (0..n).rev() {
        if !used[i] {
            continue;
        }
        for dep in &deps[i] {
            if used[*dep] {
                continue;
            }
            ans += times[*dep];
            used[*dep] = true;
        }
    }
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
