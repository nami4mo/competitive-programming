#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<ll,ll> P;
    #define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
    #define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
    #define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(),x.end()
    template<class T> vector<T> make_vec(size_t a){return vector<T>(a);}
    template<class T, class... Ts> auto make_vec(size_t a, Ts... ts){ return vector<decltype(make_vec<T>(ts...))>(a, make_vec<T>(ts...));}

    /* for debug print */
    #define DEBUG(x) cerr << #x << ": " << x << '\n'
    #define DEBUGP(x) cerr << #x << ": (" << x.first << ", " << x.second << ")" << '\n' 
    #define DEBUGL(xl) dbgl_f(#xl,xl)
    #define DEBUGLP(xl) dbglp_f(#xl,xl)
    #define DEBUGLL(xll) dbgll_f(#xll,xll)
    #define DEBUGM(xl) dbgm_f(#xl,xl)
    template<class T> void dbgl_f(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr << '\n';}
    template<class T, class U> void dbgm_f(string name, map<T,U> xl){cerr<<name<<": ";for(auto x: xl)cerr<<"("<<x.first<<": "<<x.second<<") ";cerr<<'\n';}
    template<class T> void dbglp_f(string name, vector<T> xl){cerr<<name<<": ";for(T x: xl)cerr<<"("<<x.first<<", "<< x.second<<") ";cerr<<'\n';}
    template<class T> void dbgll_f(string name, vector<vector<T>> xll){
        cerr<< name << ": " << '\n'; 
        for(vector<T> xl: xll){
            for(T x : xl) cerr << x << " ";
            cerr << '\n';
        }
    }
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;

using mint = modint1000000007;

const int MOD = 1000000007;
const int MAX = 510000;
// mint fac[MAX], finv[MAX], inv[MAX];
// void com_init() {
//     fac[0] = fac[1] = 1;
//     finv[0] = finv[1] = 1;
//     inv[1] = 1;
//     for (int i = 2; i < MAX; i++){
//         fac[i] = fac[i - 1] * i;
//         inv[i] = MOD - inv[MOD%i] * (MOD / i);
//         finv[i] = finv[i - 1] * inv[i];
//     }
// }

// mint com(int n, int k){
//     if (n < k) return 0;
//     if (n < 0 || k < 0) return 0;
//     return fac[n] * (finv[k] * finv[n - k]);
// }

mint com(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    mint top = 1;
    mint bottom = 1;
    REP(i,k){
        top *= (n-i);
        bottom *= (i+1);
    }
    return top/bottom;
}

void solve(){
    ll n; cin >> n;
    vector<ll> al(n); REP(i,n) cin >> al[i];
    bool flag = false;
    int cnt = 0;
    int prev = -1;
    mint ans = 1;
    REP(i,n){
        if(al[i] == -1){
            if(flag){
                cnt++;
            }
            else{
                cnt = 1;
                flag = true;
            }
        }
        else{
            if(flag){
                int d = al[i]-prev+1;
                // DEBUG(d);
                // DEBUG(cnt);
                // ans += pow(d, cnt);
                // ans *= mint(d).pow(cnt);s
                ans *= com(d-1+cnt,cnt);
                cnt = 0;
                flag = false;
            }
            prev = al[i];
        }
    }
    cout << ans.val() << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}