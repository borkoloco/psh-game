"""
WSGI config for pshgame project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""


import os
from crontab import CronTab
from django.core.wsgi import get_wsgi_application
from pathlib import Path


project_dir = Path(__file__).resolve().parent.parent  


simulate_script_path = project_dir / 'simulate_stats_script.py'

venv_python = project_dir / 'venv' / 'bin' / 'python'


cron_flag_file = project_dir / '.cron_setup_done'

if not cron_flag_file.exists():  
   
    cron = CronTab(user=True)

  
    command = f'cd {project_dir} && {venv_python} {simulate_script_path} >> {project_dir}/cron_log.txt 2>&1'

   
    job_exists = any(job.command == command for job in cron)

    if not job_exists:
        
        job = cron.new(command=command)
        job.minute.every(5)  
        cron.write()  
        print("Cron job added successfully.")
    
    
    with open(cron_flag_file, 'w') as f:
        f.write("Cron setup complete.")
else:
    print("Cron job setup skipped as it is already done.")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pshgame.settings')

application = get_wsgi_application()



