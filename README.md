# remote-lock
My new phone has a useless google assistant button. I'm creating a system that will allow me to rebind it to lock my computer, provided both have an internet connection.

# Architecture

## Phone

Button is rebound to a small HTTPS client that will send a message to a Flask API running on the server. Authentication will be fixed-key based. If it's breached I can always change it, and I'll put in a rate limit server-side to stop it being brute forced.

## Server

The server runs on two different systems:

First, it runs a Flask API that receives data from the phone.

Second, it establishes an authenticated and encrypted (fixed-key) socket connection with my laptop. 

When the Flask API receives a lock signal it will send a signal down the socket connection to my laptop.

## Laptop

Connects to the server over sockets, locks when it receives a lock signal. Fairly simple.
