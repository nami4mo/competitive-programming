#![allow(unused_imports)]

use std::collections::HashSet;

use num_integer::gcd;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n:usize,
        ps: [(i64,i64); n],
    }
    let mut st = HashSet::<(i64, i64)>::new();
    for i in 0..n {
        for j in 0..n {
            if i == j {
                continue;
            }
            let dy = ps[j].1 - ps[i].1;
            let dx = ps[j].0 - ps[i].0;
            if dy == 0 {
                st.insert((0, 1));
                st.insert((0, -1));
            } else if dx == 0 {
                st.insert((-1, 0));
                st.insert((1, 0));
            } else {
                let g = gcd(dy, dx);
                st.insert((dx / g, dy / g));
            }
        }
    }
    println!("{}", st.len());
}

#[fastout]
fn main() {
    solve();
}
