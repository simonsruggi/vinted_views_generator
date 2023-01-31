# vinted_views_generator

# How to run?
1) Install python 3
2) Install requests by typing: 'pip install requests' on command line
3) python3 vinted.py

# How to use proxies and why?

Vinted usually rate-limits ip if you make a lot of requests, that's why sometimes you need to use proxies.

Paste your proxies in 'proxies.txt' in format: ip:port OR ip:port:username:password, the script will use those proxies to make the requests.