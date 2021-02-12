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

const double TL = 1900.0;

int D=365;
vector<ll> cl(26); 
vector<vector<ll>> sl(D,vector<ll>(26,0));

struct State{
    ll score;
    vector<ll> tl; // contests
    vector<vector<ll>> each_t_days; // eahc contest_days
    vector<ll> costs;
    State():score(0),each_t_days(26),costs(26){}
};


// ll calc(State &state){
//     ll ans = 0;
//     vector<ll> last_di(26,-1);
//     REP(i,26){state.costs[i]=0;}
//     REP(i,D){
//         int t = state.tl[i];
//         ans += sl[i][t];
//         last_di[t] = i;
//         REP(m,26){
//             state.costs[m] += cl[m]*(i-last_di[m]);
//             ans -= cl[m]*(i-last_di[m]);
//         }
//     }
//     return ans;
// }

void change(State &state, int day, int new_t){
    ll diff = 0;
    int old_t = state.tl[day];
    int prev_old_t = -1;
    int next_old_t = D;
    for(int c_t : state.each_t_days[old_t]){
        if(c_t<day){
            prev_old_t = c_t;
        }
        else if(c_t > day){
            next_old_t = c_t;
            break;
        }
    }
    int d1 = day-prev_old_t;
    int d2 = next_old_t-day;
    int d3 = next_old_t-prev_old_t;
    diff += (d1*(d1-1)+d2*(d2-1))*cl[old_t]/2;
    diff -= d3*(d3-1)*cl[old_t]/2;

    int prev_new_t = -1;
    int next_new_t = D;
    for(int c_t : state.each_t_days[new_t]){
        if(c_t<day){
            prev_new_t = c_t;
        }
        else if(c_t > day){
            next_new_t = c_t;
            break;
        }
    }
    d1 = day-prev_new_t;
    d2 = next_new_t-day;
    d3 = next_new_t-prev_new_t;
    diff -= (d1*(d1-1)+d2*(d2-1))*cl[new_t]/2;
    diff += d3*(d3-1)*cl[new_t]/2;

    diff += sl[day][new_t];
    diff -= sl[day][old_t];

    auto del_ind = find(ALL(state.each_t_days[old_t]),day);
    state.each_t_days[old_t].erase(del_ind);
    state.each_t_days[new_t].push_back(day);
    sort(ALL(state.each_t_days[new_t]));
    state.score += diff;
    state.tl[day] = new_t;
}


void solve(){
    auto start = chrono::system_clock::now();

    cin >> D;
    REP(i,26) cin >> cl[i];
    REP(i,D){
        REP(j,26){
            cin>>sl[i][j];
        }
    }

    State state;

    vector<ll> last_di(26,-1);
    vector<ll> tl;
    REP(day,D){
        double coef = 6.0 - day/500.0;
        ll best_t = 0;
        ll best_val = (-1)*INF;
        REP(t,26){
            ll curr_val = sl[day][t];
            REP(i,26){
                if(i==t)continue;
                curr_val -= (day-last_di[i])*cl[i]*coef;
            }
            if(curr_val >= best_val){
                best_t = t;
                best_val = curr_val; 
            }
        }
        state.tl.push_back(best_t);
        state.each_t_days[best_t].push_back(day);
        last_di[best_t] = day;
        state.score += best_val;
    }

    mt19937_64 mt64(0);
    uniform_int_distribution<int> rand_day(0, D-1);
    uniform_int_distribution<int> rand_type(0, 26-1);
    uniform_int_distribution<int> rand_16(1, 16);
    uniform_real_distribution<double> rand_01(0, 1);

    double T0 = 2000.0;
    double T1 = 600.0;
    auto end = std::chrono::system_clock::now();
    double elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count();
    int cnt=0;
    while(true){
        if(elapsed > TL){
            break;
        }

        if(cnt%1000==0){
            // cout<<elapsed<<endl;
            end = std::chrono::system_clock::now();
            elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count();
        }

        cnt++;
        cnt%=10000;

        double t01 = elapsed/TL;
        double tt = pow(T0,1.0-t01) * pow(T1,t01);

        if(rand_01(mt64)<0.5){
            int day = rand_day(mt64);
            int t = rand_type(mt64);
            int prev_t = state.tl[day];
            ll prev_score = state.score;
            change(state, day, t);
            if(prev_score>state.score){
                ll delta = state.score-prev_score;
                if( rand_01(mt64)>exp(delta/tt) ){ // SA
                    change(state,day,prev_t); // rollback
                }
            }
        }
        else{
            int day1 = rand_day(mt64);
            int day2;
            if(day1<D/2){
                day2 = day1 + rand_16(mt64);
            }
            else{
                day2 = day1 - rand_16(mt64);
            }
            int t1 = state.tl[day1];
            int t2 = state.tl[day2];
            ll prev_score = state.score;
            change(state, day1, t2);
            change(state, day2, t1);
            if(prev_score>state.score){
                ll delta = state.score-prev_score;
                if( rand_01(mt64)>exp(delta/tt) ){ // SA
                    change(state,day1,t1); // rollback
                    change(state,day2,t2); // rollback
                }
            }
        }
    }

    for(int t : state.tl){
        cout << t+1 << '\n';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}