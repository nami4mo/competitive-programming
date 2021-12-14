#![allow(unused_imports)]

use std::collections::HashSet;

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n:usize,
    }
    let mut st: HashSet<Vec<usize>> = HashSet::new();
    for _ in 0..n {
        input! {
            k:usize,
            al:[usize;k],
        }
        st.insert(al.clone());
    }
    println!("{}", st.len());
}

#[fastout]
fn main() {
    solve();
}
