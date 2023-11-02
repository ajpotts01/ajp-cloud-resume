+++
title = 'Building the Blog Pt. 5: Migrating to Hugo and Firebase'
subtitle = 'Sometimes simpler is far better'
date = 2023-11-02
draft = false
show_date = true
tags = ["blog", "gcp", "dev", "django", "wagtail", "cms", "hugo", "golang", "ssg"]
show_title = true
show_subtitle = true
+++

This is the fifth (and final?) post in a series of posts about how I attempted the Cloud Resume Challenge.

Intro: [The Cloud Resume Challenge and Building the Blog]({{< ref "/blog/02-building-the-blog-pt-1/post" >}})

Part 1: [Starting the web application]({{< ref "/blog/02-building-the-blog-pt-1/post" >}})

Part 2: [Continuous Delivery]({{< ref "/blog/03-building-the-blog-pt-2/post" >}})

Part 3: ["Production" ft. SQLite]({{< ref "/blog/05-building-the-blog-pt-3/post" >}})

Part 4: [Wagtail]({{< ref "/blog/06-building-the-blog-pt-4/post" >}})

Part 5: This post

I detailed the reasons why, but I wasn't too happy with the way things were running. Cost was prohibitive thanks to the load balancer requirement, but I was still unhappy with how my website looked.

#### Switching to Hugo

A few things alerted me to [Hugo](https://gohugo.io/) as an alternative:
- Discussion of static site generators with ex-colleagues when even beginning this challenge
- [Simon Späti](https://ssp.sh/) making mention of his own SSG journey on Twitter
- Conversations with friends [Maladius](https://maladius.com/) and [Jonathan Neo](https://jonathanneo.com/) about the power of Hugo

I like the simplicity of creating Markdown files and spitting out HTML. My blog posts are now contained in a folder structure split up by post.

{{< img-custom src="/img/blog/07-building-the-blog-pt-5/blog_folder_structure.png" class="blog" alt="Screenshot of blog folder structure" >}}

#### Introducing Hugo

#### Introducing Firebase

This switch also made me re-evaluate the cloud components. I had already decided to put [Firebase Hosting](https://firebase.google.com/) in front of the Cloud Run service running my original Django application. At the time, this was the only other way to get a custom domain and SSL etc. on a Cloud Run service instead of the global load balancer I was already using. This migration to Hugo was just another reason to expedite that.

#### Reducing Complexity and Cost

There has been a massive list of pros in moving:
- Most of my GCP infrastructure has been removed
- I no longer have to maintain posts in a database
- These posts are now in Github, giving me peace-of-mind about data loss
- I can simply edit text files and merge into my `main` branch to deploy to Firebase instead of needing to log in

The one small con is that there is a lot more nuance than one would expect moving to an SSG like Hugo. I don't exactly have complete control of my layouts out of the box - my resume page is now a single column no matter what screen size you're on, and I've had to insert custom HTML shortcodes to get images displayed the way I want them.

Overall this has been more beneficial and I feel far better about the site now. I can just focus on building things and writing posts!

Thanks for reading.