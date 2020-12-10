#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
int main(){
    ifstream fin("input.txt");
    if(!fin){cout << "File could not be opened..." << endl;}else{cout << "Successfully opened input!" << endl;}
    string line;

//***************************************** WHILE LOOP
    while(getline(fin, line)){
        size_t foundNo = line.find(" no ");
        if(foundNo == string::npos){
            string parent = line.substr(0, line.find("bag") - 1);
            vector<int> quantities = {};
            vector<string> descriptions = {};
            line.erase(0, line.find("contain"));
            line.erase(0, line.find(" ") + 1);
            bool keepgoing = true;

            while(keepgoing){
            //cout << line << endl;
            quantities.push_back(stoi(line.substr(0, line.find(" ")))); 
            //cout << line.substr(0, line.find(" ")) << "***"<< endl;
            line.erase(0, line.find(" ") + 1);
            //cout << "line after erase:***" << line << endl;
            descriptions.push_back(line.substr(0, line.find("bag") - 1));
            //cout << "***" << line.substr(0, line.find("bag")) << endl;
            line.erase(0, line.find("bag"));
            line.erase(0, 2);
            size_t foundBag = line.find("bag");
            if(foundBag != string::npos){
                line.erase(0, line.find(" ") + 1);
            }
            else{
                break;
            }
            //cout << "line after erase:***" << line << endl;
            }

            cout << "parent:***" << parent << "******" << endl;
            for(int i = 0; i < descriptions.size(); i++){
                cout << "***" << quantities[i] << "***" << descriptions[i] << "***" << endl;
            }
        }
    }
//****************************************************** WHILE LOOP

    fin.close();
    return 0;
}