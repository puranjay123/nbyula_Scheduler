# nbyula_Scheduler

[![PyPI](https://img.shields.io/pypi/v/django-pg-zero-downtime-migrations.svg)](https://pypi.org/project/django-pg-zero-downtime-migrations/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-pg-zero-downtime-migrations.svg)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-pg-zero-downtime-migrations.svg?label=django)
[![PyPI - License](https://img.shields.io/pypi/l/django-pg-zero-downtime-migrations.svg)](https://raw.githubusercontent.com/tbicr/django-pg-zero-downtime-migrations/master/LICENSE)


[![GitHub last commit](https://img.shields.io/github/last-commit/tbicr/django-pg-zero-downtime-migrations/master.svg)](https://github.com/tbicr/django-pg-zero-downtime-migrations/commits/master)
[![Build Status](https://github.com/tbicr/django-pg-zero-downtime-migrations/actions/workflows/check.yml/badge.svg?branch=master)](https://github.com/tbicr/django-pg-zero-downtime-migrations/actions)
![Screenshot (2062)](https://user-images.githubusercontent.com/55429956/191023877-efec4a05-dc8b-45d7-ba04-14c09a94cc36.png)
![Screenshot (2057)](https://user-images.githubusercontent.com/55429956/191023887-f99d8c47-1253-44d5-8545-6c3413a0cb2f.png)
![Screenshot (2058)](https://user-images.githubusercontent.com/55429956/191023891-23cce450-89e3-41a3-8fa8-d0d087cc6baf.png)
![Screenshot (2059)](https://user-images.githubusercontent.com/55429956/191023894-a8f3258d-3469-46c8-9e3a-245d7d951561.png)
![Screenshot (2060)](https://user-images.githubusercontent.com/55429956/191023897-5ad5ac01-bba3-4dee-983e-c498ee007bfe.png)
![Screenshot (2061)](https://user-images.githubusercontent.com/55429956/191023903-895e3779-bf7e-4bde-b7df-1b94d9ec7bf8.png)

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** 
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Terraformers Scheduling App[VastuMantra]</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/puranjay123/nbyula_Scheduler/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/puranjay123/nbyula_Scheduler/">View Demo</a>
    ·
    <a href="https://github.com/puranjay123/nbyula_Scheduler/issues">Report Bug</a>
    ·
    <a href="https://github.com/puranjay123/nbyula_Scheduler/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

   ```from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from faunadb import query as q
import pytz
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import hashlib
import datetime



client = FaunaClient(secret="fnAEwyz9miACS-JIP4ljPrO0D506SLYVf_iIOrVW")
indexes = client.query(q.paginate(q.indexes()))


def login(request):
    if request.method == "POST":
        username = request.POST.get("username").strip().lower()
        password = request.POST.get("password")

        try:
            user = client.query(q.get(q.match(q.index("users_index"), username)))
            if hashlib.sha512(password.encode()).hexdigest() == user["data"]["password"]:
                request.session["user"] = {
                    "id": user["ref"].id(),
                    "username": user["data"]["username"]
                }
                return redirect("App:dashboard")
            else:
                raise Exception()
        except:
            messages.add_message(request, messages.INFO,"You have supplied invalid login credentials, please try again!", "danger")
            return redirect("App:login")
    return render(request,"login.html")

def create_appointment(request):
    if "user" in request.session:
        if request.method=="POST":
            name=request.POST.get("name")
            description=request.POST.get("description")
            time=request.POST.get("time")
            date=request.POST.get("date")
            try:
                user = client.query(q.get(q.match(q.index("events_index"), date,time)))
                messages.add_message(request, messages.INFO, 'An Event is already scheduled for the specified time.')
                return redirect("App:create-appointment")
            except:
                user = client.query(q.create(q.collection("Events"), {
                    "data": {
                        "name": name,
                        "description": description,
                        "time": time,
                        "date": date,
                        "user": request.session["user"]["username"],
                        "status": 'False',
                    }
                }))
                messages.add_message(request, messages.INFO, 'Appointment Scheduled Successfully.')
                return redirect("App:create-appointment")
        return render(request,"appoint/create-appointment.html")
    else:
        return HttpResponseNotFound("Page not found")


def dashboard(request):
    if "user" in request.session:
        user=request.session["user"]["username"]
        context={"user":user}
        return render(request,"index.html",context)
    else:
        return HttpResponseNotFound("Page not found")

def today_appointment(request):
    if "user" in request.session:
        appointments=client.query(q.paginate(q.match(q.index("events_today_paginate"), request.session["user"]["username"],str(datetime.date.today()))))["data"]
        appointments_count=len(appointments)
        page_number = int(request.GET.get('page', 1))
        appointment = client.query(q.get(q.ref(q.collection("Events"), appointments[page_number-1].id())))["data"]
        if request.GET.get("complete"):
            client.query(q.update(q.ref(q.collection("Events"), appointments[page_number-1].id()),{"data": {"status": "True"}}))["data"]
            return redirect("App:today-appointment")
        if request.GET.get("delete"):
            client.query(q.delete(q.ref(q.collection("Events"), appointments[page_number-1].id())))
            return redirect("App:today-appointment")
        context={"count":appointments_count,"appointment":appointment,"page_num":page_number, "next_page": min(appointments_count, page_number + 1), "prev_page": max(1, page_number - 1)}
        return render(request,"today-appointment.html",context)
    else:
        return HttpResponseNotFound("Page not found")


def all_appointment(request):
    if "user" in request.session:
        appointments=client.query(q.paginate(q.match(q.index("events_index_paginate"), request.session["user"]["username"])))["data"]
        appointments_count=len(appointments)
        page_number = int(request.GET.get('page', 1))
        appointment = client.query(q.get(q.ref(q.collection("Events"), appointments[page_number-1].id())))["data"]
        if request.GET.get("delete"):
            client.query(q.delete(q.ref(q.collection("Events"), appointments[page_number-1].id())))
            return redirect("App:all-appointment")
        context={"count":appointments_count,"appointment":appointment, "next_page": min(appointments_count, page_number + 1), "prev_page": max(1, page_number - 1)}
        return render(request,"all-appointment.html",context)
    else:
        return HttpResponseNotFound("Page not found")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username").strip().lower()
        email = request.POST.get("email").strip().lower()
        password = request.POST.get("password")

        try:
            user = client.query(q.get(q.match(q.index("users_index"), username)))
            messages.add_message(request, messages.INFO, 'User already exists with that username.')
            return redirect("App:register")
        except:
            user = client.query(q.create(q.collection("users"), {
                "data": {
                    "username": username,
                    "email": email,
                    "password": hashlib.sha512(password.encode()).hexdigest(),
                    "date": datetime.datetime.now(pytz.UTC)
                }
            }))
            messages.add_message(request, messages.INFO, 'Registration successful.')
            return redirect("App:login")
    return render(request,"register.html")```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
