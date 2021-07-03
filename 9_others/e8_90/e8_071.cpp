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

int n;
int k;
int pat=0;
vector<vector<int>> ansl;

bool dfs(unordered_set<int> &st, vector<vector<int>> &gl, vector<int> &deg, vector<int> &route, int depth){
    // DEBUG(st);
    if(ansl.size()==k) return true;
    
    if(depth==n){
        ansl.push_back(route);
        return true;
    }

    // if(st.empty()) return false;
    if(st.empty()){
        cout<<-1<<endl;
        exit(0);
    }

    vector<int> nodes;
    int cnt=0;
    for(int node:st) {
        nodes.push_back(node);
        if(cnt++>15) break;
    }

    for(int node:nodes){
        if(ansl.size()==k) return true;
        vector<int> new_nodes;

        //// choose "node"
        st.erase(st.find(node));
        for(int neib: gl[node]){
            if(ansl.size()==k) return true;
            deg[neib]--;
            if(deg[neib]==0){
                new_nodes.push_back(neib);
                st.insert(neib);
            }
        }
        route.push_back(node);

        //// dfs
        bool ret = dfs(st, gl, deg, route, depth+1);
        // if(!ret) return false;

        //// rollback
        for(int neib: gl[node]){
            deg[neib]++;
        }
        for(int new_n : new_nodes){
            st.erase(st.find(new_n));
        }
        st.insert(node);
        route.pop_back();
    }
    return true;
}


void solve(){
    ll m; cin >> n >> m >> k;
    vector<vector<int>> gl(n);
    vector<int> deg(n);
    REP(i,m){
        ll a,b; cin >> a >> b;
        a--; b--;
        gl[a].push_back(b);
        deg[b]++;
    }

    unordered_set<int> st;
    REP(i,n){
        if(deg[i]==0) st.insert(i);
    }

    vector<int> route;
    dfs(st,gl,deg,route,0);
    if(ansl.size()==k){
        for(vector<int> al:ansl){
            for(int a:al) cout<<a+1<<" ";
            cout<<endl;
        }
    }
    else{
        cout<<-1<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}