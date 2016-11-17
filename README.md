#faeria-pandora-stats-api

REST API for getting faeria-pandora-stats data

An implimentation of [Eve](http://python-eve.org/index.html)

Has CORS support, requests can be made to:

`http://faeriadecks.com:8962/ratings`

Requires

* python
* pip
* mongodb

##Install

```bash
  $ git clone https://github.com/Tidwell/faeria-pandora-stats-api
  $ cd faeria-pandora-stats-api
  $ pip install eve
```

##Run

```bash
  $ python app.py
```

Open `http://localhost:8962/ratings`


##Deploy

```bash
  $ nohup python app.py &
```