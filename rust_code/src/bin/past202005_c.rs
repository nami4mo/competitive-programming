#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        a:i64,
        r:i64,
        n:usize,
    }
    let mut v = a;
    for _ in 0..n - 1 {
        if v * r > 1000000000 {
            println!("large");
            return;
        }
        v *= r;
    }
    println!("{}", v);
}
