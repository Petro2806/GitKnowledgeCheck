#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> v{10, 7, 9};
    int sum = std::accumulate(v.begin(), v.end(), 0);
    std::cout << "Campus Toolkit demo. Sum=" << sum << "\n";
    return 0;
}
