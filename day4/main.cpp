#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool validateField(string field, string value){
    bool isValid = false;
    if(field == "byr"){if(stoi(value) >= 1920 && stoi(value) <= 2002){isValid = true;}}
    else if(field == "iyr"){if(stoi(value) >= 2010 && stoi(value) <= 2020){isValid = true;}}
    else if(field == "eyr"){if(stoi(value) >= 2020 && stoi(value) <= 2030){isValid = true;}}
    else if(field == "hgt"){}
    else if(field == "hcl"){}
    else if(field == "ecl"){}
    else if(field == "pid"){}
    else if(field == "cid"){isValid == true;}
    return isValid;
}

int main(){
    ifstream fin("input.txt");
    if(!fin){cout << "File could not be opened..." << endl;}else{cout << "Successfully opened input!" << endl;}

    int validPassportCount = 0;
    string line;
    vector<string> fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"};

    /*while(getline(fin, line)){
        if(line == "")
            cout << "blank!" << endl;
    }
    */
   
    vector<string> currentFields = fields;

    while(getline(fin, line)){
        if(line == ""){
            if(currentFields.size() == 0 || (currentFields.size() == 1 && currentFields[0] == "cid")){
                validPassportCount++;
            }else{
                cout << "fields left: ";
                for(int i = 0; i < currentFields.size(); i++){
                    cout << currentFields[i] << " ";
                }
                cout << endl;
            }
            currentFields = fields;
        }
        else{
            while(line.size() != 0){
                string var = line.substr(0, line.find(":"));
                string val;
                line.erase(0, line.find(":"));
                cout << "line after erase: " << line << endl;
                size_t found = line.find(" ");

                cout << "line: " << line << endl;

                if(found != string::npos){
                    val = line.substr(line.find(":") + 1, line.find(" "));
                }else{
                    val = line.substr(line.find(":") + 1, line.find("\n"));
                }

                cout << "\n\nkey: " << var << endl;
                cout << "value: " << val << endl << endl;;

                if(found != string::npos){
                    line.erase(0, line.find(" ") + 1);
                }else{
                    line.erase(0, line.find("\n"));
                }

                for(int i = 0; i < currentFields.size(); i++){
                    if(var == currentFields[i]){
                        currentFields.erase(currentFields.begin() + i);
                    }
                }
            }
        }
    }

    if(currentFields.size() == 0 || (currentFields.size() == 1 && currentFields[0] == "cid")){
        validPassportCount++;
    }else{
        cout << "fields left: ";
        for(int i = 0; i < currentFields.size(); i++){
            cout << currentFields[i] << " ";
        }
        cout << endl;
    }

    cout << validPassportCount << endl;

    fin.close(); 

    return 0;
}