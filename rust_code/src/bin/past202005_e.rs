#![allow(unused_imports)]
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};
use std::collections::HashMap;

fn solve() {
    input! {
        n: usize, m: usize, q: usize,
        uvl: [(Usize1, Usize1); m],
        mut cl: [usize; n],
    }
    let mut gl = vec![vec![]; n];
    for &(u, v) in &uvl {
        gl[u].push(v);
        gl[v].push(u);
    }
    for _ in 0..q {
        input! {
            qq: usize,
            x: Usize1,
        }
        println!("{}", cl[x]);
        if qq == 1 {
            for &neib in &gl[x] {
                cl[neib] = cl[x];
            }
        }
        if qq == 2 {
            input! {y:usize}
            cl[x] = y;
        }
    }
}

#[fastout]
fn main() {
    solve();
}
