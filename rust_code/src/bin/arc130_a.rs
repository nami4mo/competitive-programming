#![allow(unused_imports)]

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {n: usize, s: Chars}
    let mut ans: i64 = 0;
    let mut cnt = 0;
    let mut prev = '-';
    for i in 0..n {
        if prev != s[i] {
            ans += cnt * (cnt - 1) / 2;
            cnt = 1;
        } else {
            cnt += 1;
        }
        prev = s[i];
    }
    ans += cnt * (cnt - 1) / 2;
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
