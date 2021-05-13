#line 5 "AnswerEvaluation.cpp"
#include <string>
#include <vector>
#include <sstream>
using namespace std;

class AnswerEvaluation {
  public:
  int getScore(vector <string> keywords, vector <int> scores, string answer) {
    int i, j; 
    string next;

    for(i = j = 0; i < keywords.size(); i++) {
      stringstream ss(answer);
      while (ss >> next)
        if (next == keywords[i]) {
          j += scores[i];
          break;
        }
    }
    return j;
  }
};