#!/bin/bash

echo "       ##                     ##  ##   ######   ######     ##       ####   ###### "
echo "                              ##  ##   # ## #    ##  ##   ####     ##  ##  # ## # "
echo "       ###   #####    ####     ####      ##      ##  ##  ##  ##   ##         ## "
echo "       ##   ##       ##  ##     ##       ##      #####   ##  ##   ##         ## "
echo "       ##    #####   ######    ####      ##      ## ##   ######   ##         ## "
echo "   ##  ##        ##  ##       ##  ##     ##      ##  ##  ##  ##    ##  ##    ## "
echo "   ##  ##   ######    #####   ##  ##    ####    #### ##  ##  ##     ####    #### "
echo "    ####									      "

echo "By Svaltheim"
echo
echo

 python3 JSExtract_4.py $1
 sleep 3
 cat ~/javascript_files_downloaded/* | grep -Eo  '(http|https)://[a-zA-Z0-9./?=_%:-]*' > http_links_found.txt
 cat ~/javascript_files_downloaded/* | grep -R -Eo 'aws_access_key|aws_secret_key|api key|passwd|pwd|heroku|slack|firebase|swagger|aws_secret_key|aws key|password|ftp password|jdbc|db|sql|secret jet|config|admin|pwd|json|gcp|htaccess|.env|ssh key|.git|access key|secret token|oauth_token|oauth_token_secret|smtp' -H -n > juicy_words_found.txt



