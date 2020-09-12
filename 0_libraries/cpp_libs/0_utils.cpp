#include <bits/stdc++.h>
#include <cmath>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;

const string alps = "abcdefghijklmnopqrstuvwxyz";
const string ALPs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";



void sample_char_map(){
    map<char, vector<int>> alp_d;
    for(int i = 0 ; i < 26; i++){
        vector<int> vec;
        alp_d[i+'a'] = vec;
    }
    for( char s : alps){
        alp_d[s].push_back(s-'a');
    }
}


void binary_search(){
    ll ok = 0;
    ll ng = 1e9+1;
    while(abs(ok-ng)>1){
        ll mid = (ok+ng)/2;
        bool ok_flag = true;
        //...

        if(ok_flag){
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;
}


void cumsum(){
    int n; cin >> n;
    vector<ll> al(n); 
}


int main()
{
    sample_char_map();
    binary_search();
}