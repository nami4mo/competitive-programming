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

ll p2i(int x1, int x2){
    return (1e7)*x1+x2;
}

unordered_map<ll,ll> x2i;
unordered_map<ll,ll> y2i;

ll rec(int x1, int x2, int y1, int y2, vector<vector<ll>> &dp, vector<P> &xyl){

    vector<P> inarea;
    if(dp[x2i[p2i(x1,x2)]][y2i[p2i(y1,y2)]]!=-1){
        return dp[x2i[p2i(x1,x2)]][y2i[p2i(y1,y2)]];
    }
    for(auto &[x,y]:xyl){
        if(x1<=x && x<x2 && y1<=y && y<y2){
            inarea.push_back({x,y});
        }
    }
    if(inarea.empty()){
        dp[x2i[p2i(x1,x2)]][y2i[p2i(y1,y2)]]=0;
        return 0;
    }
    ll res=-1;
    for(auto &[x,y]:inarea){
        ll score=(x2-x1+y2-y1-1)+rec(x1,x,y1,y,dp,xyl)+rec(x+1,x2,y1,y,dp,xyl)+rec(x1,x,y+1,y2,dp,xyl)+rec(x+1,x2,y+1,y2,dp,xyl);
        res=max(res,score);
    }
    dp[x2i[p2i(x1,x2)]][y2i[p2i(y1,y2)]]=res;
    return res;
}

void solve(){
    ll w,h; cin >> w >> h;
    ll n;cin>>n;
    vector<P> xyl;
    vector<ll> xl;
    vector<ll> yl;
    REP(i,n){
        ll x,y; cin >> x >> y;
        xyl.push_back({x,y});
        xl.push_back(x);
        yl.push_back(y);
    }

    sort(ALL(xl)); 
    vector<ll> xstarts={1};
    vector<ll> xends;
    for(ll x:xl){
        xstarts.push_back(x+1);
        xends.push_back(x);
    }
    xends.push_back(w+1);
    vector<P> xps;
    int ind=0;
    for(ll xs:xstarts){
        for(ll xe:xends){
            if(xs<=xe) {
                xps.push_back({xs,xe});
                x2i[p2i(xs,xe)]=ind;
                ind++;
            }
        }
    }

    sort(ALL(yl)); 
    vector<ll> ystarts={1};
    vector<ll> yends;
    for(ll y:yl){
        ystarts.push_back(y+1);
        yends.push_back(y);
    }
    yends.push_back(h+1);
    vector<P> yps;
    ind=0;
    for(ll ys:ystarts){
        for(ll ye:yends){
            if(ys<=ye) {
                yps.push_back({ys,ye});
                y2i[p2i(ys,ye)]=ind;
                ind++;
            }
        }
    }

    vector<vector<ll>> dp(x2i.size(), vector<ll>(y2i.size(),-1));
    ll ans=rec(1,w+1,1,h+1,dp,xyl);
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}