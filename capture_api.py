import os
import time

from flask import Flask, jsonify, abort

from celery import Celery

import capture_images

env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),  
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')

celery= Celery('tasks',  
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

env=os.environ
app = Flask(__name__)

tasks = {}

@app.route('/stop/<id>')
def stop(id):
    try:
        celery.control.revoke(id, terminate=True)
    except:
        abort(404)
    file = capture_images.generate_video(tasks[id]['device'], tasks[id]['folder'])
    if file is not None:
        capture_images.delete_images(tasks[id]['folder'])
    return jsonify({'result': 'ok', 'file': file})

@app.route('/capture/<device>')
def capture(device):
    if device not in ['android','iphone']:
        abort(404)
    ts = str(int(time.time()))
    res = celery.send_task('tasks.capture_image',args=[device,ts])
    id =  res.task_id
    tasks[id] = {'folder': ts, 'device':device}
    return jsonify({'id': id})

if __name__ == '__main__':
    app.run()