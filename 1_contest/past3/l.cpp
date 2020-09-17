#include <bits/stdc++.h>
#include <cmath>

using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<ll,ll> P;
    #define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
    #define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
    #define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(),x.end()

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
const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    int n; cin >> n;

    set<int> s1;
    set<int> s2;
    vector<deque<int>> tql(n);
    unordered_map<int, int> t_to_im;
    vector<int> i_to_t2(n,-1);

    REP(i,n){
        int k; cin >> k;
        REP(j,k){
            int t; cin >> t;
            t_to_im[t] = i;
            if(j == 0) {
                s1.insert(t);
            }
            else if(j == 1){
                i_to_t2[i] = t;
                s2.insert(t);
            }
            else{
                tql[i].push_back(t);
            }

        }
    }
    int m; cin >> m;
    REP(i,m){
        int a; cin >> a;

        int smax1 = *s1.rbegin();
        int smax2 = -1;
        if( s2.size() > 0 ){
            smax2 = *s2.rbegin();
        }

        if( a == 1 || smax1 > smax2 ){
            cout << smax1 << endl;
            s1.erase(smax1);
            int poped_i = t_to_im[smax1];
            int s2_val = i_to_t2[poped_i];
            if(s2_val != -1){
                s2.erase(s2_val);
                s1.insert(s2_val);
            }
            if(tql[poped_i].size() > 0){
                int poped_v = tql[poped_i].front();
                tql[poped_i].pop_front();
                i_to_t2[poped_i] = poped_v;
                s2.insert(poped_v);
            }else{
                i_to_t2[poped_i] = -1;
            }
        } 
        else {
            cout << smax2 << endl;
            s2.erase(smax2);
            int poped_i = t_to_im[smax2];
            if(tql[poped_i].size() > 0){
                int poped_v = tql[poped_i].front();
                tql[poped_i].pop_front();
                i_to_t2[poped_i] = poped_v;
                s2.insert(poped_v);
            }else{
                i_to_t2[poped_i] = -1;
            }
        }
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}