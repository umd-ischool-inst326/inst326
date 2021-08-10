---
title: Web Data
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

# 

<a href="https://www.flickr.com/photos/inkdroid/15898721715/"><img width="80%" src="images/cloud.jpg"></a>

::: notes

What does the metaphor of the cloud mean?

:::

#

<a href="http://as2914.net/#/galaxy/ipv4?cx=-39&cy=-70&cz=10475&lx=0.0324&ly=-0.0390&lz=0.0019&lw=0.9987&ml=1000&s=1.75&l=1&v=2016-09-03"><img src="images/internet.png"></a>

::: notes

The metaphor of the cloud comes from visualizations like this that show the
many connections between computers on the Internet. This is a view of routers
on the Internet. Each dot in this visualization is a computer on the
Internet. The web is a layer over the Internet, where each of the dots is a
web server.

Optionally click on image and show how you can zoom in and search for UMD.

:::

# 

There is no cloud. It's just someone else's computer.

# 

::: columns

:::: column

<a href="https://artsandculture.google.com/exhibit/mapping-knowledge/QQ_clnh7"><img height="175" src="images/otlet.jpg"></a>

::::

:::: column

<a href="https://en.wikipedia.org/wiki/The_Mother_of_All_Demos"><img height="175" src="images/moad.png"></a>

::::

:::: column

<a href="https://en.wikipedia.org/wiki/World_Wide_Web"><img height="175" src="images/berners-lee.jpg"></a>

::::

:::

::: notes

* Mundaneum: started by Paul Otlet in 1895. A index of millions of cards about newspapers 
* Mother of All Demos: Doug Engelbart in 1968 at Stanford, demonstrating graphics, hypertext, mouse, networking.
* Tim Berners-Lee: created the web at CERN in 1989.

:::

#

### The Web's Primary Innovations

::: incremental

* **HTTP**: Hypertext Transfer Protocol
* **URL**: Uniform Resource Locator
* **HTML**: Hypertext Markup Language
* **Open Standards**: non-proprietary, IETF, W3C
* **Browser**: Lynx, Mosaic, Netscape, IE, Chrome, Firefox, Safari

:::

::: notes

This week we will be using these things from Python.

:::

#

<a href="https://en.wikipedia.org/wiki/Client%E2%80%93server_model"><img src="images/client-server.png"></a>

::: notes

The web follows a basic client/server model, where clients (web browsers running on various kinds of devices) fetch data (HTML, CSS, images, etc) from web servers using URLs and HTTP. This picture is over-simplified because you often fetch data concurrently from multiple web servers when rendering a web page.

:::

# 

<img width="80%" src="images/devtools.png">

::: notes

Have you ever wondered how a web browser works? Take a quick look at the developer tools in your browser. See how you can view the HTML, and all the network connections that go on when you view a web page? This week we will be learning about how to do some of those calls from Python.

:::

# Web APIs

::: fragment
Application Programming Interface
:::

::: notes

Today we are going to focus on something called APIs. Does anyone know what API stands for? APIs allow you to use HTTP to get data (usually JSON) from the web.

:::

#

<img width="80%" src="images/apis.png">

::: notes

With the expansion of mobile computing, and "smart" phones in the early 2000s there was an increasing need to make data available to apps that ran on the phone. These are examples of web platforms that you can install apps for on your phone.

:::

#

::: left

Remember how you can *create*, *read*, *update* and *delete* data in a database? Well you can do the same things with web APIs using HTTP *methods*:

:::

* **HTTP GET**: read
* **HTTP POST**: create
* **HTTP PUT**: update
* **HTTP DELETE**: delete

::: fragment
We're only going to be focused on GET.
:::

# 

<a href="http://docs.python-requests.org/"><img width="40%" src="images/requests.png"></a>

::: notes

To use Web APIs we need to use HTTP. Python has some built in modules to make it easy to work with HTTP. There is also the Python Requests extension which you can install which makes it even easier. That's what we will be using in class

:::

# 

## pip3 install requests

::: left

Run the command above in your terminal to install the requests module.

