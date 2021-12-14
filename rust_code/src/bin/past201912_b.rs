#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n:usize,
        al:[i64;n],
    }
    for i in 0..n - 1 {
        let d = al[i + 1] - al[i];
        let ans = if d > 0 {
            format!("up {}", d)
        } else if d < 0 {
            format!("down {}", d * (-1))
        } else {
            "stay".to_string()
        };
        println!("{}", ans);
    }
}
