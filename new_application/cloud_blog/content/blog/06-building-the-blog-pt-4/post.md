+++
title = 'Building the Blog Pt. 4: Wagtail'
subtitle = 'The "C" in CMS does not stand for "Clever"'
date = 2023-10-31
draft = false
show_date = true
tags = ["blog", "gcp", "dev", "django", "wagtail", "cms"]
show_title = true
show_subtitle = true
+++

This is the fourth post in a series of posts about how I attempted the Cloud Resume Challenge.

Intro: [The Cloud Resume Challenge and Building the Blog]({{< ref "/blog/02-building-the-blog-pt-1/post" >}})

Part 1: [Starting the web application]({{< ref "/blog/02-building-the-blog-pt-1/post" >}})

Part 2: [Continuous Delivery]({{< ref "/blog/03-building-the-blog-pt-2/post" >}})

Part 3: ["Production" ft. SQLite]({{< ref "/blog/05-building-the-blog-pt-3/post" >}})

Part 4: This post

The original [Cloud Resume Challenge](https://cloudresumechallenge.dev) called for a blog post on sites like [DEV Community](https://dev.to) or [Medium](https://www.medium.com). Already being a software engineer, I figured I could simply build a blog within my existing Django site. The thought to extend it with a CMS to make myself feel clever came later after I decided I wanted some more rich-text editing capabilities and less hand-written HTML/CSS.

#### Enter Wagtail

[Wagtail](https://wagtail.org/) is a Django-based, open-source CMS. It felt immediately relevant to my needs and interests.

I simply followed the [Wagtail tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html) to get started. The original version of this blog even followed the "basic blog" section of the tutorial.

The Wagtail tutorial covers setting it up from scratch with Wagtail alone, but since I already had the site running in Django I also followed the directions to [install Wagtail alongside an existing Django installation](https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html).

This worked like a charm. I didn't even need to change any CI/CD processes or database configuration - it all worked and deployed out of the box with no issues.

#### What's the catch?

Where I ran into issues with Wagtail was customising it for a development-themed blog. Firstly - if you've read any of my old posts - you'll notice the images are resized to the point where they're not really readable.

Secondly - code snippets. I followed parts of a [tutorial by Coding for Everybody](https://www.youtube.com/watch?v=6YrbkE0_RPQ) (sadly, a channel that appears to have gone defunct after this was posted) to get some rich text capabilities added. I realised most weren't for my needs so I simply settled for the default [Wagtail StreamFields](https://docs.wagtail.org/en/v5.1.1/topics/streamfield.html) to get what I wanted.

{{< gist ajpotts01 41ccdf387419b35aa8cbcf1d7d4e3707 >}}

This is where I started to run into problems. The `code` StreamField item only supported single lines, like your backticks in Markdown. I tried to search for a Wagtail-native solution to this, but ended up having to settle for one of the following choices:

* Add [the `wagtailcodeblock` package](https://github.com/FlipperPA/wagtailcodeblock)
* Embedding [Github gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)

I ended up going with `wagtailcodeblock` as it turned out [embedding gists was not supported](https://github.com/wagtail/wagtail/issues/5087).

This functionality was in part provided by [PrismJS](https://prismjs.com/). I didn't quite figure out whether it was the Python package or PrismJS causing it, but the code snippets - while large and presentable - were always on top of every page element, including my nav bar.

{{< img-custom src="/img/blog/06-building-the-blog-pt-4/why_prismjs.png" width="700px" alt="Wagtail code block overlapping the nav bar" >}}

Not ideal. Despite my attempts, no CSS could fix this.

#### A lightbulb moment

At this point, I realised most of the Wagtail documentation, including the code snippets I was trying to emulate, were actually written in Markdown. Writing posts in Markdown is a very viable options, with [static-site generators](https://jamstack.org/generators/) becoming more popular by the day.

I don't regret choosing the Django/Wagtail combination. I think it taught me a lot of things that the regular Cloud Resume Challenge wouldn't have. But at this point:

* I don't really need a CMS
* The load balancer requirements imposed by Cloud Run are costing me a fair chunk of cash
* Static site generators can make this way easier for me

I was planning to get around the load balancer point by moving to [Firebase hosting](https://firebase.google.com/) anyway, so it's probably time to do that all in one hit.

I've already selected and am implementing my new approach - my next post will be done when I've migrated across.

If you are still interested in the Wagtail implementation, check out the pull requests [here](https://github.com/ajpotts01/ajp-cloud-resume/pull/27) and [here](https://github.com/ajpotts01/ajp-cloud-resume/pull/31).

Thanks for reading.