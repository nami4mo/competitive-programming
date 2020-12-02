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

int rhcnt[100001][4];

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};


vector<ll> dijkstra(int start, int n, vector<vector<P>> &g, vector<int> &prev_vl){
    vector<ll> d(n,INF);
    d[start] = 0;
    priority_queue<P, vector<P>, greater<P>> q;
    q.push(P(0,start));

    // vector<int> prev_vl(n,-1);
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
                prev_vl[next_v] = v;
                q.push(P(d[next_v], next_v));
            }
        }
    }
    return d;
}

void solve(){
    string start,goal;
    cin >> start >> goal;
    if(start==goal){
        cout << 0 << endl;
        cout << start << '\n' << start << '\n';
    }
    int len = start.size();
    ll n; cin >> n;
    vector<string> sl(n+2);
    sl[0] = start;
    sl[1] = goal;
    REP(i,n){
        cin >> sl[i+2];
    }
    vector<vector<P>> gl(n+2);
    REP(i,n+2){
        REP(j,n+2){
            if(i==j)continue;
            int cnt = 0;
            REP(l,len){
                if(sl[i][l] != sl[j][l]){
                    cnt++;
                }
            }
            if(cnt==1){
                gl[i].push_back(P(j,1));
            }
        }
    }

    vector<int> prev_vl(n+2,-1);
    vector<ll> dists = dijkstra(0,n+2,gl,prev_vl);
    DEBUGL(prev_vl);
    ll ans = dists[1];
    if(ans==INF){
        cout << -1 << endl;
    }
    else{
        cout << ans-1 << endl;
        vector<int> route;
        int curr_v = 1;
        route.push_back(1);
        while(true){
            int prev_v = prev_vl[curr_v];
            // DEBUG(prev_v);
            if(prev_v==-1){
                break;
            }
            route.push_back(prev_v);
            curr_v = prev_v;
        }
        reverse(ALL(route));
        for(int v : route){
            cout << sl[v] << endl;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}