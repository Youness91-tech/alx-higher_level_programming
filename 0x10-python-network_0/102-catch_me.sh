#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -s -L 0.0.0.0:5000/catch_me -d "user_id=98" -X PUT -H "Origin:School"
