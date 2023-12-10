+++
title = 'Microsoft Applied Skills: Power Automate'
subtitle = 'Microsoft attempts a new way of validating learning pathways'
date = 2023-12-10
draft = false
show_date = true
tags = ["microsoft", "automation", "power platform", "certifications", "learning", "training"]
show_title = true
show_subtitle = true
+++

Certifications are a common discussion point on just about every tech forum. A lot of newcomers to the industry - not knowing where to start - might think that getting one or many certifications is an easy entry point into a new tech career.

There are many reasons why you may think this is the case:

- Certifications aren't cheap (and expensive == valuable, right?)
- They do appear to validate your experience with an external authority (e.g. Google/Microsoft/Amazon)
- It's easy to pick one since just about every discipline has a certification these days
- They usually offer some kind of associated learning path or training material to prepare for the exam.

These aren't really the best reasons to get a certification. The main issue with them tends to be that they are written exams. Probably the most common meme for exams of any kind - high school, university, certifications, whatever - is that everyone crams for them just to get through it. This does lead to a problem in the industry where someone has every certification under the sun, but when faced with the first step of building a new solution in a given technology, they're completely lost.

There are still some valid reasons for certifications:

- They are a nice cherry-on-top of prior professional experience
- If you are a consultant, they make you and your firm more marketable
- The learning material, if applied to a real project, is usually a really great place to start.

Still, the "certification hoarder" issue remains.

#### A new way to test technical competency

Microsoft is looking to fix that with their new [Applied Skills](https://learn.microsoft.com/en-us/credentials/browse/?credential_types=applied%20skills) program, [announced in October 2023](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/announcing-microsoft-applied-skills-the-new-credentials-to/ba-p/3775645). The idea behind this is you earn these credentials through practical work in a lab environment instead of answering 60 to 90 multiple choice questions.

Each applied skill comes with a complete Microsoft Learn path to follow.

{{< img-custom src="/img/blog/09-ms-applied-skills-power-automate/power_automate_learning_path.png" class="blog" alt="Screenshot of Power Automate learning path on Microsoft Learn" >}}

I still think Microsoft Learn is the strongest general tech education platform online for a few reasons:
- It is completely free
- It has almost enough quality information to pass certification exams - I studied for my original Power Platform certification using only Learn
- It features either sandboxes or links to free trials for real Azure/Office/Power Platform tenants
- It features learning paths for non-Microsoft technologies like [Go](https://learn.microsoft.com/en-us/training/paths/go-first-steps/) and [Django](https://learn.microsoft.com/en-us/training/paths/django-create-data-driven-websites/).

The only specific training I have found to be higher quality than Microsoft Learn is [UiPath's RPA Academy](https://www.uipath.com/rpa/academy) - but it is focused on one technology platform. I really think Google needs to pick up their game on training - [Cloud Skills Boost](https://cloudskillsboost.google) is not free, and the Qwiklabs are nothing more than glorified copy/paste exercises.

I originally picked up the [Kubernetes](https://learn.microsoft.com/en-us/credentials/applied-skills/deploy-containers-by-using-azure-kubernetes-service/) path as I am very focused on learning cloud platform (or "DevOps") technologies lately, and have never touched Kubernetes. I got through the learning path over the past few weeks as I had time. But I found myself sick with a cold this weekend - such is life when you are a new parent.

Even though that meant a forced break from spending a ton of brainpower on learning new things, I could give the assessment platform a shot by revisiting an old favourite - Microsoft's [Power Platform](https://powerplatform.microsoft.com/en-au/).

#### Is low-code really that good?

Some of my favourite projects in my brief time as an Azure consultant involved the Power Platform. It's broken down into a few components:

- [Power Apps](https://powerapps.microsoft.com/en-au/landing/developer-plan) - low code applications of varying types
- [Power Automate](https://powerautomate.microsoft.com/en-au) - automation components for both cloud-based workflows and classic robotic process automation
- [Power Pages](https://powerpages.microsoft.com/en-au/) - low code public-facing websites
- [Copilot Studio](https://www.microsoft.com/en-au/microsoft-copilot/microsoft-copilot-studio) - chatbot functionality, formerly known as Power Virtual Agents
- [Power BI](https://powerbi.microsoft.com/en-au/landing) - the well-known Microsoft analytics powerhouse
- [Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intro) - database technology to support most of the above.

Power Platform has a lot of Microsoft Dynamics components under the hood, so it's common to see consultants doing both Dynamics and Power Platform work to extend that.

I have found the Power Platform - especially the combination of Power Apps and Automate - to be incredibly useful in creating easy business value without much effort that doesn't require a full-blown development team. There are still cost-of-ownership questions that an organisation must consider when building these, but that's for another post. I highly recommend the Power Platform for many scenarios.

#### Taking the test

I had already completed most of the [learning path material](https://learn.microsoft.com/en-us/training/paths/create-manage-automated-processes-by-using-power-automate/) while studying for my [PL-100 certification](https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-100/) last year. There was a guided project that is directly relevant to the final assessment questions, so I do recommend attempting it.

Upon starting, you have two hours to complete the test. You aren't monitored or anything like a remote proctored certification exam, so are free to look up any resources you like. You are logged straight into a virtual machine with a sidebar dialog that gives you instructions on how to complete the assessment.

{{< img-custom src="/img/blog/09-ms-applied-skills-power-automate/power_automate_assessment.png" class="blog" alt="Screenshot of Power Automate assessment on Microsoft Learn" >}}

I've obfuscated the actual screen in the screenshot so I don't give anything away, but this was worth sharing. The one criticism I have of the assessment is that on a single screen laptop, the viewport is awfully tiny. In a way, I was playing this assessment on hard mode.

All the instructions for the actual tasks are given to you via a fake e-mail portal with requests from an imaginary client. For the Power Automate assessment, the following topics are covered:

- How to create automation flows with different triggers
- How to interact with Excel, Sharepoint, Outlook, the Dataverse, and Microsoft 365
- Conditional logic in automation flows

Overall, I did not have too much trouble with the assessment. The passing mark was 67% and and I scored 83%. The final score screen doesn't tell you what you got wrong, just like certification exams. I suspect I may have missed a detail in some of the tasks requiring sending e-mails - perhaps not 100% correct text somewhere.

When complete, you get a proper credential like you do with the certifications. Mine is [here](https://learn.microsoft.com/api/credentials/share/en-au/AlexanderPotts-2118/D0A073A87BBC0798?sharingId=D39C391635FCB630).

#### Summary

Overall it was a positive experience. I'm going to complete a few more of these. The Kubernetes one is at the top of my list, but there are others covering technologies I've previously touched, like C#/ASP.NET and Azure DevOps.

These may help newcomers in their journey a bit more than a pure certification - they make you do "real" work, thus demonstrating practical skills. I think they're also really useful in giving you ideas as to how you can build your own side projects and continue your learning journey. I highly recommend them.

Thanks for reading.