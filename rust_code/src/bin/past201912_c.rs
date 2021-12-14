#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        mut al: [i64;6],
    }
    al.sort();
    al.reverse();
    println!("{}", al[2]);
}
