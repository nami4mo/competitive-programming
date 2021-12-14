#![allow(unused_imports)]

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        v:f64,
    }
    let ans = v.round() as i64;
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
