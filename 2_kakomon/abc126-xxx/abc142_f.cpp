#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef long long ll;
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

vector<int> get_shortest_path(int start, vector<vector<int>> &gl, int n){
    vector<int> prevs(n+1,-1);
    vector<bool> visited(n+1, false);
    deque<int> q;
    bool ok = false;
    q.push_back(start);
    while(!q.empty()){
        int node = q.front(); q.pop_front();
        for(int neib : gl[node]){
            if(visited[neib])continue;
            visited[neib] = true;
            q.push_back(neib);
            prevs[neib] = node;
            if(neib==start){
                ok = true;
                break;
            }
        }
    }

    // DEBUGL(prevs);

    if(ok){
        vector<int> ansl;
        int c_node = start;
        while(true){
            int prev = prevs[c_node];
            ansl.push_back(prev);
            c_node = prev;
            if(c_node==start)break;
        }
        return ansl;
    }
    else{
        return vector<int>(1,-1);
    }
}

void solve(){
    int n,m; cin >> n >> m;
    vector<vector<int>> gl(n+1);
    REP(i,m){
        int a,b; cin >> a >> b;
        gl[a].push_back(b);
    }

    vector<int> ansl(10000,-1);
    REP(i,n+1){
        vector<int> c_ansl = get_shortest_path(i, gl, n);
        if(c_ansl[0]==-1)continue;
        if(ansl.size()>c_ansl.size()){
            ansl = c_ansl;
        }
    }
    if(ansl[0]==-1){
        cout<<-1<<endl;
    }
    else{
        cout<<ansl.size()<<'\n';
        for(int a:ansl){
            cout<<a<<'\n';
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}