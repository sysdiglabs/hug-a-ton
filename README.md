# Hug-a-ton

Hug-a-ton is a Slack bot to share love & appreciation with your coworkers.

This project has been greatly influenced by the ideas implemented by https://github.com/Pagepro/open-kudos,
so you might want to check that project first, specially since it's feature-richer and complete.

Hug-a-ton attempts to be a simplified version of [OPEN KUDOS](https://pagepro.co/open-kudos.html) which
might suit the following use cases:

* You have already an AWS infrastructure and want to deploy the backend there.
* You like `Infra as Code` and want to have a repeatable way of deploying your infrastrucure.
* You get scared by TypeScript and rather use good old Python.

Logo designed by http://www.instagram.com/tinarose_artist


# How it works

## Give a hug

Somebody helped you out? Have you seen an awesome contribution? Just send a hug to a coworker with:

    /hug @john.doe [message]

An anonymous message will be posted to `#-hugs_` with your message tagging the _hugee_

## Check your balance

Wanna know the hugs you have available to give, or the hugs you've received? Use:

    /hug balance

You'll get a private message with your balance

## Pay it forward

Got enough hugs from your coworkers? Share the love outside your company with:

    /hug donate [quantity] [charity_link]

A message will be post to the configure channel about the donation and HR will reach out to proceed with it.

# Installation

Check the [Installation Guide](INSTALLATION.md)

# Backlog

Feature we will like to get in (PRs welcome!):

* Full customization of user messages
* Admin dashboard
* Hugs analytics
* Tag hugs with custom company values
* Implement measures to prevent misuse
