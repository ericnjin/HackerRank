# include <iostream>
# include <cstring>
using namespace std;

int abd(int x,int y){
    if(x > y){
        return x - y;
    } else {
        return y - x;
    }
}

int main(){
    int testcase;
    cin >> testcase;
    
    while(testcase--){
        
        char A[10000];
        
        scanf("%s",A);
        
        int L = strlen(A);
        if( L % 2 == 0 ){
            
            int count[26];
            int count2[26];
            
            for(int i = 0; i < 26; i++){
                count[i] = 0;
                count2[i] = 0;
            }
            
            for(int i = 0; i < L/2; i++){
                count[A[i] - 'a']++;

            }
            for(int i = L/2; i < L; i++){
                count2[A[i] - 'a']++;
            }
            
            int difsum = 0;
            for(int k = 0; k < 26; k++){
                difsum += abd(count[k],count2[k]);
            }
            cout << difsum/2 << endl;
        } else {
            cout << "-1" << endl;
        }
        
    }
    
    return 0;
}
