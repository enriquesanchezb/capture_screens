# Capture Simulator/Emulator screens on demand

Buddy project to capture screens of Android Emulators or iPhone Simulator on demand and save the screen recording as GIF.


## How it works

Install [foreman](https://github.com/ddollar/foreman), [redis](https://redis.io/), [imagemagick](https://www.imagemagick.org) and [virtualenv](https://virtualenv.pypa.io/en/stable/).

Create a new Python environment and install requirements.

Launch foreman with `foreman s`. This will launch a service in `http://localhost:5000/' you can use to start and stop a recording session.

The service takes a screenshot of the window every second and save the image into `captures` folder. Once you request stop the screen recording all the images will attached to a gif file and saved into `videos` folder.


### Start a recording session

`http://localhosto:5000/capture/<device>`

Where `<device>` could be `android` or `iphone`.

If everything is ok, the service will respond you with an **id** that you need to use to stop the service.


### Stop a recording session

`http://localhosto:5000/stop/<id>`

Where `<id>` is the id you received when you started the recording session.

Returns the name and the path of the gif generated.


## Others scripts

The screen recording uses a binary executable to identifies all the windows. You can find this script into `helpers` folder as `GetWindowList`. If you need recompilate this executable you can do it using `generate_window_script.sh`.

## License MIT

Copyright 2017 Enrique Sánchez-Bayuela

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.