#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

struct Bag {
    int quantity;
    string description;
    vector<Bag*> children;
};

bool insertBag(Bag* bagptr, Bag aBag) {
    Bag* tempBag = bagptr;
    bool found = false;
    //cout << "current bag we're looking at: " << tempBag->description << endl;
    if (tempBag->children.size() != 0) {
        for (int i = 0; i < tempBag->children.size(); i++) {
            if (insertBag(tempBag->children[i], aBag)) { found = true; }
        }
    }
    if (tempBag->description == aBag.description) {

        tempBag->children = aBag.children;
        return true;
    }
    else {
        return found;
    }
}

void addBag(vector<Bag>& roots, Bag aBag) {
    

    bool found = false;
    for (int i = 0; i < roots.size(); i++) {
        Bag* bagptr = &roots[i];
        if (insertBag(bagptr, aBag)) { found = true; }
    }
    if (!found) {
        roots.push_back(aBag);
    }
}

void addBagToGoldContainers(vector<string>& bagsWithGoldBags, string aBag) {
    bool found = false;
    for (int i = 0; i < bagsWithGoldBags.size(); i++) {
        if (bagsWithGoldBags[i] == aBag) {
            found = true;
            break;
        }
    }
    if (!found) {
        bagsWithGoldBags.push_back(aBag);
    }
}

bool searchBags(Bag* bagptr, vector<string>& bagsWithGoldBags) {
    Bag* tempBag = bagptr;
    bool found = false;
    if (tempBag->children.size() != 0) {
        for (int i = 0; i < tempBag->children.size(); i++) {
            if (searchBags(tempBag->children[i], bagsWithGoldBags)){
                addBagToGoldContainers(bagsWithGoldBags, tempBag->description);
                found = true;
            }
        }
    }
    if (tempBag->description == "shiny gold") {
        return true;
    }
    else {
        return found;
    }

}

void findNumGoldBags(vector<Bag>& rootBags, vector<string>& bagsWithGoldBags) {
    for (int i = 0; i < rootBags.size(); i++) {
        Bag* bagptr = &rootBags[i];

        if (searchBags(bagptr, bagsWithGoldBags)) {
            addBagToGoldContainers(bagsWithGoldBags, rootBags[i].description);
        }
    }
}


int main() {
    ifstream fin("input.txt");
    if (!fin) { cout << "File could not be opened..." << endl; }
    else { cout << "Successfully opened input!" << endl; }
    string line;
    vector<Bag> rootBags;

    while (getline(fin, line)) {
        size_t foundNo = line.find(" no ");
        if (foundNo == string::npos) {
            string parent = line.substr(0, line.find("bag") - 1);
            vector<int> quantities = {};
            vector<string> descriptions = {};
            line.erase(0, line.find("contain"));
            line.erase(0, line.find(" ") + 1);
            bool keepgoing = true;

            while (keepgoing) {
                quantities.push_back(stoi(line.substr(0, line.find(" "))));
                line.erase(0, line.find(" ") + 1);
                descriptions.push_back(line.substr(0, line.find("bag") - 1));
                line.erase(0, line.find("bag"));
                line.erase(0, 2);
                size_t foundBag = line.find("bag");
                if (foundBag != string::npos) {
                    line.erase(0, line.find(" ") + 1);
                }
                else {
                    break;
                }
            }

            Bag aBag;
            aBag.description = parent;
            aBag.quantity = 1;
            for (int i = 0; i < quantities.size(); i++) {
                Bag *childBag = new Bag;
                childBag->quantity = quantities[i];
                childBag->description = descriptions[i];
                aBag.children.push_back(childBag);
            }
            addBag(rootBags, aBag);
        }
    }

    vector<string> bagsWithGoldBags = {};
    findNumGoldBags(rootBags, bagsWithGoldBags);
    cout << "Number of bags: " << bagsWithGoldBags.size() << endl;
    //cout << rootBags[1].description << "->" << rootBags[1].children[0]->description << endl;
    
    fin.close();
    return 0;
}