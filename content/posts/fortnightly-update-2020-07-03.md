---
title: "Spelling suggestions are live!"
date: 2020-07-03
author: James
tags:
- status-update
---
Q2 2020 is now complete, and I'm glad to say that we managed to achieve almost all of the [goals](https://github.com/openculinary/company/blob/main/roadmap/reciperadar.md#q2-2020) for the quarter. The only task that has rolled over into Q3 is the selection of a graph database technology, in order to support the [`knowledge-graph`](https://github.com/openculinary/knowledge-graph) component.

**Spelling Suggestions**

During the last update I mentioned that we had discovered the [`fast-autocomplete`](https://github.com/seperman/fast-autocomplete) software library as a candidate to provide spelling suggestions on RecipeRadar.

Although that project does look great, we discovered an issue with it during integration. Out of the box, it doesn't provide search suggestions when you search for a word that is in the middle or at the end of an ingredient name.

For example, searching for 'cream' would _not_ suggest 'sour cream' using the default fast-autocomplete configuration.

That's significant because it's an existing feature that we support and would like to retain for RecipeRadar - it's useful and has been [requested](https://github.com/openculinary/frontend/issues/90) in the past.

As a result, we've decided to re-use our existing [`Elasticsearch`](https://www.elastic.co/) search engine to provide ingredient spelling suggestions.

When you start entering some text, the application looks in the set of ingredients for near-matches on _any_ word in the ingredient:

![A user has mis-spelled "hummus" and the system is able to display the correct spelling](/images/suggestions.png)

I'm glad to report that this feature is now [live on RecipeRadar](https://www.reciperadar.com/#search); please give it a try and let me know what you think.

**Coming up next**

With the previous quarter recently complete, it's a good time to look further into the horizon to see what's planned over the next few months.

Among the most promising planned features are:

- Restoring multi-user collaboration support, so that you can share your meal planning session with friends and family

- Providing ingredient substitutions, so that you're able to find more recipes that use the ingredients you have in stock

- Gathering nutritional information into the knowledge graph, so that we can use that information to unobtrusively guide users towards making healthy eating decisions

These are ambitious, and will run in parallel with our regular work including bugfixes, incrementally adding user interface improvements, and recipe search result tuning.

We may have to rearrange the roadmap tasks a little as we learn more about the size of work involved for each feature, but this is what we're setting out to do, starting on Monday.
