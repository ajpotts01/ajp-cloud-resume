+++
title = 'Deploying Cloud Run with Service YAML'
subtitle = 'Declarative, source-controllable configuration'
date = 2023-12-21
draft = false
show_date = true
tags = ["gcp", "serverless", "cloud run", "devops"]
show_title = true
show_subtitle = true
+++

Automated deployments and continuous delivery always has a bit of an open-world video game feel to it. There are many different ways one can deploy a piece of software and at times it feels like there's no right or wrong way, just your preferred one.

The whole "DevOps" engineering topic has been a favourite lately. This is not influenced only by the construction of this blog. It is also influenced by my work as a data engineer over the last two years. "DevOps" in itself shouldn't really be the term for someone's role - but it has been co-opted over time in the same way that software "engineers" stole that label from the real engineers out there. That's an argument for another day.

In my data engineering work, I have largely used shell commands in CI/CD runners to get my deployments done. These are usually interacting with cloud CLIs, building [Docker](https://www.docker.com) images, running unit tests, etc. These work fine, but I'm sure everyone reading this knows of the pain of getting shell commands exactly right.

In some cases, there's a better way. This post will show how to keep declarative, version-controlled configuration files to deploy Cloud Run services, and how to use them in your CI/CD pipelines.

#### The setup

My reference repository is [here](https://github.com/ajpotts01/url-shortener). It is a straightforward, simple URL shortening API written in [Go](https://go.dev), another recent favourite. I did this project for practice developing in Go, as well as a few other components:
- Infrastructure as code using [OpenTofu](https://opentofu.org)
- Serverless compute using [Cloud Run](https://cloud.google.com/run)
- NoSQL database using [Cloud Firestore](https://firebase.google.com/docs/firestore)
- Automated deployments using [Github Actions](https://github.com/features/actions) to tie it all together.

The deployments also cover GCP Workload Identity Federation, which I covered in a [previous blog]({{< ref "/blog/08-gcp-workload-identity/post" >}}).

When deploying a Cloud Run service, a few things need to be specified:
- The service account the service will run under
- The container image to deploy
- The project and region to deploy to
- The name of the service itself.

Note: My pipeline is deployed by one service account, while being invoked by another. The executor account requires the "Cloud Run Invoker" role, and the deployment service account requires "Cloud Run Admin".

To finish setting the scene, my service needs a few extra variables set on deploy:
- The project ID
- The Firestore database ID to connect to
- The domain name being served.

#### Cloud Run deployments - the old way

If you've followed this blog for a while, you may have already seen [part 2]({{< ref "/blog/03-building-the-blog-pt-2/post" >}}) of building the blog, which covered similar ground.

To deploy my service to Cloud Run via the CLI, I would likely do something like this - from my old repo:

{{< gist ajpotts01 626645267a68b11c4ace696c4e00c59b >}}

This works, is totally fine, and how most demos/tutorials/blogs will show you how to do things.

#### Cloud Run deployments - the new way

Cloud Run is a managed version of an open-source framework called [KNative](https://knative.dev/). This in itself is a managed layer on top of [Kubernetes](https://k8s.io). Together, they form a powerful serverless framework that abstracts away all the hard work and leaves you to simply deploy a container.

However, the upside of its roots is that we can specify a Kubernetes-style [service YAML file](https://kubernetes.io/docs/concepts/services-networking/service/) to declaratively configure our service.

The full specification for the YAML can be found [here](https://cloud.google.com/run/docs/reference/yaml/v1), but a simpler snippet is in the deployment guide for Cloud Run [here](https://cloud.google.com/run/docs/deploying#service)

This can be a bit much to wade through, so I recommend learning the same way I did: deploying your Cloud Run service in a development environment using either GCP UI or CLI, then pulling the auto-generated YAML file it creates and editing that to your heart's content.

{{< img-custom src="/img/blog/10-cloud-run-service-yaml/gcr_yaml_sample.png" class="blog" alt="Screenshot of sample Google Cloud Run service YAML" >}}

This is the full YAML file as it sits now in my URL shortener's repository.

{{< gist ajpotts01 d02a218d7bcd2e4427411875ce766020 >}}

#### Deploying in a CI/CD pipeline

My YAML file specifies all the settings you'd require for a Cloud Run service - % of traffic allocation to the service, resource limits for CPU and memory, timeouts, etc. Of note are the placeholder values for the configuration items listed earlier in this post.

These values are all placeholders surrounded by angle brackets (<>). They are not known before deploy time, and are injected into the container by this service's CI/CD pipeline. The trick to this is our trusty Unix tool `sed`.

The full Github workflow is publicly available [here](https://github.com/ajpotts01/url-shortener/blob/main/.github/workflows/cd-application.yml), but I'll focus on the deployment steps.

{{< gist ajpotts01 c06793eb3c07ee106a9ba472f023a612 >}}

The first step of this excerpt uses [`sed`](https://www.gnu.org/software/sed/manual/sed.html) to do global replaces of the placeholder values with secrets stored in my Github repository. Each `sed` call pipes its output into the next call, and the final result is output to a `service.yaml` file. There are no real surprises here - I have gone into detail about using Github secrets in examples during my posts on building this blog. I generally set the secrets up as environment variables for the workflow, which is why they are referenced with the `env` prefix instead of `secrets`.

It is also possible to link secrets in GCP's secret manager to the container using similar YAML. The below example would be used if I wanted my `DATABASE_ID` environment variable to be pulled from secret manager. The "key" is actually the version of the secret you want - this can be a number, or just the latest value.

{{< gist ajpotts01 d0e04ec6b93bcd7e798a108a84b17ba7 >}}

The only gotcha here is my `DOMAIN_NAME` environment variable. The domain name is needed to prefix any shortened URLs with the domain the service is running from. It is not known at service deploy time, unless you have bought a domain for the service and know what to put in here ahead of time. I don't, so I'm using a little trick: use `gcloud run services describe` to get my newly-deployed service's URL, and use `gcloud run services update` to inject a new environment variable into the container.

I am not sure if there's a better way to do this, so please contact me on Linkedin if you have any suggestions.

This same approach can also be used for Cloud Run Jobs - my first production use of this method was done with a Job, with no issues. The full reference is [here](https://cloud.google.com/run/docs/reference/yaml/v1#job) in case you are interested - some of the static configuration values need to be slightly different. 

In any case, this approach offers a declarative way of deploying your service configuration. To me, it feels a bit cleaner - source controlled in a separate section of your repository, not getting lost in all the other script commands in a CI/CD pipeline. Back in my site deployment blogs, I noted that since I had a comma-separated list of allowed hosts for Django, I had to specify a substitute delimiter for my environment variables at deploy time. This approach would have avoided having to do this. It is slightly more complex than just writing your deploy scripts in the Github workflow, but I think over time it will pay off with a more understandable code base and a smaller blast radius if you need to make changes.

I hope this has been useful. Feel free to contact me on [LinkedIn](https://linkedin.com/alexander-potts-9b4a41aa/) if you have any questions or suggestions. 

Thanks for reading.