#include <set> 
#include <tuple> 
#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std; 

int dir[6][2] = {{1, 1}, {0, 1}, {-1, 1}, {1, 0}, {-1,0}, {0,-1}};

int dfs(long long curr_num, int prime){
}

int main(){
    int n, x, y; 

    // cin >> n >> x >> y;
    // for( int i = 0 ; i < n ; i++ ){
    //     int ox, oy; 
    //     cin >> ox >> oy;
    //     ol.insert(make_tuple(ox,oy));
    // }
    int ans = bfs(ol,x,y);
    cout << ans << endl;
}