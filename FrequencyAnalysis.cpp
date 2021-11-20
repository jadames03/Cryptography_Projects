#include <iostream>
#include <string>
#include <iomanip>
#include <iterator>
#include <algorithm>

using namespace std;

unsigned int occurenceContainer[26]{0};
double alphaContainer[26]{0.0817, 0.0150, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0403, 0.0241,
0.0675, 0.0751, 0.0193, 0.0010, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007};

int main()
{
    cout << "Ciphertext:\n";
    string outString = "\tlrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi\n"
                            "bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx\n"
                            "ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr\n"
                            "yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk\n"
                            "lmird jk xjubt trmui jx ibndt\n"
                            "\twb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi\n"
                            "iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower\n"
                            "vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd\n"
                            "wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr\n"
                            "jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii\n"
                            "ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh\n"
                            "mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb\n"
                            "bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd\n"
                            "wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr\n"
                            "riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb\n";

    string outString2 = "\tlrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi\n"
                            "bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx\n"
                            "ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr\n"
                            "yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk\n"
                            "lmird jk xjubt trmui jx ibndt\n"
                            "\twb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi\n"
                            "iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower\n"
                            "vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd\n"
                            "wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr\n"
                            "jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii\n"
                            "ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh\n"
                            "mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb\n"
                            "bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd\n"
                            "wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr\n"
                            "riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb\n";

    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    cout << outString << endl;

    replace(outString2.begin(), outString2.end(), 'r', 'E');
    replace(outString2.begin(), outString2.end(), 'b', 'T');
    replace(outString2.begin(), outString2.end(), 'm', 'A');
    replace(outString2.begin(), outString2.end(), 'k', 'N');
    replace(outString2.begin(), outString2.end(), 'j', 'O');
    replace(outString2.begin(), outString2.end(), 'w', 'I');
    replace(outString2.begin(), outString2.end(), 'i', 'S');
    replace(outString2.begin(), outString2.end(), 'p', 'H');
    replace(outString2.begin(), outString2.end(), 'u', 'R');
    replace(outString2.begin(), outString2.end(), 'd', 'D');
    replace(outString2.begin(), outString2.end(), 'h', 'L');
    replace(outString2.begin(), outString2.end(), 'v', 'C');
    replace(outString2.begin(), outString2.end(), 'x', 'F');
    replace(outString2.begin(), outString2.end(), 'y', 'M');
    replace(outString2.begin(), outString2.end(), 'n', 'U');
    replace(outString2.begin(), outString2.end(), 's', 'P');
    replace(outString2.begin(), outString2.end(), 't', 'Y');
    replace(outString2.begin(), outString2.end(), 'l', 'B');
    replace(outString2.begin(), outString2.end(), 'q', 'K');
    replace(outString2.begin(), outString2.end(), 'o', 'G');
    replace(outString2.begin(), outString2.end(), 'e', 'V');
    replace(outString2.begin(), outString2.end(), 'a', 'X');
    replace(outString2.begin(), outString2.end(), 'c', 'W');
    replace(outString2.begin(), outString2.end(), 'f', 'Q');
    replace(outString2.begin(), outString2.end(), 'g', 'Z');

    cout << "Plaintext:" << endl;
    cout << outString2 << endl << endl;
    cout << "   alphabet frequency table:" << endl;
    cout << "\n   letter  freq[%]" << endl;
    cout << "   ===============" << endl;
    double freqPercentage;

    size_t n = sizeof(alphaContainer)/sizeof(alphaContainer[0]);
    for(size_t i = 0; i < n; i++){
        freqPercentage = (alphaContainer[i] * 100.00);
        cout << "   |" << alphabet.at(i) << "    | " << fixed << setprecision(2) << freqPercentage << endl;
    }
    cout << endl;

    for(unsigned int i = 0; i < 784; i++){                           //traversing through the string
        int charIndex = -1;

        if((int)outString[i] >= 97 && (int)outString[i] <= 122){
            charIndex = ((int)outString[i]%97);
        }
        occurenceContainer[charIndex] += 1;
    }
    cout << "   encrypted letter frequency table:" << endl;
    cout << "\n   letter  count    freq[%]" << endl;
    cout << "   ========================" << endl;

    int w;
    double freqDecimal, freqPercentage2, total_char{645};
    w = outString.size();

    for(unsigned int i = 0; i != w; i++){
        int charIndex = -1;
        if((outString.at(i) != ' ') && (outString.at(i) != '\t') && (outString.at(i) != '\n'))
        {
            if((int)outString[i] >= 97 && (int)outString[i] <= 122){
                charIndex = ((int)outString[i]%97);
            }
        freqDecimal = occurenceContainer[charIndex]/total_char;
        freqPercentage2 = (freqDecimal*100.00);

        auto last = outString.end();

        for(auto first = outString.begin(); first != last; ++first){                       //this ranged-base for loop removes duplicates from the encrypted string
            last = remove(next(first), last, *first);
        }
        outString.erase(last, outString.end());

            if(occurenceContainer[charIndex] < 10){
                cout << "   |" << outString.at(i) << "    | 0" << occurenceContainer[charIndex];
                cout << "/" << fixed << setprecision(0) << total_char << " | " << fixed << setprecision(2) << freqPercentage2 << endl;
            }
            else {
                cout << "   |" << outString.at(i) << "    | " << occurenceContainer[charIndex];
                cout << "/" << fixed << setprecision(0) << total_char << " | " << fixed << setprecision(2) << freqPercentage2 << endl;
            }
        }
    }
    return 0;
}
