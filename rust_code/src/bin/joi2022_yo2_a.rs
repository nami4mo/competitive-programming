#![allow(unused_imports)]

use std::collections::VecDeque;

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

// #[fastout]
fn solve() {
    input! {
        q:usize,
    }
    let mut deq = VecDeque::<String>::new();
    for _ in 0..q {
        input! {s: String}
        if s == "READ" {
            let ans = deq.pop_back().unwrap();
            println!("{}", ans);
        } else {
            deq.push_back(s);
        }
    }
}

fn main() {
    solve();
}
