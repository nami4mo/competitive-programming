#include <set> 
#include <tuple> 
#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std; 

int dir[6][2] = {{1, 1}, {0, 1}, {-1, 1}, {1, 0}, {-1,0}, {0,-1}};

int bfs(set< std::tuple<int, int>> ol, int gx, int gy){
    map< tuple<int, int>, int> visited;
    queue< tuple<int, int>> que;
    visited[make_tuple(0,0)] = 0;
    que.push(make_tuple(0,0));
    while (!que.empty()) {
        tuple<int, int> v = que.front();
        int x = get<0>(v);
        int y = get<1>(v);
        que.pop();
        if( x == gx && y == gy){
            return visited[make_tuple(gx,gy)];
        }
        for( int i = 0 ; i < 6 ; i++ ){
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];
            tuple<int, int> nxy = make_tuple(nx,ny);
            if( ol.find( nxy ) == ol.end() && visited.find( nxy ) == visited.end()){
                visited[nxy] = visited[make_tuple(x,y)] + 1;
                que.push(nxy);
            }
        }
    }
    return -1;
}

int main(){
    int n, x, y; 
    set< std::tuple<int, int> > ol;

    cin >> n >> x >> y;
    for( int i = 0 ; i < n ; i++ ){
        int ox, oy; 
        cin >> ox >> oy;
        ol.insert(make_tuple(ox,oy));
    }
    int ans = bfs(ol,x,y);
    cout << ans << endl;
}