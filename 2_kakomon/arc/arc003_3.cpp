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
    ll h,w; cin >> h >> w;
    vector<vector<int>> cl(h, vector<int>(w,0));
    int sy,sx;
    REP(i,h){
        string s; cin>>s;
        REP(j,w){
            char c=s[j];
            if(c=='s'){
                sy=i,sx=j;
                cl[i][j]=0;
            }
            else if(c=='g') cl[i][j]=10;
            else if(c=='#') cl[i][j]=-1;
            else cl[i][j]=c-'0';
        }
    }
    DEBUG(cl);
    vector<double> t99s;
    double tmp=1.0;
    REP(i,h*w+1){
        t99s.push_back(tmp);
        tmp*=0.99;
    }

    bool reach=false;
    double ok=-1,ng=9.0;
    vector<P> ds={{-1,0},{1,0},{0,-1},{0,1}};
    double EPS=pow(10,-10);
    while(abs(ok-ng)>EPS){
        double mid=(ok+ng)/2.0;
        bool res=false;
        deque<P> q;
        vector<vector<int>> dists(h, vector<int>(w,-1));
        dists[sy][sx]=0;
        q.push_back({sy,sx});
        while(!q.empty()){
            auto [py,px]=q.front(); q.pop_front();
            int pd=dists[py][px];
            for(auto &[dy,dx]:ds){
                int yy=py+dy,xx=px+dx;
                if(yy<0||h<=yy||xx<0||w<=xx) continue;
                if(dists[yy][xx]!=-1) continue;
                if(cl[yy][xx]==10){
                    res=true;break;
                }
                if(cl[yy][xx]==-1)continue;
                if(cl[yy][xx]*t99s[pd+1]<mid) continue;
                dists[yy][xx]=pd+1;
                q.push_back({yy,xx});
            }
            if(res)break;
        }
        if(res) {
            ok=mid; reach=true;
        } 
        else ng=mid;
    }
    if(!reach) cout<<-1<<endl;
    else cout<<setprecision(18)<<ok<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}