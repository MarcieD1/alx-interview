# Log Parsing Script

## Overview

This script is designed to process log data read from standard input (stdin). It's particularly useful for parsing web server logs to compute and display metrics such as the total size of files requested and the count of HTTP status codes returned by the server.

## Functionality

The script operates by continuously reading lines of text from stdin. Each line is expected to represent a log entry from a web server, containing an IP address, a date, a request method with a resource path, an HTTP version, a status code, and the size of the response. The script specifically looks for the status code and the size of the response in each log entry.

As it processes each line, the script updates two main pieces of information:
1. **Total File Size:** The cumulative size of all files sent in response to requests, as indicated by the size portion of each log entry.
2. **HTTP Status Code Counts:** A tally of how many times each HTTP status code appears in the log data.

After every 10 lines of log data processed, or when the script is interrupted (e.g., via CTRL+C), it prints out the current total file size and the counts of each HTTP status code encountered so far, in ascending order by status code.

## Usage

To use this script, you should pipe log data into it from a file or another command. Here's an example of how to use it with a log file:

```bash
cat access.log | ./log_parsing_script.py

This command reads `access.log` line by line and passes each line to the script for processing.

## Requirements

- Python 3.4.3 or higher
- The script must be run on a Unix-like operating system, such as Linux or macOS, that supports piping data through the command line.

## Implementation Details

The script is implemented in Python and makes use of:
- The `sys.stdin` file object to read input lines from stdin.
- A dictionary to keep track of the counts of each HTTP status code.
- A running total to keep track of the cumulative file size.
- Exception handling to gracefully handle keyboard interrupts and ensure that the current statistics are printed before the script exits.

## Conclusion

This log parsing script is a handy tool for quickly summarizing important metrics from web server logs. It's designed to be simple to use, requiring only that the user pipe log data into it. Whether you're monitoring the health of a web server, debugging issues, or just curious about the traffic your server is handling, this script provides valuable insights at a glance.
```
