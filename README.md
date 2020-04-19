![Alt text](/docs/screenshot.png?raw=true)

# COVID-19 Screensaver
COVID-19 themed screensaver for Linux inspired by the classic flying toasters screensaver from After Dark.

### Requirements

* X Window System
* Python 3.8
* Pyglet 1.5.0
* Numpy 1.18.2

### Installation

Clone the repository to a local directory:
```bash
git clone https://github.com/martinsprojects/covid19-screensaver.git
```

Install the Python 3.8 dependencies:
```bash
pip install -r requirements.txt
```

Run the software:
```
python covid19-screensaver.py
```

### Todo

* Add batch rendering of sprites.
* Make sprite animation asynchronous.
* Make it run as an actual screensaver using Xscreensaver.
* Other optimizations and code refactoring/cleanup.