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
    template<class T> void dbg(string name, multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x;cerr<<'\n';}
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

int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};

double dp[65536];
bool visited[65536];

double rec(ll state){
    if(visited[state]){
        return dp[state];
    }

    bool flag[4][4]={false,};
    Fill(flag,false);
    int all_cnt=0;
    REP(i,16){
        if( (state>>i)%2==1 ){
            int y=i/4;
            int x=i%4;
            flag[y][x] = true;
            all_cnt++;
        }
    }
    if(all_cnt==0){
        visited[state]=true;
        dp[state]=0.0;
        return 0.0;
    }
    if(all_cnt==1){
        visited[state]=true;
        dp[state]=5.0;
        return 5.0;
    }

    double res=1000.0;
    REP(y,4){
        REP(x,4){
            int c_cnt=0;
            vector<int> neibs;
            if(flag[y][x]){
                c_cnt++;
                neibs.push_back(y*4+x);
            }
            REP(i,4){
                int dyy=dy[i];
                int dxx=dx[i];
                int yy=y+dyy;
                int xx=x+dxx;
                if(yy<0||yy>=4||xx<0||xx>=4)continue;
                if(flag[yy][xx]){
                    c_cnt++;
                    neibs.push_back(yy*4+xx);
                }
            }
            if(c_cnt==0)continue;
            // DEBUG(neibs);
            // DEBUG(c_cnt);
            double c_res=0.0;
            for(int neib:neibs){
                c_res+=5.0/c_cnt;
                c_res+=rec(state-pow(2,neib));
            }
            c_res/=c_cnt;
            res=min(res,c_res);
        }
    }
    visited[state]=true;
    dp[state]=res;
    return res;
}

void solve(){
    Fill(dp, 1000.0);
    Fill(visited,false);
    ll state=0;
    REP(i,4){
        string s; cin>>s;
        REP(j,4){
            char c=s[j];
            int pos=i*4+j;
            if(c=='#'){
                state+=pow(2,pos);
            }
        }
    }
    // cout<<rec(state)<<endl;
    printf("%.8f\n",rec(state));
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}