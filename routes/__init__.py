from flask import Flask

app = Flask(__name__)
import routes.square
import routes.lazydev
import routes.greedymonkey
import routes.digitalcolony
import routes.railway
import routes.payload
import routes.swissbyte