+++
title = 'Building the Blog Pt. 3: "Production" ft. SQLite'
subtitle = 'Insane approaches to running at low cost'
date = 2023-10-25
draft = false
show_date = true
tags = ["blog", "gcp", "dev", "django", "terraform", "github", "ci/cd", "sqlite", "litestream"]
show_title = true
show_subtitle = true
+++

This is the fourth post in a series of posts about how I attempted the Cloud Resume Challenge.

Intro: [The Cloud Resume Challenge and Building the Blog]({{< ref "/blog/02-building-the-blog-pt-1/post" >}})

Part 1: [Starting the web application]({{< ref "/blog/02-building-the-blog-pt-1/post" >}})

Part 2: [Continuous Delivery]({{< ref "/blog/03-building-the-blog-pt-2/post" >}})

Part 3: This post

At this point, the site was functional and deploying, but not really ready for a few reasons:

* I was still using the insecure Django secret key that comes with the project by default
* The site was running on Cloud Run, with the development webserver
* The site was running with the development SQLite - so any time the Cloud Run container shut down you'd lose any dynamic content
* Static resources were in the container, not stored in a storage bucket per best practice.

I'm sure there were others. At this point the site was just a proof of concept.

#### The Database Dilemma

The Cloud Resume Challenge's GCP version assumes:

* One is creating a static set of pages
* Hosting them in a bucket behind a load balancer
* Using Cloud Functions for extra backend functionality (visitor counter)
* Using Javascript for extra frontend functionality (calling the visitor counter)
* Storing any data in Firestore.

This is a great, easy, cheap approach.

Doing this the "hard" way messed things up for me in one way: Django doesn't natively support Firestore. This has a few options to solve with, and I think I settled on djangae at the time. However, my goal with this was to also set up a CMS for blog posts. In the Django universe, this leads to Wagtail. At time of build, Wagtail didn't support any of djangae's extras.

Cloud SQL was the obvious choice for Django, but there's no real cheap option - Cloud SQL is really an enterprise-licenced product, even if using MySQL. I sat on the fence for a week between two options:

* Running Postgres or MySQL myself on the cheapest possible Compute Engine VM
* Taking the hit and spending money on Cloud SQL for a blog that might never have any readers.

At this point something ridiculous occurred to me.

#### Enter SQLite... but not as you know it

SQLite is gaining popularity for real, production web applications. The most recent example is Turso, but there are a number of SQLite or SQLite-like products that offer what you need and scale to ridiculous like [4 million queries per second on a single server](https://use.expensify.com/blog/scaling-sqlite-to-4m-qps-on-a-single-server).

My idea was to just see if I could use [GCS Fuse](https://github.com/GoogleCloudPlatform/gcsfuse) to directly interact with Google Cloud Storage. I actually don't remember any roadblocks I ran into, but something gave me the impression that it was a dead end. The perils of writing a blog post way after it was built.

However, I found merit in an open-source project called [Litestream](https://litestream.io/), and its replication capabilities are in use right now, as you read this blog. It was simple to set up, using [this blog post](https://usher.dev/posts/django-on-flyio-with-litestream-litefs/) as the majority of my technical inspiration, and it was simple enough to edit it for my GCS purposes.

The Litestream configuration was dead simple:

{{< gist ajpotts01 da32a6d708a48e019cf96ace4e248d60 >}}

I set an environment variable in the deployment pipeline for my desired bucket URL, and Litestream's configuration takes care of the actual command to run once it starts up. In this fashon, I'm able to run gunicorn as my web server to start my Django app for the site.

There are a couple of other things in my server startup script, for doing static file collection, running database migrations, etc.

{{< gist ajpotts01 d6992e69bfb0e0ea9691f017f37fd999 >}}

This has worked like a dream out of the box, and costs me probably 2 cents a month to run.

Just on migrations. If you look at the code merge for this part of the build, there is some code for setting up the Django admin panel user.

{{< gist ajpotts01 ba96f1b08d745013ed27aa2401c0c3db >}}

This code is run on migration so a super user can be created, since there's no way to do it from the command line for a production application. I have the password stored in GCP Secret Manager, and the service account running the app has permissions to access it.

I have some extra code in there for running migrations locally - if I'm running in debug mode or unit tests, the code would fail if trying to access Secret Manager since it's likely my environment variables aren't set. The link to explain this code is added as a comment in the snippet above.

So, there you have it. Litestream was a bit of a godsend here, but on review I think GCS Fuse might have worked just as well.

The pull request and merge for this part of the build can be found [here](https://github.com/ajpotts01/ajp-cloud-resume/pull/25).

In the next post I'll cover adding Wagtail to the project and getting this blog rolling.

Thanks for reading.