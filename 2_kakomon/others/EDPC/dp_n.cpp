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
const int MOD = 1'000'000'007;

ll dp[440][440];
vector<ll> cumsums(440,0);

ll rec(int l, int r){
    if(l>=r-1){
        return 0;
    }
    if(dp[l][r]!=0){
        return dp[l][r];
    }
    ll v=cumsums[r]-cumsums[l];
    ll min_v=INF;
    FOR(i,l+1,r){
        ll v2=rec(l,i)+rec(i,r);
        min_v=min(min_v,v2);
    }
    return dp[l][r]=v+min_v;
}

void solve(){
    int n; cin >> n;
    vector<ll> al(n); REP(i,n) cin >> al[i];
    REP(i,440)REP(j,440)dp[i][j]=0;
    ll c=0;
    REP(i,n){
        c+=al[i];
        cumsums[i+1]=c;
    }
    ll ans=rec(0,n);
    cout << ans << endl;
    // int k; cin >> k;
    // vector<ll> hl(n); REP(i,n) cin >> hl[i];
    // vector<ll> dp(n+1,INF);
    // dp[0] = 0;
    // REP(i,n){
    //     FOR(j,1,k+1){
    //         if(i+j<n) dp[i+j] = min(dp[i+j], dp[i]+abs(hl[i]-hl[i+j]));
    //     }
    // }
    // cout << dp[n-1] << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}