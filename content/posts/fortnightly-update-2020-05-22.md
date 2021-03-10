---
title: "Partial ingredient search, meal planner updates, and more"
date: 2020-05-22
author: James
tags:
- status-update
---
The last two weeks have included improvements to our ingredient search engine suggestions, meal planning improvements, and proposal of a [product roadmap](https://github.com/openculinary/company/pull/4). We'd love feedback on these, and the roadmap in particular!

We made incremental progress on our internationalization processes (by [trialing](https://github.com/openculinary/internationalization/pull/16) use of an application called [`poedit`](https://poedit.net/)), but the process still involves some friction.

Support for viewing historic meal calendar entries remains on the near-term task list.

**Partial Ingredient Name Suggestions**

When you start typing 'tomato' on RecipeRadar, the search engine will scan for suggestions across recipes that contain matching ingredient text, such as `1 tomato` or `two tomatoes` (i.e. both plural and singular forms).

In this example, RecipeRadar suggests the plural name 'tomatoes' to you, because the plural text appears more often in the recipe set than the singular form 'tomato'.

Until recently, these suggestions would _only_ include ingredients where your input is a strict prefix of the ingredient name. So you might be offered "tomatoes" and "tomato sauce" as selections, but you would not be prompted with "cherry tomatoes" as an ingredient to search for.

This limitation (as [reported](https://github.com/openculinary/frontend/issues/90) a little over a month ago) has now been removed, making it easier to search for all kinds of ingredients and ingredient variants.

Have you encountered any problems finding ingredients or recipes on RecipeRadar? Let us know via the 'Feedback' button or by [filing a GitHub issue](https://github.com/openculinary/frontend/issues/new) and we'll take a look.

**Meal Planner Messaging**

Some small changes have been applied to meal planning in the application this week.

While users can still create a shopping list without planning any meals, the 'suggested action' for each recipe search result now leads them towards meal planning rather than shopping list creation:

![A recipe result with a button labeled "Add to meal planner"](/images/call-to-action.png)

This aligns with our idea that users can save time, eat more healthily, and reduce food wastage by planning ahead for multiple meals.

To further attract users towards meal planning and to inform them about the state of their meal calendar, we have added a visual cue with the number of entries in the meal planner:

![Navigation menu, with notifications displaying the number of meal planner and shopping list items](/images/meal-planner-cue.png)

These small features will become increasingly valuable after we re-enable multi-device and multi-user session sharing.

Allowing family members and friends to view the state of meal planning and shopping at-a-glance, and providing access to the shopping list you created at home on your desktop computer while out with your smartphone are two of the cases we are considering.

**Product Roadmap**

Progress on RecipeRadar over the next few months should be methodical and sustainable; we have a large number of product goals, and while we can't achieve them all instantly, we can arrange them thoughtfully so that we gradually deliver application improvements for users while retaining high quality and ensuring that our code remains easy to modify and extend, allowing us to reach our longer-term goals eventually.

To more easily communicate what those product goals are, and in what order we currently plan to implement them, we have drafted a [RecipeRadar Product Roadmap](https://github.com/openculinary/company/pull/4). Please take a look and provide your feedback here or on the GitHub pull request.

**Coming up next**

As you'll see on the roadmap, there are a number of architectural investments that we believe make sense to apply during the remainder of Q2 2020 (Apr to Jun 2020).

It's likely that these will compose the bulk of our engineering work over the next two weeks; we may also take the opportunity to look into improving company transparency via [OpenCollective](https://opencollective.com/) and perhaps by increasing the external visibility of internal mailing lists.

As mentioned previously, adding the ability to view historic meal calendar entries in the application also remains on the near-term todo-list.
