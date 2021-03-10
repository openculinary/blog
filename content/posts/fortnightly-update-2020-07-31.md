---
title: "Getting started with Nutritional Information"
date: 2020-07-31
author: James
tags:
- status-update
---
While there's no single large feature that has landed in RecipeRadar in the past fortnight, there are a number of irons in the fire.

This week's update is primarily textual rather than visual -- we don't have any screenshots to share this time -- but as you'll see, that's appropriate given some of the work we've been doing.

The items we're making progress on currently include:

**Nutritional Information**

We've identified a number of trustworthy and authoritative sources of ingredient nutritional information, including the USDA's [FoodData Central](https://fdc.nal.usda.gov/) and UK's [CoFID](https://www.gov.uk/government/publications/composition-of-foods-integrated-dataset-cofid) dataset.

The next challenge is to find a good way to associate the records from these datasets with the ingredient identifiers that RecipeRadar uses internally, and to update the knowledge-graph so that it can store and serve the associated metadata.

Please note that we don't intend to surface this nutritional information to users via the application during Q3; we do however have [plans](https://github.com/openculinary/company/blob/main/roadmap/reciperadar.md#q4-2020) to offer functionality related to dietary planning in Q4, and that will incorporate nutritional factors.

**Direction Metadata**

Over the past couple of weeks, we've explored various options related to extraction of metadata from recipe text -- we want to identify the various _actions_ involved when preparing recipes ("`combine` the flour and milk") and also to discover the important _entities_ involved in each step ("pre-heat the oven to `200 F`").

The ideal outcome of this -- which could take some time -- is that we will be able to use the [co-references](https://en.wikipedia.org/wiki/Coreference) discovered in recipe directions to represent those visually, as in the example diagram included in the application's [vision statement](https://www.reciperadar.com/#about-vision).

As part of the work towards this, we have [re-structured](https://github.com/openculinary/knowledge-graph/pull/45) some of the responses of the knowledge-graph so that they return data in XML format. The primary driving reasons for this are that XML can represent data as a tree/graph (which we want) and also that it can represent entities interleaved in-line with natural language text (which we also want).

In addition, we are now performing [basic identification of verbs](https://github.com/openculinary/knowledge-graph/pull/47) in recipe directions. This is relatively straightforward thanks to modern open-source natural language processing libraries. We'll need to introduce more advanced techniques from these libraries in order to reach a better understanding and representation of recipe text.

**Coming up next**

It's hard to say precisely where we'll get to with each of these goals within the next two weeks -- perhaps moreso because our entire engineering team (currently a euphemism for 'me') will be on holiday until mid-late August.

Integrating nutritional data before then seems like an ambitious but achievable goal, and we may send a mini-update if we manage that.

Either way, you can expect the next 'fortnightly' update roughly a month from now.
