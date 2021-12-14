#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashMap;

// #[fastout]
fn main() {
    input! {
        s:String,
    }
    match s.parse::<i64>() {
        Ok(n) => println!("{}", n * 2),
        Err(_) => println!("error"),
    }
}
