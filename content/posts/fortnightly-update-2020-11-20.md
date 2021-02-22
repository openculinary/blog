---
title: Fortnightly Update - 2020-11-20
date: 2020-11-20
author: James
tags:
- status-update
---
Welcome to another almost-fortnightly RecipeRadar update.

There have been a few developments since the last update:

- Our first feature-related blog post, ["An introduction to ingredient parsing"](https://blog.reciperadar.com/posts/introduction-to-ingredient-parsing/) went live in early November - part of a series with follow-up posts coming soon

- We've [completed](https://github.com/openculinary/backend/issues/34) a large-scale refactoring (re-organization of code and data) to make it easier to manage and correct the information that we store about ingredients. As a side-effect, this has further improved our recipe indexing performance.

- We've added the ability to [filter search results by recipe website](https://github.com/openculinary/frontend/pull/177). If you have a favourite recipe website, or if there are websites that you don't like, you can now choose to show/hide those in your search results.

- The application now displays dietary properties alongside each recipe, indicating whether they are dairy-free, gluten-free, vegan and vegetarian

![Four icons indicating the dietary properties of a recipe](/images/dietary-properties.png)

**Coming up next**

The largest work-in-progress feature is the long-awaited _collaboration_ feature,

restoring multi-device application sessions.

It's proving difficult for the engineering team to get traction on - the design in particular is fairly complicated and important to get right, but we're working on it.

Additionally, we have some smaller features that we're hoping to look at soon:

- Adding a ['share link' option](https://github.com/openculinary/frontend/issues/176) from the recipe view page may be a quick win

- We may be able to improve search performance by [removing some unused fields](https://github.com/openculinary/backend/issues/38)

Finally, we're still hoping to surface recipe nutritional information once this is available via the [`recipe-scrapers`](https://github.com/hhursev/recipe-scrapers) library. More news on that when we have it.
