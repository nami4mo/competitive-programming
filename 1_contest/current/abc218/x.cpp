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
    #define DEBUG(x) dbg(#x,x)
    template<class T> void dbg(string name, T x){cerr<<name<<": "<<x<<"\n";}
    template<> void dbg<P>(string name, P x){cerr<<name<<": ("<<x.first<<","<<x.second<<")\n";}
    template<class T> void dbg(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr<<'\n';}
    template<> void dbg<P>(string name, vector<P> xl){cerr<<name<<": "; for(P x:xl){cerr<<"("<<x.first<<","<<x.second<<"), ";}cerr<<"\n";}
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
const ll INF = 1'001'001'001'001ll;
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;

struct Res{
    vector<ll> dist;
    vector<ll> route;
};

Res dijkstra(int start, int n, vector<vector<P>> &g, bool ro=false, int not_u=-1, int not_v=-1){
    vector<ll> d(n,INF);
    d[start] = 0;
    priority_queue<P, vector<P>, greater<P>> q;
    q.push(P(0,start));

    // DEBUG(start);

    vector<ll> prev_vl(n,-1);
    // DEBUG(d);
    while(!q.empty()){
        P dist_v = q.top();
        ll dist = dist_v.first;
        ll v = dist_v.second;
        q.pop();
        if( d[v] < dist ) continue;
        for( P v_cost : g[v] ){
            ll next_v = v_cost.first;
            ll cost = v_cost.second;
            // DEBUG(v);
            // DEBUG(next_v);
            if(not_u==v && not_v==next_v) continue;
            // cost = INF;
            if( d[next_v] > d[v] + cost){
                d[next_v] = d[v] + cost;
                prev_vl[next_v] = v;
                q.push(P(d[next_v], next_v));
            }
        }
    }

    Res res;
    res.dist=d;
    if(ro){
        ll goal = n-1;
        vector<ll> route = {goal};
        ll curr_v = goal;
        while(true){
            int prev_v = prev_vl[curr_v];
            if (prev_v == -1)break;
            route.push_back(prev_v);
            curr_v = prev_v;
        }
        reverse(ALL(route));
        res.route=route;
    }
    // DEBUG(start);


    return res;
}


void solve(){
    ll n,m; cin>>n>>m;
    vector<vector<P>> gl(n);
    vector<ll> ansl(m,-1);
    vector<vector<ll>> st2edge(n,vector<ll>(n,-1));

    REP(i,m){
        ll s,t; cin >> s >> t;
        s--; t--;
        gl[s].push_back({t,1});
        st2edge[s][t]=i;
    }
    // DEBUG(n);
    Res res=dijkstra(0,n,gl,true);
    // DEBUG(res.dist);
    // DEBUG(res.route);
    ll normal_dist=res.dist[n-1];
    if(normal_dist>=INF){
        REP(i,m){
            cout<<-1<<'\n';
        }
        return;
    }
    REP(i,m){
        ansl[i]=normal_dist;
    }

    REP(i, res.route.size()-1){
        ll u=res.route[i];
        ll v=res.route[i+1];
        ll ei = st2edge[u][v];
        Res c_res=dijkstra(0,n,gl,false,u,v);
        ll dist=c_res.dist[n-1];
        if(dist>=INF) dist=-1;
        ansl[ei]=dist;
    }
    REP(i,m){
        // ansl[i]=normal_dist;
        ll ans=ansl[i];
        if(ans>=INF) ans=-1;
        cout<<ans<<'\n';
    }


}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}