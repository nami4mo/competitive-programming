#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n:usize,
        al:[i64; n],
    }
    let mut map = HashMap::<i64, i64>::new();
    for a in &al {
        if map.contains_key(a) {
            map.insert(*a, map[a] + 1);
        } else {
            map.insert(*a, 1);
        }
    }
    let mut ans_v = 10000000;
    let mut ans = -1;
    for (k, v) in &map {
        if ans_v > *v {
            ans_v = *v;
            ans = *k;
        } else if ans_v == *v && ans > *k {
            ans_v = *v;
            ans = *k;
        }
    }
    println!("{}", ans);
}
