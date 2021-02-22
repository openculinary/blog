---
title: Fortnightly Update - 2020-04-24
date: 2020-04-24
author: James
tags:
- status-update
---
The last two weeks have involved quality improvements, design prototyping, and preparatory work as we prepare to introduce more contributors to RecipeRadar.

Have you experienced any ingredient shortages or price changes during the coronavirus pandemic?

In future we hope that RecipeRadar will automatically offer information on local ingredient availability, seasonality, and pricing. This and other plans will be detailed in an upcoming roadmap document.

**Design Iteration**

As you may have seen on the mailing list, **Monica** has been preparing screens to provide an improved search experience in the application.

![A design for updated search controls](/images/ingredient-selection.png)

These are exciting changes and they provide the opportunity to make each RecipeRadar session more intuitive and rewarding.

Please provide your feedback about the prototype screens with the volunteers@reciperadar.com mailing list.

**Improvements**

A [long-standing issue](https://github.com/openculinary/api/issues/3) that allowed duplicate recipes to appear in search results has been thoroughly solved!

The solution took some careful planning and implementation, and is [documented](https://github.com/openculinary/api/pull/45/files#diff-8849635885fa3990203733414322d517R125-R181) for future reference.

If you see anything that looks unusual while using RecipeRadar, please feel free to report an issue via the 'Feedback' button in the app, or directly [on GitHub](https://github.com/openculinary/frontend/issues).

**Call for Developers**

We're looking for more software developers to help implement features and improvements for RecipeRadar.

Alongside the Code of Conduct mentioned in the last update, we now also have a set of [Contribution Guidelines](https://github.com/openculinary/.github/blob/1b423f23ce6ec48ad7bd95f59189e81617ab21f5/CONTRIBUTING.md) to help developers (and other contributors) get started in the most effective way possible.

If you know any software developers who are looking for projects to contribute to, please send them our way. Soon we'll also be ready to invite help from anyone who can offer translations of the application into different languages.

Although we don't currently offer financial compensation, we can offer attribution and credit for work provided, and I'd personally be glad to supply references for any work contributed to RecipeRadar when people are applying for jobs in future.

**PWA Store**

RecipeRadar has been submitted for inclusion in the [Progressive Web App Store](https://progressiveapp.store/)!

The PWA Store is similar to the iOS App Store and Android Play Store that you are more likely to be familiar with, and offers web-based applications that you can install for free on your own devices.

**Coming up next**

One of the features we're most excited about is the inclusion of more ingredient context in recipe search results.

Where you would previously have seen a recipe call simply for `onions`, in future you'll see the full ingredient description, such as `large onions, diced`.

The ingredient name will continue to be highlighted so that you can see at-a-glance how many ingredients match in each search result.

Thanks again to **Citra** for [reporting](https://github.com/openculinary/frontend/issues/94#issuecomment-613155354) this issue -- it should soon be resolved thanks to a lot of [preparatory work](https://github.com/openculinary/api/pull/49) behind-the-scenes.
