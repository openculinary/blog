---
title: "Construction continues.. and an update on indexing performance"
date: 2020-10-23
author: James
tags:
- status-update
---
At RecipeRadar engineering HQ, feature development has been continuing - at a slightly unpredictable pace - in a few parallel areas.

**Collaboration (unblocked)**

As mentioned during the previous update, we had been blocked on multi-device collaboration work due to an [issue](https://github.com/dfahlander/Dexie.js/issues/1126) affecting database unit tests. The good news is that the issue has since been [fixed](https://github.com/dfahlander/Dexie.js/pull/1138)!

Work on multi-device sessions should recommence shortly.

**Surfacing nutritional information (blocked)**

Display of nutritional information within the application is in progress, but we've hit some snags estimating aggregate nutritional information for recipes.

In short, there are too many gaps in the data for us to accurately predict recipe nutrition from the ingredients where we have known metric quantities.

We're likely to wait until nutritional information is [supported natively](https://github.com/hhursev/recipe-scrapers/issues/241) in the _recipe-scrapers_ library before continuing. We're optimistic that this feature will simultaneously allow us to display accurate nutritional information, while also allowing us to backfill gaps in our knowledge base.

**Dietary properties (landing soon)**

Support for recipe dietary properties ('dairy free', 'vegetarian', ...) is in progress, and should be ready for user testing next week.

The RecipeRadar application will display icons to indicate the dietary properties of recipes in the search results, and also allow searching/filtering by those properties.

**(Re)Indexing performance**

Recent work related to recipe metadata has highlighted performance problems during (re)indexing of search engine contents.

Currently it takes approximately two days to reindex the entire recipe document set, which makes development iteration challenging.

We've spent time to identify areas for performance improvement and it appears that disk storage is our current bottleneck.

We may need to order some new disks for our server to make significant improvements; this work is planned and tracked in [infrastructure issue #27](https://github.com/openculinary/infrastructure/issues/27).

**Coming up next**

Resuming work on collaborative sessions and surfacing additional recipe metadata in the application will be our primary focuses over the next two weeks.

The past few weeks have been very consciously focused on data and enabling features, and we hope to revisit application UI and UX improvements in the near future.
