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

vector<ll> dijkstra(int start, int n, vector<vector<P>> &g){
    vector<ll> d(n,INF);
    d[start] = 0;
    priority_queue<P, vector<P>, greater<P>> q;
    q.push(P(0,start));

    while(!q.empty()){
        P dist_v = q.top();
        ll dist = dist_v.first;
        ll v = dist_v.second;
        q.pop();
        if( d[v] < dist ) continue;
        for( P v_cost : g[v] ){
            ll next_v = v_cost.first;
            ll cost = v_cost.second;
            if( d[next_v] > d[v] + cost ){
                d[next_v] = d[v] + cost;
                q.push(P(d[next_v], next_v));
            }
        }
    }
    return d;
}

void solve(){
    ll n,m,t; cin >> n >> m >> t;
    vector<ll> al(n); REP(i,n) cin >> al[i];
    vector<vector<P>> g(n);
    vector<vector<P>> gr(n);
    REP(i,m){
        ll a,b,c; cin >> a >> b >> c;
        a-=1;
        b-=1;
        g[a].push_back(P(b,c));
        gr[b].push_back(P(a,c));
    }
    vector<ll> go_d = dijkstra(0,n,g);
    vector<ll> back_d = dijkstra(0,n,gr);
    ll ans = 0;
    REP(i,n){
        ll rem = t-go_d[i]-back_d[i];
        if(rem <= 0) continue;
        ll val = rem*al[i];
        ans = max(ans,val);
    }
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}