*pip* is the python packaging utility for installing *open source* software distributed through the [Python Package Index](https://pypi.python.org).

:::

::: notes

You will need to install the requests module first before you can use it, since it is a third party extension to Python that is distributed through the Python Package Index.

:::

# 

``` {.python .numberLines}
import requests

resp = requests.get('https://umd.edu')
print(resp)
```

::: fragment
<Response [200]>
:::

::: incremental
1. create Python HTTP request object for a GET
2. send HTTP request to webserver at umd.edu
3. receive the response from umd.edu
4. create and return a Python HTTP Response object
:::

#

::: left

We can use the Response object to print out the text of the response that was sent back. In this case we see HTML.

:::

``` {.python .numberLines}
import requests

resp = requests.get('https://umd.edu')
print(resp.text)
```

#

<a href="https://www.propublica.org/datastore/api/propublica-congress-api"><img src="images/propublica.png"></a>

# 

::: left
Now lets GET JSON data for the current members of the House of Representatives using the [ProPublica Congress API](https://www.propublica.org/datastore/api/propublica-congress-api). Notice that we need a key? You can get your own if you want or you can use the one I've put on ELMS.
:::

``` {.python .numberLines .smaller}
import requests

headers = {"X-API-KEY": "INSERT_VALID_KEY_HERE"}
url = 'https://api.propublica.org/congress/v1/116/house/members.json'

resp = requests.get(url, headers=headers)
print(resp.json())
```

#

::: left
Let's use Python's [json](https://docs.python.org/3.7/library/json.html) module that we've used in the past to pretty-print the data, so that it isn't all on one line, and uses an indent of 2 spaces.
:::


``` {.python .numberLines .smaller}
import json
import requests

headers = {"X-API-KEY": "INSERT_VALID_KEY_HERE"}
url = 'https://api.propublica.org/congress/v1/116/house/members.json'

members = requests.get(url, headers=headers).json()
print(json.dumps(members, indent=2))
```

#

## API Documentation

::: left

So how did I know about the special URL for the current members of the House? Most APIs come with *documentation* that explains how to use the API, which often includes the URLs you can use when talking to the APi, and what kinds of data you can expect to get back.

Let's look a little more closely at the [ProPublica API documentation](https://projects.propublica.org/api-docs/congress-api/).

:::

#

::: left

Let's use the [Get Current Members by State/District](https://projects.propublica.org/api-docs/congress-api/members/#get-current-members-by-statedistrict) and the [Get Recent Bills by a Specific Member](https://projects.propublica.org/api-docs/congress-api/bills/#get-recent-bills-by-a-specific-member) API calls together to print out the bills introduced by MD House members.

:::

<a href="https://en.wikipedia.org/wiki/Maryland%27s_congressional_districts"><img height="400" src="images/md-districts.png"></a>

# 

``` {.python .numberLines .smaller}
import json
import requests

def get(url):
    headers = {"X-API-KEY": "INSERT_KEY_HERE"}
    url = "https://api.propublica.org/congress/v1" + url
    data = requests.get(url, headers=headers).json()
    return data['results']

for member in get("/members/house/md/current.json"):
    print(member['name'], member['id'])
```

::: notes

Since we are going to be making multiple calls to the ProPublica API let's create a little function that will do the HTTP request and get the data back as JSON so we don't have to repeat this.

:::

# 

``` {.python .numberLines .smaller}
import json
import requests

def get(url):
    headers = {"X-API-KEY": "INSERT_KEY_HERE"}
    url = "https://api.propublica.org/congress/v1" + url
    data = requests.get(url, headers=headers).json()
    return data['results']

for member in get("/members/house/md/current.json"):
    print(member['name'])
    bill_data = get('/members/' + member['id'] + '/bills/introduced')
    for bill in bill_data[0]['bills']:
        print(bill['title'])
        print(bill['congressdotgov_url'])
    print('')
```

#

``` {.python .numberLines .smaller}
import json
import requests

def get(url):
    headers = {"X-API-KEY": "INSERT_YOUR_KEY"}
    url = "https://api.propublica.org/congress/v1" + url
    data = requests.get(url, headers=headers).json()
    return data['results']

for member in get("/members/house/md/current.json"):
    print(member['name'])
    bill_data = get('/members/' + member['id'] + '/bills/introduced')
    for bill in bill_data[0]['bills']:
        if bill['congress'] == "116":
            print(bill['title'])
            print(bill['congressdotgov_url'])
            print('')
```

::: notes

Limit output to bills introduced in the current (116th) congress.

:::