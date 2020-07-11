python check_empty_folder.py
set /p message="Message to commit: "
git add *
git commit  -m "%message%"
git push origin master
pause