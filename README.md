# Linkr :paperclip:

Linkr is a simple way to save, organize, and share web pages. Links are separated into user-defined `buckets`, which can be as broad or narrow as desired. multiple buckets can be grouped into a `tub`. A sample structure is outlined below.

```
├── Search Engines
│   ├── Bing
│   ├── DuckDuckGo
│   ├── Google
│   └── Yahoo
└── Social
    ├── Photos
    │   ├── Flickr
    │   └── Instagram
    ├── Places
    │   ├── Facebook
    │   └── FourSquare
    └── Work
        └── LinkedIn
```

Why use Linkr instead of your browser's built-in Bookmarks? Linkr securely stores all your pages in the cloud and won't require you to sync your browser by linking it with your email account. In addition, Linkr allows you to easily share any bucket with a single click--letting you pass them along to coworkers, family, and friends--who can then easily view and access the links through our simple iterface. No more emailing lists of links!


## Getting Started
Before you begin, make sure you have the lastest version of Python & pip
```bash
python --version
>>> Python 3.7.3
pip --version
>>> pip 19.1.1 from /../../pip (Python 3.7)
```

If necessary, download both with the python-dev package
```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

[1] Clone the repository
```bash
git clone https://github.com/minelminel/linkr.git
cd linkr
```

[2] Create virtual environment (optional)
```bash
virtualenv -p python3.7 .
source bin/activate
```

[3] Install dependencies
```bash
pip install -r requirements.txt
```

[4] Start the server
```bash
python manage.py runserver
```

[5] View in browser

[localhost:8000](localhost:8000)

## Docker
[1] Make sure you have Docker Desktop & Docker Compose installed
```bash
docker --version
docker-compose --version
```

Docker Desktop can be downloaded by visiting [this link](https://www.docker.com/products/docker-desktop)

docker-compose can be installed via `pip`
```bash
pip install docker-compose
```

[2] Build Docker Image
```bash
docker build -t linkr:lastest .
```

[3] Spin Up Container
```bash
docker-compose up
```