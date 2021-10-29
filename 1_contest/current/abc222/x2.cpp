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
    template<typename A, size_t N, typename T> void Fill(A (&array)[N], const T &val){std::fill( (T*)array, (T*)(array+N), val );}

    /* for debug */
    void NEWLINE(){cerr<<'\n';}
    void COMMA(){cerr<<", ";}
    #define DEBUG1(x) dbg(#x,x); NEWLINE();
    #define DEBUG2(x1,x2) dbg(#x1,x1); COMMA(); dbg(#x2,x2); NEWLINE();
    #define DEBUG3(x1,x2,x3) dbg(#x1,x1); COMMA(); dbg(#x2,x2); COMMA(); dbg(#x3,x3); NEWLINE();
    #define DEBUG4(x1,x2,x3,x4) dbg(#x1,x1); COMMA(); dbg(#x2,x2); COMMA(); dbg(#x3,x3); COMMA(); dbg(#x4,x4); NEWLINE();
    #define DEBUG_OVERLOAD(x1, x2, x3, x4, x5, ...) x5
    #define DEBUG(...) DEBUG_OVERLOAD(__VA_ARGS__, DEBUG4, DEBUG3, DEBUG2, DEBUG1)(__VA_ARGS__)
    template<class T> void dbg(string name, T x){cerr<<name<<": "<<x<<"";}
    template<> void dbg<P>(string name, P x){cerr<<name<<": ("<<x.first<<","<<x.second<<")";}
    template<class T> void dbg(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr<<"";}
    template<> void dbg<P>(string name, vector<P> xl){cerr<<name<<": "; for(P x:xl){cerr<<"("<<x.first<<","<<x.second<<"), ";}cerr<<"";}
    template<class T> void dbg(string name, vector<vector<T>> xl){ cerr<<name<<": \n"; int ml=1;for(vector<T> row: xl){for(T x:row){stringstream sstm; sstm<<x; ml=max(ml,(int)sstm.str().size());}}; for(vector<T> row: xl){{for(T x:row) cerr<<std::right<<std::setw(ml+1)<<x;} cerr << '\n';}}
    template<class T> void dbg(string name, set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, unordered_set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, unordered_multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x;cerr<<'\n';}
    template<class T, class U> void dbg(string name, map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
    template<class T, class U> void dbg(string name, unordered_map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
// const int MOD = 1'000'000'007;
const ll MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;

const int MAX=200100;
vector<ll> dp(MAX,-1);
vector<vector<P>> gl(MAX);
vector<ll> dl(MAX,0);

ll dfs(int node, int pare){
    ll res=dl[node];
    for(auto &[neib,cost]:gl[node]){
        if(neib==pare)continue;
        res=max({res, dfs(neib,node)+cost, dl[neib]});
    }
    dp[node]=res;
    return res;
}

void dfs2(int node, int pare, ll pare_v){
    vector<ll> vals;
    for(auto &[neib,cost]:gl[node]){
        if(neib==pare)continue;
        vals.push_back(dp[neib]+cost);
    }

    vector<ll> lsum={0};
    ll curr=0;
    ll res=0;
    for(ll v:vals){
        curr=max(curr,v);
        lsum.push_back(curr);
    }

    vector<ll> rsum={0};
    curr=0;
    reverse(ALL(vals));
    for(ll v:vals){
        curr=max(curr,v);
        rsum.push_back(curr);
    }

    res=curr;
    dp[node]=max({res,pare_v});
    int ind=0;
    
    for(auto &[neib,cost]:gl[node]){
        if(neib==pare)continue;
        ll lmax=lsum[ind];
        ll rmax=rsum[rsum.size()-2-ind];
        ll c_max=max({lmax,rmax,pare_v});
        ll c_pare_v=max({c_max+cost, cost+dl[node]});
        dfs2(neib,node,c_pare_v);
        ind++;
    }
    
}

void solve(){
    ll n; cin >> n;
    // vector<vector<P>> gl(n);
    REP(i,n-1){
        ll a,b,c; cin >> a >> b >> c;
        a--;b--;
        gl[a].push_back({b,c});
        gl[b].push_back({a,c});
    }
    REP(i,n) cin >> dl[i];
    dp[0]=0;
    dfs(0,-1);
    // DEBUG(dp);
    // REP(i,n){
    //     ans[0]=max(ans[0],dp[i]);
    // }
    DEBUG(dp);
    dfs2(0,-1,0);
    REP(i,n){
        cout<<dp[i]<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}   