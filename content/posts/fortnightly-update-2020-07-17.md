---
title: Fortnightly Update - 2020-07-17
date: 2020-07-17
author: James
tags:
- status-update
---
The last couple of weeks have been slow and steady in terms of RecipeRadar software engineering progress.

The main focus recently has been on providing [recipe data debug tooling](https://github.com/openculinary/frontend/issues/38) in order to help identify and fix future data quality issues. Here's an overview of how that works.

**Recipe Data Diagnostics**

When users are searching for recipes, it's important that we display accurate representations of the ingredients and directions for each recipe.

RecipeRadar takes recipes from all over the web and translates them into a common representation in a format called [`JSON`](https://en.wikipedia.org/wiki/JSON), with a lot of help from the ever-improving [`recipe-scrapers`](https://github.com/hhursev/recipe-scrapers) library.

Sometimes, the contents or format of the recipe website may change -- and sometimes our own processing of the data may change (for example, after we learn about a new ingredient or item of kitchen equipment, we can add additional metadata to the JSON format).

The newly-added recipe diagnostics page shows the contents of the recipe, as it was _last indexed_ into RecipeRadar's search engine, and also as it _appears currently_ when applying the latest crawling & post-processing operations.

How does that all look in practice? Well, [here's an example](https://www.reciperadar.com/diagnostics/#recipe&id=cpkVntbJ8jDNE1yj1f1caJsuR9):

![A JSON-format diff that indicates that a red chilli ingredient has been added](/images/recipe-diff.png)

In this case we can see that the version of the recipe in the search engine contains 19 unique ingredient products (note the strikeout text in red), and the newly-crawled version of the recipe contains 21 -- one new ingredient is visible in the large block of green text.

That means we should probably re-crawl and re-index this recipe so that users can find the updated (and in this case, more accurate) representation of the recipe.

Something's still a little unusual in this case however - the singular form of the product name is 'red chilly'. It'd be worth investigating and resolving that as well.

**Coming up next**

It's uncertain exactly what feature we'll be working on next, but it's likely _either_ going to be gathering ingredient nutritional data, _or_ it'll be figuring out how to support ingredient substitutions (for example, substitute spices or proteins).
