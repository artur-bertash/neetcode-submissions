class Solution {
public:

    string encode(vector<string>& strs) {
        std::string encoded;
    for (auto &str : strs)
    {
        encoded += std::to_string(str.length()) + "#" + str;
    }
    std::cout << encoded << std::endl;
    return encoded;
    }

    vector<string> decode(string s) {
         std::vector<std::string> decoded;
    int num = 0;

    for (int i = 0; i < s.length(); i++)
    {

        while (isdigit(s[i]) && i < s.length())
        {
            num = num * 10 + (s[i] - '0');
            i++;
        }

        if (s[i] == '#' && i < s.length())
            i++;

        std::string word = s.substr(i, num);
        decoded.push_back(word);
        i += num - 1;
        num = 0;
    }
    return decoded;
    }
};
