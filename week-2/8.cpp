class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        while (s[i] == ' ') {
            i++;
        }
        int sign = 0; // positive
        if (s[i] == '-') {
            sign = 1;
            i++;
        } else if (s[i] == '+') {
            i++;
        }

        while (s[i] == '0') i++;

        long int ans = 0;
        while(s[i] >= '0' && s[i] <= '9') {
            if(ans > INT_MAX) {
                if(sign) return INT_MIN;
                return INT_MAX;
            }
            ans = ans * 10 + s[i] - '0';
            i++;
        }

        if(sign) {
            ans *= -1;
        }

        if(ans > INT_MAX) return INT_MAX;
        if(ans < INT_MIN) return INT_MIN;
        
        return (int)ans;

    }
};
