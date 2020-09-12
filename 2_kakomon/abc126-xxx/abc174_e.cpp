#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;


#define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
#define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
#define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
#define ALL(x) x.begin(),x.end()
#define debug(x) cerr << #x << ": " << x << '\n'

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    int n,k; cin >> n >> k;
    vector<ll> al(n); REP(i,n) cin >> al[i];

    ll ng = 0;
    ll ok = 1e9+1;
    while(abs(ok-ng)>1){
        ll mid = (ok+ng)/2;
        ll cnt = 0;
        for( ll a : al ){
            cnt += (a-1)/mid;
        }
        if(cnt <= k){
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
