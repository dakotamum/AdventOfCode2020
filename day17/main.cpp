#include <iostream>
#include <string>
#include <vector>
#include <fstream>

// read input and initialize 3D Vector
std::vector<std::vector<std::string>> initialize3D()
{
	std::vector<std::vector<std::string>> threeDVector;
	std::vector<std::string> twoDVector;
	std::ifstream fin("input.txt");
	std::string line;

	while(getline(fin, line))
	{
		twoDVector.push_back(line);
	}

	std::string blankRow(twoDVector[0].size(), '.');

	std::vector<std::string> blank2D;
	for (int i = 0; i < twoDVector.size(); i++)
	{
		blank2D.push_back(blankRow);
	}

	threeDVector.push_back(twoDVector);

	fin.close();
	return threeDVector;
}

void expand3D(std::vector<std::vector<std::string>>& threeD)
{
	for(int z = 0; z < threeD.size(); z++)
	{
		for(int y = 0; y < threeD[z].size(); y++)
		{
			threeD[z][y].insert(0, 1, '.');
			threeD[z][y].append(".");
		}
		std::string blankRow(threeD[z].size() + 2, '.');
		threeD[z].push_back(blankRow);
		threeD[z].insert(threeD[z].begin(), blankRow);
	}

	std::string blankRow(threeD[0].size(), '.');
	std::vector<std::string> blank2D;
	for (int i = 0; i < threeD[0].size(); i++)
	{
		blank2D.push_back(blankRow);
	}
	threeD.insert(threeD.begin(), blank2D);
	threeD.push_back(blank2D);
}

void print3D(std::vector<std::vector<std::string>> threeD)
{
	for(int z = 0; z < threeD.size(); z++)
	{
		for(int y = 0; y < threeD[z].size(); y++)
		{
			std::cout << threeD[z][y] << std::endl;
		}
		std::cout << std::endl;
	}
}

int countTwoDNeighbors(std::vector<std::string> twoD, int i, int j, bool includeCenter = true)
{
	int count = 0;	
	// adjacent spaces
	if (i-1 >= 0) { if (twoD[i-1][j] == '#') count += 1; }
	if (j-1 >= 0) { if (twoD[i][j-1] == '#') count += 1; }
	if (i+1 < twoD.size()) { if (twoD[i+1][j] == '#') count += 1; }
	if (j+1 < twoD[i].size()) { if (twoD[i][j+1] == '#') count += 1; }
	// diagonal spaces
	if (i-1 >= 0 && j-1 >= 0) { if (twoD[i-1][j-1] == '#') count += 1; }
	if (i-1 >= 0 && j+1 < twoD[i].size()) { if (twoD[i-1][j+1] == '#') count += 1; }
	if (i+1 < twoD.size() && j-1 >= 0) { if (twoD[i+1][j-1] == '#') count += 1; }
	if (i+1 < twoD.size() && j+1 < twoD[i].size()) { if (twoD[i+1][j+1] == '#') count += 1; }
	// center space
	if(includeCenter) { if (twoD[i][j] == '#') count += 1; }
	return count;	
}

int countThreeDNeighbors(std::vector<std::vector<std::string>> threeD, int i, int j, int k)
{
	int count = 0;
	if (k-1 >= 0) { count += countTwoDNeighbors(threeD[k-1], i, j); }
	count += countTwoDNeighbors(threeD[k], i, j, false);	
	if (k+1 < threeD.size()) { count += countTwoDNeighbors(threeD[k+1], i, j); }
	return count;
}

void newDayThreeD(std::vector<std::vector<std::string>>& threeD)
{
	expand3D(threeD);
	std::vector<std::vector<std::string>> newThreeD = threeD;


	for (int k = 0; k < threeD.size(); k++)
	{
		for (int j = 0; j < threeD[k].size(); j++)
		{
			for (int i = 0; i < threeD[k][j].size(); i++)
			{
				//std::cout << countThreeDNeighbors(threeD, j, i, k);
				if (threeD[k][j][i] == '.')
				{
					if (countThreeDNeighbors(threeD, j, i, k) == 3) newThreeD[k][j][i] = '#';
					else newThreeD[k][j][i] = '.';
				}
				else
				{
					if (countThreeDNeighbors(threeD, j, i, k) == 2 || countThreeDNeighbors(threeD, j, i, k) == 3) newThreeD[k][j][i] = '#';
					else newThreeD[k][j][i] = '.';
				}
			}
			//std::cout << std::endl;
		}
		//std::cout << std::endl;
	}
	threeD = newThreeD;
}

int countActivesThreeD(std::vector<std::vector<std::string>> threeD)
{
	int count = 0;
	for(int z = 0; z < threeD.size(); z++)
	{
		for(int y = 0; y < threeD[z].size(); y++)
		{
			for (int x = 0; x < threeD[z][y].size(); x++)
			{
				if (threeD[z][y][x] == '#') count += 1;
			}
		}
	}
	return count;
}

int main()
{
	std::vector<std::vector<std::string>> threeD = initialize3D();
	newDayThreeD(threeD);
	newDayThreeD(threeD);
	newDayThreeD(threeD);
	newDayThreeD(threeD);
	newDayThreeD(threeD);
	newDayThreeD(threeD);
	print3D(threeD);
	std::cout << countActivesThreeD(threeD) << std::endl;
	return 0;
}