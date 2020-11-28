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
const ll INF = 1'001'001'001'001'001ll;
const int MOD = 1'000'000'007;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

void solve(){
    ll n,k; cin >> n >> k;
    vector<vector<ll>> al(n, vector<ll>(n));
    REP(i,n){REP(j,n){ cin >> al[i][j]; }}
    mcf_graph<ll,ll> mg(n*2+2);
    int s = n*2;
    int t = n*2+1;
    mg.add_edge(s,t,n*k,INF);
    REP(i,n){
        mg.add_edge(s,i,k,0);
        mg.add_edge(n+i,t,k,0);
    }
    REP(i,n){
        REP(j,n){
            ll a = al[i][j];
            mg.add_edge(i, n+j, 1, INF-a);
        }
    }
    P ansp = mg.flow(s,t, n*k);
    ll ans = INF*n*k - ansp.second;
    cout<<ans<<endl;
    vector<vector<char>> ansl(n, vector<char>(n,'.'));
    for(auto e : mg.edges()){
        if(e.flow==0)continue;
        if(e.from < n){
            ansl[e.from][e.to-n] = 'X';
        }
    }
    REP(i,n){
        REP(j,n){
            cout<<ansl[i][j];
        }
        cout<<'\n';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}