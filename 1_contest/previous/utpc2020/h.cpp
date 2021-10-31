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

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;


void solve(){
    int h,w; cin>>h>>w;
    vector<string> sl(h);
    REP(i,h){
        cin>>sl[i];
    }

    vector<int> row_blacks(h);
    vector<int> col_blacks(w);

    REP(i,h){
        REP(j,w){
            if(sl[i][j]=='#'){
                row_blacks[i]++;
                col_blacks[j]++;
            }
        }
    }
    int ans=0;
    deque<pair<int,int>> q;
    int r_rem=h, c_rem=w;
    vector<bool> r_used(h,false);
    vector<bool> c_used(w,false);
    REP(i,h){
        int l=row_blacks[i];
        if(l==0 || l==w){
            q.push_back({0,i});
            r_used[i]=true;
        }
    }
    REP(j,w){
        int l=col_blacks[j];
        if(l==0 || l==h){
            q.push_back({1,j});
            c_used[j]=true;
        }
    }

    while(!q.empty()){
        auto &[rc,ind]=q.front(); q.pop_front();
        // DEBUG(rc); DEBUG(ind);

        if(r_rem==1){
            ans+=c_rem;
            break;
        }
        else if(c_rem==1){
            ans+=r_rem;
            break;
        }

        ans+=1;
        if(rc==0){ // r
            r_rem--;
            REP(j,w){
                if(c_used[j])continue;
                if(sl[ind][j]=='#') col_blacks[j]--;
                int l=col_blacks[j];
                if(l==0 || l==r_rem){
                    q.push_back({1,j});
                    c_used[j]=true;
                }
            }
        }
        if(rc==1){ // c
            c_rem--;
            REP(i,h){
                if(r_used[i])continue;
                if(sl[i][ind]=='#') row_blacks[i]--;
                int l=row_blacks[i];
                if(l==0 || l==c_rem){
                    q.push_back({0,i});
                    r_used[i]=true;
                }
            }
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