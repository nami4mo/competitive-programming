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

void solve(){
    ll n,m; cin >> n >> m;
    vector<tuple<ll,ll,ll>> abcl;
    vector<tuple<ll,ll,ll>> defl;
    set<ll> stx={0};
    set<ll> sty={0};
    REP(i,n){
        ll a,b,c; cin >> a >> b >> c;
        abcl.push_back({a,b,c});
        stx.insert(a);
        stx.insert(b);
        sty.insert(c);
    } 
    REP(i,m){
        ll a,b,c; cin >> a >> b >> c;
        defl.push_back({a,b,c});
        stx.insert(a);
        sty.insert(b);
        sty.insert(c);
    } 
    unordered_map<ll,ll> x2x;
    unordered_map<ll,ll> y2y;
    vector<ll> x2orig;
    vector<ll> y2orig;
    int cnt=0;
    for(ll x:stx){
        x2x[x]=cnt;
        x2orig.push_back(x);
        cnt++;
    }
    cnt=0;
    for(ll y:sty){
        y2y[y]=cnt;
        y2orig.push_back(y);
        cnt++;
    }

    ll xlen=x2x.size();
    ll ylen=y2y.size();
    vector<vector<bool>> syl(xlen+1, vector<bool>(ylen+1,true));
    vector<vector<bool>> sxl(xlen+1, vector<bool>(ylen+1,true));
    for(auto&[x1,x2,y]:abcl){
        for(int i=x2x[x1]+1; i<=x2x[x2] ; i++){
            syl[i][y2y[y]]=false;
        }
    }
    for(auto&[x,y1,y2]:defl){
        for(int i=y2y[y1]+1; i<=y2y[y2] ; i++){
            sxl[x2x[x]][i]=false;
        }
    }

    DEBUG(x2x);
    DEBUG(y2y);

    ll ans=0;
    deque<P> q;
    P start={x2x[0],y2y[0]};
    q.push_back(start);
    // TODO

    if(start.first==0 || start.second==0){
        cout<<"INF"<<endl;
        return;
    }
    ans+=x2orig[start.first-1]*y2orig[start.second-1];

    // DEBUG(ans);
    vector<vector<bool>> visited(xlen+1, vector<bool>(ylen+1,false));
    visited[start.first][start.second]=true;
    // DEBUG(sl);
    int loop=0;
    while(!q.empty()){
        // cout<<"-----"<<endl;
        // for(P p:q){
        //     DEBUG(p);
        //     // DEBUG(y);
        // }
        P poped=q.front(); q.pop_front();
        auto& [px,py]=poped;
        // if(px==2)
        if(px-1>=0){
            if(sxl[px-1][py] && !visited[px-1][py]){
                if(px-1==0){
                    cout<<"INF"<<endl;
                    return;
                }
                int dy=y2orig[py]-y2orig[py-1];
                int dx=x2orig[px-1]-x2orig[px-2];
                ans+=dy*dx;
                q.push_back({px-1,py});
                visited[px-1][py]=true;
            }
        }
        if(py-1>=0){
            if(syl[px][py-1] && !visited[px][py-1]){
                if(py-1==0){
                    cout<<"INF"<<endl;
                    return;
                }
                int dy=y2orig[py-1]-y2orig[py-2];
                int dx=x2orig[px]-x2orig[px-1];
                ans+=dy*dx;
                q.push_back({px,py-1});
                visited[px][py-1]=true;
            }
        }
        if(px+1<xlen){
            if(sxl[px][py] && !visited[px+1][py]){
                int dy=y2orig[py]-y2orig[py-1];
                int dx=x2orig[px+1]-x2orig[px];
                ans+=dy*dx;
                q.push_back({px+1,py});
                visited[px+1][py]=true;
            }
        }
        if(py+1<ylen){
            if(syl[px][py] && !visited[px][py+1]){
                int dy=y2orig[py+1]-y2orig[py];
                int dx=x2orig[px]-x2orig[px-1];
                ans+=dy*dx;
                q.push_back({px,py+1});
                visited[px][py+1]=true;
            }
        }
        loop++;
        if(loop>1e7){
            cout<<"INF"<<endl;
            return;
        }
    }
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}