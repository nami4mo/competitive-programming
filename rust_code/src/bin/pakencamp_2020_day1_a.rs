#![allow(unused_imports)]

use num_traits::Pow;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n: Chars
    }
    let mut ans = 0;
    for &c in &n {
        ans = ans.max(c.to_digit(10).unwrap());
    }
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
