# JSExtract
Small tool to extract JS files of a website. This tool is useful for bug hunters mainly because you can extract the JS files of the domain and after the Bash script extract the HTTP links inside the JS files, so you can find possible endpoints like API or other things. I recommend using the Bash script, I programmed the Bash script to launch the Python script and extract the HTTP link and juicy words inside the JS files, but if you want, you can customize your own bash script and use only the Python file with your Bash script.

HOW IT WORKS

./runme.sh file.txt

Keep in mind that maybe be necessary to change the routes inside the Bash script and adapt them to your directory routes, in addition the directory or folder name *javascript_files_downloaded* is created by the tool **LinkTracker** (My other tool)


<img width="1154" alt="image" src="https://github.com/svaltheim/JSExtract/assets/30341113/841549ce-845d-4168-864b-67f7b8331f8f">



>NOTE The TXT file is generated by the other tool in my GitHub **LinkTracker**, this tool extracts all hyperlinks in TXT files then you can send these files to JSExtract to get the HTTP links hidden and juicy words inside the JS file>


