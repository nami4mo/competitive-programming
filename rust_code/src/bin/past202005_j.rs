#![allow(unused_imports)]
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};
use std::collections::{HashMap, VecDeque};
use std::mem::swap;

fn solve() {
    input! {
        n: usize,
        q: usize,
    }
    let mut rev = false;
    let mut rows: Vec<usize> = (0..n).collect();
    let mut cols: Vec<usize> = (0..n).collect();
    for _ in 0..q {
        input! {t: usize}
        if t == 1 || t == 2 {
            input! {a: Usize1, b: Usize1}
            if (t == 1 && !rev) || (t == 2 && rev) {
                rows.swap(a, b);
            } else {
                cols.swap(a, b);
            }
        } else if t == 3 {
            rev = !rev;
        } else {
            input! {mut a: Usize1, mut b: Usize1}
            if rev {
                swap(&mut a, &mut b);
            }
            let val = rows[a] * n + cols[b];
            println!("{}", val);
        }
    }
}

#[fastout]
fn main() {
    solve();
}
