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
using mint = modint1000000007;


typedef pair<mint,int> P;

const int MOD = 1000000007;
const int MAX = 510000;
mint fac[MAX], finv[MAX], inv[MAX];
void com_init() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i;
        inv[i] = MOD - inv[MOD%i] * (MOD / i);
        finv[i] = finv[i - 1] * inv[i];
    }
}

mint com(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k]);
}

mint perm(int n, int r){
    if(n < r) return 0;
    if(n < 0 || r < 0) return 0;
    return fac[n] * finv[n-r];
}


P dfs1(int pare, int node, vector<vector<int>> &gl, vector<P> &dp){
    mint node_v = 1;
    int node_size = 1;
    for( int neib : gl[node]){
        if(pare==neib) continue;
        auto [child_v, child_size] = dfs1(node, neib, gl, dp);
        node_v *= child_v;
        node_v /= fac[child_size];
        node_size += child_size;
    }
    node_v *= fac[node_size-1];
    return dp[node] = P(node_v, node_size);
}

void dfs2(int pare, int node, mint pare_v, int pare_size, vector<vector<int>> &gl, vector<P> &dp, vector<mint> &ansl){
    auto [node_v, node_size] = dp[node];
    node_v *= perm(node_size-1+pare_size, pare_size);
    node_v /= fac[pare_size];
    node_v *= pare_v;
    node_size += pare_size;
    ansl[node] = node_v;

    for( int neib : gl[node]){
        if(pare==neib) continue;
        auto [chi_v, chi_size] = dp[neib];
        mint new_node_v = node_v;
        new_node_v /= perm(node_size-1,chi_size);
        new_node_v *= fac[chi_size];
        new_node_v /= chi_v;
        int new_node_size = node_size - chi_size;
        dfs2(node, neib, new_node_v, new_node_size, gl, dp, ansl);
    }
}


void solve(){
    com_init();
    ll n; cin >> n;
    vector<vector<int>> gl(n);
    vector<P> dp(n,P(0,-1));
    REP(i,n-1){
        ll a,b; cin >> a >> b;
        a-=1; b-=1;
        gl[a].push_back(b);
        gl[b].push_back(a);
    }
    dfs1(-1,0,gl,dp);
    // for( auto [v,s] : dp){
    //     cout << v.val() << endl;
    // }
    vector<mint> ansl(n,0);
    dfs2(-1,0,1,0,gl,dp,ansl);
    for(mint a :ansl){
        cout << a.val() << '\n';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}