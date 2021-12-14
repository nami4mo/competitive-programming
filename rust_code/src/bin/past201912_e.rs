#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
    }
    let mut follow = vec![vec![false; n]; n];
    for _ in 0..q {
        input! {q0: usize}
        match q0 {
            1 => {
                input! {a: usize, b:usize};
                follow[a - 1][b - 1] = true;
            }
            2 => {
                input! {mut a: usize};
                a -= 1;
                for i in 0..n {
                    if follow[i][a] {
                        follow[a][i] = true;
                    }
                }
            }
            3 => {
                input! {mut a: usize};
                a -= 1;
                let mut new_follow = vec![];
                for i in 0..n {
                    if a == i {
                        continue;
                    }
                    if follow[a][i] {
                        for j in 0..n {
                            if follow[i][j] {
                                new_follow.push(j);
                            }
                        }
                    }
                }
                for v in &new_follow {
                    follow[a][*v] = true;
                }
            }
            _ => {}
        }
    }
    for i in 0..n {
        follow[i][i] = false;
    }
    for i in 0..n {
        for j in 0..n {
            print!("{}", if follow[i][j] { "Y" } else { "N" });
        }
        println!("");
    }
}
