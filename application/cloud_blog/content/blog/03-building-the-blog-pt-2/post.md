+++
title = 'Building the Blog Pt. 2: Continuous Delivery'
subtitle = 'Automating the boring stuff'
date = 2023-10-23
draft = false
show_date = true
tags = ["blog", "gcp", "dev", "django", "terraform", "github", "ci/cd"]
show_title = true
show_subtitle = true
+++

This is the third post in a series of posts about how I attempted the [Cloud Resume Challenge](https://cloudresumechallenge.dev/).

Intro: [The Cloud Resume Challenge and Building the Blog]({{< ref "/blog/01-cloud-resume-challenge/post" >}})

Part 1: [Starting the web application]({{< ref "/blog/02-building-the-blog-pt-1/post" >}})

Part 2: This post

CI/CD was actually a much later step in the challenge, but I really believe in the idea of continuous delivery, even with personal projects. I have a few reasons:

1. Manual deployments are simultaneously boring and unpredictable
2. Enforcing rules at the beginning sets good habits early
3. On larger projects, implementing these things gets harder as time goes on, so it's best to start early.

I'll split this into two sections: continuous integration and continuous deployment.

#### Continuous Integration

When starting these initiatives, things don't have to be perfect on the first go. I had very simple goals here:

* Force me to use pull requests for each feature
* Make sure nothing broke when installing project dependencies from scratch
* Check formatting rules (black's default ones)
* Run some simple Django unit tests.

[CI pipelines](https://en.wikipedia.org/wiki/Continuous_integration) have been generally easier for me to implement than [CD pipelines](https://en.wikipedia.org/wiki/Continuous_deployment).

{{< gist ajpotts01 f366c1c26dfeb01fad6b167bf21cd661 >}}

There are a few important components to this pipeline.

#### Triggering the Pipeline

First, the pipeline is targeted on the application folder - purely for this site (the `application/**` path).

I'm also following a [trunk-based development approach](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development) - short-lived feature branches going straight to `main`. The idea is any features that aren't ready for prod are turned off with feature flags.

#### Installing Dependencies

All of the CI steps run on an Ubuntu runner. My Docker image uses the official `python:3.9.17-slim` image, which runs on Debian, but I'm willing to let that slide for CI.

I use [Pipenv](https://pipenv.pypa.io/en/latest/) for package management, and install all its dependencies using the `Pipfile` it creates.

#### Running Tests

At this stage I only run formatting checks with [Black](https://black.readthedocs.io/en/stable/) and a few unit tests using Django's built-in testing framework.

{{< gist ajpotts01 5ae23431b673e2c3a88a6146f934b59d >}}

These tests are super basic and just check that the right templates are being loaded.

The visitor counter tests are still there and still work, but I don't display them anywhere on the actual site right now while I find time to build a better visitor count.

#### Continuous Deployment

I never get these right the first time. Does anyone?

There are quite a few more considerations when it comes to deploying the site:

* Interactions with the cloud
* Building a container image
* Deploying with the right configuration
* Using secrets to hide credentials

{{< gist ajpotts01 ae1749fac16ebea0e2bf1a053e28b054 >}}

This pipeline triggers on any merge into the `main` branch, but I also added a `workflow_dispatch` trigger. This gives me a neat button on the Actions page for my repo so I can trigger a deployment any time I want to.

{{< img-custom src="/img/blog/03-building-the-blog-pt-2/cd_dispatch_example.png" class="blog" alt="Workflow Dispatch button in Github Actions" >}}

The pipeline starts out largely the same as CI, but needs to activate a service account for deployment. This service account is managed using [Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account). In addition, I've set up a bucket for Cloud Build logs to be stored in. This appears to be a [GCP requirement](https://cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-bucket) for Cloud Build to succeed with a service account.

In my case, I've made the service account storage admin in general. For a service account to have access to the default location Cloud Build places logs, it needs to be even higher - Editor or Owner - and I'm not willing to do that for security reasons. Don't do this!

On that note, secrets are stored in Github. To access them on your own repositories, check `Settings -> Secrets and Variables -> Actions`

{{< img-custom src="/img/blog/03-building-the-blog-pt-2/secrets.png" class="blog" alt="Secrets in Github Actions" >}}

Secrets are then referenced in your pipelines as in the above code block.

#### Deploying to Cloud Run

There are a few considerations when deploying.

In Django's `settings.py` file, an [`ALLOWED_HOSTS` setting is tracked](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts). This prevents requests being made from unknown hosts. In my case, my only allowed hosts are my load balancer. Accessing the Cloud Run URL directly, if you even figure it out, will not work.

Note that I used an @ when injecting the environment variable for allowed hosts into my container. I pass it along as a comma-separated list, which breaks Cloud Run's deployment CLI, but it [allows for substitute characters](https://cloud.google.com/run/docs/configuring/services/environment-variables#escaping) when deploying.

Additionally, the allowed hosts are configured as a Github variable, not a secret. The CD pipeline appears to obfuscate the secret when trying to inject it into the container. This doesn't happen for any other environment variables I injected later in the project, and I haven't had time to troubleshoot.

There are additional security items to add, but they are for another blog post - I updated the CI/CD several times during development, and want to cover this in the order I worked. If you're an experienced Django developer reading this and wondering where some things are - don't worry, the real site is using the correct standards and the work will be covered in a new post.

#### Wrapping up

This covers the absolute basics - again, this was the part where I just did the bare essentials to set myself up for success.

You can find the relevant code changes below:

* CI pipeline
  * [Initial skeleton](https://github.com/ajpotts01/ajp-cloud-resume/pull/17)
  * [Proper trigger, Python version and unit tests](https://github.com/ajpotts01/ajp-cloud-resume/pull/18)
* CD pipeline
  * [Initial run](https://github.com/ajpotts01/ajp-cloud-resume/pull/19)
  * [Finishing it off + infrastructure for Cloud Build](https://github.com/ajpotts01/ajp-cloud-resume/pull/21)

Thanks for reading.