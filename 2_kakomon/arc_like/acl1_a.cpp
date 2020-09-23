#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
#endif
using namespace std;
using namespace atcoder;
namespace defines{
    typedef long long ll;
    typedef pair<ll,ll> P;
    #define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
    #define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
    #define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(),x.end()
    template<class T> vector<T> make_vec(size_t a){return vector<T>(a);}
    template<class T, class... Ts> auto make_vec(size_t a, Ts... ts){ return vector<decltype(make_vec<T>(ts...))>(a, make_vec<T>(ts...));}

    /* for debug print */
    #define DEBUG(x) cerr << #x << ": " << x << '\n'
    #define DEBUGP(x) cerr << #x << ": (" << x.first << ", " << x.second << ")" << '\n' 
    #define DEBUGS(s) dbgs_f(#s,s)
    #define DEBUGL(xl) dbgl_f(#xl,xl)
    #define DEBUGLP(xl) dbglp_f(#xl,xl)
    #define DEBUGLL(xll) dbgll_f(#xll,xll)
    #define DEBUGM(xl) dbgm_f(#xl,xl)
    template<class T> void dbgs_f(string name, set<T> s){cerr<<name<<": "; for(T x: s) cerr<<x<<" "; cerr << '\n';}
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

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    int n; cin >> n;
    dsu d(n);
    set<int> min_ys;
    set<int> rem_ys;
    vector<tuple<int,int,int>> xyil;
    vector<int> ansl(n);
    vector<int> y_to_x(n);
    vector<int> i_to_y(n);

    REP(i,n){
        int x,y; cin >> x >> y;
        x-=1;
        y-=1;
        xyil.push_back(make_tuple(x,y,i));
        rem_ys.insert(y);
        y_to_x[y] = x;
        i_to_y[i] = y;
    }
    sort(ALL(xyil));
    
    // DEBUG(n);
    for( tuple<int,int,int> xyi : xyil ){
        int x = get<0>(xyi);
        int y = get<1>(xyi);
        int i = get<2>(xyi);
        // cerr << endl;
        // DEBUG(i);
        // DEBUG(x);
        // DEBUG(y);
        rem_ys.erase(y);
        int min_y = y;
        auto iter = min_ys.lower_bound(y);
        vector<int> to_erase;
        if( iter != min_ys.begin()){
            while( min_ys.begin() != iter-- ){
                int merged_y = *iter;
                int merged_x = y_to_x[merged_y];
                // DEBUG(merged_y);
                d.merge(y,merged_y);
                // min_ys.erase(merged_y);
                to_erase.push_back(merged_y);
                min_y = merged_y;
            }
        }
        for( int erase_y : to_erase ){
            min_ys.erase(erase_y);
        }
        min_ys.insert(min_y);

        // DEBUGS(min_ys);
        // DEBUGS(rem_ys);
        int front_cnt = d.size(y);
        auto iter2 = rem_ys.upper_bound(min_y);
        int back_cnt = rem_ys.size() - distance(rem_ys.begin(), iter2);
        // DEBUG(front_cnt);
        // DEBUG(back_cnt);
        // ansl[i] = front_cnt + back_cnt;
    }
    REP(i,n){
        int cy = i_to_y[i];
        cout << d.size(cy) << endl;
    }

    // for( int a : ansl ){
    //     cout << a << endl;
    // }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}