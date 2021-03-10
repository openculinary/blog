---
title: "A new way to find recipes: the Recipe Explorer!"
date: 2020-12-04
author: James
tags:
- status-update
---
During the last two weeks, we had a relatively radical idea for a way to explore recipes on RecipeRadar.

Rather than prompting people to enter the ingredients they have (requiring a modest but noticeable amount of data entry), we can _present_ a list of common recipe ingredients to the user, and allow them to use swipe gestures to say yes/no to the ingredients that they have, saving on typing.

As they swipe to indicate whether each ingredient is available, the list of subsequent ingredient choices updates dynamically based on the recipes that match the ingredient selections made so far.

A beta version of this interface is [now live](https://www.reciperadar.com/#explore) - please try it out if you have time, and send us some feedback!

Here's a screenshot to give you an idea how this works:

![A list of ingredient names arranged vertically, with four ingredients selected as available and one selected as unavailable by the user](/images/recipe-explorer.png)

**Coming up next**

Work continues towards restoring multi-user collaboration (as we seem to keep on harping on about in these updates). It'd be great to re-release that functionality before the end of the year; let's see how we get on.

We are also planning on generating a web of static content pages based on the recipe and ingredient metadata we have within RecipeRadar.

The goal is for these pages to be genuinely useful to users who are looking for information about ingredients while also providing a search-engine-friendly content directory that generalized search engines like Google, Bing and Yahoo can index.
