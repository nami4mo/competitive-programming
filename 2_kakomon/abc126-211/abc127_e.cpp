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

const int MAX = 510000;
long long fac[MAX], finv[MAX], inv[MAX];

void com_init() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

long long com(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}


void solve(){
    com_init();
    int n,m,k; cin >> n >> m >> k;

    ll pattern_m = n*n * com(n*m-2,k-2);
    ll pattern_n = m*m * com(n*m-2,k-2);
    pattern_m%=MOD;
    pattern_n%=MOD;
    ll ans = 0;
    FOR(i,1,m){
        ans += (m-i)*pattern_m*i;
        ans %= MOD;       
    }
    FOR(i,1,n){
        ans += (n-i)*pattern_n*i;
        ans %= MOD;       
    }
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}