#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef long long ll;
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


ll rec(int l, int r, int n, vector<ll> &al, vector<vector<ll>> &dp){
    if(l==r){
        if(n%2==1) return dp[l][r] = al[l];
        else return dp[l][r] = 0;
    }
    if(dp[l][r] != -1){
        return dp[l][r];
    }

    int rem;
    if(l>=r) rem = (r+n)-l+1;
    else rem = r-l+1;
    int got_cnt = n-rem;

    int next_l = l+1;
    int next_r = r-1;
    if(next_l>=n) next_l=0;
    if(next_r<0) next_r=n-1;
    if(got_cnt%2==0){ //JOI
        dp[l][r] = max( rec(next_l,r,n,al,dp)+al[l], rec(l,next_r,n,al,dp)+al[r] );
    }
    else{
        if(al[l]>al[r]) dp[l][r] = rec(next_l,r,n,al,dp);
        else dp[l][r] = rec(l,next_r,n,al,dp);
    }
    return dp[l][r];
}


void solve(){
    int n; cin >> n;
    vector<ll> al(n); REP(i,n) cin >> al[i];

    vector<vector<ll>> dp(n,vector<ll>(n,-1));
    ll ans = 0;
    REP(i,n){
        int next_l = i+1;
        int next_r = i-1;
        if(next_l>=n) next_l=0;
        if(next_r<0) next_r=n-1;
        ll val = al[i] + rec(next_l, next_r, n, al, dp);
        ans = max(ans,val);
    }
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}