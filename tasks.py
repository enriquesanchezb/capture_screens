from __future__ import absolute_import
import os
import time  
from celery import Celery
import capture_images

env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),  
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


celery= Celery('tasks',  
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

@celery.task(name="tasks.capture_image", bind=True)
def capture_image(self,device, folder):
    capture_images.generate_captures_folder(folder)
    while True:
        time.sleep(1)
        capture_images.get_capture(device, folder)

if __name__ == "__main__":
    celery.start()