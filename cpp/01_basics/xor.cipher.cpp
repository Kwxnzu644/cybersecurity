#include <iostream>   // For input/output (cout, cerr)
#include <fstream>    // For file read/write streams
using namespace std;

// 🔐 XOR encryption/decryption function
char xorCipher(char byte, char key) {
    return byte ^ key;  // XOR each byte with the key
}

int main(int argc, char* argv[]) {
    // 📌 Check if user passed correct arguments: <input> <output> <key>
    if (argc != 4) {
        cerr << "Usage: " << argv[0] << " <input_file> <output_file> <key_char>" << endl;
        return 1;
    }

    // 🧾 Get inputs
    string inputFile = argv[1];
    string outputFile = argv[2];
    char key = argv[3][0];  // Only first char used for XOR key

    // 📂 Open input and output files in binary mode
    ifstream inFile(inputFile, ios::binary);
    ofstream outFile(outputFile, ios::binary);

    // ❗ Check if files opened correctly
    if (!inFile || !outFile) {
        cerr << "❌ Error opening input/output files." << endl;
        return 1;
    }

    // 🔁 Process each byte
    char byte;
    while (inFile.get(byte)) {
        char encrypted = xorCipher(byte, key); // Encrypt or decrypt byte
        outFile.put(encrypted);               // Write to output
    }

    // ✅ Done — clean up
    inFile.close();
    outFile.close();

    cout << "✅ File processed using XOR cipher. Output saved to '" << outputFile << "'." << endl;
    return 0;
}
