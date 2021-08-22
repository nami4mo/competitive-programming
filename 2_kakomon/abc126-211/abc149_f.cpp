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

using mint = modint1000000007;
mint ans = 0;
mint all_cnt;
ll n;

int dfs(int pare, int node, vector<vector<ll>> &gl){
    int child_cnt = 0;
    mint not_cnt = 0;
    for(int neib : gl[node]){
        if(pare==neib)continue;
        int neib_cnt = dfs(node, neib, gl)+1;
        child_cnt += neib_cnt;
        not_cnt += (mint(2).pow(neib_cnt)-1);
    }
    int rem_cnt = n-1-child_cnt;
    not_cnt += (mint(2).pow(rem_cnt)-1);
    ans += (all_cnt-not_cnt-1);
    return child_cnt;
}

void solve(){
    // ll n; cin >> n;
    cin >> n;
    vector<vector<ll>> gl(n);
    REP(i,n-1){
        ll u,v; cin >> u >> v;
        u-=1;v-=1;
        gl[u].push_back(v);
        gl[v].push_back(u);
    }
    all_cnt = mint(2).pow(n-1);
    dfs(-1,0,gl);
    ans/=mint(2).pow(n);
    cout << ans.val() << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}