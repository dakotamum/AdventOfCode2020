/*--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Your puzzle answer was 6170.

--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

Your puzzle answer was 2947.
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
int main(){
    ifstream fin("input.txt");
    if(!fin){cout << "File could not be opened..." << endl;}else{cout << "Successfully opened input!" << endl;}
    string line;
    string currentLettersUsed;
    string currentFoundInAll;
    int totalYesQuestions = 0;
    int totalAllYesQuestions = 0;
    vector<string> yesesInQuestion = {};

    while(getline(fin, line)){
        if(line == ""){
            totalYesQuestions += currentLettersUsed.size();

            //cout << "yessesInQuestion: "; for(int i = 0; i < yesesInQuestion.size(); i++){cout << yesesInQuestion[i] << " ";}
            //cout << endl;

            if(yesesInQuestion.size() == 1){
                //cout << currentLettersUsed << " is on one line. Adding: " << currentLettersUsed.size() << "." << endl;
                totalAllYesQuestions += yesesInQuestion[0].size();
            }
            else{
                // for every letter in the first string...
                for(int i = 0; i < yesesInQuestion[0].size(); i++){
                    //cout << "comparing " << yesesInQuestion[0][i] << " to every string" << endl;
                    bool foundInEveryLine = true;
                    // loop through every string in the vector
                    for(int j = 1; j < yesesInQuestion.size(); j++){
                        // loop through every letter in the ith string
                        bool foundInLine = false;
                        for(int k = 0; k < yesesInQuestion[j].size(); k++){
                            //cout << "comparing " << yesesInQuestion[0][i] << " to " << yesesInQuestion[j][k] << endl;
                            if(yesesInQuestion[0][i] == yesesInQuestion[j][k]){
                                foundInLine = true;
                                break;
                            }
                        }
                        if(!foundInLine){
                            foundInEveryLine = false;
                            break;
                        }
                    }
                    if(foundInEveryLine){
                        currentFoundInAll.push_back(yesesInQuestion[0][i]);
                        //cout << "added " << yesesInQuestion[0][i] << endl;
                    }
                }
                //cout << "adding " << currentFoundInAll.size() << " to the total" << endl;
                totalAllYesQuestions += currentFoundInAll.size();
            }
            currentLettersUsed = "";
            yesesInQuestion = {};
            currentFoundInAll = "";
        }
        else{
            yesesInQuestion.push_back(line);
            while(line.size() != 0){
                bool foundInString = false;
                for(int i = 0; i < currentLettersUsed.size(); i++){
                    if(line[0] == currentLettersUsed[i]){
                        foundInString = true;
                        break;
                    }
                }
                if(!foundInString){
                    currentLettersUsed.push_back(line[0]);
                }
                line.erase(line.begin());
            }
        }
    }

    totalYesQuestions += currentLettersUsed.size(); 

    if(yesesInQuestion.size() == 1){
        cout << currentLettersUsed << " is on one line. Adding: " << currentLettersUsed.size() << "." << endl;
        totalAllYesQuestions += yesesInQuestion[0].size();
    }
    else{
        // for every letter in the first string...
        for(int i = 0; i < yesesInQuestion[0].size(); i++){
            //cout << "comparing " << yesesInQuestion[0][i] << " to every string" << endl;
            bool foundInEveryLine = true;
            // loop through every string in the vector
            for(int j = 1; j < yesesInQuestion.size(); j++){
                // loop through every letter in the ith string
                bool foundInLine = false;
                for(int k = 0; k < yesesInQuestion[j].size(); k++){
                    //cout << "comparing " << yesesInQuestion[0][i] << " to " << yesesInQuestion[j][k] << endl;
                    if(yesesInQuestion[0][i] == yesesInQuestion[j][k]){
                        foundInLine = true;
                        break;
                    }
                }
                if(!foundInLine){
                    foundInEveryLine = false;
                    break;
                }
            }
            if(foundInEveryLine){
                currentFoundInAll.push_back(yesesInQuestion[0][i]);
                //cout << "added " << yesesInQuestion[0][i] << endl;
            }
        }
        //cout << "adding " << currentFoundInAll.size() << " to the total" << endl;
        totalAllYesQuestions += currentFoundInAll.size();
    }

    cout << "Total \'yes\' resonses: " << totalYesQuestions << endl;
    cout << "Total all \'yes\' resonses: " << totalAllYesQuestions << endl;
    fin.close();
    return 0;
}