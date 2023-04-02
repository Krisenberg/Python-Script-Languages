#include <iostream>
#include <string>
#include <fstream>
#include <vector>

bool filePathChecker(const std::string& path)
{
    std::ifstream file(path);
    return file.good();
}

std::string pathReader()
{
    std::string path ="";
    std::getline(std::cin, path);
    return path;
}

int countWords(const std::string& line)
{
    int counter = 0;
    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] == ' ' || line[i] == '\t')
            counter++;
    }
    /*if (line[line.length() - 1] != '-')
        counter++;*/
    counter++;
    return counter;
}

void addLineToCharHist(const std::string& line, std::vector<char>& keys, std::vector<int>& values)
{
    bool found;
    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] != ' ' && line[i] != '\t') {
            found = false;
            for (int j = 0; j < keys.size(); j++)
            {
                if (line[i] == keys[j])
                {
                    found = true;
                    values[j]++;
                    j = keys.size();
                }
            }
            if (!found)
            {
                keys.push_back(line[i]);
                values.push_back(1);
            }
        }
    }
}

void addLineToWordHist(const std::string& line, std::vector<std::string>& keys, std::vector<int>& values)
{
    bool found;
    int startIndex = 0;
    int lenSubstr;
    std::string word;
    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] == ' ' || line[i] == '\t')
        {
            lenSubstr = i - startIndex;
            word = line.substr(startIndex, lenSubstr);
            found = false;
            for (int j = 0; j < keys.size(); j++)
            {
                if (word == keys[j])
                {
                    found = true;
                    values[j]++;
                    j = keys.size();
                }
            }
            if (!found)
            {
                keys.push_back(word);
                values.push_back(1);
            }
            startIndex = i + 1;
        }
    }
}

char findMostFreqChar(std::vector<char>& keys, std::vector<int>& values)
{
    int maxValue = 0;
    int indexMaxValue = 0;

    for (int i = 0; i < keys.size(); i++)
    {
        if (values[i] > maxValue)
        {
            maxValue = values[i];
            indexMaxValue = i;
        }
    }
    return keys[indexMaxValue];
}

std::string findMostFreqWord(std::vector<std::string>& keys, std::vector<int>& values)
{
    int maxValue = 0;
    int indexMaxValue = 0;

    for (int i = 0; i < keys.size(); i++)
    {
        if (values[i] > maxValue)
        {
            maxValue = values[i];
            indexMaxValue = i;
        }
    }
    return keys[indexMaxValue];
}

std::string analyzeFile(const std::string& path)
{
    std::ifstream file;
    if (filePathChecker(path))
    {
        int linesCounter = 0;
        int charCounter = 0;
        int wordsCounter = 0;
        std::vector<char> charHistogram;
        std::vector<int> charHistogramValues;
        std::vector<std::string> stringHistogram;
        std::vector<int> stringHistogramValues;

        file.open(path);
        std::string line;
        while (file) 
        {
            std::getline(file, line, '\n');
            charCounter += line.length();
            wordsCounter += countWords(line);
            linesCounter++;
            addLineToCharHist(line, charHistogram, charHistogramValues);
            addLineToWordHist(line, stringHistogram, stringHistogramValues);
        }
        linesCounter--;
        wordsCounter--;
        std::string retString = path + "," + std::to_string(charCounter) + "," + std::to_string(wordsCounter) + ","
            + std::to_string(linesCounter);
        std::string mostFreqChar;
        mostFreqChar.push_back(findMostFreqChar(charHistogram, charHistogramValues));
        std::string mostFreqWord = findMostFreqWord(stringHistogram, stringHistogramValues);
        retString.append(","+mostFreqChar);
        retString.append("," + mostFreqWord + '\n');
        file.close();
        return (retString);
    }
    return (path + " is not a valid path!");
}

int main()
{
    bool EOIflag = false;
    std::string path;
    while (!EOIflag)
    {
        path = pathReader();
        if (path == "")
            EOIflag = true;
        else
            std::cout << analyzeFile(path);
    }

    return 0;
}
