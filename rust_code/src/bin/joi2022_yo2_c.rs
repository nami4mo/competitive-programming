#![allow(unused_imports)]

use std::collections::VecDeque;

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn get_cval(csums: &Vec<Vec<i64>>, y0: usize, x0: usize, yd: usize, xd: usize) -> i64 {
    csums[y0 + yd][x0 + xd] - csums[y0 + yd][x0] - csums[y0][x0 + xd] + csums[y0][x0]
}

// #[fastout]
fn solve() {
    input! {
        h: usize, w: usize,
        al: [[i64; w]; h],
    }
    let asum: i64 = al.iter().map(|x| -> i64 { x.iter().sum() }).sum();
    let hsums: Vec<i64> = al.iter().map(|x| -> i64 { x.iter().sum() }).collect();

    let mut csums = vec![vec![0; w + 1]; h + 1];
    for i in 0..h {
        for j in 0..w {
            csums[i + 1][j + 1] = csums[i + 1][j] + csums[i][j + 1] - csums[i][j] + al[i][j];
        }
    }

    let mut ans = 0;
    'outer: for hcnt in 1..h + 1 {
        if asum % hcnt as i64 != 0 {
            continue;
        }
        let target = asum / hcnt as i64;
        let mut hs = vec![];
        let mut curr_sum = 0;
        let mut curr_hs = vec![];
        for hi in 0..h {
            if curr_sum + hsums[hi] > target {
                continue 'outer;
            }
            if curr_sum + hsums[hi] == target {
                curr_hs.push(hi);
                hs.push(curr_hs.clone());
                curr_hs.clear();
                curr_sum = 0;
            } else {
                curr_hs.push(hi);
                curr_sum += hsums[hi];
            }
        }

        'outer2: for wcnt in 1..w + 1 {
            if target % wcnt as i64 != 0 {
                continue;
            }
            let w_target = target / wcnt as i64;
            let mut ws = vec![];
            let mut curr_sum = 0;
            let mut curr_ws = vec![];
            let hs1 = &hs[0];
            let h0 = hs1[0];
            let hd = hs1.last().unwrap() - h0 + 1;

            for wi in 0..w {
                let next_val = get_cval(&csums, h0, wi, hd, 1);
                if curr_sum + next_val > w_target {
                    continue 'outer2;
                }
                if curr_sum + next_val == w_target {
                    curr_ws.push(wi);
                    ws.push(curr_ws.clone());
                    curr_ws.clear();
                    curr_sum = 0;
                } else {
                    curr_ws.push(wi);
                    curr_sum += next_val;
                }
            }

            for c_hs in &hs {
                for c_ws in &ws {
                    let y0 = c_hs[0];
                    let yd = c_hs.last().unwrap() - y0 + 1;
                    let x0 = c_ws[0];
                    let xd = c_ws.last().unwrap() - x0 + 1;
                    let val = get_cval(&csums, y0, x0, yd, xd);
                    if val != w_target {
                        continue 'outer2;
                    }
                }
            }
            // eprintln!("{} {}", &hcnt, &wcnt);
            ans += 1;
        }
    }
    println!("{}", ans - 1);
}

fn main() {
    solve();
}
