#!/bin/bash



nfc-list -t 1 > key_plaintext
base64 key_plaintext > key_encoded

if cmp -s key_encoded Users/Austin; then
 touch True
elif cmp -s key_encoded Users/Brian; then
 touch True
else
 touch False
fi


rm key_encoded
rm key_plaintext