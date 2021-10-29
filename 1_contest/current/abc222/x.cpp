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

vector<vector<ll>> gl_num(1000,vector<ll>(1000,-1));
bool finish=false;

void dfs(int node, int pare, vector<vector<ll>> &gl, vector<ll> &routes, ll to, vector<ll> &cnts){
    if(finish)return;
    routes.push_back(node);
    if(node==to){
        int len=routes.size();
        REP(i,len-1){
            ll u=routes[i];
            ll v=routes[i+1];
            ll num=gl_num[u][v];
            // DEBUG(num);
            cnts[num]++;
        }
        finish=true;
        // DEBUG(routes);
    }
    for(int neib:gl[node]){
        if(neib==pare)continue;
        dfs(neib,node,gl,routes,to,cnts);
    }
    routes.pop_back();
}

void solve(){
    ll n,m,k; cin >> n >> m >> k;
    vector<ll> al(m); REP(i,m) cin >> al[i];
    vector<vector<ll>> gl(n);

    REP(i,n-1){
        ll u,v; cin >> u >> v;
        u--; v--;
        gl[u].push_back(v);
        gl[v].push_back(u);
        gl_num[u][v]=i;
        gl_num[v][u]=i;
    }

    if(n==2){

    }

    vector<ll> cnts(n-1,0);
    int curr=al[0]-1;
    REP(i,m-1){
        finish=false;
        ll to=al[i+1];
        to--;
        // DEBUG(curr,to);
        vector<ll> routes;
        // routes.push_back(curr);
        dfs(curr,-1,gl,routes,to,cnts);
        curr=to;
        // DEBUG(cnts);
    }
    // DEBUG(cnts);
    ll dsum=0;
    for(int v:cnts) dsum+=v;
    if( (dsum+k)%2!=0 ){
        cout<<0<<endl;
        return;
    }
    ll rcnt=(dsum+k)/2;
    if(rcnt<0){
        cout<<0<<endl;
        return;
    }
    vector<vector<ll>> dp(n, vector<ll>(rcnt+1,0));
    dp[0][0]=1;
    REP(i,n-1){
        ll a=cnts[i];
        // vector<ll> mods(a,0);
        REP(j,rcnt+1){
            dp[i+1][j]+=dp[i][j];
            dp[i+1][j]%=MOD;
            if(j+a<=rcnt){
                dp[i+1][j+a]+=dp[i][j];
                dp[i+1][j+a]%=MOD;
            }
            // mods[j%a]+=dp[i][j];
            // mods[j%a]%=MOD;
            // dp[i+1][j]+=mods[j%a];
            // dp[i+1][j]%=MOD;
        }
    }
    ll ans=dp[n-1][rcnt];
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}   