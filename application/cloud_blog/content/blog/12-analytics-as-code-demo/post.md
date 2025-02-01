+++
title = 'Exploring "Analytics as Code"'
subtitle = 'From database to dashboard with no BI tool in sight'
date = '2024-02-25'
draft = false
show_date = true
tags = ["data analysis", "data engineering", "duckdb", "malloy", "notebooks"]
show_title = true
show_subtitle = true
+++

#### The beginning
Data and analytics projects have gradually introduced more software engineering practices over the past decade. When I first discovered business intelligence and worked on a data warehouse, the toolkit was largely UI driven:
- A drag and drop ETL tool (e.g. [Microsoft SSIS](https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services?view=sql-server-ver16), [Informatica PowerCenter](https://docs.informatica.com/data-integration/powercenter/10-5/getting-started/product-overview/introduction.html), [IBM DataStage](https://www.ibm.com/products/datastage)) to create a data warehouse
- A general-purpose, OLTP database to store the data
- Some form of [MOLAP](https://en.wikipedia.org/wiki/Online_analytical_processing#Multidimensional_OLAP_.28MOLAP.29) - AKA "cubes" - to store measures/logic over the top of the database (e.g. [Microsoft SSAS](), [IBM Cognos/TM1](), [SAP Business Objects]())
- Tools for dashboarding (e.g. [Tableau](), [QlikView]()) and paginated reporting (e.g. [Crystal Reports](), [Microsoft SSRS]()).

These did require some level of code to be written, but they were usually declarative, domain-specific languages. SQL has always ruled the database. For cubes, MDX was popular, and most dashboarding tools have some kind of their own language for calculating measures on the fly.

#### Hello, Modern Data Stack
A lot of things happened between the early BI days and now. I'm not going to write an entire history of the "big data" explosion. But the move towards today's "Modern Data Stack" has gradually removed the dependency on UIs:
- Small to medium data is more easily processed with cheap yet powerful serverless compute, running code in a language of your choice
- Larger datasets are easily handled with massively-parallel processing technologies like Apache Spark, Snowflake and BigQuery
- The wide-ranging support of SQL across all these technologies has allowed transformation to happen later in the pipeline
- The new generation of SQL runners like dbt, Dataform and SQLMesh make it easier to run complex workflows than ever before.

All of the above have allowed us to follow an extract-load-transform pattern - ingesting data faster, storing it cheaply in its original form, and transforming it with the native language of data and powerful compute. All of this has let us write code to do so instead of our IP living inside a GUI. There are exceptions - tools like Fivetran still put a UI in front of us. But these tools focus purely on ingestion, still allowing us to write code everywhere else.

This has given us 

#### But the frontend is still hanging on
- [DataEngBytes](https://dataengconf.com.au/) was a great day of data and ML talks. My favourite was probably [Ben Boyter's talk](https://www.youtube.com/watch?v=ovXPxdJJSU8) on the possibilities of data processing with [Go](https://go.dev). Utah Go community regular [Miriah Peterson](https://www.youtube.com/c/Miriahpeterson) is another figure to follow in this space. She's actually doing a [presentation](https://www.linkedin.com/events/end2enddataanalyticsfornon-prof7148080306338578432/?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_content%3BYB8KerkfQQqDiuN4pLCPYA%3D%3D) tomorrow on end-to-end analytics with the language.

- On the topic of Go, the [Golang Syd](https://www.meetup.com/golang-syd/) meetup has had killer talks in both events I attended in 2023:
  - [Evergen](https://evergen.energy/) using Go in their renewable energy platform

  - [Nearmap](https://www.nearmap.com/au/en?utm_source=google&utm_medium=organic) using Go in their highly advanced computer vision/GIS solutions

  - Broderick Westrope's talk on [terminal user interfaces and charm.sh](https://github.com/Broderick-Westrope/golang-syd-meetup-nov2023) really opened me up to some project ideas with Go that I will take a crack at this year.

#### Books
I read a LOT of books this year, so here are a few favourites:
- [Network Science with Python](https://www.packtpub.com/product/network-science-with-python/9781801073691). I really think this is an untapped resource, especially in the security domain where I currently work. David Knickerbocker has put together some great exercises and has an easily digestible writing style.

- [Data Engineering with AWS - Second Edition](https://www.packtpub.com/product/data-engineering-with-aws-second-edition/9781804614426). What a whopper. This is easily one of the most comprehensive data engineering books I've read. I wish I had read the original edition in 2021. Despite the AWS tag, this really goes into a lot of detail about data modelling approaches, small-to-medium data processing with serverless frameworks, and - gasp - tips for having meetings with stakeholders!

- [Test Driven Development with Python](https://www.amazon.com/Test-Driven-Development-Python-Selenium-JavaScript-ebook/dp/B074HXXXLS). This is an old one, but I still highly recommend. The second edition might have a few things in it that modern developers don't recommend anymore, and its examples are in Django 1.x, but I have still found it very useful. It also punches well above its weight in examples - going into deploying apps on VMs and using nginx to serve them, which are skills still very relevant today. Note: A free version is available on the [author's website](https://obeythetestinggoat.com) and a 3rd edition is currently being phased in on this version with Django 4.x!

- [The Cloud Resume Challenge Guidebook](https://cloudresumechallenge.dev/). I got the GCP version, and it inspired the creation of this website.

The first two books from Packt are on sale in digital form for $10 right now - I highly recommend them.

#### Courses
I've gone through [MOOCs](https://en.wikipedia.org/wiki/Massive_open_online_course) this year to get further up to date with my software development skills:

- [Boot.dev](https://boot.dev) is entirely focused on backend development, with courses in Python, Javascript and Go. There are also courses on modern CI/CD and a new one on Kubernetes. A lot of the material is introductory for people that don't have a CS background, but I learned a ton from the Go courses and some of the things I built after following them have featured on this blog. Highly recommended for beginners or people who want to learn Go in a very practical way.

- [testdriven.io](https://testdriven.io). I have done their courses on [TDD with Django Rest Framework and Docker](https://testdriven.io/courses/tdd-django/) and [Full-stack Django with HTMX, Alpine and Tailwind](https://testdriven.io/courses/django-htmx/). Both are fantastic and cheap, although it is all written material, no videos. I don't think this matters. I still have a few to go through as I picked up a holiday bundle.

Also a special shout-out to [Microsoft Learn](https://learn.microsoft.com). I covered the applied skills experiment in a [previous blog post]({{< ref "/blog/09-ms-applied-skills-power-automate/post" >}}) and will continue with these this year.

#### What am I doing in 2024?

Here are my learning goals in 2024:

- Attend, at the very least, one developer conference. I missed [GopherCon](https://gophercon.com.au) last year to scheduling issues and have attended multiple data engineering conferences before, so want to change it up. NDC Sydney is **very** expensive to the point where I'm too guilty to ask my employer to subsidise it, so I'll likely target [ServerlessDays ANZ](https://anz.serverlessdays.io/). [Peter Hanssens](https://www.peterhanssens.com.au/) is a great conference organiser and gives his all for multiple engineering communities, so it will be good to continue supporting him and his team of organisers

- Achieve my [Terraform certification](https://www.hashicorp.com/certification/terraform-associate). I believe in the technology - despite the HashiCorp drama - and wanted to get his done over the holidays but just didn't have the time

- Achieve my [Microsoft Azure Developer certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/). I have a 50% off voucher from MS and am annoyed that I haven't kept my .NET skills up to date at all so this seems to be a way to do it and study the MS approach to serverless computing

- Build more projects: 

  - With [HTMX](https://htmx.org). I don't know if this will ever become a skill needed for my line of work, but I don't care. I love it and will make future blog posts on it soon

  - With [Django](https://djangoproject.com). The first version of this site was a Django site and even though it didn't survive, I want to keep building with it

  - With [Angular](https://angular.io). It was my first SPA framework and as you can probably tell, I'm a big fan of opinionated frameworks. I think they help generalists like me just get work done

  - With [ASP.NET](https://asp.net). While I love Django, it's not hugely popular in Australia and I'd like to get back to my C# roots

  - With [Go](https://go.dev). I have a terminal UI project in mind for later this year and I still want to get better at using Go to build APIs and DevOps tooling

  - With [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric). Community legend [Mimoune Djouallah](https://datamonkeysite.com/about/) was the first person to make me aware of the power of [BigQuery](https://cloud.google.com/bigquery) and we've talked about random data engineering stuff for years. He's now over at Microsoft as a program manager for Fabric and he's convinced me to take a stab at it.

- Keep reading!

This seems like a lot, and I'm sure it will change over time as my priorities shift and new shiny rabbits appear. But it's a start, and hitting one or two of these really well will still make me happy by the end of the year.

Thanks for reading, and happy new year.