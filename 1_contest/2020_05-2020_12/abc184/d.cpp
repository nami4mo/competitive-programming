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
    ll h,w; cin >> h >> w;
    char c; 
    char al[2000][2000];

    REP(i,h){
        REP(j,w){
            cin >> c;
            al[i][j] = c;
        }
    }

    ll s = -1;
    ll goal = -1;
    vector<vector<P>> g(h*w+26, vector<P>(0));
    REP(hi,h){
        REP(wi,w){
            char curr = al[hi][wi];
            if(curr=='#') continue;
            ll u = hi*w+wi;
            if(curr == 'S') s = u;
            else if(curr=='G') goal = u;
            else if(curr!='.'){
                ll super_v = curr-'a';
                super_v += h*w;
                g[super_v].push_back(P(u,0));
                g[u].push_back(P(super_v,1));
            }

            if(hi+1<h && al[hi+1][wi] != '#'){
                ll v = (hi+1)*w+wi;
                g[u].push_back(P(v,1));
                g[v].push_back(P(u,1));
            }
            if(wi+1<w && al[hi][wi+1] != '#'){
                ll v = hi*w+wi+1;
                g[u].push_back(P(v,1));
                g[v].push_back(P(u,1));
            }
        }
    }
    
    vector<ll> ansd = dijkstra(s, h*w+26, g);
    ll ans = ansd[goal];
    if(ans==INF) ans = -1;
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}