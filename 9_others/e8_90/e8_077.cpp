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
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;

const ll MAX=1e9+1;
ll get_pos(ll x, ll y){
    if(x<0 || x>=MAX || y<0 || y>=MAX) return -1;
    return y*MAX+x;
}

ll get_dir(ll dx, ll dy){
    if(dx==0){
        if(dy<0) return 7;
        if(dy==0) return -1;
        if(dy>0) return 3;
    }
    if(dx>0){
        if(dy<0) return 8;
        if(dy==0) return 1;
        if(dy>0) return 2;
    }
    if(dx<0){
        if(dy<0) return 6;
        if(dy==0) return 5;
        if(dy>0) return 4;
    }
}

void solve(){
    ll n,t; cin>>n>>t;
    vector<P> al(n);
    vector<P> bl(n);
    unordered_map<ll,ll> mp;
    REP(i,n){
        ll x,y; cin >> x >> y;
        al[i]={x,y};
    }
    REP(i,n){
        ll x,y; cin >> x >> y;
        bl[i]={x,y};
        mp[get_pos(x,y)]=i;
    }

    mf_graph<int> g(2*n+2);
    ll start = 2*n;
    ll goal = 2*n+1;
    REP(i,n){
        g.add_edge(start,i,1);
        g.add_edge(n+i,goal,1);
    }
    REP(i,n){
        auto [x,y]=al[i];
        for(ll dx:{-1,0,1}){
            for(ll dy:{-1,0,1}){
                if(dy==0 && dx==0) continue;
                ll nx=x+dx*t, ny=y+dy*t;
                ll pos=get_pos(nx,ny);
                if(pos==-1)continue;
                if(mp.find(pos)==mp.end()) continue;
                ll target=mp[pos];
                g.add_edge(i,n+target,1);
            }
        }
    }
    ll res=g.flow(start,goal);
    if(res<n){
        cout<<"No"<<endl; return;
    }
    auto edges=g.edges();
    cout<<"Yes"<<endl;
    vector<ll> ansl(n);
    for(auto e:edges){
        if(e.flow==0)continue;
        if(e.from>=n) continue;
        ll from=e.from;
        ll to=e.to;
        // DEBUG(from); DEBUG(to);
        auto [x,y]=al[from];
        auto [x1,y1]=bl[to-n];
        int d=get_dir(x1-x,y1-y);
        // DEBUG(d);
        ansl[from]=d;
    }
    for(int d:ansl){
        cout<<d<<" ";
    }
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}