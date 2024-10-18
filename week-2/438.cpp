class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        map<int,int> freq, window;
        // get the frequency of letters in p
        for (int i = 0; i < p.size(); i++) {
            freq[p[i]]++;
        }

        // p is the start of the window and j is the end
        int j = p.size()-1;
        int i = 0;
        int ptr = i;
        vector<int> ans;

        // get the frequency of letters in our sliding window
        while (ptr <= j) {
            window[s[ptr]]++;
            ptr++;
        }
               
        if (freq == window) {
            ans.push_back(i);
        }
    
           
        while (i < s.size()) {
            window[s[i]]--;
            if (window[s[i]] == 0) {
                window.erase(s[i]);
            }
            i++;
            j++;
            
            if (j < s.size()) {
                window[s[j]]++;
            } 
            
           
            if (freq == window) {
                ans.push_back(i);
            }
            
       }

        return ans;
    }
};
