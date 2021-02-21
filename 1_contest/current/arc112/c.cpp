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


// P {cnt, turn}


vector<P> dp(100001,{-1,-1});
vector<int> chs(100000,-1);

int dfs2(int node, vector<vector<int>> &gl){
    if(chs[node]!=-1)return chs[node];
    int cnt=1;
    for(int neib:gl[node]){
        cnt+=dfs2(neib,gl);
    }
    chs[node]=cnt;
    return cnt;
}

P dfs(int node, vector<vector<int>> &gl){
    int cnt=1;
    int turn=-1; //change
    if(chs[node]%2==0) turn=1;
    else turn=-1;
    vector<int> changes;
    int not_changes_p=0;
    if(gl[node].size()==0){
        dp[node]={1,-1};
        return {1,-1};
    }
    for(int neib:gl[node]){
        P cnt_turn=dfs(neib,gl);
        if(cnt_turn.second==-1){
            changes.push_back(cnt_turn.first);
        }
        else{
            if(cnt_turn.first<0){
                cnt+=cnt_turn.first;
            }
            else{
                not_changes_p+=cnt_turn.first;
            }
        }
    }
    if(changes.size()%2==0)cnt+=not_changes_p;
    else cnt-=not_changes_p;
    sort(ALL(changes));
    for(int i=0 ; i<changes.size(); i++){
        if(i%2==0) cnt+=changes[i];
        else cnt-=changes[i];
    }
    dp[node]={cnt,turn};
    return {cnt,turn};
}


void solve(){
    int n;cin>>n;
    vector<vector<int>> gl(n,vector<int>());
    REP(i,n-1){
        int node=i+1;
        int pare; cin>>pare;
        pare--;
        gl[pare].push_back(node);
    }
    dfs2(0,gl);
    P ansp=dfs(0,gl);
    int ans=(n+ansp.first)/2;
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}