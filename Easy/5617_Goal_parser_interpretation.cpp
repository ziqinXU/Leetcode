class Solution {
public:
    string interpret(string command) {
        string res="";
        for(int i = 0; i < command.length(); i++)
        {
            if(command[i] == 'G')
            {
                res += command[i];
            }
            else if(command[i] == '(')
            {
                if(command[i+1] == ')')
                {
                    res += "o";
                    i++;
                }
                else
                {
                    res += "al";
                    i += 3;
                }
            }
        }
        return res;

    }
};
