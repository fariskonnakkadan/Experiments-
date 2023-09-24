#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <getopt.h>

#define MAX_URL_LENGTH 256
#define MAX_WORD_LENGTH 128

// Callback function to handle HTTP responses
size_t response_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    // You can add more handling logic here if needed.
    return size * nmemb;
}

int main(int argc, char *argv[]) {
    char url[MAX_URL_LENGTH] = "";
    char wordlist[MAX_WORD_LENGTH] = "";

    int option;
    while ((option = getopt(argc, argv, "u:w:")) != -1) {
        switch (option) {
            case 'u':
                strncpy(url, optarg, MAX_URL_LENGTH - 1);
                break;
            case 'w':
                strncpy(wordlist, optarg, MAX_WORD_LENGTH - 1);
                break;
            default:
                printf("Usage: %s -u <URL> -w <wordlist>\n", argv[0]);
                return 1;
        }
    }

    if (strlen(url) == 0 || strlen(wordlist) == 0) {
        printf("Both -u and -w options are required.\n");
        return 1;
    }

    FILE *file = fopen(wordlist, "r");
    if (!file) {
        perror("Error opening the wordlist file");
        return 1;
    }

    char word[MAX_WORD_LENGTH];

    CURL *curl = curl_easy_init();
    if (curl) {
        // Set callback function to handle the HTTP response
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, response_callback);

        while (fgets(word, MAX_WORD_LENGTH, file)) {
            // Remove newline characters from the word
            size_t len = strlen(word);
            if (len > 0 && (word[len - 1] == '\n' || word[len - 1] == '\r')) {
                word[len - 1] = '\0';
            }

            // Create a new URL with the current word
            char full_url[MAX_URL_LENGTH];
            snprintf(full_url, MAX_URL_LENGTH, "%s/%s", url, word);

            // Set the URL for the request
            curl_easy_setopt(curl, CURLOPT_URL, full_url);

            // Perform the HTTP GET request
            CURLcode res = curl_easy_perform(curl);

            // Check the HTTP status code
            long http_code;
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &http_code);

            // Print the word if the status code is not 404
            if (res == CURLE_OK && http_code != 404) {
                printf("Status Code %ld: %s\n", http_code, word);
            }
        }

        // Clean up curl
        curl_easy_cleanup(curl);
    } else {
        fprintf(stderr, "Failed to initialize libcurl\n");
    }

    fclose(file);

    return 0;
}
