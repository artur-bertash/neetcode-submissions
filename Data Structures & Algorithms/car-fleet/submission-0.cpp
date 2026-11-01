class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        double lastTime = -1;
        int counter = 0;
        vector<pair<int, int>> combined;

        for (int i = 0; i < position.size(); i++) {
            combined.push_back({position[i], speed[i]});
        }

        sort(combined.begin(), combined.end(), [](auto &x, auto &y) {
            return x.first > y.first;
        });

        for (int i = 0; i < position.size(); i++) {
            double time = (target - combined[i].first) / (double)combined[i].second;

            if (lastTime == -1 || time > lastTime) {
                lastTime = time;
                counter++;
            }
        }
        return counter;
    }
};
