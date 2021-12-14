#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        s:Chars,
    }
    let mut words = vec![];
    let mut flag = true;
    let mut tmp_word = "".to_string();
    for si in &s {
        tmp_word.push(*si);
        if si.is_uppercase() {
            if flag {
                flag = false;
            } else {
                flag = true;
                words.push(tmp_word);
                tmp_word = "".to_string();
            }
        }
    }
    // println!("{:?}", words);
    words.sort_by_cached_key(|v| v.to_lowercase());
    for v in &words {
        print!("{}", *v);
    }
    println!();
}
