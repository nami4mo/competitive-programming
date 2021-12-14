#![allow(unused_imports)]

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n: usize,
        k: Usize1,
        pl: [[usize;3];n],
    }
    let scores_orig: Vec<usize> = pl.iter().map(|x| x.iter().sum()).collect();
    let mut scores_sorted = scores_orig.clone();
    scores_sorted.sort_by(|a, b| b.cmp(a));
    let target = scores_sorted[k];
    for v in &scores_orig {
        println!("{}", if v + 300 >= target { "Yes" } else { "No" });
    }
}

#[fastout]
fn main() {
    solve();
}
