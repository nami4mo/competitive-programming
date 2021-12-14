#![allow(unused_imports)]

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        q: usize,
        txs: [(i64,i64); q],
    }
    let n = 2_usize.pow(20);
    let mut edges = vec![0; n];
    for i in 0..n {
        edges[i] = (i + 1) % n;
    }
    let mut nums = vec![-1; n];
    for (t, x) in &txs {
        if t == &1 {
            let mut curr = *x as usize;
            curr %= n;
            let mut routes = vec![curr];
            loop {
                if nums[curr] == -1 {
                    break;
                }
                // eprintln!("{}", curr);
                curr = edges[curr];
                routes.push(curr);
            }
            nums[curr] = *x;
            // eprintln!("{} {}", curr, x);
            for i in &routes {
                edges[*i] = curr;
            }
            edges[curr] = (curr + 1) % n;
        } else {
            println!("{}", nums[*x as usize % n]);
        }
    }
}

#[fastout]
fn main() {
    solve();
}
