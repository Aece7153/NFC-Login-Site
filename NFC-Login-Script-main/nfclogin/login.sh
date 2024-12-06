#!/bin/bash

echo "Place Card on Reader Then"
echo ""
read -n 1 -p "Press Enter:" "mainmenuinput"


nfc-list -t 1 > key_plaintext




base64 key_plaintext > key_encoded

if cmp -s key_encoded Austin; then
 echo "Hello Austin"
elif cmp -s key_encoded Brian; then
 echo "Hello Brian"
else
 echo "No User Found"
fi


rm key_encoded
rm key_plaintext
