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
    int h,w; cin>>h>>w;
    vector<vector<char>> cl(h, vector<char>(w,'.'));
    REP(i,h)REP(j,w) cin>>cl[i][j];
    vector<vector<bool>> visited(h, vector<bool>(w,false));
    int ac=0,bc=0,cc=0;
    REP(i,h){
        REP(j,w){
            int cnt=1;
            ll minx=100000, maxx=-1;
            deque<P> q;
            if(visited[i][j] || cl[i][j]=='.') continue;
            q.push_back({i,j});
            minx=min(minx,j); maxx=max(maxx,j);
            visited[i][j]=true;
            while(!q.empty()){
                auto [y,x]=q.front(); q.pop_front();
                for(ll dx:{-1,0,1}){
                    for(ll dy:{-1,0,1}){
                        ll yy=y+dy, xx=x+dx;
                        if(yy<0||h<=y||xx<0||w<=x) continue;
                        if(visited[yy][xx] || cl[yy][xx]=='.') continue;
                        q.push_back({yy,xx});
                        minx=min(minx,xx); maxx=max(maxx,xx);
                        cnt+=1;
                        visited[yy][xx]=true;
                    }
                }
            }
            ll dist=maxx-minx+1;
            ll ratio=dist/5;
            ratio*=ratio;
            // DEBUG(maxx); DEBUG(minx); DEBUG(cnt);
            if(cnt/ratio==12)ac++;
            if(cnt/ratio==16)bc++;
            if(cnt/ratio==11)cc++;
        }
    }
    cout<<ac<<" "<<bc<<" "<<cc<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}