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

#### Introducing Hugo

[Hugo](https://gohugo.io) is a static site generator written in [Go](https://go.dev/). It follows the conventions of a lot of other static site generators:
- Pages are written in the [CommonMark](https://commonmark.org/) dialect of Markdown
- An opinionated project structure is provided for ease-of-use
- Some form of extra HTML templating is supported (in our case, [Go templates](https://pkg.go.dev/html/template)) for flexibility
- A CLI tool parses all the Markdown and spits out HTML for publishing.

#### Switching to Hugo

A few things alerted me to Hugo as an alternative:
- Discussion of static site generators with ex-colleagues when even beginning this challenge
- [Simon Späti](https://ssp.sh/) making mention of his own SSG journey on Twitter
- Conversations with friends [Maladius](https://maladius.com/) and [Jonathan Neo](https://jonathanneo.com/) about the power of Hugo

I like the simplicity of creating Markdown files and spitting out HTML. My blog posts are now contained in a folder structure split up by post.

{{< img-custom src="/img/blog/07-building-the-blog-pt-5/blog_folder_structure.png" class="blog" alt="Screenshot of blog folder structure" >}}

Hugo supports custom themes, and there are [many](https://themes.gohugo.io/) of them, but I opted to start by recreating the original site's look and feel. Studying some of the more popular themes like [PaperMod](https://themes.gohugo.io/themes/hugo-papermod/) and [Ananke](https://themes.gohugo.io/themes/gohugo-theme-ananke/) has helped me tweak some of the CSS.

I've also introduced some [shortcodes](https://gohugo.io/content-management/shortcodes/) to better manage how I embed images in posts, but for the most part this is just pure Markdown.

#### Introducing Firebase

This switch also made me re-evaluate the cloud components. I had already decided to put [Firebase Hosting](https://firebase.google.com/) in front of the Cloud Run service running my original Django application. At the time, this was the only other way to get a custom domain and SSL etc. on a Cloud Run service instead of the global load balancer I was already using. This migration to Hugo was just another reason to expedite that.

Firebase is an all-in-one "backend as a service" solution backed by Google Cloud. It offers easy integration with cloud storage, serverless compute, databases, and authentication services to make building apps easier. A lot of the features would go unused with this static site, but it is still a cost effective option that can be attached to my existing Google Cloud project.

In addition, Google Analytics can be added to the site, which I will definitely do soon.

#### Moving Across

The steps were actually fairly simple once I'd built the site:
- Use Terraform to create my Firebase project
- Migrate CI/CD to Hugo + Firebase
- Update my Google Domains
- Decommission the old site

There's only two pieces of Terraform required to set up - turning on the API, and creating the project, attaching it to my existing Google Cloud project.

{{< gist ajpotts01 81ddb1577bc2b218b0f26bbfd9f9bf74 >}}

I had permissions issues trying to create the Firebase project, so I created it in the UI, and [imported](https://developer.hashicorp.com/terraform/cli/import) it into my Terraform state.

The CI is really simple: install Hugo and try build the site.

{{< gist ajpotts01 c64d0ee2091e976166970f47dbf278c5 >}}

To deploy, I first needed to install Firebase tooling and add a few artefacts to my project. The Firebase CLI is a Typescript app, so you need [NodeJS](https://nodejs.org) to install it. I use [nvm for Windows](https://github.com/coreybutler/nvm-windows) to manage my Node versions instead of downloading the latest version. Once it's installed, you simply run `npm install -g firebase-tools` and you're good to go.

I ran `firebase init` in the root of my `cloud_blog` folder and set it up for hosting only.

{{< img-custom src="/img/blog/07-building-the-blog-pt-5/firebase_example.png" class="blog" alt="Screenshot of Firebase CLI" >}}

In my case, I followed the prompts to hook it up to an existing project, and chose not to set up Github Actions, as I did that myself after the fact.

This is done by running `firebase login:ci` - which generates a token to use. This then gets used in my deployment pipeline.

{{< gist ajpotts01 917bf31afe2eba524891dd409bafa7cb >}}

This is much simpler than what I was doing before.

#### Reducing Complexity and Cost

There has been a massive list of pros in moving:
- Most of my GCP infrastructure has been removed
- I no longer have to maintain posts in a database
- These posts are now in Github, giving me peace-of-mind about data loss
- I can simply edit text files and merge into my `main` branch to deploy to Firebase instead of needing to log in

The one small con is that there is a lot more nuance than one would expect moving to an SSG like Hugo. I don't exactly have complete control of my layouts out of the box - my resume page is now a single column no matter what screen size you're on, and I've had to insert the custom HTML shortcodes to get images displayed the way I want them.

Overall this has been more beneficial and I feel far better about the site now. I can just focus on building things and writing posts!

Thanks for reading.