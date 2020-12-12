/*-- - Day 7: Handy Haversacks-- -
You land at the regional airport in time for your next flight.In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules(your puzzle input) are being enforced about bagsand their contents; bags must be color - coded and must contain specific quantities of other color - coded bags.Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules :

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types.In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags(5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag.If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag ? (In other words : how many colors can, eventually, contain at least one shiny gold bag ? )

In the above rules, the following options would be available to you :

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright whiteand muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright whiteand muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag ? (The list of rules is quite long; make sure you get all of it.)

Your puzzle answer was 355.

-- - Part Two-- -
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example :

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags : 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags : 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag(and the 7 bags within it) plus 2 vibrant plum bags(and the 11 bags within each of those) : 1 + 1 * 7 + 2 + 2 * 11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag ?

Your puzzle answer was 5312.
*/

// This code is definitely not the best or cleanest way to do things I'm sure. I could probably consolidate
// many of my functions together as most of them do very similiar things. I also need to go back sometime
// and figure out how to clean up the memory. But for the intents and purposes of AOC, it works!

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

void deleteBag(Bag* aBag) {
    if (aBag->children.size() == 0) {
        aBag->children.clear();
        delete aBag;
    }
    else {
        for (int i = 0; i < aBag->children.size(); i++) {
            if (aBag->children[i] != nullptr) {
                deleteBag(aBag->children[i]);
            }
        }
        aBag->children.clear();
        delete aBag;
    }
}

bool insertBag(Bag* bagptr, Bag aBag) {
    Bag* tempBag = bagptr;
    bool found = false;
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

bool updateChild(Bag* rootBag, Bag* aBag) {
    bool found = false;
    if (rootBag->children.size() != 0) {
        for (int i = 0; i < rootBag->children.size(); i++) {
            if (updateChild(rootBag->children[i], aBag)) { found = true; }
        }
    }
    if (rootBag->description == aBag->description) {
        aBag->children = rootBag->children;
        return true;
    }
    else {
        return found;
    }
}

void addBag(vector<Bag>& roots, Bag aBag) {
    for (int i = 0; i < aBag.children.size(); i++) {
        Bag* childBagPtr = aBag.children[i];
        
        for (int j = 0; j < roots.size(); j++) {
            if (updateChild(&roots[j], childBagPtr)) {
                break;
            }
        }
    }

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

bool findGold(Bag rootBag, Bag& goldBag) {
    bool found = false;
    if (rootBag.description == "shiny gold") {
        goldBag = rootBag;
        return true;
    }
    if (rootBag.children.size() != 0) {
        for (int i = 0; i < rootBag.children.size(); i++) {
            if (findGold(*rootBag.children[i], goldBag)) { found = true; }
        }
    }
    else {
        return found;
    }
}

int countBagsInGold(Bag* rootBag) {
    int sum = 0;
    if (rootBag->children.size() == 0) {
        return rootBag->quantity;
    }
    else{
        for (int i = 0; i < rootBag->children.size(); i++) {
            sum += countBagsInGold(rootBag->children[i]);
        }
    }
    cout << "returning " << rootBag->quantity << " + " << sum << " * " << rootBag->quantity << endl;;
    return rootBag->quantity + sum * rootBag->quantity;
}

void getNumberOfBagsInGold(vector<Bag>& rootBags) {
    bool found = false;
    Bag goldBag;
    for (int i = 0; i < rootBags.size(); i++) {
        if (findGold(rootBags[i], goldBag)) { found = true; }
    }
    goldBag.quantity = 1;
    cout << "Number of bags in a gold bag: " << countBagsInGold(&goldBag) - 1 << endl;
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
    getNumberOfBagsInGold(rootBags);
   
    // my attempt to cleanup... still not working quite right. I'll come back to it later.
    //for (int i = 0; i < rootBags.size(); i++) {
    //    deleteBag(&rootBags[i]);
    //}
    
    fin.close();
    return 0;
}