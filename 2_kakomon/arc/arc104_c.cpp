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

const int INF = 1'001'001'001;
// const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;


int n;
vector<vector<int>> dp(210,vector<int>(210,-1));
vector<int> a2b(210, INF);
vector<int> b2a(210, INF);

int rec(int l, int r){
    // DEBUG(l);
    // DEBUG(r);
    if(r-l==0) return 0;
    if((r-l)%2==0) return 0;
    if(dp[l][r]!=-1) return dp[l][r];

    int d=(r-l+1)/2;
    bool res=true;
    REP(i,d){
        int li=l+i;
        int ri=li+d;
        if(a2b[li]==ri) continue;
        if(a2b[li]==INF && b2a[ri]==INF) continue;
        if(a2b[li]==-1 && b2a[ri]==INF) continue;
        if(a2b[li]==INF && b2a[ri]==-1) continue;
        res=false;
        break;
    }
    if(res){
        dp[l][r]=1;
        return 1;
    }
    if(r-l==1){
        dp[l][r]=0;
        return 0;
    }

    for(int i=l+1; i<r; i++){
        int v=rec(l,i)*rec(i+1,r);
        if(v==1) {
            dp[l][r]=1;
            return 1;
        }
    }
    dp[l][r]=0;
    return 0;
}

void solve(){
    cin >> n;
    REP(i,n){
        int a,b;cin>>a>>b;
        if(a!=-1) a--;
        if(b!=-1) b--;
        // DEBUG(a);
        // DEBUG(b);
        if(a>=b && a!=-1 && b!=-1){cout<<"No"<<endl;return;}
        if(a==-1&&b==-1){
            continue;
        }
        if(a!=-1){
            if(a2b[a]!=INF){cout<<"No"<<endl;return;}
            a2b[a]=b;
        }
        if(b!=-1){
            if(b2a[b]!=INF){cout<<"No"<<endl;return;}
            b2a[b]=a;
        }
    }
    int res=rec(0,2*n-1);
    if(res==1) cout<<"Yes"<<endl;
    else cout<<"No"<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}