#![allow(unused_imports)]

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n: usize,
        x: Usize1,
        al: [Usize1;n],
    }
    let mut ans = 1;
    let mut used = vec![false; n];
    let mut curr = x;
    used[curr] = true;

    loop {
        curr = al[curr];
        if used[curr] {
            break;
        } else {
            ans += 1;
            used[curr] = true;
        }
    }
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
