# Kin Proxy

A proxy to make Kin's calendar output more sensible.

## Requirements

* Flask
* icalendar
* pytz

## Running

You can run it locally using `python kinproxy.py`, but for actual internet use I set it up beind nginx using [uWSGI](http://flask.pocoo.org/docs/0.10/deploying/uwsgi/).

## Usage

The server requires you to supply a `token` parameter; this token is the same one given in your Kin calendar's URI.

A valid URL for the Kin proxy would look like `http://localhost:5000/?token=00000000-0000-0000-0000-000000000000`.
