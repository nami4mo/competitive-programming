#![allow(unused_imports)]

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

#[fastout]
fn solve() {
    input! {n: usize}
    let mut ans = String::from("");
    let mut rem = n;
    let mut curr = 1;
    while rem > 0 {
        if rem >= curr {
            ans += "7";
            rem -= curr;
            curr += 1;
        } else {
            ans += "97";
            rem -= 1;
            curr = 2;
        }
    }
    // println!("{}", ans);
    println!("{}", ans.len());
}

fn main() {
    solve();
}
