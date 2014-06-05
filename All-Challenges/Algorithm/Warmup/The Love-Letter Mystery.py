for i in range(int(raw_input())):
    string = raw_input()
    sigma = 0
    
    for j in range(len(string)/2):
        sigma += abs(ord(string[j]) - ord(string[-1*(j+1)]))
                    
    
    print sigma                
