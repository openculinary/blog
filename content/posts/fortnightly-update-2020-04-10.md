---
title: Fortnightly Update - 2020-04-10
date: 2020-04-10
author: James
tags:
- status-update
---
Progress on RecipeRadar has been ramping up over the past few days; here are some updates on recent developments.

**Homepage Updates**

Thanks to **Susan** and **Liz**, the homepage search controls have had a revamp:

![The RecipeRadar homepage recipe search controls](/images/homepage.png)

All three of the recipe search fields are now shown by default, and the wording has been simplified and improved to cater to people finding ingredients unavailable due to the COVID-19 crisis.

**User Experience Improvements**

While [more work remains](https://github.com/openculinary/frontend/issues/70) to improve ingredient search, incremental progress is being made.

- Handling of 'enter' keypresses has been [adjusted](https://github.com/openculinary/frontend/pull/75), with more improvements to follow.

- **Citra** has reported an [issue](https://github.com/openculinary/frontend/issues/90) regarding 'partial' ingredient search and there is a plan to handle this in the RecipeRadar Search API.

- A [bugfix](https://github.com/openculinary/frontend/pull/84) has been applied to ensure that pressing the search button always scrolls the user to see their search results. In future we plan to add [automated testing](https://github.com/openculinary/frontend/issues/87) to ensure that the bug can't reappear.

- A [performance issue](https://github.com/openculinary/frontend/pull/86) relating to recipe result lists was identified and fixed, leading to a more responsive search experience

**Blog is Ready to Roll**

The [RecipeRadar blog](https://blog.reciperadar.com/) is up and running, and posts can be added via the blog's [GitHub repository](https://github.com/openculinary/blog). If you'd feel like writing some content for the service - or know someone who would - please contact [James](mailto:james@reciperadar.com) with details.

**Code of Conduct**

An organization-wide [Code of Conduct](https://github.com/openculinary/.github/blob/master/CODE_OF_CONDUCT.md) has been introduced, and aims to foster a comfortable and pleasant environment for discussion and collaboration.

If you have any concerns about anyone's conduct relating to RecipeRadar, please contact us at conduct@reciperadar.com and we'll address it.

**Coming up next**

There's plenty more in store over the next couple of weeks.

- We'll be investigating improvements to [link sharing](https://github.com/openculinary/frontend/issues/89#issuecomment-612141517) so that people can more easily share recipe ideas they find with friends

- There's a [user experience bug](https://github.com/openculinary/frontend/issues/88) relating to 'jumpy' search results that we're planning to get rid of

- We'll be [upgrading the recipe crawling library](https://github.com/openculinary/crawler/issues/6) that we use, and that will provide us with more sources of recipes from the web
