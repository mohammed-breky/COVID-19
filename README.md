# COVID-19
*sending new articles headlins from WHO website*

to install and run 

first please install the requirements.txt inside your <b>virtual enviroment</b> file with

```$pip install -r requirements.txt```

after that navigate to <b>email.json</b> file and change the settings to your server and email credentials

<b>last step</b>

change the reciver email in <b>main.py</b> with what ever email you want or replaced with ```email``` variable to send the email to your email

you can deploy this project to your host and make a <b>CRON JOB</b> to send the email automatically

<b>PLEASE DONT RUIN UP THE WHO SERVERS AND RUN THE CODE EVERY HOUR AT LEAST</b>

the code will send email even if there is No New Articles with *stay safe and wash your hands* email 🧼👁️

it uses a ```.txt``` file to compare if there is a new article or not

don't worry <b>YOU DO NOT HAVE TO CREATE THE .TXT FILE</b> Python will handle it because it can🔥lol

if you have time, help to improve this little project and make it better 💖
