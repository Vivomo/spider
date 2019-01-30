# spider
spider test

* scrapy startproject <project name>
cd
* scrapy genspider comix twcomix.com

debug

create main.py
```python
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'comix'])
```