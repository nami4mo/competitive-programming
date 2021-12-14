#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::cmp::*;
use std::collections::HashSet;

fn rec(groups: &mut Vec<i64>, ind: usize, n: usize, happy: &Vec<Vec<i64>>) -> i64 {
    let mut res = -1e9 as i64;
    if ind == n {
        res = 0;
        for i in 0..n {
            for j in i + 1..n {
                if groups[i] == groups[j] {
                    res += happy[i][j];
                }
            }
        }
        return res;
    }

    for i in 0..3 {
        groups[ind] = i;
        res = max(res, rec(groups, ind + 1, n, happy));
        groups[ind] = -1;
    }

    return res;
}

#[fastout]
fn main() {
    input! {
        n:usize,
    }
    let mut happy = vec![vec![0; n]; n];
    for i in 0..n - 1 {
        input! {
            mut al: [i64; n-i-1],
        }
        for j in 0..n {
            if j < i {
                happy[i][j] = happy[j][i];
            } else if j > i {
                happy[i][j] = al[j - i - 1];
            }
        }
    }

    let mut groups: Vec<i64> = vec![-1; n];
    let ans = rec(&mut groups, 0, n, &happy);
    println!("{}", ans);
}
