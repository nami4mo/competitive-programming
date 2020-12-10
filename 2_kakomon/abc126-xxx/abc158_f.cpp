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
typedef pair<ll,ll> P;
using mint = modint998244353;

int op(int a, int b){return max(a,b);} 
int e(){return 0;}
void solve(){
    // segtree<S, op, e> seg(vector<S> v)
    ll n; cin >> n;
    vector<P> xdl(n);
    REP(i,n){
        ll x,d; cin >> x >> d;
        xdl[i] = P(x,d);
    }
    sort(ALL(xdl));
    vector<ll> xl(n);
    vector<ll> dl(n);
    REP(i,n){
        xl[i] = xdl[i].first;
        dl[i] = xdl[i].second;
    }
    vector<int> reaches(n);
    REP(i,n){
        ll right = xl[i]+dl[i];
        auto iter4 = lower_bound(ALL(xl), right);
        int ind4 = iter4 - xl.begin() - 1;
        reaches[i] = ind4;
    }

    segtree<int, op, e> seg(n);
    for(int i = n-1 ; i >= 0 ; i--){
        seg.set(i,i);
        int rmax = seg.prod(i,reaches[i]+1);
        seg.set(i,rmax);
    }
    // REP(i,n){
    //     cout<<seg.get(i)<<endl;
    // }

    vector<mint> dp(n,0);
    // dp[n] = 1;
    mint ans = 1; // empty
    for(int i = n-1 ; i >= 0 ; i--){
        int rmax = seg.get(i);
        mint prev_ans = ans;
        if(i == rmax){
            ans *= 2;
        }
        else{
            ans += dp[rmax];
        }
        dp[i] = ans - prev_ans;
        // if(i==n-1) dp[i] = 1;
        // cout<<dp[i].val()<<endl;
    }
    cout << ans.val() << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}