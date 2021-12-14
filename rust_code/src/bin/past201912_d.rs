#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        al: [usize;n],
    }
    let mut cnts = vec![0; n + 1];
    for a in &al {
        cnts[*a] += 1;
    }
    let mut del = 0;
    let mut dup = 0;
    for i in 1..n + 1 {
        if cnts[i] == 0 {
            del = i;
        }
        if cnts[i] == 2 {
            dup = i;
        }
    }
    if del == 0 {
        println!("Correct");
    } else {
        print!("{} {}", dup, del);
    }
}
