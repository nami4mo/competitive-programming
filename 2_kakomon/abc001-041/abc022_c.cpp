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

void solve(){
    ll n,m; cin >> n >> m;
    vector<P> neibs;
    vector<vector<ll>> d(n,vector<ll>(n,INF));
    REP(i,m){
        ll u,v,l; cin >> u >> v >> l;
        u-=1;
        v-=1;
        if(u==0){
            neibs.push_back(P(v,l));
        }
        else{
            d[u][v]=l;
            d[v][u]=l;
        }
    }
    REP(i,n){
        REP(j,n){
            REP(k,n){
                d[j][k] = min(d[j][k], d[j][i]+d[i][k]);
            }
        }
    }

    ll ans = INF;
    int len = neibs.size();
    if(len < 2){
        cout << -1 << endl;
    }
    else{
        FOR(i,0,len-1){
            FOR(j,i+1,len){
                ll v = neibs[i].second + neibs[j].second + d[neibs[i].first][neibs[j].first];
                ans = min(ans,v);
            }
        }
        if(ans>=INF){
            cout << -1 << endl;
        }
        else{
            cout << ans << endl;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}