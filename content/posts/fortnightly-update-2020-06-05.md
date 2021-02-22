---
title: Fortnightly Update - 2020-06-05
date: 2020-06-05
author: James
tags:
- status-update
---
**Updated Website Prototypes**

Please take a look at the latest v6 website prototypes from **Monica** and provide your feedback. Mobile versions should also be arriving in the near future.

One of the features of the screens that may involve the most complex user interactions and information presentation is the selection, display and navigation of planned meals (calendarization).

**Architecture Investments**

When you interact with RecipeRadar on your phone or on your computer, the information presented to you is served by our recipe search engine, which is based on the open source [`Elasticsearch`](https://www.elastic.co/elasticsearch/) product.

We also use the popular open source [`PostgreSQL`](https://www.postgresql.org/) database to store persistent data: ingredients, recipes, our progress crawling the recipe web, and user search logs (which do not contain any [personally-identifying information](https://en.wikipedia.org/wiki/Personal_data)).

Until recently, both the search engine and database have had to be online continuously for the application to work correctly, and upgrades to the latter were performed manually.

The main risk introduced during manual database upgrades is that there are fewer guarantees that the changes will be applied and will behave the same way that they did during development.

I'm glad to say that following [some modifications](https://github.com/openculinary/infrastructure/issues/8), the entire RecipeRadar application experience can now be served by the search engine [API](https://github.com/openculinary/api), even when the database is temporarily unavailable. Support has also [been added](https://github.com/openculinary/backend/issues/2) -- albeit not yet thoroughly tested -- for scripted database upgrades.

These improvements reflect progress against our tentative [product roadmap](https://github.com/openculinary/company/pull/4).

**Company Accounts**

Although I don't have much feedback to report yet, I've been spending a little time investigating potential options around company financial reporting and accounting. This will take place in the UK and I hope that there will be a good level of transparency achieved in the process.

**Internationalization Support**

Does anyone on our list have experience using [`Weblate`](https://weblate.org/en/)?

It looks perfect for our translation use cases; it's open source, and provides 'continuous localization' -- the idea is that translators' work should be incorporated into the application on a regular basis, matching the cadence of application releases.

Ideally, if we release two updates for RecipeRadar during a given day, and a contributor provides a verified, approved translation in the time between those two releases, then it should be included in the second release).

**Coming up next**

Looking at our Q2 2020 roadmap, we have a few user-facing features that we're aiming to implement over the next few weeks. The next items we'll be looking at include:

- A 'recipe detail' page in the application

- The ability to scale up/down the number of servings for recipes on the detail page

- Support for spelling corrections during ingredient and equipment search

It may be a stretch to achieve all of these within a two-week duration, but we'll see how we get on. Expect to hear some updates on these in the next fortnightly update.
