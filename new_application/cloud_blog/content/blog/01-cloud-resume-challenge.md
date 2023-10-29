+++
title = 'The Cloud Resume Challenge and Building the Blog'
subtitle = 'The where, why and how this blog started'
date = 2023-10-02
draft = false
show_date = true
tags = ["blog", "post", "gcp", "dev"]
+++

This is the first post in a series of posts about how I attempted the Cloud Resume Challenge.

Intro: This post

Part 1: Building the Blog Pt. 1: Starting the web application

Welcome to the blog.

There are two parts to building this and they sort of happened along a common thread:

- I discovered Forrest Brazeal's excellent [Cloud Resume Challenge](https://cloudresumechallenge.dev) through reading online
- I got really into a few side projects of mine that warranted longer-form writing - a Github README wasn't sufficient

The challenge itself is designed for people looking to get into cloud infrastructure - many of the people who complete it go on to take jobs in cloud engineering and DevOps. It breaks down into a few pieces:

1. Get an introductory cloud certification
2. Build a static website with a resume using HTML/CSS
3. Serve it online in a public cloud (with HTTPS + DNS component)
4. Add a backend with serverless compute and a database to track visitor counts
5. "DevOps" stuff (infrastructure-as-code, CI/CD)
6. A blog post on a public site like [DEV Community](https://dev.to) or [Medium](https://www.medium.com). <== we are here.

I've worked in technology for 15+ years, done a lot of the above before in my line of work, and am already multi-cloud-certified, so don't fit into the entry-level audience. I was still looking to refresh a lot of skills and learn newer ones, so I've followed the basics, with a few differences:

1. The initial site was built with [Django](https://djangoproject.com), a technology I've wanted to put into use for ages
2. Infrastructure-as-code and CI/CD were done from step 1 instead of the end
3. The whole site is an application hosted with Google Cloud Run
4. I built my own blog component using the [Wagtail CMS](https://wagtail.org)
5. The database is an experimental combination of [SQLite](https://sqlite.org) with [Litestream](https://litestream.io), replicating to Google Cloud Storage.

This is just the first post to get the blog up and running. I'll do this as a series of shorter posts!

Thanks for reading.