# -*- coding: utf-8 -*-

from eve import Eve
app = Eve()

if __name__ == '__main__':
    app.run(port=8962, host='0.0.0.0')