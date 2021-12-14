#![allow(unused_imports)]

use im_rc::HashSet;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

#[fastout]
fn solve() {
    input! {
        h: usize, w: usize, c: usize, q: usize,
        ql: [(usize, Usize1, Usize1); q],
    }
    let mut ans = vec![0; c];
    let mut row_used = HashSet::<usize>::new();
    let mut col_used = HashSet::<usize>::new();
    let mut row_cnt = 0;
    let mut col_cnt = 0;
    for &(t, n, cc) in ql.iter().rev() {
        if t == 1 {
            if row_used.contains(&n) {
                continue;
            }
            ans[cc] += w - col_cnt;
            row_used.insert(n);
            row_cnt += 1;
        } else {
            if col_used.contains(&n) {
                continue;
            }
            ans[cc] += h - row_cnt;
            col_used.insert(n);
            col_cnt += 1;
        }
    }
    println!(
        "{}",
        ans.iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}

#[fastout]
fn main() {
    solve();
}
